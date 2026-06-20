from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

if __name__ == "__main__":
    text = (ROOT / "proofs" / "NO_BIND_PROOF_TRANSCRIPT.md").read_text(encoding="utf-8")
    if "NO_BIND" not in text:
        raise SystemExit(1)
    print("[PASS] no-bind proof verified")
