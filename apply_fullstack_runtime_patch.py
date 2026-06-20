from pathlib import Path
import json

ROOT = Path.cwd()

def write(path: str, content: str):
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    print(f"wrote {path}")

write("CLAIMS_BOUNDARY.md", """# Claims Boundary

## Admissible Public Claim

This repository demonstrates a public-safe MACI-on-Elyria consequence runtime where MACI operates as the customer-facing domain/context layer and Elyria/VERITA operates as the consequence-boundary runtime.

## Non-Negotiable Rule

```text
MACI may structure and submit domain/context signals.
MACI may not independently bind consequence.
Nothing becomes protected consequence until the Elyria boundary runtime admits formation.
Allowed Claims
MACI can structure proposed movement into a movement packet.
MACI can preserve language, input, context, risk, and consequence signals.
Elyria/VERITA can resolve boundary status before protected consequence forms.
Refusal, hold, escalation, narrowing, conditional admissibility, and admission are distinct.
Refused movement produces no-bind/non-formation proof.
Receipts bind packet, result, policy version, and replay token.
Replay can confirm same-condition results and changed-condition results.
Disallowed Claims
production certified
regulatory certification authority
legal opinion
medical treatment decision engine
financial advice or instrument approval
protected Elyria kernel exposure
commercial deployment rights
customer-managed production-candidate runtime
MACI-owned governance substrate
Commercial Boundary

Any client-facing deployment, resale, product integration, commercial pilot, managed-service use, or implementation of this pattern in customer offerings requires separate written scope.
""")

write("FULLSTACK_ARCHITECTURE.md", """# Full-Stack Architecture

Purpose

This document defines the public-safe full-stack expansion of the MACI-Elyria seam pilot.

Stack Shape
Customer / Buyer / Workflow
        ↓
MACI Surface Layer
        ↓
Structured Movement Packet
        ↓
Workflow Harness
        ↓
Elyria Consequence Boundary Runtime
        ↓
Standing / Authority / Evidence / Scope / Custody Resolver
        ↓
Result:
REFUSE / HOLD / ESCALATE / NARROW / CONDITIONALLY_ADMISSIBLE / ADMIT
        ↓
Formation Status:
NO_BIND / NON_FORMED / PENDING_REVIEW / NARROWED / CONDITIONALLY_ADMITTED / ADMITTED
        ↓
Receipt Service
        ↓
Replay Service
        ↓
Proof Viewer
Service Boundaries
Layer	Responsibility	Binding Authority
MACI intake	Domain/context intake and packet creation	No
Workflow harness	Wraps proposed movement into proof workflow	No
Boundary runtime	Resolves admissibility and formation status	Yes
Receipt service	Emits deterministic receipt for result	No, proof only
Replay service	Replays same/changed conditions	No, proof only
Witness service	Anchors public seam witness digest	No, proof only
Proof viewer	Displays transcript and replay result	No
Boundary Rule

A workflow may not proceed to protected effect unless the boundary runtime returns ADMIT or an explicitly allowed CONDITIONALLY_ADMISSIBLE state with human review.
""")

write("BUYER_REVIEW_GUIDE.md", """# Buyer Review Guide

What Buyers Should Look For
Can the system show the proposed movement?
Can it show who/what had standing?
Can it show authority?
Can it show evidence sufficiency?
Can it show scope?
Can it show custody?
Can it refuse?
Can it prove no-bind?
Can it prevent MACI or workflow from binding independently?
Can it generate a receipt?
Can it replay the result?
Can it replay under changed conditions?
Buyer Interpretation

This repository is not asking buyers to trust a dashboard. It shows whether a proposed movement was admitted, refused, held, escalated, narrowed, or conditionally admitted before protected consequence could form.

Failure-Closed Buyer Standard

If standing, authority, evidence, scope, custody, language certainty, or route closure fails, the buyer should expect no automatic binding.
""")

write("REGULATOR_REVIEW_GUIDE.md", """# Regulator Review Guide

This repository does not ask regulators to trust a dashboard.

It shows pre-operation boundary behavior.

Review Question
Did the system prove whether the proposed movement could become consequence before operation?
Inspectable Artifacts
movement packet
boundary inputs
standing result
authority result
evidence result
scope result
custody result
boundary result
formation status
no-bind status
receipt
replay
changed-condition replay
workflow stop/allow behavior
Regulatory Boundary

This repository is not a regulatory certification authority. It is a public-safe demonstration of consequence-boundary behavior and replayable proof.
""")

write("README.md", """# MACI-Elyria Seam Pilot / Full-Stack Consequence Runtime

Public-safe MACI-on-Elyria full-stack expansion demo.

MACI remains the customer-facing domain/context layer. Elyria/VERITA remains the protected consequence-boundary runtime underneath. MACI may structure and submit domain/context signals. MACI may not independently bind consequence.

Core Rule
MACI may inform.
MACI may not bind.
Workflow may not bypass.
Receipt must prove.
Replay must verify.
Refusal must produce no-bind.
Admitted movement is the only movement allowed to form protected consequence.
Runtime Path
Customer / Buyer / Workflow
        ↓
MACI Surface Layer
        ↓
Structured Movement Packet
        ↓
Workflow Harness
        ↓
Elyria Consequence Boundary Runtime
        ↓
Standing / Authority / Evidence / Scope / Custody Resolver
        ↓
REFUSE / HOLD / ESCALATE / NARROW / CONDITIONALLY_ADMISSIBLE / ADMIT
        ↓
NO_BIND / NON_FORMED / PENDING_REVIEW / NARROWED / CONDITIONALLY_ADMITTED / ADMITTED
        ↓
Receipt Service
        ↓
Replay Service
        ↓
Proof Viewer
Inversion

Old stack:

workflow acts → governance records

New substrate/runtime:

movement is proposed → boundary resolves → only admitted movement may proceed
What MACI Is

MACI is the customer-facing surface layer. It handles domain intake, workflow descriptions, business context, language/context signals, risk/context notes, evidence references, human-readable explanation, and structured movement packet creation.

MACI output is structured context for boundary review. It is not binding.

What Elyria/VERITA Does

Elyria/VERITA is the consequence-boundary runtime. It resolves proposed movement, attempted consequence, standing, authority, evidence sufficiency, scope, custody, route closure, no-bind status, receipt proof, and replay behavior.

Required Boundary Results
REFUSE
HOLD
ESCALATE
NARROW
CONDITIONALLY_ADMISSIBLE
ADMIT
HALT
Required Formation Statuses
NO_BIND
NON_FORMED
PENDING_REVIEW
NARROWED
CONDITIONALLY_ADMITTED
ADMITTED
INVALID
Quickstart

Run the API:

python -m api.app

Evaluate one packet:

curl -X POST http://localhost:8080/boundary/resolve \\
  -H "Content-Type: application/json" \\
  -d @corridors/ai-agent-action/packets/missing_authority.json

Run tests:

pytest
Public Boundary

This repository is a public-safe runtime demonstration. It does not expose protected Elyria kernel mechanics, private admissibility geometry, production enforcement rules, partner-specific deployment internals, legal advice, certification authority, or regulatory certification.
""")

write("pyproject.toml", """[project]
name = "maci-elyria-seam-pilot"
version = "0.2.0"
description = "Public-safe MACI-on-Elyria consequence-boundary runtime demo"
requires-python = ">=3.10"
dependencies = [
"flask>=3.0.0"
]

[project.optional-dependencies]
test = [
"pytest>=8.0.0"
]

[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["."]
""")

write("package.json", """{
"name": "maci-elyria-seam-pilot",
"version": "0.2.0",
"private": false,
"description": "Public-safe MACI-on-Elyria full-stack consequence runtime demo",
"scripts": {
"test": "pytest",
"api": "python -m api.app"
}
}
""")

write("docker-compose.yml", """services:
api:
image: python:3.11-slim
working_dir: /workspace
volumes:
- .:/workspace
command: sh -c "pip install -r requirements.txt && python -m api.app"
ports:
- "8080:8080"
""")

write("maci_elyria/models.py", """from future import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, Literal, Optional
import hashlib
import json

BoundaryDecision = Literal[
"CONDITIONALLY_ADMISSIBLE",
"REFUSE",
"HOLD",
"ESCALATE",
"NARROW",
"ADMIT",
"HALT",
"REPLAY_REQUIRED",
]

FormationStatus = Literal[
"NO_BIND",
"NON_FORMED",
"PENDING_REVIEW",
"NARROWED",
"CONDITIONALLY_ADMITTED",
"ADMITTED",
"INVALID",
]

CheckResult = Literal["PASS", "FAIL", "UNKNOWN"]

def canonical_json(value: Any) -> str:
return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)

def sha256_json(value: Any) -> str:
return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()

def utc_now_iso() -> str:
return datetime.now(timezone.utc).replace(microsecond=0).isoformat()

@dataclass(frozen=True)
class BoundaryResult:
input_packet_id: str
boundary_decision: BoundaryDecision
decision_class: str
admissibility_status: str
language_status: str
input_status: str
consequence_status: str
authority_status: str
changed_context_status: str
effect_binding_status: str
public_reason: Optional[str] = None
receipt_hash: Optional[str] = None
formation_status: FormationStatus = "NO_BIND"
reason_code: str = "UNSPECIFIED"
standing_result: CheckResult = "UNKNOWN"
authority_result: CheckResult = "UNKNOWN"
evidence_result: CheckResult = "UNKNOWN"
scope_result: CheckResult = "UNKNOWN"
custody_result: CheckResult = "UNKNOWN"
route_closure_result: CheckResult = "UNKNOWN"
maci_binding_status: str = "INFORM_ONLY"
explanation: str = ""

def as_dict(self) -> Dict[str, Any]:
    data = dict(self.__dict__)
    data["packet_id"] = self.input_packet_id
    data["boundary_result"] = self.boundary_decision
    return data

@dataclass(frozen=True)
class BoundaryReceipt:
receipt_type: str
input_packet_id: str
boundary_decision: str
effect_binding_status: str
public_reason_class: str
packet_hash: str
result_hash: str
replay_token: str
policy_version: str
prior_receipt_hash: Optional[str]
created_at_utc: str
formation_status: str = "NO_BIND"
no_bind_status: str = "NO_BIND"
witness_digest: str = "PUBLIC_SEAM_WITNESS"
receipt_id: str = ""
receipt_hash: str = field(default="")

def without_hash(self) -> Dict[str, Any]:
    data = dict(self.__dict__)
    data.pop("receipt_hash", None)
    return data

def with_hash(self) -> "BoundaryReceipt":
    data = self.without_hash()
    deterministic_core = {
        "receipt_type": data["receipt_type"],
        "input_packet_id": data["input_packet_id"],
        "packet_hash": data["packet_hash"],
        "result_hash": data["result_hash"],
        "policy_version": data["policy_version"],
        "formation_status": data["formation_status"],
        "no_bind_status": data["no_bind_status"],
        "prior_receipt_hash": data["prior_receipt_hash"],
    }
    receipt_hash = sha256_json(deterministic_core)
    receipt_id = data.get("receipt_id") or f"receipt_{receipt_hash[:16]}"
    return BoundaryReceipt(**{**data, "receipt_id": receipt_id}, receipt_hash=receipt_hash)

def as_dict(self) -> Dict[str, Any]:
    data = dict(self.__dict__)
    data["packet_id"] = self.input_packet_id
    return data

""")

write("maci_elyria/validator.py", """from future import annotations

from typing import Any

LEGACY_REQUIRED_FIELDS = [
"language_context",
"input_context",
"consequence_signal",
]

FULLSTACK_REQUIRED_FIELDS = [
"packet_id",
"source_layer",
"domain",
"actor",
"proposed_movement",
"maci_context",
"boundary_inputs",
"seam_guard",
]

MACI_CONTEXT_REQUIRED_FIELDS = [
"language_context",
"input_context",
"consequence_signal",
]

BOUNDARY_INPUT_REQUIRED_FIELDS = [
"standing",
"authority",
"evidence",
"scope",
"custody",
]

def _is_object(value: Any) -> bool:
return isinstance(value, dict)

def validate_packet(packet: dict) -> list[str]:
failures: list[str] = []

if not isinstance(packet, dict):
    return ["packet:not_object"]

if "maci_context" in packet or "boundary_inputs" in packet or "seam_guard" in packet:
    for field in FULLSTACK_REQUIRED_FIELDS:
        if field not in packet:
            failures.append(f"missing:{field}")
        elif field in {"actor", "proposed_movement", "maci_context", "boundary_inputs", "seam_guard"} and not _is_object(packet[field]):
            failures.append(f"not_object:{field}")

    maci_context = packet.get("maci_context", {})
    if _is_object(maci_context):
        for field in MACI_CONTEXT_REQUIRED_FIELDS:
            if field not in maci_context:
                failures.append(f"missing:maci_context.{field}")
            elif not _is_object(maci_context[field]):
                failures.append(f"not_object:maci_context.{field}")

    boundary_inputs = packet.get("boundary_inputs", {})
    if _is_object(boundary_inputs):
        for field in BOUNDARY_INPUT_REQUIRED_FIELDS:
            if field not in boundary_inputs:
                failures.append(f"missing:boundary_inputs.{field}")
            elif not _is_object(boundary_inputs[field]):
                failures.append(f"not_object:boundary_inputs.{field}")

    return failures

for field in LEGACY_REQUIRED_FIELDS:
    if field not in packet:
        failures.append(f"missing:{field}")
    elif not _is_object(packet[field]):
        failures.append(f"not_object:{field}")

return failures

""")

write("maci_elyria/resolver.py", """from future import annotations

from typing import Any, Dict, Tuple

from .models import BoundaryResult
from .validator import validate_packet

POLICY_VERSION = "ELYRIA_MACI_PUBLIC_SEAM_POLICY_V0_2"

def _status(obj: Dict[str, Any], key: str = "status", default: str = "UNKNOWN") -> str:
if not isinstance(obj, dict):
return default
return str(obj.get(key, default)).upper()

def _pass_fail(status: str) -> str:
if status in {"VALID", "PRESENT", "SUFFICIENT", "PASS", "CURRENT", "UNCHANGED", "IN_SCOPE", "NARROW_VALID"}:
return "PASS"
if status in {"MISSING", "INVALID", "REVOKED", "INSUFFICIENT", "FAIL", "CHANGED", "MATERIAL_CHANGE", "TOO_BROAD", "OUT_OF_SCOPE"}:
return "FAIL"
return "UNKNOWN"

def _extract(packet: Dict[str, Any]) -> Tuple[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]]:
if "maci_context" in packet:
maci_context = packet.get("maci_context", {})
boundary_inputs = packet.get("boundary_inputs", {})
seam_guard = packet.get("seam_guard", {})
return (
maci_context.get("language_context", {}),
maci_context.get("input_context", {}),
maci_context.get("consequence_signal", {}),
boundary_inputs,
seam_guard,
)

input_context = packet.get("input_context", {})
legacy_boundary_inputs = {
    "standing": {"status": "VALID"},
    "authority": input_context.get("authority", {"status": "UNKNOWN"}),
    "evidence": {"status": "SUFFICIENT"},
    "scope": {"status": "VALID"},
    "custody": {"status": "VALID"},
}
legacy_seam_guard = {
    "maci_can_bind": bool(packet.get("consequence_signal", {}).get("bind_attempt", False))
    and not bool(packet.get("consequence_signal", {}).get("boundary_controlled", False)),
    "requires_elyria_boundary_result": True,
}
return (
    packet.get("language_context", {}),
    input_context,
    packet.get("consequence_signal", {}),
    legacy_boundary_inputs,
    legacy_seam_guard,
)

def _make_result(
*,
packet_id: str,
boundary_decision: str,
decision_class: str,
formation_status: str,
effect_binding_status: str,
public_reason: str,
language_status: str,
input_status: str,
consequence_status: str,
authority_status: str,
changed_context_status: str,
standing_status: str = "UNKNOWN",
evidence_status: str = "UNKNOWN",
scope_status: str = "UNKNOWN",
custody_status: str = "UNKNOWN",
maci_binding_status: str = "INFORM_ONLY",
explanation: str = "",
) -> BoundaryResult:
return BoundaryResult(
input_packet_id=packet_id,
boundary_decision=boundary_decision, # type: ignore[arg-type]
decision_class=decision_class,
admissibility_status="ADMISSIBLE" if boundary_decision == "ADMIT" else "REVIEW_REQUIRED" if boundary_decision in {"HOLD", "ESCALATE", "CONDITIONALLY_ADMISSIBLE", "NARROW"} else "NOT_ADMISSIBLE",
language_status=language_status,
input_status=input_status,
consequence_status=consequence_status,
authority_status=authority_status,
changed_context_status=changed_context_status,
effect_binding_status=effect_binding_status,
public_reason=public_reason,
formation_status=formation_status, # type: ignore[arg-type]
reason_code=decision_class,
standing_result=_pass_fail(standing_status),
authority_result=_pass_fail(authority_status),
evidence_result=_pass_fail(evidence_status),
scope_result=_pass_fail(scope_status),
custody_result=_pass_fail(custody_status),
route_closure_result="PASS" if effect_binding_status != "BINDING_WITHOUT_BOUNDARY" else "FAIL",
maci_binding_status=maci_binding_status,
explanation=explanation or public_reason,
)

def evaluate_boundary(packet: Dict[str, Any]) -> BoundaryResult:
failures = validate_packet(packet)
packet_id = str(packet.get("packet_id", "UNKNOWN_PACKET"))

if failures:
    return _make_result(
        packet_id=packet_id,
        boundary_decision="HALT",
        decision_class="PAYLOAD_INVALID",
        formation_status="NO_BIND",
        effect_binding_status="NO_BIND",
        public_reason=";".join(failures),
        language_status="UNKNOWN",
        input_status="UNKNOWN",
        consequence_status="UNKNOWN",
        authority_status="UNKNOWN",
        changed_context_status="UNKNOWN",
        maci_binding_status="BIND_ATTEMPT_REFUSED",
        explanation="Packet failed structural validation; proposed movement cannot form consequence.",
    )

language, input_context, consequence, boundary_inputs, seam_guard = _extract(packet)

language_status = _status(language)
input_status = _status(input_context, default="CURRENT")
consequence_status = _status(consequence, default="CURRENT")
standing_status = _status(boundary_inputs.get("standing", {}))
authority_status = _status(boundary_inputs.get("authority", {}))
evidence_status = _status(boundary_inputs.get("evidence", {}))
scope_status = _status(boundary_inputs.get("scope", {}))
custody_status = _status(boundary_inputs.get("custody", {}))
changed_context_status = _status(input_context.get("changed_context", {}), default="UNCHANGED")
maci_can_bind = bool(seam_guard.get("maci_can_bind", False))
requires_boundary = bool(seam_guard.get("requires_elyria_boundary_result", True))

base = {
    "packet_id": packet_id,
    "language_status": language_status,
    "input_status": input_status,
    "consequence_status": consequence_status,
    "authority_status": authority_status,
    "changed_context_status": changed_context_status,
    "standing_status": standing_status,
    "evidence_status": evidence_status,
    "scope_status": scope_status,
    "custody_status": custody_status,
}

if maci_can_bind or not requires_boundary:
    return _make_result(**base, boundary_decision="HALT", decision_class="MACI_CANNOT_BIND_CONSEQUENCE", formation_status="NO_BIND", effect_binding_status="NO_BIND", public_reason="maci_signal_cannot_bind_consequence_by_itself", maci_binding_status="BIND_ATTEMPT_REFUSED")

if standing_status in {"MISSING", "INVALID", "REVOKED", "UNKNOWN"}:
    return _make_result(**base, boundary_decision="REFUSE", decision_class="MISSING_STANDING", formation_status="NO_BIND", effect_binding_status="NO_BIND", public_reason="standing_not_valid")

if authority_status in {"MISSING", "INVALID", "REVOKED", "UNKNOWN"}:
    return _make_result(**base, boundary_decision="REFUSE", decision_class="MISSING_AUTHORITY", formation_status="NO_BIND", effect_binding_status="NO_BIND", public_reason="authority_not_valid")

if custody_status in {"MISSING", "INVALID", "REVOKED", "UNKNOWN"}:
    return _make_result(**base, boundary_decision="REFUSE", decision_class="CUSTODY_INVALID", formation_status="NO_BIND", effect_binding_status="NO_BIND", public_reason="custody_not_valid")

if language_status in {"UNCERTAIN", "AMBIGUOUS", "LOW_CONFIDENCE"}:
    return _make_result(**base, boundary_decision="ESCALATE", decision_class="LANGUAGE_UNCERTAINTY", formation_status="NO_BIND", effect_binding_status="NO_BIND", public_reason="language_context_requires_review")

if changed_context_status in {"CHANGED", "MATERIAL_CHANGE"}:
    return _make_result(**base, boundary_decision="ESCALATE", decision_class="CHANGED_CONTEXT", formation_status="NO_BIND", effect_binding_status="NO_BIND", public_reason="changed_context_requires_review")

if evidence_status in {"MISSING", "INSUFFICIENT"}:
    return _make_result(**base, boundary_decision="HOLD", decision_class="INSUFFICIENT_EVIDENCE", formation_status="NO_BIND", effect_binding_status="NO_BIND", public_reason="evidence_not_sufficient")

if evidence_status == "UNKNOWN":
    return _make_result(**base, boundary_decision="ESCALATE", decision_class="EVIDENCE_UNKNOWN", formation_status="NO_BIND", effect_binding_status="NO_BIND", public_reason="evidence_unknown")

if scope_status in {"TOO_BROAD", "OVERBROAD", "OUT_OF_SCOPE"}:
    return _make_result(**base, boundary_decision="NARROW", decision_class="SCOPE_MISMATCH", formation_status="NARROWED", effect_binding_status="NO_BIND", public_reason="scope_requires_narrowing")

if scope_status in {"MISSING", "INVALID", "UNKNOWN"}:
    return _make_result(**base, boundary_decision="REFUSE", decision_class="SCOPE_INVALID", formation_status="NO_BIND", effect_binding_status="NO_BIND", public_reason="scope_not_valid")

if str(packet.get("proposed_movement", {}).get("execution_mode", "")).upper() == "ADMIT_ALLOWED":
    return _make_result(**base, boundary_decision="ADMIT", decision_class="ADMITTED", formation_status="ADMITTED", effect_binding_status="ADMITTED", public_reason="all_boundary_inputs_passed")

return _make_result(**base, boundary_decision="CONDITIONALLY_ADMISSIBLE", decision_class="BOUNDARY_SUPPORTED", formation_status="CONDITIONALLY_ADMITTED", effect_binding_status="BOUNDARY_RESULT_REQUIRED_BEFORE_BIND", public_reason="structured_context_supports_boundary_review")

""")

write("maci_elyria/receipt.py", """from future import annotations

from typing import Any, Dict, Optional

from .models import BoundaryReceipt, sha256_json, utc_now_iso
from .resolver import POLICY_VERSION, evaluate_boundary

def issue_receipt(packet: Dict[str, Any], prior_receipt_hash: Optional[str] = None) -> Dict[str, Any]:
result = evaluate_boundary(packet).as_dict()
packet_hash = sha256_json(packet)
result_hash = sha256_json(result)

replay_token = sha256_json({
    "packet_hash": packet_hash,
    "result_hash": result_hash,
    "policy_version": POLICY_VERSION,
    "prior_receipt_hash": prior_receipt_hash,
})

formation_status = str(result.get("formation_status", "NO_BIND"))
no_bind_status = "NO_BIND" if formation_status in {"NO_BIND", "NON_FORMED", "PENDING_REVIEW", "NARROWED", "CONDITIONALLY_ADMITTED"} else "BIND_ALLOWED"

receipt = BoundaryReceipt(
    receipt_type="ELYRIA_MACI_BOUNDARY_RECEIPT",
    input_packet_id=str(packet.get("packet_id", "UNKNOWN_PACKET")),
    boundary_decision=result["boundary_decision"],
    effect_binding_status=result["effect_binding_status"],
    public_reason_class=result["decision_class"],
    packet_hash=packet_hash,
    result_hash=result_hash,
    replay_token=replay_token,
    policy_version=POLICY_VERSION,
    prior_receipt_hash=prior_receipt_hash,
    created_at_utc=str(packet.get("created_at") or packet.get("created_at_utc") or utc_now_iso()),
    formation_status=formation_status,
    no_bind_status=no_bind_status,
    witness_digest=sha256_json({
        "packet_hash": packet_hash,
        "result_hash": result_hash,
        "policy_version": POLICY_VERSION,
        "witness": "PUBLIC_SEAM_WITNESS",
    }),
).with_hash()

result["receipt_hash"] = receipt.receipt_hash

return {"boundary_result": result, "receipt": receipt.as_dict()}

""")

write("maci_elyria/replay.py", """from future import annotations

from copy import deepcopy
from typing import Any, Dict

from .models import sha256_json
from .receipt import issue_receipt

def _full_boundary_inputs(packet: Dict[str, Any]) -> Dict[str, Any]:
if "boundary_inputs" not in packet:
packet["boundary_inputs"] = {
"standing": {"status": "VALID"},
"authority": packet.get("input_context", {}).get("authority", {"status": "VALID"}),
"evidence": {"status": "SUFFICIENT"},
"scope": {"status": "VALID"},
"custody": {"status": "VALID"},
}
return packet["boundary_inputs"]

def _mutate_for_mode(packet: Dict[str, Any], mode: str) -> Dict[str, Any]:
changed = deepcopy(packet)
mode = mode.upper()

if mode == "CHANGED_AUTHORITY":
    _full_boundary_inputs(changed)["authority"] = {"status": "REVOKED", "changed_by": "replay"}
elif mode == "CHANGED_EVIDENCE":
    _full_boundary_inputs(changed)["evidence"] = {"status": "INSUFFICIENT", "changed_by": "replay"}
elif mode == "CHANGED_SCOPE":
    _full_boundary_inputs(changed)["scope"] = {"status": "TOO_BROAD", "changed_by": "replay"}
elif mode == "CHANGED_CUSTODY":
    _full_boundary_inputs(changed)["custody"] = {"status": "INVALID", "changed_by": "replay"}
elif mode == "TAMPERED_PACKET":
    if "proposed_movement" in changed:
        changed["proposed_movement"]["action"] = "tampered_action"
    else:
        changed.setdefault("consequence_signal", {})["proposed_action"] = "tampered_action"

return changed

def _receipt_hash_valid(receipt: Dict[str, Any]) -> bool:
if not receipt or "receipt_hash" not in receipt:
return False
deterministic_core = {
"receipt_type": receipt.get("receipt_type"),
"input_packet_id": receipt.get("input_packet_id"),
"packet_hash": receipt.get("packet_hash"),
"result_hash": receipt.get("result_hash"),
"policy_version": receipt.get("policy_version"),
"formation_status": receipt.get("formation_status"),
"no_bind_status": receipt.get("no_bind_status"),
"prior_receipt_hash": receipt.get("prior_receipt_hash"),
}
return sha256_json(deterministic_core) == receipt.get("receipt_hash")

def replay_receipt(packet: Dict[str, Any], receipt: Dict[str, Any], replay_mode: str = "SAME_CONDITIONS") -> Dict[str, Any]:
mode = replay_mode.upper()

if mode == "TAMPERED_RECEIPT":
    tampered = dict(receipt)
    tampered["result_hash"] = "tampered"
    return {
        "replay_id": f"replay_{sha256_json({'mode': mode, 'packet': packet})[:16]}",
        "packet_id": str(packet.get("packet_id", "UNKNOWN_PACKET")),
        "receipt_id": receipt.get("receipt_id", "UNKNOWN_RECEIPT"),
        "replay_mode": mode,
        "replay_status": "INVALID",
        "original_boundary_result": receipt.get("boundary_decision"),
        "replayed_boundary_result": "INVALID",
        "original_formation_status": receipt.get("formation_status"),
        "replayed_formation_status": "INVALID",
        "packet_hash_matches": sha256_json(packet) == receipt.get("packet_hash"),
        "result_hash_matches": False,
        "policy_version_matches": False,
        "replay_token_matches": False,
        "receipt_hash_valid": _receipt_hash_valid(tampered),
        "proof": "Tampered receipt failed deterministic receipt validation.",
    }

replay_packet = _mutate_for_mode(packet, mode)
replayed = issue_receipt(replay_packet, prior_receipt_hash=receipt.get("prior_receipt_hash"))
replayed_receipt = replayed["receipt"]
replayed_boundary = replayed["boundary_result"]

packet_hash_matches = sha256_json(replay_packet) == receipt.get("packet_hash")
result_hash_matches = replayed_receipt.get("result_hash") == receipt.get("result_hash")
policy_version_matches = replayed_receipt.get("policy_version") == receipt.get("policy_version")
replay_token_matches = replayed_receipt.get("replay_token") == receipt.get("replay_token")

if mode == "SAME_CONDITIONS" and packet_hash_matches and result_hash_matches and policy_version_matches and replay_token_matches:
    status = "MATCH"
elif mode == "TAMPERED_PACKET":
    status = "MISMATCH"
elif replayed_boundary.get("boundary_decision") != receipt.get("boundary_decision"):
    status = "CHANGED_RESULT"
else:
    status = "MATCH" if result_hash_matches else "CHANGED_RESULT"

return {
    "replay_id": f"replay_{sha256_json({'mode': mode, 'packet': replay_packet})[:16]}",
    "packet_id": str(packet.get("packet_id", "UNKNOWN_PACKET")),
    "receipt_id": receipt.get("receipt_id", "UNKNOWN_RECEIPT"),
    "replay_mode": mode,
    "replay_status": status,
    "original_boundary_result": receipt.get("boundary_decision"),
    "replayed_boundary_result": replayed_boundary.get("boundary_decision"),
    "original_formation_status": receipt.get("formation_status"),
    "replayed_formation_status": replayed_boundary.get("formation_status"),
    "packet_hash_matches": packet_hash_matches,
    "result_hash_matches": result_hash_matches,
    "policy_version_matches": policy_version_matches,
    "replay_token_matches": replay_token_matches,
    "receipt_hash_valid": _receipt_hash_valid(receipt),
    "proof": f"Replay mode {mode} returned {status}. No automatic binding occurs unless the boundary admits formation.",
}

""")

write("api/app.py", """from future import annotations

from datetime import datetime, timezone
from typing import Any, Dict
from uuid import uuid4

from flask import Flask, jsonify, request

from maci_elyria.receipt import issue_receipt
from maci_elyria.replay import replay_receipt
from maci_elyria.resolver import evaluate_boundary

app = Flask(name)
PROOF_STORE: dict[str, dict[str, Any]] = {}

def _utc_now() -> str:
return datetime.now(timezone.utc).replace(microsecond=0).isoformat()

def _json_body() -> Dict[str, Any]:
return request.get_json(force=True) or {}

@app.get("/health")
def health():
return jsonify({"status": "ok", "service": "maci-elyria-seam-pilot"})

@app.post("/evaluate")
def evaluate():
packet = _json_body()
return jsonify(issue_receipt(packet))

@app.post("/maci/intake")
def maci_intake():
body = json_body()
packet = {
"packet_id": body.get("packet_id") or f"pkt{uuid4().hex[:12]}",
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
return jsonify({"movement_packet": packet})

@app.post("/workflow/harness")
def workflow_harness():
body = json_body()
packet = body.get("movement_packet") or body
boundary = evaluate_boundary(packet).as_dict()
workflow = {
"workflow_id": body.get("workflow_id") or f"wf{uuid4().hex[:12]}",
"step_id": body.get("step_id") or "proposed_movement",
"movement_packet_id": packet.get("packet_id", "UNKNOWN_PACKET"),
"boundary_result": boundary.get("boundary_decision"),
"formation_status": boundary.get("formation_status"),
"allowed_next_step": "execute_with_receipt" if boundary.get("boundary_decision") == "ADMIT" else "review_only",
"blocked_next_step": "protected_effect" if boundary.get("boundary_decision") != "ADMIT" else None,
}
return jsonify(workflow)

@app.post("/boundary/resolve")
def boundary_resolve():
packet = _json_body()
return jsonify(evaluate_boundary(packet).as_dict())

@app.post("/receipt/create")
def receipt_create():
body = _json_body()
packet = body.get("movement_packet") or body.get("packet") or body
return jsonify(issue_receipt(packet, prior_receipt_hash=body.get("prior_receipt_hash")))

@app.post("/replay/run")
def replay_run():
body = _json_body()
packet = body.get("movement_packet") or body.get("packet") or {}
receipt = body.get("receipt") or issue_receipt(packet)["receipt"]
mode = body.get("replay_mode", "SAME_CONDITIONS")
return jsonify(replay_receipt(packet, receipt, mode))

@app.post("/proof/create")
def proof_create():
body = json_body()
packet = body.get("movement_packet") or body.get("packet") or body
issued = issue_receipt(packet)
replay = replay_receipt(packet, issued["receipt"], body.get("replay_mode", "SAME_CONDITIONS"))
proof_id = body.get("proof_id") or f"proof{uuid4().hex[:12]}"
proof = {
"proof_id": proof_id,
"case_name": body.get("case_name", packet.get("packet_id", "unnamed_case")),
"movement_packet": packet,
"boundary_result": issued["boundary_result"],
"receipt": issued["receipt"],
"replay": replay,
"final_claim": f"The proposed movement resolved as {issued['boundary_result']['boundary_decision']} / {issued['boundary_result']['formation_status']} under the public seam policy.",
}
PROOF_STORE[proof_id] = proof
return jsonify(proof)

@app.get("/proof/<proof_id>")
def proof_get(proof_id: str):
proof = PROOF_STORE.get(proof_id)
if not proof:
return jsonify({"error": "proof_not_found", "proof_id": proof_id}), 404
return jsonify(proof)

if name == "main":
app.run(host="0.0.0.0", port=8080)
""")

movement_schema = {
"$schema": "https://json-schema.org/draft/2020-12/schema",
"title": "MACI Elyria Movement Packet",
"type": "object",
"required": ["packet_id", "created_at", "source_layer", "domain", "actor", "proposed_movement", "maci_context", "boundary_inputs", "seam_guard"],
"properties": {
"packet_id": {"type": "string"},
"created_at": {"type": "string"},
"source_layer": {"const": "MACI"},
"domain": {"type": "string"},
"actor": {"type": "object"},
"proposed_movement": {"type": "object"},
"maci_context": {"type": "object"},
"boundary_inputs": {"type": "object"},
"seam_guard": {"type": "object"}
}
}

boundary_schema = {
"$schema": "https://json-schema.org/draft/2020-12/schema",
"title": "Elyria Boundary Result",
"type": "object",
"required": ["packet_id", "boundary_result", "formation_status", "reason_code"],
"properties": {
"packet_id": {"type": "string"},
"boundary_result": {"enum": ["REFUSE", "HOLD", "ESCALATE", "NARROW", "CONDITIONALLY_ADMISSIBLE", "ADMIT", "HALT"]},
"formation_status": {"enum": ["NO_BIND", "NON_FORMED", "PENDING_REVIEW", "NARROWED", "CONDITIONALLY_ADMITTED", "ADMITTED", "INVALID"]},
"reason_code": {"type": "string"}
}
}

receipt_schema = {
"$schema": "https://json-schema.org/draft/2020-12/schema",
"title": "Elyria MACI Boundary Receipt",
"type": "object",
"required": ["receipt_id", "packet_hash", "result_hash", "policy_version", "formation_status", "no_bind_status", "receipt_hash", "witness_digest"]
}

replay_schema = {
"$schema": "https://json-schema.org/draft/2020-12/schema",
"title": "Elyria MACI Replay Result",
"type": "object",
"required": ["replay_id", "packet_id", "receipt_id", "replay_mode", "replay_status"]
}

write("packages/schemas/movement_packet.schema.json", json.dumps(movement_schema, indent=2) + "\n")
write("packages/schemas/boundary_result.schema.json", json.dumps(boundary_schema, indent=2) + "\n")
write("packages/schemas/receipt.schema.json", json.dumps(receipt_schema, indent=2) + "\n")
write("packages/schemas/replay.schema.json", json.dumps(replay_schema, indent=2) + "\n")

for path, title, body in [
("apps/operator-console/README.md", "Operator Console", "Operator-facing UI shell for submitting and inspecting proposed movement."),
("apps/buyer-demo/README.md", "Buyer Demo", "Buyer-facing demo shell for movement intake, boundary result, receipt, and replay."),
("apps/proof-viewer/README.md", "Proof Viewer", "Public-safe proof viewer for receipt, replay, and transcript inspection."),
("services/maci-intake-api/README.md", "MACI Intake API", "Receives customer/domain input and creates structured movement packets."),
("services/workflow-harness/README.md", "Workflow Harness", "Wraps movement packets into proof workflows and prevents bypass."),
("services/boundary-runtime/README.md", "Boundary Runtime", "Resolves standing, authority, evidence, scope, custody, route closure, and formation status."),
("services/receipt-service/README.md", "Receipt Service", "Issues deterministic receipts for packet, result, policy version, and witness digest."),
("services/replay-service/README.md", "Replay Service", "Runs same-condition and changed-condition replay."),
("services/witness-service/README.md", "Witness Service", "Provides public seam witness digest without exposing protected runtime internals."),
("packages/canonicalization/README.md", "Canonicalization", "Defines stable JSON hashing and deterministic receipt inputs."),
("packages/sdk-python/README.md", "Python SDK", "Future public-safe client wrapper for the MACI-Elyria API."),
("packages/sdk-typescript/README.md", "TypeScript SDK", "Future public-safe client wrapper for UI and buyer integrations."),
]:
write(path, f"# {title}\n\n{body}\n\nBoundary rule: MACI may inform. MACI may not bind consequence.\n")

write("corridors/ai-agent-action/README.md", """# AI Agent Action Corridor

Scenario: an AI agent wants to send a customer-impacting email.

This corridor proves that MACI can structure context, but cannot bind consequence. Elyria/VERITA resolves whether the proposed movement must refuse, hold, escalate, narrow, conditionally admit, or admit.
""")

def packet(name, overrides):
base = {
"packet_id": name,
"created_at": "2026-06-17T00:00:00+00:00",
"source_layer": "MACI",
"domain": "ai-agent-action",
"actor": {"agent_id": "agent-demo", "human_requester": "operator-demo", "system_origin": "buyer-demo"},
"proposed_movement": {"action": "send_customer_impacting_email", "target": "customer", "intended_consequence": "customer-impacting communication", "affected_party": "customer"},
"maci_context": {
"language_context": {"status": "CURRENT", "language": "en", "confidence": 0.98},
"input_context": {"status": "CURRENT", "changed_context": {"status": "UNCHANGED"}},
"consequence_signal": {"status": "CURRENT", "bind_attempt": False},
"risk_notes": []
},
"boundary_inputs": {
"standing": {"status": "VALID"},
"authority": {"status": "VALID"},
"evidence": {"status": "SUFFICIENT"},
"scope": {"status": "VALID"},
"custody": {"status": "VALID"}
},
"seam_guard": {"maci_can_bind": False, "requires_elyria_boundary_result": True}
}

def deep_update(target, changes):
    for k, v in changes.items():
        if isinstance(v, dict) and isinstance(target.get(k), dict):
            deep_update(target[k], v)
        else:
            target[k] = v

deep_update(base, overrides)
return json.dumps(base, indent=2) + "\n"

write("corridors/ai-agent-action/packets/valid_structured_context.json", packet("ai-agent-valid-structured-context", {}))
write("corridors/ai-agent-action/packets/missing_authority.json", packet("ai-agent-missing-authority", {"boundary_inputs": {"authority": {"status": "MISSING"}}}))
write("corridors/ai-agent-action/packets/uncertain_language.json", packet("ai-agent-uncertain-language", {"maci_context": {"language_context": {"status": "UNCERTAIN", "language": "en", "confidence": 0.41}}}))
write("corridors/ai-agent-action/packets/changed_context.json", packet("ai-agent-changed-context", {"maci_context": {"input_context": {"status": "CURRENT", "changed_context": {"status": "CHANGED"}}}}))
write("corridors/ai-agent-action/packets/maci_bind_attempt.json", packet("ai-agent-maci-bind-attempt", {"seam_guard": {"maci_can_bind": True, "requires_elyria_boundary_result": True}, "maci_context": {"consequence_signal": {"status": "CURRENT", "bind_attempt": True}}}))
write("corridors/ai-agent-action/packets/insufficient_evidence.json", packet("ai-agent-insufficient-evidence", {"boundary_inputs": {"evidence": {"status": "INSUFFICIENT"}}}))
write("corridors/ai-agent-action/packets/scope_too_broad.json", packet("ai-agent-scope-too-broad", {"boundary_inputs": {"scope": {"status": "TOO_BROAD"}}}))
write("corridors/ai-agent-action/packets/invalid_custody.json", packet("ai-agent-invalid-custody", {"boundary_inputs": {"custody": {"status": "INVALID"}}}))

expected = {
"valid_structured_context": {"boundary_result": "CONDITIONALLY_ADMISSIBLE", "formation_status": "CONDITIONALLY_ADMITTED"},
"missing_authority": {"boundary_result": "REFUSE", "formation_status": "NO_BIND", "reason_code": "MISSING_AUTHORITY"},
"uncertain_language": {"boundary_result": "ESCALATE", "formation_status": "NO_BIND", "reason_code": "LANGUAGE_UNCERTAINTY"},
"changed_context": {"boundary_result": "ESCALATE", "formation_status": "NO_BIND", "reason_code": "CHANGED_CONTEXT"},
"maci_bind_attempt": {"boundary_result": "HALT", "formation_status": "NO_BIND", "reason_code": "MACI_CANNOT_BIND_CONSEQUENCE"},
"insufficient_evidence": {"boundary_result": "HOLD", "formation_status": "NO_BIND", "reason_code": "INSUFFICIENT_EVIDENCE"},
"scope_too_broad": {"boundary_result": "NARROW", "formation_status": "NARROWED", "reason_code": "SCOPE_MISMATCH"},
"invalid_custody": {"boundary_result": "REFUSE", "formation_status": "NO_BIND", "reason_code": "CUSTODY_INVALID"}
}

for name, value in expected.items():
write(f"corridors/ai-agent-action/expected_results/{name}.json", json.dumps(value, indent=2) + "\n")

for corridor in ["healthcare", "finance", "procurement"]:
write(f"corridors/{corridor}/README.md", f"# {corridor.title()} Corridor\n\nReserved public-safe corridor scaffold.\n")

for proof_dir in [
"proofs/refusal-cases",
"proofs/hold-cases",
"proofs/no-bind-cases",
"proofs/changed-condition-replay",
"proofs/non-bypass-cases",
"proofs/proof-transcripts",
]:
write(f"{proof_dir}/.gitkeep", "")

write("proofs/README.md", """# Proofs

Proof transcripts bind:

movement packet
boundary result
receipt
replay result
final no-bind/admission claim

No workflow proof is valid unless it shows whether movement was allowed, refused, held, escalated, narrowed, or admitted before protected consequence could form.
""")

write("tests/test_fullstack_runtime_expansion.py", """import json
from pathlib import Path

from maci_elyria.receipt import issue_receipt
from maci_elyria.replay import replay_receipt

def load_packet(name: str):
return json.loads(Path(f"corridors/ai-agent-action/packets/{name}.json").read_text())

def assert_boundary(name: str, result: str, formation: str):
issued = issue_receipt(load_packet(name))
boundary = issued["boundary_result"]
assert boundary["boundary_decision"] == result
assert boundary["boundary_result"] == result
assert boundary["formation_status"] == formation
assert issued["receipt"]["formation_status"] == formation

def test_valid_packet_conditionally_admissible():
assert_boundary("valid_structured_context", "CONDITIONALLY_ADMISSIBLE", "CONDITIONALLY_ADMITTED")

def test_missing_authority_refuses_no_bind():
assert_boundary("missing_authority", "REFUSE", "NO_BIND")

def test_uncertain_language_escalates_no_bind():
assert_boundary("uncertain_language", "ESCALATE", "NO_BIND")

def test_changed_context_escalates_no_bind():
assert_boundary("changed_context", "ESCALATE", "NO_BIND")

def test_maci_bind_attempt_halts():
assert_boundary("maci_bind_attempt", "HALT", "NO_BIND")

def test_insufficient_evidence_holds_no_bind():
assert_boundary("insufficient_evidence", "HOLD", "NO_BIND")

def test_invalid_scope_narrows():
assert_boundary("scope_too_broad", "NARROW", "NARROWED")

def test_invalid_custody_refuses_no_bind():
assert_boundary("invalid_custody", "REFUSE", "NO_BIND")

def test_tampered_packet_replay_mismatch():
packet = load_packet("valid_structured_context")
issued = issue_receipt(packet)
replay = replay_receipt(packet, issued["receipt"], "TAMPERED_PACKET")
assert replay["replay_status"] == "MISMATCH"

def test_tampered_receipt_replay_invalid():
packet = load_packet("valid_structured_context")
issued = issue_receipt(packet)
replay = replay_receipt(packet, issued["receipt"], "TAMPERED_RECEIPT")
assert replay["replay_status"] == "INVALID"

def test_changed_authority_replay_changes_result():
packet = load_packet("valid_structured_context")
issued = issue_receipt(packet)
replay = replay_receipt(packet, issued["receipt"], "CHANGED_AUTHORITY")
assert replay["replay_status"] == "CHANGED_RESULT"
assert replay["replayed_boundary_result"] == "REFUSE"

def test_changed_evidence_replay_holds_or_changes():
packet = load_packet("valid_structured_context")
issued = issue_receipt(packet)
replay = replay_receipt(packet, issued["receipt"], "CHANGED_EVIDENCE")
assert replay["replay_status"] == "CHANGED_RESULT"
assert replay["replayed_boundary_result"] == "HOLD"

def test_changed_scope_replay_narrows():
packet = load_packet("valid_structured_context")
issued = issue_receipt(packet)
replay = replay_receipt(packet, issued["receipt"], "CHANGED_SCOPE")
assert replay["replay_status"] == "CHANGED_RESULT"
assert replay["replayed_boundary_result"] == "NARROW"
""")

print("Full-stack runtime patch applied.")
PYEOFcat > apply_fullstack_runtime_patch.py <<'PYEOF'
from pathlib import Path
import json

ROOT = Path.cwd()

def write(path: str, content: str):
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    print(f"wrote {path}")

write("CLAIMS_BOUNDARY.md", """# Claims Boundary

## Admissible Public Claim

This repository demonstrates a public-safe MACI-on-Elyria consequence runtime where MACI operates as the customer-facing domain/context layer and Elyria/VERITA operates as the consequence-boundary runtime.

## Non-Negotiable Rule

```text
MACI may structure and submit domain/context signals.
MACI may not independently bind consequence.
Nothing becomes protected consequence until the Elyria boundary runtime admits formation.
Allowed Claims
MACI can structure proposed movement into a movement packet.
MACI can preserve language, input, context, risk, and consequence signals.
Elyria/VERITA can resolve boundary status before protected consequence forms.
Refusal, hold, escalation, narrowing, conditional admissibility, and admission are distinct.
Refused movement produces no-bind/non-formation proof.
Receipts bind packet, result, policy version, and replay token.
Replay can confirm same-condition results and changed-condition results.
Disallowed Claims
production certified
regulatory certification authority
legal opinion
medical treatment decision engine
financial advice or instrument approval
protected Elyria kernel exposure
commercial deployment rights
customer-managed production-candidate runtime
MACI-owned governance substrate
Commercial Boundary

Any client-facing deployment, resale, product integration, commercial pilot, managed-service use, or implementation of this pattern in customer offerings requires separate written scope.
""")

write("FULLSTACK_ARCHITECTURE.md", """# Full-Stack Architecture

Purpose

This document defines the public-safe full-stack expansion of the MACI-Elyria seam pilot.

Stack Shape
Customer / Buyer / Workflow
        ↓
MACI Surface Layer
        ↓
Structured Movement Packet
        ↓
Workflow Harness
        ↓
Elyria Consequence Boundary Runtime
        ↓
Standing / Authority / Evidence / Scope / Custody Resolver
        ↓
Result:
REFUSE / HOLD / ESCALATE / NARROW / CONDITIONALLY_ADMISSIBLE / ADMIT
        ↓
Formation Status:
NO_BIND / NON_FORMED / PENDING_REVIEW / NARROWED / CONDITIONALLY_ADMITTED / ADMITTED
        ↓
Receipt Service
        ↓
Replay Service
        ↓
Proof Viewer
Service Boundaries
Layer	Responsibility	Binding Authority
MACI intake	Domain/context intake and packet creation	No
Workflow harness	Wraps proposed movement into proof workflow	No
Boundary runtime	Resolves admissibility and formation status	Yes
Receipt service	Emits deterministic receipt for result	No, proof only
Replay service	Replays same/changed conditions	No, proof only
Witness service	Anchors public seam witness digest	No, proof only
Proof viewer	Displays transcript and replay result	No
Boundary Rule

A workflow may not proceed to protected effect unless the boundary runtime returns ADMIT or an explicitly allowed CONDITIONALLY_ADMISSIBLE state with human review.
""")

write("BUYER_REVIEW_GUIDE.md", """# Buyer Review Guide

What Buyers Should Look For
Can the system show the proposed movement?
Can it show who/what had standing?
Can it show authority?
Can it show evidence sufficiency?
Can it show scope?
Can it show custody?
Can it refuse?
Can it prove no-bind?
Can it prevent MACI or workflow from binding independently?
Can it generate a receipt?
Can it replay the result?
Can it replay under changed conditions?
Buyer Interpretation

This repository is not asking buyers to trust a dashboard. It shows whether a proposed movement was admitted, refused, held, escalated, narrowed, or conditionally admitted before protected consequence could form.

Failure-Closed Buyer Standard

If standing, authority, evidence, scope, custody, language certainty, or route closure fails, the buyer should expect no automatic binding.
""")

write("REGULATOR_REVIEW_GUIDE.md", """# Regulator Review Guide

This repository does not ask regulators to trust a dashboard.

It shows pre-operation boundary behavior.

Review Question
Did the system prove whether the proposed movement could become consequence before operation?
Inspectable Artifacts
movement packet
boundary inputs
standing result
authority result
evidence result
scope result
custody result
boundary result
formation status
no-bind status
receipt
replay
changed-condition replay
workflow stop/allow behavior
Regulatory Boundary

This repository is not a regulatory certification authority. It is a public-safe demonstration of consequence-boundary behavior and replayable proof.
""")

write("README.md", """# MACI-Elyria Seam Pilot / Full-Stack Consequence Runtime

Public-safe MACI-on-Elyria full-stack expansion demo.

MACI remains the customer-facing domain/context layer. Elyria/VERITA remains the protected consequence-boundary runtime underneath. MACI may structure and submit domain/context signals. MACI may not independently bind consequence.

Core Rule
MACI may inform.
MACI may not bind.
Workflow may not bypass.
Receipt must prove.
Replay must verify.
Refusal must produce no-bind.
Admitted movement is the only movement allowed to form protected consequence.
Runtime Path
Customer / Buyer / Workflow
        ↓
MACI Surface Layer
        ↓
Structured Movement Packet
        ↓
Workflow Harness
        ↓
Elyria Consequence Boundary Runtime
        ↓
Standing / Authority / Evidence / Scope / Custody Resolver
        ↓
REFUSE / HOLD / ESCALATE / NARROW / CONDITIONALLY_ADMISSIBLE / ADMIT
        ↓
NO_BIND / NON_FORMED / PENDING_REVIEW / NARROWED / CONDITIONALLY_ADMITTED / ADMITTED
        ↓
Receipt Service
        ↓
Replay Service
        ↓
Proof Viewer
Inversion

Old stack:

workflow acts → governance records

New substrate/runtime:

movement is proposed → boundary resolves → only admitted movement may proceed
What MACI Is

MACI is the customer-facing surface layer. It handles domain intake, workflow descriptions, business context, language/context signals, risk/context notes, evidence references, human-readable explanation, and structured movement packet creation.

MACI output is structured context for boundary review. It is not binding.

What Elyria/VERITA Does

Elyria/VERITA is the consequence-boundary runtime. It resolves proposed movement, attempted consequence, standing, authority, evidence sufficiency, scope, custody, route closure, no-bind status, receipt proof, and replay behavior.

Required Boundary Results
REFUSE
HOLD
ESCALATE
NARROW
CONDITIONALLY_ADMISSIBLE
ADMIT
HALT
Required Formation Statuses
NO_BIND
NON_FORMED
PENDING_REVIEW
NARROWED
CONDITIONALLY_ADMITTED
ADMITTED
INVALID
Quickstart

Run the API:

python -m api.app

Evaluate one packet:

curl -X POST http://localhost:8080/boundary/resolve \\
  -H "Content-Type: application/json" \\
  -d @corridors/ai-agent-action/packets/missing_authority.json

Run tests:

pytest
Public Boundary

This repository is a public-safe runtime demonstration. It does not expose protected Elyria kernel mechanics, private admissibility geometry, production enforcement rules, partner-specific deployment internals, legal advice, certification authority, or regulatory certification.
""")

write("pyproject.toml", """[project]
name = "maci-elyria-seam-pilot"
version = "0.2.0"
description = "Public-safe MACI-on-Elyria consequence-boundary runtime demo"
requires-python = ">=3.10"
dependencies = [
"flask>=3.0.0"
]

[project.optional-dependencies]
test = [
"pytest>=8.0.0"
]

[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["."]
""")

write("package.json", """{
"name": "maci-elyria-seam-pilot",
"version": "0.2.0",
"private": false,
"description": "Public-safe MACI-on-Elyria full-stack consequence runtime demo",
"scripts": {
"test": "pytest",
"api": "python -m api.app"
}
}
""")

write("docker-compose.yml", """services:
api:
image: python:3.11-slim
working_dir: /workspace
volumes:
- .:/workspace
command: sh -c "pip install -r requirements.txt && python -m api.app"
ports:
- "8080:8080"
""")

write("maci_elyria/models.py", """from future import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, Literal, Optional
import hashlib
import json

BoundaryDecision = Literal[
"CONDITIONALLY_ADMISSIBLE",
"REFUSE",
"HOLD",
"ESCALATE",
"NARROW",
"ADMIT",
"HALT",
"REPLAY_REQUIRED",
]

FormationStatus = Literal[
"NO_BIND",
"NON_FORMED",
"PENDING_REVIEW",
"NARROWED",
"CONDITIONALLY_ADMITTED",
"ADMITTED",
"INVALID",
]

CheckResult = Literal["PASS", "FAIL", "UNKNOWN"]

def canonical_json(value: Any) -> str:
return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)

def sha256_json(value: Any) -> str:
return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()

def utc_now_iso() -> str:
return datetime.now(timezone.utc).replace(microsecond=0).isoformat()

@dataclass(frozen=True)
class BoundaryResult:
input_packet_id: str
boundary_decision: BoundaryDecision
decision_class: str
admissibility_status: str
language_status: str
input_status: str
consequence_status: str
authority_status: str
changed_context_status: str
effect_binding_status: str
public_reason: Optional[str] = None
receipt_hash: Optional[str] = None
formation_status: FormationStatus = "NO_BIND"
reason_code: str = "UNSPECIFIED"
standing_result: CheckResult = "UNKNOWN"
authority_result: CheckResult = "UNKNOWN"
evidence_result: CheckResult = "UNKNOWN"
scope_result: CheckResult = "UNKNOWN"
custody_result: CheckResult = "UNKNOWN"
route_closure_result: CheckResult = "UNKNOWN"
maci_binding_status: str = "INFORM_ONLY"
explanation: str = ""

def as_dict(self) -> Dict[str, Any]:
    data = dict(self.__dict__)
    data["packet_id"] = self.input_packet_id
    data["boundary_result"] = self.boundary_decision
    return data

@dataclass(frozen=True)
class BoundaryReceipt:
receipt_type: str
input_packet_id: str
boundary_decision: str
effect_binding_status: str
public_reason_class: str
packet_hash: str
result_hash: str
replay_token: str
policy_version: str
prior_receipt_hash: Optional[str]
created_at_utc: str
formation_status: str = "NO_BIND"
no_bind_status: str = "NO_BIND"
witness_digest: str = "PUBLIC_SEAM_WITNESS"
receipt_id: str = ""
receipt_hash: str = field(default="")

def without_hash(self) -> Dict[str, Any]:
    data = dict(self.__dict__)
    data.pop("receipt_hash", None)
    return data

def with_hash(self) -> "BoundaryReceipt":
    data = self.without_hash()
    deterministic_core = {
        "receipt_type": data["receipt_type"],
        "input_packet_id": data["input_packet_id"],
        "packet_hash": data["packet_hash"],
        "result_hash": data["result_hash"],
        "policy_version": data["policy_version"],
        "formation_status": data["formation_status"],
        "no_bind_status": data["no_bind_status"],
        "prior_receipt_hash": data["prior_receipt_hash"],
    }
    receipt_hash = sha256_json(deterministic_core)
    receipt_id = data.get("receipt_id") or f"receipt_{receipt_hash[:16]}"
    return BoundaryReceipt(**{**data, "receipt_id": receipt_id}, receipt_hash=receipt_hash)

def as_dict(self) -> Dict[str, Any]:
    data = dict(self.__dict__)
    data["packet_id"] = self.input_packet_id
    return data

""")

write("maci_elyria/validator.py", """from future import annotations

from typing import Any

LEGACY_REQUIRED_FIELDS = [
"language_context",
"input_context",
"consequence_signal",
]

FULLSTACK_REQUIRED_FIELDS = [
"packet_id",
"source_layer",
"domain",
"actor",
"proposed_movement",
"maci_context",
"boundary_inputs",
"seam_guard",
]

MACI_CONTEXT_REQUIRED_FIELDS = [
"language_context",
"input_context",
"consequence_signal",
]

BOUNDARY_INPUT_REQUIRED_FIELDS = [
"standing",
"authority",
"evidence",
"scope",
"custody",
]

def _is_object(value: Any) -> bool:
return isinstance(value, dict)

def validate_packet(packet: dict) -> list[str]:
failures: list[str] = []

if not isinstance(packet, dict):
    return ["packet:not_object"]

if "maci_context" in packet or "boundary_inputs" in packet or "seam_guard" in packet:
    for field in FULLSTACK_REQUIRED_FIELDS:
        if field not in packet:
            failures.append(f"missing:{field}")
        elif field in {"actor", "proposed_movement", "maci_context", "boundary_inputs", "seam_guard"} and not _is_object(packet[field]):
            failures.append(f"not_object:{field}")

    maci_context = packet.get("maci_context", {})
    if _is_object(maci_context):
        for field in MACI_CONTEXT_REQUIRED_FIELDS:
            if field not in maci_context:
                failures.append(f"missing:maci_context.{field}")
            elif not _is_object(maci_context[field]):
                failures.append(f"not_object:maci_context.{field}")

    boundary_inputs = packet.get("boundary_inputs", {})
    if _is_object(boundary_inputs):
        for field in BOUNDARY_INPUT_REQUIRED_FIELDS:
            if field not in boundary_inputs:
                failures.append(f"missing:boundary_inputs.{field}")
            elif not _is_object(boundary_inputs[field]):
                failures.append(f"not_object:boundary_inputs.{field}")

    return failures

for field in LEGACY_REQUIRED_FIELDS:
    if field not in packet:
        failures.append(f"missing:{field}")
    elif not _is_object(packet[field]):
        failures.append(f"not_object:{field}")

return failures

""")

write("maci_elyria/resolver.py", """from future import annotations

from typing import Any, Dict, Tuple

from .models import BoundaryResult
from .validator import validate_packet

POLICY_VERSION = "ELYRIA_MACI_PUBLIC_SEAM_POLICY_V0_2"

def _status(obj: Dict[str, Any], key: str = "status", default: str = "UNKNOWN") -> str:
if not isinstance(obj, dict):
return default
return str(obj.get(key, default)).upper()

def _pass_fail(status: str) -> str:
if status in {"VALID", "PRESENT", "SUFFICIENT", "PASS", "CURRENT", "UNCHANGED", "IN_SCOPE", "NARROW_VALID"}:
return "PASS"
if status in {"MISSING", "INVALID", "REVOKED", "INSUFFICIENT", "FAIL", "CHANGED", "MATERIAL_CHANGE", "TOO_BROAD", "OUT_OF_SCOPE"}:
return "FAIL"
return "UNKNOWN"

def _extract(packet: Dict[str, Any]) -> Tuple[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]]:
if "maci_context" in packet:
maci_context = packet.get("maci_context", {})
boundary_inputs = packet.get("boundary_inputs", {})
seam_guard = packet.get("seam_guard", {})
return (
maci_context.get("language_context", {}),
maci_context.get("input_context", {}),
maci_context.get("consequence_signal", {}),
boundary_inputs,
seam_guard,
)

input_context = packet.get("input_context", {})
legacy_boundary_inputs = {
    "standing": {"status": "VALID"},
    "authority": input_context.get("authority", {"status": "UNKNOWN"}),
    "evidence": {"status": "SUFFICIENT"},
    "scope": {"status": "VALID"},
    "custody": {"status": "VALID"},
}
legacy_seam_guard = {
    "maci_can_bind": bool(packet.get("consequence_signal", {}).get("bind_attempt", False))
    and not bool(packet.get("consequence_signal", {}).get("boundary_controlled", False)),
    "requires_elyria_boundary_result": True,
}
return (
    packet.get("language_context", {}),
    input_context,
    packet.get("consequence_signal", {}),
    legacy_boundary_inputs,
    legacy_seam_guard,
)

def _make_result(
*,
packet_id: str,
boundary_decision: str,
decision_class: str,
formation_status: str,
effect_binding_status: str,
public_reason: str,
language_status: str,
input_status: str,
consequence_status: str,
authority_status: str,
changed_context_status: str,
standing_status: str = "UNKNOWN",
evidence_status: str = "UNKNOWN",
scope_status: str = "UNKNOWN",
custody_status: str = "UNKNOWN",
maci_binding_status: str = "INFORM_ONLY",
explanation: str = "",
) -> BoundaryResult:
return BoundaryResult(
input_packet_id=packet_id,
boundary_decision=boundary_decision, # type: ignore[arg-type]
decision_class=decision_class,
admissibility_status="ADMISSIBLE" if boundary_decision == "ADMIT" else "REVIEW_REQUIRED" if boundary_decision in {"HOLD", "ESCALATE", "CONDITIONALLY_ADMISSIBLE", "NARROW"} else "NOT_ADMISSIBLE",
language_status=language_status,
input_status=input_status,
consequence_status=consequence_status,
authority_status=authority_status,
changed_context_status=changed_context_status,
effect_binding_status=effect_binding_status,
public_reason=public_reason,
formation_status=formation_status, # type: ignore[arg-type]
reason_code=decision_class,
standing_result=_pass_fail(standing_status),
authority_result=_pass_fail(authority_status),
evidence_result=_pass_fail(evidence_status),
scope_result=_pass_fail(scope_status),
custody_result=_pass_fail(custody_status),
route_closure_result="PASS" if effect_binding_status != "BINDING_WITHOUT_BOUNDARY" else "FAIL",
maci_binding_status=maci_binding_status,
explanation=explanation or public_reason,
)

def evaluate_boundary(packet: Dict[str, Any]) -> BoundaryResult:
failures = validate_packet(packet)
packet_id = str(packet.get("packet_id", "UNKNOWN_PACKET"))

if failures:
    return _make_result(
        packet_id=packet_id,
        boundary_decision="HALT",
        decision_class="PAYLOAD_INVALID",
        formation_status="NO_BIND",
        effect_binding_status="NO_BIND",
        public_reason=";".join(failures),
        language_status="UNKNOWN",
        input_status="UNKNOWN",
        consequence_status="UNKNOWN",
        authority_status="UNKNOWN",
        changed_context_status="UNKNOWN",
        maci_binding_status="BIND_ATTEMPT_REFUSED",
        explanation="Packet failed structural validation; proposed movement cannot form consequence.",
    )

language, input_context, consequence, boundary_inputs, seam_guard = _extract(packet)

language_status = _status(language)
input_status = _status(input_context, default="CURRENT")
consequence_status = _status(consequence, default="CURRENT")
standing_status = _status(boundary_inputs.get("standing", {}))
authority_status = _status(boundary_inputs.get("authority", {}))
evidence_status = _status(boundary_inputs.get("evidence", {}))
scope_status = _status(boundary_inputs.get("scope", {}))
custody_status = _status(boundary_inputs.get("custody", {}))
changed_context_status = _status(input_context.get("changed_context", {}), default="UNCHANGED")
maci_can_bind = bool(seam_guard.get("maci_can_bind", False))
requires_boundary = bool(seam_guard.get("requires_elyria_boundary_result", True))

base = {
    "packet_id": packet_id,
    "language_status": language_status,
    "input_status": input_status,
    "consequence_status": consequence_status,
    "authority_status": authority_status,
    "changed_context_status": changed_context_status,
    "standing_status": standing_status,
    "evidence_status": evidence_status,
    "scope_status": scope_status,
    "custody_status": custody_status,
}

if maci_can_bind or not requires_boundary:
    return _make_result(**base, boundary_decision="HALT", decision_class="MACI_CANNOT_BIND_CONSEQUENCE", formation_status="NO_BIND", effect_binding_status="NO_BIND", public_reason="maci_signal_cannot_bind_consequence_by_itself", maci_binding_status="BIND_ATTEMPT_REFUSED")

if standing_status in {"MISSING", "INVALID", "REVOKED", "UNKNOWN"}:
    return _make_result(**base, boundary_decision="REFUSE", decision_class="MISSING_STANDING", formation_status="NO_BIND", effect_binding_status="NO_BIND", public_reason="standing_not_valid")

if authority_status in {"MISSING", "INVALID", "REVOKED", "UNKNOWN"}:
    return _make_result(**base, boundary_decision="REFUSE", decision_class="MISSING_AUTHORITY", formation_status="NO_BIND", effect_binding_status="NO_BIND", public_reason="authority_not_valid")

if custody_status in {"MISSING", "INVALID", "REVOKED", "UNKNOWN"}:
    return _make_result(**base, boundary_decision="REFUSE", decision_class="CUSTODY_INVALID", formation_status="NO_BIND", effect_binding_status="NO_BIND", public_reason="custody_not_valid")

if language_status in {"UNCERTAIN", "AMBIGUOUS", "LOW_CONFIDENCE"}:
    return _make_result(**base, boundary_decision="ESCALATE", decision_class="LANGUAGE_UNCERTAINTY", formation_status="NO_BIND", effect_binding_status="NO_BIND", public_reason="language_context_requires_review")

if changed_context_status in {"CHANGED", "MATERIAL_CHANGE"}:
    return _make_result(**base, boundary_decision="ESCALATE", decision_class="CHANGED_CONTEXT", formation_status="NO_BIND", effect_binding_status="NO_BIND", public_reason="changed_context_requires_review")

if evidence_status in {"MISSING", "INSUFFICIENT"}:
    return _make_result(**base, boundary_decision="HOLD", decision_class="INSUFFICIENT_EVIDENCE", formation_status="NO_BIND", effect_binding_status="NO_BIND", public_reason="evidence_not_sufficient")

if evidence_status == "UNKNOWN":
    return _make_result(**base, boundary_decision="ESCALATE", decision_class="EVIDENCE_UNKNOWN", formation_status="NO_BIND", effect_binding_status="NO_BIND", public_reason="evidence_unknown")

if scope_status in {"TOO_BROAD", "OVERBROAD", "OUT_OF_SCOPE"}:
    return _make_result(**base, boundary_decision="NARROW", decision_class="SCOPE_MISMATCH", formation_status="NARROWED", effect_binding_status="NO_BIND", public_reason="scope_requires_narrowing")

if scope_status in {"MISSING", "INVALID", "UNKNOWN"}:
    return _make_result(**base, boundary_decision="REFUSE", decision_class="SCOPE_INVALID", formation_status="NO_BIND", effect_binding_status="NO_BIND", public_reason="scope_not_valid")

if str(packet.get("proposed_movement", {}).get("execution_mode", "")).upper() == "ADMIT_ALLOWED":
    return _make_result(**base, boundary_decision="ADMIT", decision_class="ADMITTED", formation_status="ADMITTED", effect_binding_status="ADMITTED", public_reason="all_boundary_inputs_passed")

return _make_result(**base, boundary_decision="CONDITIONALLY_ADMISSIBLE", decision_class="BOUNDARY_SUPPORTED", formation_status="CONDITIONALLY_ADMITTED", effect_binding_status="BOUNDARY_RESULT_REQUIRED_BEFORE_BIND", public_reason="structured_context_supports_boundary_review")

""")

write("maci_elyria/receipt.py", """from future import annotations

from typing import Any, Dict, Optional

from .models import BoundaryReceipt, sha256_json, utc_now_iso
from .resolver import POLICY_VERSION, evaluate_boundary

def issue_receipt(packet: Dict[str, Any], prior_receipt_hash: Optional[str] = None) -> Dict[str, Any]:
result = evaluate_boundary(packet).as_dict()
packet_hash = sha256_json(packet)
result_hash = sha256_json(result)

replay_token = sha256_json({
    "packet_hash": packet_hash,
    "result_hash": result_hash,
    "policy_version": POLICY_VERSION,
    "prior_receipt_hash": prior_receipt_hash,
})

formation_status = str(result.get("formation_status", "NO_BIND"))
no_bind_status = "NO_BIND" if formation_status in {"NO_BIND", "NON_FORMED", "PENDING_REVIEW", "NARROWED", "CONDITIONALLY_ADMITTED"} else "BIND_ALLOWED"

receipt = BoundaryReceipt(
    receipt_type="ELYRIA_MACI_BOUNDARY_RECEIPT",
    input_packet_id=str(packet.get("packet_id", "UNKNOWN_PACKET")),
    boundary_decision=result["boundary_decision"],
    effect_binding_status=result["effect_binding_status"],
    public_reason_class=result["decision_class"],
    packet_hash=packet_hash,
    result_hash=result_hash,
    replay_token=replay_token,
    policy_version=POLICY_VERSION,
    prior_receipt_hash=prior_receipt_hash,
    created_at_utc=str(packet.get("created_at") or packet.get("created_at_utc") or utc_now_iso()),
    formation_status=formation_status,
    no_bind_status=no_bind_status,
    witness_digest=sha256_json({
        "packet_hash": packet_hash,
        "result_hash": result_hash,
        "policy_version": POLICY_VERSION,
        "witness": "PUBLIC_SEAM_WITNESS",
    }),
).with_hash()

result["receipt_hash"] = receipt.receipt_hash

return {"boundary_result": result, "receipt": receipt.as_dict()}

""")

write("maci_elyria/replay.py", """from future import annotations

from copy import deepcopy
from typing import Any, Dict

from .models import sha256_json
from .receipt import issue_receipt

def _full_boundary_inputs(packet: Dict[str, Any]) -> Dict[str, Any]:
if "boundary_inputs" not in packet:
packet["boundary_inputs"] = {
"standing": {"status": "VALID"},
"authority": packet.get("input_context", {}).get("authority", {"status": "VALID"}),
"evidence": {"status": "SUFFICIENT"},
"scope": {"status": "VALID"},
"custody": {"status": "VALID"},
}
return packet["boundary_inputs"]

def _mutate_for_mode(packet: Dict[str, Any], mode: str) -> Dict[str, Any]:
changed = deepcopy(packet)
mode = mode.upper()

if mode == "CHANGED_AUTHORITY":
    _full_boundary_inputs(changed)["authority"] = {"status": "REVOKED", "changed_by": "replay"}
elif mode == "CHANGED_EVIDENCE":
    _full_boundary_inputs(changed)["evidence"] = {"status": "INSUFFICIENT", "changed_by": "replay"}
elif mode == "CHANGED_SCOPE":
    _full_boundary_inputs(changed)["scope"] = {"status": "TOO_BROAD", "changed_by": "replay"}
elif mode == "CHANGED_CUSTODY":
    _full_boundary_inputs(changed)["custody"] = {"status": "INVALID", "changed_by": "replay"}
elif mode == "TAMPERED_PACKET":
    if "proposed_movement" in changed:
        changed["proposed_movement"]["action"] = "tampered_action"
    else:
        changed.setdefault("consequence_signal", {})["proposed_action"] = "tampered_action"

return changed

def _receipt_hash_valid(receipt: Dict[str, Any]) -> bool:
if not receipt or "receipt_hash" not in receipt:
return False
deterministic_core = {
"receipt_type": receipt.get("receipt_type"),
"input_packet_id": receipt.get("input_packet_id"),
"packet_hash": receipt.get("packet_hash"),
"result_hash": receipt.get("result_hash"),
"policy_version": receipt.get("policy_version"),
"formation_status": receipt.get("formation_status"),
"no_bind_status": receipt.get("no_bind_status"),
"prior_receipt_hash": receipt.get("prior_receipt_hash"),
}
return sha256_json(deterministic_core) == receipt.get("receipt_hash")

def replay_receipt(packet: Dict[str, Any], receipt: Dict[str, Any], replay_mode: str = "SAME_CONDITIONS") -> Dict[str, Any]:
mode = replay_mode.upper()

if mode == "TAMPERED_RECEIPT":
    tampered = dict(receipt)
    tampered["result_hash"] = "tampered"
    return {
        "replay_id": f"replay_{sha256_json({'mode': mode, 'packet': packet})[:16]}",
        "packet_id": str(packet.get("packet_id", "UNKNOWN_PACKET")),
        "receipt_id": receipt.get("receipt_id", "UNKNOWN_RECEIPT"),
        "replay_mode": mode,
        "replay_status": "INVALID",
        "original_boundary_result": receipt.get("boundary_decision"),
        "replayed_boundary_result": "INVALID",
        "original_formation_status": receipt.get("formation_status"),
        "replayed_formation_status": "INVALID",
        "packet_hash_matches": sha256_json(packet) == receipt.get("packet_hash"),
        "result_hash_matches": False,
        "policy_version_matches": False,
        "replay_token_matches": False,
        "receipt_hash_valid": _receipt_hash_valid(tampered),
        "proof": "Tampered receipt failed deterministic receipt validation.",
    }

replay_packet = _mutate_for_mode(packet, mode)
replayed = issue_receipt(replay_packet, prior_receipt_hash=receipt.get("prior_receipt_hash"))
replayed_receipt = replayed["receipt"]
replayed_boundary = replayed["boundary_result"]

packet_hash_matches = sha256_json(replay_packet) == receipt.get("packet_hash")
result_hash_matches = replayed_receipt.get("result_hash") == receipt.get("result_hash")
policy_version_matches = replayed_receipt.get("policy_version") == receipt.get("policy_version")
replay_token_matches = replayed_receipt.get("replay_token") == receipt.get("replay_token")

if mode == "SAME_CONDITIONS" and packet_hash_matches and result_hash_matches and policy_version_matches and replay_token_matches:
    status = "MATCH"
elif mode == "TAMPERED_PACKET":
    status = "MISMATCH"
elif replayed_boundary.get("boundary_decision") != receipt.get("boundary_decision"):
    status = "CHANGED_RESULT"
else:
    status = "MATCH" if result_hash_matches else "CHANGED_RESULT"

return {
    "replay_id": f"replay_{sha256_json({'mode': mode, 'packet': replay_packet})[:16]}",
    "packet_id": str(packet.get("packet_id", "UNKNOWN_PACKET")),
    "receipt_id": receipt.get("receipt_id", "UNKNOWN_RECEIPT"),
    "replay_mode": mode,
    "replay_status": status,
    "original_boundary_result": receipt.get("boundary_decision"),
    "replayed_boundary_result": replayed_boundary.get("boundary_decision"),
    "original_formation_status": receipt.get("formation_status"),
    "replayed_formation_status": replayed_boundary.get("formation_status"),
    "packet_hash_matches": packet_hash_matches,
    "result_hash_matches": result_hash_matches,
    "policy_version_matches": policy_version_matches,
    "replay_token_matches": replay_token_matches,
    "receipt_hash_valid": _receipt_hash_valid(receipt),
    "proof": f"Replay mode {mode} returned {status}. No automatic binding occurs unless the boundary admits formation.",
}

""")

write("api/app.py", """from future import annotations

from datetime import datetime, timezone
from typing import Any, Dict
from uuid import uuid4

from flask import Flask, jsonify, request

from maci_elyria.receipt import issue_receipt
from maci_elyria.replay import replay_receipt
from maci_elyria.resolver import evaluate_boundary

app = Flask(name)
PROOF_STORE: dict[str, dict[str, Any]] = {}

def _utc_now() -> str:
return datetime.now(timezone.utc).replace(microsecond=0).isoformat()

def _json_body() -> Dict[str, Any]:
return request.get_json(force=True) or {}

@app.get("/health")
def health():
return jsonify({"status": "ok", "service": "maci-elyria-seam-pilot"})

@app.post("/evaluate")
def evaluate():
packet = _json_body()
return jsonify(issue_receipt(packet))

@app.post("/maci/intake")
def maci_intake():
body = json_body()
packet = {
"packet_id": body.get("packet_id") or f"pkt{uuid4().hex[:12]}",
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
return jsonify({"movement_packet": packet})

@app.post("/workflow/harness")
def workflow_harness():
body = json_body()
packet = body.get("movement_packet") or body
boundary = evaluate_boundary(packet).as_dict()
workflow = {
"workflow_id": body.get("workflow_id") or f"wf{uuid4().hex[:12]}",
"step_id": body.get("step_id") or "proposed_movement",
"movement_packet_id": packet.get("packet_id", "UNKNOWN_PACKET"),
"boundary_result": boundary.get("boundary_decision"),
"formation_status": boundary.get("formation_status"),
"allowed_next_step": "execute_with_receipt" if boundary.get("boundary_decision") == "ADMIT" else "review_only",
"blocked_next_step": "protected_effect" if boundary.get("boundary_decision") != "ADMIT" else None,
}
return jsonify(workflow)

@app.post("/boundary/resolve")
def boundary_resolve():
packet = _json_body()
return jsonify(evaluate_boundary(packet).as_dict())

@app.post("/receipt/create")
def receipt_create():
body = _json_body()
packet = body.get("movement_packet") or body.get("packet") or body
return jsonify(issue_receipt(packet, prior_receipt_hash=body.get("prior_receipt_hash")))

@app.post("/replay/run")
def replay_run():
body = _json_body()
packet = body.get("movement_packet") or body.get("packet") or {}
receipt = body.get("receipt") or issue_receipt(packet)["receipt"]
mode = body.get("replay_mode", "SAME_CONDITIONS")
return jsonify(replay_receipt(packet, receipt, mode))

@app.post("/proof/create")
def proof_create():
body = json_body()
packet = body.get("movement_packet") or body.get("packet") or body
issued = issue_receipt(packet)
replay = replay_receipt(packet, issued["receipt"], body.get("replay_mode", "SAME_CONDITIONS"))
proof_id = body.get("proof_id") or f"proof{uuid4().hex[:12]}"
proof = {
"proof_id": proof_id,
"case_name": body.get("case_name", packet.get("packet_id", "unnamed_case")),
"movement_packet": packet,
"boundary_result": issued["boundary_result"],
"receipt": issued["receipt"],
"replay": replay,
"final_claim": f"The proposed movement resolved as {issued['boundary_result']['boundary_decision']} / {issued['boundary_result']['formation_status']} under the public seam policy.",
}
PROOF_STORE[proof_id] = proof
return jsonify(proof)

@app.get("/proof/<proof_id>")
def proof_get(proof_id: str):
proof = PROOF_STORE.get(proof_id)
if not proof:
return jsonify({"error": "proof_not_found", "proof_id": proof_id}), 404
return jsonify(proof)

if name == "main":
app.run(host="0.0.0.0", port=8080)
""")

movement_schema = {
"$schema": "https://json-schema.org/draft/2020-12/schema",
"title": "MACI Elyria Movement Packet",
"type": "object",
"required": ["packet_id", "created_at", "source_layer", "domain", "actor", "proposed_movement", "maci_context", "boundary_inputs", "seam_guard"],
"properties": {
"packet_id": {"type": "string"},
"created_at": {"type": "string"},
"source_layer": {"const": "MACI"},
"domain": {"type": "string"},
"actor": {"type": "object"},
"proposed_movement": {"type": "object"},
"maci_context": {"type": "object"},
"boundary_inputs": {"type": "object"},
"seam_guard": {"type": "object"}
}
}

boundary_schema = {
"$schema": "https://json-schema.org/draft/2020-12/schema",
"title": "Elyria Boundary Result",
"type": "object",
"required": ["packet_id", "boundary_result", "formation_status", "reason_code"],
"properties": {
"packet_id": {"type": "string"},
"boundary_result": {"enum": ["REFUSE", "HOLD", "ESCALATE", "NARROW", "CONDITIONALLY_ADMISSIBLE", "ADMIT", "HALT"]},
"formation_status": {"enum": ["NO_BIND", "NON_FORMED", "PENDING_REVIEW", "NARROWED", "CONDITIONALLY_ADMITTED", "ADMITTED", "INVALID"]},
"reason_code": {"type": "string"}
}
}

receipt_schema = {
"$schema": "https://json-schema.org/draft/2020-12/schema",
"title": "Elyria MACI Boundary Receipt",
"type": "object",
"required": ["receipt_id", "packet_hash", "result_hash", "policy_version", "formation_status", "no_bind_status", "receipt_hash", "witness_digest"]
}

replay_schema = {
"$schema": "https://json-schema.org/draft/2020-12/schema",
"title": "Elyria MACI Replay Result",
"type": "object",
"required": ["replay_id", "packet_id", "receipt_id", "replay_mode", "replay_status"]
}

write("packages/schemas/movement_packet.schema.json", json.dumps(movement_schema, indent=2) + "\n")
write("packages/schemas/boundary_result.schema.json", json.dumps(boundary_schema, indent=2) + "\n")
write("packages/schemas/receipt.schema.json", json.dumps(receipt_schema, indent=2) + "\n")
write("packages/schemas/replay.schema.json", json.dumps(replay_schema, indent=2) + "\n")

for path, title, body in [
("apps/operator-console/README.md", "Operator Console", "Operator-facing UI shell for submitting and inspecting proposed movement."),
("apps/buyer-demo/README.md", "Buyer Demo", "Buyer-facing demo shell for movement intake, boundary result, receipt, and replay."),
("apps/proof-viewer/README.md", "Proof Viewer", "Public-safe proof viewer for receipt, replay, and transcript inspection."),
("services/maci-intake-api/README.md", "MACI Intake API", "Receives customer/domain input and creates structured movement packets."),
("services/workflow-harness/README.md", "Workflow Harness", "Wraps movement packets into proof workflows and prevents bypass."),
("services/boundary-runtime/README.md", "Boundary Runtime", "Resolves standing, authority, evidence, scope, custody, route closure, and formation status."),
("services/receipt-service/README.md", "Receipt Service", "Issues deterministic receipts for packet, result, policy version, and witness digest."),
("services/replay-service/README.md", "Replay Service", "Runs same-condition and changed-condition replay."),
("services/witness-service/README.md", "Witness Service", "Provides public seam witness digest without exposing protected runtime internals."),
("packages/canonicalization/README.md", "Canonicalization", "Defines stable JSON hashing and deterministic receipt inputs."),
("packages/sdk-python/README.md", "Python SDK", "Future public-safe client wrapper for the MACI-Elyria API."),
("packages/sdk-typescript/README.md", "TypeScript SDK", "Future public-safe client wrapper for UI and buyer integrations."),
]:
write(path, f"# {title}\n\n{body}\n\nBoundary rule: MACI may inform. MACI may not bind consequence.\n")

write("corridors/ai-agent-action/README.md", """# AI Agent Action Corridor

Scenario: an AI agent wants to send a customer-impacting email.

This corridor proves that MACI can structure context, but cannot bind consequence. Elyria/VERITA resolves whether the proposed movement must refuse, hold, escalate, narrow, conditionally admit, or admit.
""")

def packet(name, overrides):
base = {
"packet_id": name,
"created_at": "2026-06-17T00:00:00+00:00",
"source_layer": "MACI",
"domain": "ai-agent-action",
"actor": {"agent_id": "agent-demo", "human_requester": "operator-demo", "system_origin": "buyer-demo"},
"proposed_movement": {"action": "send_customer_impacting_email", "target": "customer", "intended_consequence": "customer-impacting communication", "affected_party": "customer"},
"maci_context": {
"language_context": {"status": "CURRENT", "language": "en", "confidence": 0.98},
"input_context": {"status": "CURRENT", "changed_context": {"status": "UNCHANGED"}},
"consequence_signal": {"status": "CURRENT", "bind_attempt": False},
"risk_notes": []
},
"boundary_inputs": {
"standing": {"status": "VALID"},
"authority": {"status": "VALID"},
"evidence": {"status": "SUFFICIENT"},
"scope": {"status": "VALID"},
"custody": {"status": "VALID"}
},
"seam_guard": {"maci_can_bind": False, "requires_elyria_boundary_result": True}
}

def deep_update(target, changes):
    for k, v in changes.items():
        if isinstance(v, dict) and isinstance(target.get(k), dict):
            deep_update(target[k], v)
        else:
            target[k] = v

deep_update(base, overrides)
return json.dumps(base, indent=2) + "\n"

write("corridors/ai-agent-action/packets/valid_structured_context.json", packet("ai-agent-valid-structured-context", {}))
write("corridors/ai-agent-action/packets/missing_authority.json", packet("ai-agent-missing-authority", {"boundary_inputs": {"authority": {"status": "MISSING"}}}))
write("corridors/ai-agent-action/packets/uncertain_language.json", packet("ai-agent-uncertain-language", {"maci_context": {"language_context": {"status": "UNCERTAIN", "language": "en", "confidence": 0.41}}}))
write("corridors/ai-agent-action/packets/changed_context.json", packet("ai-agent-changed-context", {"maci_context": {"input_context": {"status": "CURRENT", "changed_context": {"status": "CHANGED"}}}}))
write("corridors/ai-agent-action/packets/maci_bind_attempt.json", packet("ai-agent-maci-bind-attempt", {"seam_guard": {"maci_can_bind": True, "requires_elyria_boundary_result": True}, "maci_context": {"consequence_signal": {"status": "CURRENT", "bind_attempt": True}}}))
write("corridors/ai-agent-action/packets/insufficient_evidence.json", packet("ai-agent-insufficient-evidence", {"boundary_inputs": {"evidence": {"status": "INSUFFICIENT"}}}))
write("corridors/ai-agent-action/packets/scope_too_broad.json", packet("ai-agent-scope-too-broad", {"boundary_inputs": {"scope": {"status": "TOO_BROAD"}}}))
write("corridors/ai-agent-action/packets/invalid_custody.json", packet("ai-agent-invalid-custody", {"boundary_inputs": {"custody": {"status": "INVALID"}}}))

expected = {
"valid_structured_context": {"boundary_result": "CONDITIONALLY_ADMISSIBLE", "formation_status": "CONDITIONALLY_ADMITTED"},
"missing_authority": {"boundary_result": "REFUSE", "formation_status": "NO_BIND", "reason_code": "MISSING_AUTHORITY"},
"uncertain_language": {"boundary_result": "ESCALATE", "formation_status": "NO_BIND", "reason_code": "LANGUAGE_UNCERTAINTY"},
"changed_context": {"boundary_result": "ESCALATE", "formation_status": "NO_BIND", "reason_code": "CHANGED_CONTEXT"},
"maci_bind_attempt": {"boundary_result": "HALT", "formation_status": "NO_BIND", "reason_code": "MACI_CANNOT_BIND_CONSEQUENCE"},
"insufficient_evidence": {"boundary_result": "HOLD", "formation_status": "NO_BIND", "reason_code": "INSUFFICIENT_EVIDENCE"},
"scope_too_broad": {"boundary_result": "NARROW", "formation_status": "NARROWED", "reason_code": "SCOPE_MISMATCH"},
"invalid_custody": {"boundary_result": "REFUSE", "formation_status": "NO_BIND", "reason_code": "CUSTODY_INVALID"}
}

for name, value in expected.items():
write(f"corridors/ai-agent-action/expected_results/{name}.json", json.dumps(value, indent=2) + "\n")

for corridor in ["healthcare", "finance", "procurement"]:
write(f"corridors/{corridor}/README.md", f"# {corridor.title()} Corridor\n\nReserved public-safe corridor scaffold.\n")

for proof_dir in [
"proofs/refusal-cases",
"proofs/hold-cases",
"proofs/no-bind-cases",
"proofs/changed-condition-replay",
"proofs/non-bypass-cases",
"proofs/proof-transcripts",
]:
write(f"{proof_dir}/.gitkeep", "")

write("proofs/README.md", """# Proofs

Proof transcripts bind:

movement packet
boundary result
receipt
replay result
final no-bind/admission claim

No workflow proof is valid unless it shows whether movement was allowed, refused, held, escalated, narrowed, or admitted before protected consequence could form.
""")

write("tests/test_fullstack_runtime_expansion.py", """import json
from pathlib import Path

from maci_elyria.receipt import issue_receipt
from maci_elyria.replay import replay_receipt

def load_packet(name: str):
return json.loads(Path(f"corridors/ai-agent-action/packets/{name}.json").read_text())

def assert_boundary(name: str, result: str, formation: str):
issued = issue_receipt(load_packet(name))
boundary = issued["boundary_result"]
assert boundary["boundary_decision"] == result
assert boundary["boundary_result"] == result
assert boundary["formation_status"] == formation
assert issued["receipt"]["formation_status"] == formation

def test_valid_packet_conditionally_admissible():
assert_boundary("valid_structured_context", "CONDITIONALLY_ADMISSIBLE", "CONDITIONALLY_ADMITTED")

def test_missing_authority_refuses_no_bind():
assert_boundary("missing_authority", "REFUSE", "NO_BIND")

def test_uncertain_language_escalates_no_bind():
assert_boundary("uncertain_language", "ESCALATE", "NO_BIND")

def test_changed_context_escalates_no_bind():
assert_boundary("changed_context", "ESCALATE", "NO_BIND")

def test_maci_bind_attempt_halts():
assert_boundary("maci_bind_attempt", "HALT", "NO_BIND")

def test_insufficient_evidence_holds_no_bind():
assert_boundary("insufficient_evidence", "HOLD", "NO_BIND")

def test_invalid_scope_narrows():
assert_boundary("scope_too_broad", "NARROW", "NARROWED")

def test_invalid_custody_refuses_no_bind():
assert_boundary("invalid_custody", "REFUSE", "NO_BIND")

def test_tampered_packet_replay_mismatch():
packet = load_packet("valid_structured_context")
issued = issue_receipt(packet)
replay = replay_receipt(packet, issued["receipt"], "TAMPERED_PACKET")
assert replay["replay_status"] == "MISMATCH"

def test_tampered_receipt_replay_invalid():
packet = load_packet("valid_structured_context")
issued = issue_receipt(packet)
replay = replay_receipt(packet, issued["receipt"], "TAMPERED_RECEIPT")
assert replay["replay_status"] == "INVALID"

def test_changed_authority_replay_changes_result():
packet = load_packet("valid_structured_context")
issued = issue_receipt(packet)
replay = replay_receipt(packet, issued["receipt"], "CHANGED_AUTHORITY")
assert replay["replay_status"] == "CHANGED_RESULT"
assert replay["replayed_boundary_result"] == "REFUSE"

def test_changed_evidence_replay_holds_or_changes():
packet = load_packet("valid_structured_context")
issued = issue_receipt(packet)
replay = replay_receipt(packet, issued["receipt"], "CHANGED_EVIDENCE")
assert replay["replay_status"] == "CHANGED_RESULT"
assert replay["replayed_boundary_result"] == "HOLD"

def test_changed_scope_replay_narrows():
packet = load_packet("valid_structured_context")
issued = issue_receipt(packet)
replay = replay_receipt(packet, issued["receipt"], "CHANGED_SCOPE")
assert replay["replay_status"] == "CHANGED_RESULT"
assert replay["replayed_boundary_result"] == "NARROW"
""")

print("Full-stack runtime patch applied.")
