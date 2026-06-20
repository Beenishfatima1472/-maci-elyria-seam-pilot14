from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

if __name__ == "__main__":
    text = (ROOT / "CLAIM_BOUNDARY.md").read_text(encoding="utf-8")
    if "MACI informs" not in text:
        raise SystemExit(1)
    print("[PASS] claim boundary verified")
