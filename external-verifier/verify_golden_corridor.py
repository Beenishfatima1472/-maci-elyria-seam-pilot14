from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INVARIANT = "MACI informs. Elyria resolves. No consequence binds without the boundary result."


def load(rel: str) -> dict:
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


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


def materialize_flows_if_missing(failures: list[str]) -> None:
    flows_path = ROOT / "simulated_flows" / "flows_v1.jsonl"
    if flows_path.exists():
        return
    result = subprocess.run([sys.executable, "scripts/materialize_a_plus_benchmark.py"], cwd=ROOT)
    if result.returncode != 0 or not flows_path.exists():
        fail_line("simulated MACI flows missing and materialization failed")
        failures.append("simulated MACI flows missing and materialization failed")


def main() -> int:
    print("MACI–ELYRIA GOLDEN CORRIDOR VERIFICATION")
    print()

    failures: list[str] = []
    materialize_flows_if_missing(failures)

    packet = load("golden_corridor/input_packet_valid.json")
    admit = load("golden_corridor/boundary_result_admit.json")
    receipt_admit = load("golden_corridor/receipt_admit.json")
    receipt_refuse = load("golden_corridor/receipt_refuse.json")
    same = load("golden_corridor/replay_same_condition.json")
    changed = load("golden_corridor/replay_changed_condition.json")
    no_bind = (ROOT / "golden_corridor" / "no_bind_transcript.md").read_text(encoding="utf-8")

    check(packet.get("source_layer") == "MACI", "input packet schema valid", failures)
    check(admit.get("boundary_result_present") is True, "boundary result present", failures)
    check(packet["maci_context"]["consequence_signal"].get("bind_attempt") is False, "MACI did not bind consequence", failures)
    check(receipt_admit.get("boundary_result_required") is True, "Elyria boundary result required", failures)
    check(receipt_admit.get("boundary_decision") == "ADMIT", "admit receipt valid", failures)
    check(receipt_refuse.get("boundary_decision") == "REFUSE" and receipt_refuse.get("bind_status") == "NO_BIND", "refuse receipt valid", failures)
    check("NO_BIND" in no_bind and INVARIANT in no_bind, "no-bind transcript valid", failures)
    check(same.get("replay_status") == "MATCH" and same.get("original_boundary_decision") == same.get("replay_boundary_decision"), "same-condition replay matched", failures)
    check(changed.get("replay_status") == "LAWFUL_CHANGE" and changed.get("replay_bind_status") == "NO_BIND", "changed-condition replay changed lawfully", failures)
    check((ROOT / "golden_corridor" / "digest_manifest.json").exists(), "digest manifest present", failures)

    flows_path = ROOT / "simulated_flows" / "flows_v1.jsonl"
    flows = [json.loads(line) for line in flows_path.read_text(encoding="utf-8").splitlines() if line.strip()] if flows_path.exists() else []
    check(len(flows) >= 100, "100 simulated MACI flows present", failures)
    check(all(flow.get("expected_bind_status") != "BOUND" or flow.get("expected_boundary_result") == "ADMIT" for flow in flows), "all bound flows require ADMIT", failures)
    check(all(flow.get("expected_bind_status") == "NO_BIND" for flow in flows if flow.get("reason_code") in {"bypass_attempt", "missing_boundary_result", "replay_mismatch"}), "bypass/mismatch flows are no-bind", failures)

    print()
    if failures:
        print("RESULT: A+ BENCHMARK FAIL")
        return 1

    print("RESULT: A+ BENCHMARK PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
