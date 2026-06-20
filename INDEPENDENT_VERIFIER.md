
Independent Receipt Verifier
Purpose

The independent verifier checks signed receipts without relying on the UI.

Command
python3 scripts/verify_receipts.py proofs

Expected:

OK verified signed receipt(s)
Tamper Model

The verifier detects:

boundary decision tampering
receipt field modification
hash/signature mismatch
missing signature
Public Review Limit

The public verifier uses a demo public-review HMAC key.

Production requires external verifier separation and KMS/HSM-backed signing.
