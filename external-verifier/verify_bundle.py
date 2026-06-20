from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from maci_elyria.proof_bundle_verifier import verify_proof_bundle_file


def main() -> int:
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "proofs" / "proof-transcripts"
    if not target.is_absolute():
        target = ROOT / target

    files = sorted(target.glob("**/*.proof.json")) if target.is_dir() else [target]
    failures = []

    for path in files:
        result = verify_proof_bundle_file(path)
        if not result["valid"]:
            failures.append(result)
        print(json.dumps({"path": str(path.relative_to(ROOT)), **result}, indent=2))

    summary = {
        "verifier_type": "ELYRIA_EXTERNAL_VERIFIER_PACKAGE",
        "checked": len(files),
        "failed": len(failures),
        "status": "PASS" if not failures else "FAIL",
        "claim": "external verifier checks proof bundle without trusting live app state",
    }
    print(json.dumps(summary, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
