from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HEX64 = re.compile(r"^[0-9a-f]{64}$")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def record_failure(failures: list[str], message: str) -> None:
    print(f"[FAIL] {message}")
    failures.append(message)


def main() -> int:
    manifest = ROOT / "golden_corridor" / "digest_manifest.json"
    digest_sha_file = ROOT / "signatures" / "digest_manifest.sha256"
    failures: list[str] = []

    if not manifest.exists():
        record_failure(failures, "digest manifest missing")
        print("RESULT: A+ BENCHMARK FAIL")
        return 1

    data = json.loads(manifest.read_text(encoding="utf-8"))

    for item in data.get("artifacts", []):
        artifact_name = item.get("artifact", "")
        expected = item.get("sha256", "")
        artifact = ROOT / artifact_name
        if not artifact.exists():
            record_failure(failures, f"missing digest artifact: {artifact_name}")
            continue
        if not expected:
            record_failure(failures, f"empty digest hash: {artifact_name}")
            continue
        if not HEX64.fullmatch(expected):
            record_failure(failures, f"malformed digest hash: {artifact_name}")
            continue
        actual = sha256_file(artifact)
        if actual != expected:
            record_failure(failures, f"digest mismatch: {artifact_name}")
            print(f"       expected: {expected}")
            print(f"       actual:   {actual}")
        else:
            print(f"[PASS] digest match: {artifact_name}")

    if not digest_sha_file.exists():
        record_failure(failures, "digest SHA file missing")
    else:
        raw = digest_sha_file.read_text(encoding="utf-8").strip()
        expected_manifest_hash = raw.split()[0] if raw else ""
        if not expected_manifest_hash:
            record_failure(failures, "digest SHA file empty")
        elif not HEX64.fullmatch(expected_manifest_hash):
            record_failure(failures, "digest SHA file malformed")
        else:
            actual_manifest_hash = sha256_file(manifest)
            if actual_manifest_hash != expected_manifest_hash:
                record_failure(failures, "digest SHA file mismatch")
                print(f"       expected: {expected_manifest_hash}")
                print(f"       actual:   {actual_manifest_hash}")
            else:
                print("[PASS] digest SHA file verified")

    if failures:
        print("RESULT: A+ BENCHMARK FAIL")
        return 1

    print("[PASS] digest manifest verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
