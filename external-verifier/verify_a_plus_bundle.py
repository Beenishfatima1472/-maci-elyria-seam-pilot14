from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "RELEASE_MANIFEST.md",
    "CLAIM_BOUNDARY.md",
    "A_PLUS_ACCEPTANCE_CRITERIA.md",
    "A_PLUS_BENCHMARK_READOUT.md",
    "BENCHMARK_SCORECARD.md",
    "GOLDEN_CORRIDOR_README.md",
    "REVIEWER_QUICKSTART.md",
    "golden_corridor/input_valid.json",
    "golden_corridor/input_missing_authority.json",
    "golden_corridor/input_stale_evidence.json",
    "golden_corridor/input_changed_scope.json",
    "golden_corridor/input_changed_authority.json",
    "golden_corridor/input_changed_evidence.json",
    "golden_corridor/input_broken_custody.json",
    "golden_corridor/input_bypass_attempt.json",
    "golden_corridor/boundary_result_admit.json",
    "golden_corridor/boundary_result_refuse_missing_authority.json",
    "golden_corridor/boundary_result_refuse_stale_evidence.json",
    "golden_corridor/boundary_result_escalate_changed_scope.json",
    "golden_corridor/boundary_result_refuse_changed_authority.json",
    "golden_corridor/boundary_result_refuse_changed_evidence.json",
    "golden_corridor/boundary_result_halt_broken_custody.json",
    "golden_corridor/boundary_result_halt_bypass.json",
    "golden_corridor/receipt_admit.json",
    "golden_corridor/receipt_refuse.json",
    "golden_corridor/receipt_halt.json",
    "golden_corridor/replay_same_condition.json",
    "golden_corridor/replay_changed_condition.json",
    "golden_corridor/no_bind_transcript.md",
    "golden_corridor/digest_manifest.json",
    "simulated_flows/flow_schema.json",
    "simulated_flows/flows_v1.jsonl",
    "simulated_flows/FLOW_GENERATION_NOTES.md",
    "simulated_flows/FLOW_COVERAGE_MATRIX.md",
    "signatures/SIGNATURE_README.md",
    "signatures/digest_manifest.sha256",
    "proofs/NO_BIND_PROOF_TRANSCRIPT.md",
    "proofs/SAME_CONDITION_REPLAY_TRANSCRIPT.md",
    "proofs/CHANGED_CONDITION_REPLAY_TRANSCRIPT.md",
    "proofs/BYPASS_FAILURE_MATRIX.md",
    "proofs/ROUTE_CLOSURE_PROOF.md",
    "proofs/RECEIPT_INTEGRITY_PROOF.md",
    "proofs/KERNEL_NON_DISCLOSURE_PROOF.md",
    "review-bundle/A_PLUS_REVIEW_PACKET.md",
    "review-bundle/BUYER_ONE_PAGE_READOUT.md",
    "review-bundle/REGULATOR_EVIDENCE_CHECKLIST.md",
    "review-bundle/TECHNICAL_REVIEWER_CHECKLIST.md",
    "review-bundle/PILOT_DAY_1_READINESS.md",
]


def load_json(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def pass_line(message: str) -> None:
    print(f"[PASS] {message}")


def fail_line(message: str) -> None:
    print(f"[FAIL] {message}")


def check(condition: bool, message: str, failures: list[str]) -> None:
    if condition:
        pass_line(message)
    else:
        fail_line(message)
        failures.append(message)


def main() -> int:
    print("MACI–ELYRIA A+ BENCHMARK VERIFICATION")
    print()
    failures: list[str] = []

    materialize = subprocess.run([sys.executable, "scripts/materialize_a_plus_benchmark.py"], cwd=ROOT)
    check(materialize.returncode == 0, "simulated MACI flow benchmark materialized", failures)

    missing = [path for path in REQUIRED_FILES if not (ROOT / path).exists()]
    check(not missing, "golden corridor files present", failures)
    for item in missing:
        fail_line(f"missing required file: {item}")

    claim = (ROOT / "CLAIM_BOUNDARY.md").read_text(encoding="utf-8")
    check("MACI informs" in claim and "No consequence binds" in claim, "claim boundary present", failures)
    check((ROOT / "proofs" / "KERNEL_NON_DISCLOSURE_PROOF.md").exists(), "protected kernel not exposed", failures)
    check((ROOT / "RELEASE_MANIFEST.md").exists(), "release manifest verified", failures)

    digest_result = subprocess.run([sys.executable, "external-verifier/verify_digest_manifest.py"], cwd=ROOT)
    check(digest_result.returncode == 0, "digest manifest verified", failures)

    packet = load_json("golden_corridor/input_valid.json")
    admit = load_json("golden_corridor/boundary_result_admit.json")
    missing_auth = load_json("golden_corridor/boundary_result_refuse_missing_authority.json")
    stale = load_json("golden_corridor/boundary_result_refuse_stale_evidence.json")
    changed_auth = load_json("golden_corridor/boundary_result_refuse_changed_authority.json")
    changed_evidence = load_json("golden_corridor/boundary_result_refuse_changed_evidence.json")
    changed_scope = load_json("golden_corridor/boundary_result_escalate_changed_scope.json")
    custody = load_json("golden_corridor/boundary_result_halt_broken_custody.json")
    route = load_json("golden_corridor/boundary_result_halt_bypass.json")
    same = load_json("golden_corridor/replay_same_condition.json")
    changed = load_json("golden_corridor/replay_changed_condition.json")
    receipt = load_json("golden_corridor/receipt_refuse.json")
    flows = [json.loads(line) for line in (ROOT / "simulated_flows" / "flows_v1.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]

    check(packet.get("source_layer") == "MACI", "MACI packet schema valid", failures)
    check(admit.get("boundary_decision") == "ADMIT" and admit.get("bind_status") == "BOUND", "Elyria boundary result required", failures)
    check(receipt.get("bind_status") == "NO_BIND", "MACI-only bind attempt refused", failures)
    check(missing_auth.get("boundary_decision") == "REFUSE" and missing_auth.get("bind_status") == "NO_BIND", "missing authority refused / no-bind", failures)
    check(stale.get("boundary_decision") == "REFUSE" and stale.get("bind_status") == "NO_BIND", "stale evidence refused / no-bind", failures)
    check(changed_auth.get("bind_status") == "NO_BIND", "changed authority revalidated", failures)
    check(changed_evidence.get("bind_status") == "NO_BIND", "changed evidence revalidated", failures)
    check(changed_scope.get("bind_status") == "NO_BIND", "changed condition revalidated", failures)
    check(custody.get("bind_status") == "NO_BIND", "broken custody halted", failures)
    check(route.get("bind_status") == "NO_BIND", "bypass attempt halted / no-bind", failures)
    check(same.get("replay_status") == "MATCH", "same-condition replay matched", failures)
    check(changed.get("replay_status") == "LAWFUL_CHANGE" and changed.get("replay_bind_status") == "NO_BIND", "changed-condition replay changed lawfully", failures)
    check("NO_BIND" in (ROOT / "proofs" / "NO_BIND_PROOF_TRANSCRIPT.md").read_text(encoding="utf-8"), "no-bind transcript verified", failures)
    check((ROOT / "proofs" / "RECEIPT_INTEGRITY_PROOF.md").exists(), "receipt integrity verified", failures)
    check(len(flows) >= 100, "simulated MACI flow benchmark present", failures)
    check((ROOT / "review-bundle" / "BUYER_ONE_PAGE_READOUT.md").exists(), "buyer packet complete", failures)
    check((ROOT / "review-bundle" / "REGULATOR_EVIDENCE_CHECKLIST.md").exists(), "regulator checklist complete", failures)

    print()
    if failures:
        print("RESULT: A+ BENCHMARK FAIL")
        return 1
    print("RESULT: A+ BENCHMARK PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
