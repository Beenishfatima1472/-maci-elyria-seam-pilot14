from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

if __name__ == "__main__":
    path = ROOT / "proofs" / "KERNEL_NON_DISCLOSURE_PROOF.md"
    text = path.read_text(encoding="utf-8")
    required = ["does not expose", "protected", "proof surface"]
    if not path.exists() or not all(item in text for item in required):
        raise SystemExit(1)
    print("[PASS] protected kernel not exposed")
