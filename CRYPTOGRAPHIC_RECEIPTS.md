# Cryptographic Receipts

## Public Review Receipt Layer

This repository signs public-safe receipts.

Receipt signing provides visible tamper evidence for the public review build.

Each receipt includes:

```text
receipt_hash
packet_hash
result_hash
replay_token
witness_digest
signature_algorithm
signature_key_id
signature_issued_by
receipt_signature
Public Review Signing Mode

The public repository uses:

HMAC-SHA256-PUBLIC-REVIEW

This demonstrates:

canonical receipt payload
signature attachment
signature verification
tamper detection
independent verifier path
Production Requirement

Production deployment must replace the demo key path with:

KMS/HSM-backed signing
asymmetric public verification
key rotation
key revocation
signer identity policy
audit log persistence
access-controlled key use
independent verifier separation
Claim Boundary

Use this claim:

Receipts are signed and independently verifiable in the public review build.

Do not use this claim:

Receipts are production-certified cryptographic authority.

