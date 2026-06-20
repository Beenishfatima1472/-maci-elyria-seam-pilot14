# Persistent Receipt Store Contract

## Status

Implemented as a SQLite-backed production-runtime candidate control for reviewer evaluation.

Customer production approval remains gated.

This artifact documents the persistent receipt-store contract used by the public-safe MACI / Elyria candidate runtime.

It does not certify a customer storage backend.

## Runtime Evidence

Code and tests:

- `maci_elyria/sqlite_runtime_store.py`
- `maci_elyria/signing.py`
- `api/app.py`
- `tests/test_a_plus_api_runtime_controls.py`
- `scripts/verify_receipts.py`

## Receipt Record Contract

A persisted receipt record contains:

- receipt_id
- tenant_id
- packet_id
- packet_digest
- boundary_result
- policy_version
- replay_token
- signature
- key_id
- timestamp
- verification_status
- receipt_json

## Storage Behavior

The candidate store provides:

1. Insert or update receipt by receipt ID.
2. Tenant-scoped receipt lookup.
3. Tenant-scoped receipt export.
4. Signature material preservation.
5. Replay-token preservation.
6. Verification-status preservation.
7. Deterministic JSON serialization for stored payloads.

## Failure Behavior

Expected failure behavior:

- Missing receipt returns not found.
- Wrong tenant returns not found for tenant.
- Missing signature fails verification.
- Wrong key ID fails verification.
- Packet tamper fails verification.
- Changed-condition replay fails verification.

## Reviewer Verification

```bash
PYTHONPATH="$PWD" pytest -q tests/test_a_plus_api_runtime_controls.py
PYTHONPATH="$PWD" python3 scripts/verify_receipts.py
```

## Customer Gate

A customer deployment must still approve:

- durable database backend
- backup policy
- retention policy
- restore procedure
- incident evidence preservation
- database access-control model

## Allowed Claim

```text
Persistent receipt-store candidate contract is implemented and visible for audit review.
```

## Forbidden Claims

```text
customer storage backend approved
regulatory evidence-store certification
immutable ledger certification
customer security approved
```
