from __future__ import annotations

import json
from pathlib import Path

from maci_elyria.receipt import issue_receipt


CASES = [
    "valid_signal_packet.json",
    "uncertain_language_packet.json",
    "missing_authority_packet.json",
    "changed_context_packet.json",
    "no_bind_attempt_packet.json",
]


def main() -> int:
    for name in CASES:
        packet = json.loads(Path("examples", name).read_text(encoding="utf-8"))
        result = issue_receipt(packet)
        boundary = result["boundary_result"]
        print(
            f"{name} => "
            f"{boundary['boundary_decision']} / "
            f"{boundary['decision_class']} / "
            f"{boundary['effect_binding_status']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
