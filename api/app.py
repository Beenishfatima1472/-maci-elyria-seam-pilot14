from __future__ import annotations

import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict
from uuid import uuid4

from flask import Flask, jsonify, request, send_from_directory, g

from maci_elyria.api_hardening import (
    InMemoryRateLimiter,
    SECURITY_HEADERS,
    require_idempotency_key,
    validate_request_size,
)
from maci_elyria.assumptions import assumption_precheck
from maci_elyria.audit_chain import append_audit_event as append_legacy_audit_event
from maci_elyria.audit_chain import verify_audit_chain
from maci_elyria.boundary_engine import engine_descriptor, resolve_boundary
from maci_elyria.models import sha256_json
from maci_elyria.proof import create_proof_transcript
from maci_elyria.rbac import authorize_action
from maci_elyria.receipt import issue_receipt
from maci_elyria.replay import replay_receipt
from maci_elyria.runtime_ready import runtime_status, should_fail_closed_for_runtime
from maci_elyria.security import authenticate_request, audit_enabled, production_gate_status, require_auth
from maci_elyria.signing import verify_receipt_signature
from maci_elyria.sqlite_runtime_store import (
    append_db_audit_event,
    export_receipts_for_tenant,
    get_proof_for_tenant,
    get_receipt_for_tenant,
    idempotency_seen,
    receipt_json_from_record,
    record_idempotency_key,
    store_packet,
    store_proof,
    store_receipt,
    verify_db_audit_ledger,
)
from maci_elyria.tenant_isolation import enforce_tenant_access
from maci_elyria.workflow import evaluate_workflow


app = Flask(__name__)
RATE_LIMITER = InMemoryRateLimiter()
PROOF_STORE: dict[str, dict[str, Any]] = {}

ROOT_DIR = Path(__file__).resolve().parents[1]
VIEWER_DIR = ROOT_DIR / "apps" / "proof-viewer"
BUYER_DEMO_DIR = ROOT_DIR / "apps" / "buyer-demo"


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _json_body() -> Dict[str, Any]:
    return request.get_json(force=True) or {}


def _safe_json_body() -> Dict[str, Any]:
    return request.get_json(silent=True) or {}


def _production_mode() -> bool:
    return os.getenv("APP_ENV") == "production"


def _security() -> dict:
    return getattr(g, "elyria_security", {}) or {}


def _tenant_id() -> str:
    return str(_security().get("tenant_id") or "public-review")


def _actor() -> str:
    return str(_security().get("actor") or "anonymous-reviewer")


def _roles() -> list[str]:
    return list(_security().get("roles") or [])


def _body_tenant_hint(body: Dict[str, Any]) -> str | None:
    direct = body.get("tenant_id")
    if direct:
        return str(direct)

    for key in ("movement_packet", "packet", "receipt", "proof"):
        value = body.get(key)
        if isinstance(value, dict) and value.get("tenant_id"):
            return str(value["tenant_id"])

    return None


def _endpoint_action(method: str, path: str) -> str | None:
    method = method.upper()

    if path.startswith("/proof/") and method == "GET":
        return "proof:read"

    mapping = {
        ("GET", "/security/status"): "audit:read",
        ("GET", "/audit/verify"): "audit:read",
        ("POST", "/evaluate"): "receipt:issue",
        ("POST", "/maci/intake"): "packet:intake",
        ("POST", "/assumptions/precheck"): "assumption:precheck",
        ("POST", "/workflow/harness"): "workflow:gate",
        ("POST", "/boundary/resolve"): "boundary:resolve",
        ("POST", "/receipt/create"): "receipt:issue",
        ("POST", "/receipt/verify"): "receipt:verify",
        ("GET", "/receipt/export"): "receipt:export",
        ("POST", "/replay/run"): "replay:run",
        ("POST", "/proof/create"): "proof:export",
    }
    return mapping.get((method, path))


def _audit(event_type: str, resource_id: str, outcome: str, details: dict | None = None) -> None:
    if not audit_enabled():
        return

    try:
        append_db_audit_event(
            event_type=event_type,
            tenant_id=_tenant_id(),
            actor=_actor(),
            resource_id=resource_id,
            outcome=outcome,
            details=details or {},
        )
    except Exception:
        pass


@app.before_request
def production_security_guard():
    if should_fail_closed_for_runtime(request.path, request.method):
        return jsonify({
            "error": "production_runtime_not_ready",
            "runtime_status": runtime_status(),
        }), 503

    size_check = validate_request_size(request.content_length)
    if not size_check.get("allowed"):
        return jsonify({"error": size_check["reason"], **size_check}), 413

    guard_result = authenticate_request(request.headers, request.path)
    if not guard_result.get("allowed"):
        return jsonify({
            "error": guard_result.get("reason", "request_denied"),
            "security_status": production_gate_status(),
        }), int(guard_result.get("status_code", 403))

    g.elyria_security = guard_result

    if _production_mode():
        rate_key = f"{_tenant_id()}:{_actor()}:{request.path}"
        rate = RATE_LIMITER.allow(rate_key)
        if not rate.get("allowed"):
            return jsonify({"error": "rate_limit_exceeded", **rate}), 429

    body = _safe_json_body()
    body_tenant = _body_tenant_hint(body)

    if body_tenant:
        tenant_access = enforce_tenant_access(
            actor_tenant_id=_tenant_id(),
            resource_tenant_id=body_tenant,
            action=f"{request.method}:{request.path}",
            actor_roles=_roles(),
        )
        if not tenant_access.get("allowed"):
            return jsonify({"error": "tenant_scope_violation", **tenant_access}), 403

    action = _endpoint_action(request.method, request.path)
    if require_auth() and action:
        rbac = authorize_action(
            _roles(),
            action,
            tenant_match=True,
            allow_cross_tenant_admin=False,
        )
        if not rbac.get("allowed"):
            return jsonify({"error": rbac.get("reason", "rbac_denied"), **rbac}), 403

    if _production_mode() and request.method.upper() in {"POST", "PUT", "PATCH", "DELETE"}:
        idem = require_idempotency_key(request.method, request.headers)
        if not idem.get("allowed"):
            return jsonify({"error": idem["reason"], **idem}), 400

        key = str(request.headers.get("Idempotency-Key"))
        body_digest = sha256_json(body)
        if idempotency_seen(key, _tenant_id(), body_digest):
            return jsonify({
                "error": "duplicate_idempotency_key",
                "tenant_id": _tenant_id(),
                "idempotency_key": key,
            }), 409
        record_idempotency_key(key, _tenant_id(), body_digest)


@app.after_request
def production_audit_event(response):
    for key, value in SECURITY_HEADERS.items():
        response.headers.setdefault(key, value)

    try:
        if audit_enabled() and request.path not in {"/health"}:
            append_legacy_audit_event({
                "method": request.method,
                "path": request.path,
                "status_code": response.status_code,
                "actor": _actor(),
                "tenant_id": _tenant_id(),
                "roles": _roles(),
            })
            append_db_audit_event(
                event_type="api_request",
                tenant_id=_tenant_id(),
                actor=_actor(),
                resource_id=request.path,
                outcome=str(response.status_code),
                details={
                    "method": request.method,
                    "path": request.path,
                    "roles": _roles(),
                },
            )
    except Exception:
        pass

    return response


@app.get("/")
def root():
    return send_from_directory(BUYER_DEMO_DIR, "index.html")


@app.get("/buyer-demo")
def buyer_demo():
    return send_from_directory(BUYER_DEMO_DIR, "index.html")


@app.get("/viewer")
def proof_viewer():
    return send_from_directory(VIEWER_DIR, "index.html")


@app.get("/runtime/status")
def runtime_status_route():
    status = runtime_status()
    return jsonify(status), 200 if status["runtime_ready"] or not status["production_mode"] else 503


@app.get("/security/status")
def security_status_route():
    return jsonify(production_gate_status())


@app.get("/audit/verify")
def audit_verify_route():
    return jsonify({
        "legacy_audit_chain": verify_audit_chain(),
        "sqlite_audit_ledger": verify_db_audit_ledger(),
    })


@app.get("/live")
def live():
    return jsonify({"status": "alive", "service": "maci-elyria-seam-pilot"})


@app.get("/ready")
def ready():
    gate = production_gate_status()
    production_mode = os.getenv("APP_ENV") == "production"
    ready_status = bool(gate.get("production_ready_gate")) if production_mode else True

    return jsonify({
        "status": "ready" if ready_status else "not_ready",
        "production_mode": production_mode,
        "production_gate": gate,
    }), 200 if ready_status else 503


@app.get("/health")
def health():
    return jsonify({"status": "ok", "service": "maci-elyria-seam-pilot", "engine": engine_descriptor()})


@app.get("/engine/status")
def engine_status():
    return jsonify(engine_descriptor())


@app.post("/evaluate")
def evaluate():
    packet = _json_body()
    packet.setdefault("tenant_id", _tenant_id())
    result = issue_receipt(packet)
    result["receipt"]["tenant_id"] = _tenant_id()
    store_packet(_tenant_id(), packet)
    store_receipt(_tenant_id(), result["receipt"])
    _audit("receipt_issue", result["receipt"]["receipt_id"], result["receipt"]["boundary_decision"])
    return jsonify(result)


@app.post("/maci/intake")
def maci_intake():
    body = _json_body()
    packet = {
        "packet_id": body.get("packet_id") or f"pkt_{uuid4().hex[:12]}",
        "tenant_id": _tenant_id(),
        "created_at": body.get("created_at") or _utc_now(),
        "source_layer": "MACI",
        "domain": body.get("domain", "ai-agent-action"),
        "actor": {
            "agent_id": body.get("agent_id", "agent-demo"),
            "human_requester": body.get("human_requester", "human-demo"),
            "system_origin": body.get("system_origin", "maci-intake-api"),
        },
        "proposed_movement": {
            "action": body.get("proposed_action", "send_customer_impacting_email"),
            "target": body.get("target", "customer"),
            "intended_consequence": body.get("intended_consequence", "customer-impacting communication"),
            "affected_party": body.get("affected_party", "customer"),
        },
        "maci_context": {
            "language_context": body.get("language_context", {"status": "CURRENT", "language": "en"}),
            "input_context": body.get("input_context", {"status": "CURRENT", "changed_context": {"status": "UNCHANGED"}}),
            "consequence_signal": body.get("consequence_signal", {"status": "CURRENT", "bind_attempt": False}),
            "risk_notes": body.get("risk_notes", []),
        },
        "boundary_inputs": {
            "standing": body.get("standing", {"status": "VALID"}),
            "authority": body.get("authority", {"status": "VALID"}),
            "evidence": body.get("evidence", {"status": "SUFFICIENT"}),
            "scope": body.get("scope", {"status": "VALID"}),
            "custody": body.get("custody", {"status": "VALID"}),
        },
        "seam_guard": {
            "maci_can_bind": bool(body.get("maci_can_bind", False)),
            "requires_elyria_boundary_result": True,
        },
    }
    stored = store_packet(_tenant_id(), packet)
    _audit("intake", packet["packet_id"], "stored", stored)
    return jsonify({"movement_packet": packet, "persistence": stored})


@app.post("/assumptions/precheck")
def assumptions_precheck():
    packet = _json_body()
    result = assumption_precheck(packet)
    _audit("assumption_precheck", str(packet.get("packet_id", "UNKNOWN_PACKET")), result.get("precheck_status", "UNKNOWN"))
    return jsonify(result)


@app.post("/workflow/harness")
def workflow_harness():
    body = _json_body()
    packet = body.get("movement_packet") or body
    result = evaluate_workflow(packet, workflow_id=body.get("workflow_id"), step_id=body.get("step_id") or "proposed_movement")
    _audit("workflow_gate", str(packet.get("packet_id", "UNKNOWN_PACKET")), result.get("workflow_status", "UNKNOWN"))
    return jsonify(result)


@app.post("/boundary/resolve")
def boundary_resolve():
    packet = _json_body()
    result = resolve_boundary(packet).as_dict()
    _audit("boundary_resolve", str(packet.get("packet_id", "UNKNOWN_PACKET")), result.get("boundary_decision", "UNKNOWN"))
    return jsonify(result)


@app.post("/receipt/create")
def receipt_create():
    body = _json_body()
    packet = body.get("movement_packet") or body.get("packet") or body
    packet.setdefault("tenant_id", _tenant_id())

    result = issue_receipt(packet, prior_receipt_hash=body.get("prior_receipt_hash"))
    result["receipt"]["tenant_id"] = _tenant_id()

    store_packet(_tenant_id(), packet)
    stored = store_receipt(_tenant_id(), result["receipt"])
    _audit("receipt_issue", result["receipt"]["receipt_id"], result["receipt"]["boundary_decision"], stored)

    result["persistence"] = stored
    return jsonify(result)


@app.post("/receipt/verify")
def receipt_verify():
    body = _json_body()
    receipt_id = body.get("receipt_id")

    if receipt_id:
        record = get_receipt_for_tenant(_tenant_id(), str(receipt_id))
        if not record:
            return jsonify({"error": "receipt_not_found_for_tenant", "receipt_id": receipt_id}), 404
        receipt = receipt_json_from_record(record)
    else:
        receipt = body.get("receipt") or body
        receipt_tenant = receipt.get("tenant_id")
        if receipt_tenant:
            access = enforce_tenant_access(
                actor_tenant_id=_tenant_id(),
                resource_tenant_id=str(receipt_tenant),
                action="receipt_verify",
                actor_roles=_roles(),
            )
            if not access.get("allowed"):
                return jsonify({"error": "tenant_scope_violation", **access}), 403

    result = verify_receipt_signature(receipt)
    _audit("verifier_action", str(receipt.get("receipt_id", receipt_id or "UNKNOWN_RECEIPT")), result.get("reason", "verified"), result)
    return jsonify(result)


@app.get("/receipt/export")
def receipt_export():
    return jsonify({"tenant_id": _tenant_id(), "receipts": export_receipts_for_tenant(_tenant_id())})


@app.post("/replay/run")
def replay_run():
    body = _json_body()

    if body.get("proof_id"):
        proof = get_proof_for_tenant(_tenant_id(), str(body["proof_id"]))
        if not proof:
            return jsonify({"error": "proof_not_found_for_tenant", "proof_id": body["proof_id"]}), 404
        packet = proof.get("movement_packet") or {}
        receipt = proof.get("receipt") or {}
    else:
        packet = body.get("movement_packet") or body.get("packet") or {}

        if body.get("receipt_id"):
            record = get_receipt_for_tenant(_tenant_id(), str(body["receipt_id"]))
            if not record:
                return jsonify({"error": "receipt_not_found_for_tenant", "receipt_id": body["receipt_id"]}), 404
            receipt = receipt_json_from_record(record)
        else:
            receipt = body.get("receipt") or issue_receipt(packet)["receipt"]

    receipt_tenant = receipt.get("tenant_id")
    if receipt_tenant:
        access = enforce_tenant_access(
            actor_tenant_id=_tenant_id(),
            resource_tenant_id=str(receipt_tenant),
            action="replay_run",
            actor_roles=_roles(),
        )
        if not access.get("allowed"):
            return jsonify({"error": "tenant_scope_violation", **access}), 403

    mode = body.get("replay_mode", "SAME_CONDITIONS")
    result = replay_receipt(packet, receipt, mode)
    _audit("replay_run", str(receipt.get("receipt_id", "UNKNOWN_RECEIPT")), result.get("replay_status", "UNKNOWN"), result)
    return jsonify(result)


@app.post("/proof/create")
def proof_create():
    body = _json_body()
    packet = body.get("movement_packet") or body.get("packet") or body
    packet.setdefault("tenant_id", _tenant_id())

    proof = create_proof_transcript(
        packet,
        case_name=body.get("case_name", packet.get("packet_id", "unnamed_case")),
        replay_modes=[body["replay_mode"]] if body.get("replay_mode") else None,
    )
    proof["tenant_id"] = _tenant_id()
    PROOF_STORE[proof["proof_id"]] = proof
    stored = store_proof(_tenant_id(), proof)

    _audit("verifier_action", proof["proof_id"], "proof_created", stored)
    return jsonify(proof)


@app.get("/proof/<proof_id>")
def proof_get(proof_id: str):
    proof = get_proof_for_tenant(_tenant_id(), proof_id)

    if not proof and not require_auth():
        proof = PROOF_STORE.get(proof_id)

    if not proof:
        return jsonify({"error": "proof_not_found_for_tenant", "proof_id": proof_id}), 404

    return jsonify(proof)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
