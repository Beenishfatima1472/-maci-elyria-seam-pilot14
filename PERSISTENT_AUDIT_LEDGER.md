# Persistent Audit Ledger Contract

## Status

Implemented as a SQLite-backed append-only candidate audit ledger for reviewer evaluation.

Customer production approval remains gated.

This artifact documents the public-safe audit-ledger contract for the MACI / Elyria production-runtime candidate shell.

It is not a certified production audit system.

## Runtime Evidence

Code and tests:

- `maci_elyria/sqlite_runtime_store.py`
- `maci_elyria/audit_ledger.py`
- `api/app.py`
- `tests/test_a_plus_api_runtime_controls.py`

## Audit Event Contract

A persisted audit event contains:

- id
- event_type
- tenant_id
- actor
- resource_id
- outcome
- timestamp
- prior_hash
- event_hash
- details_json

## Candidate Event Types

The audit model is designed to preserve events for:

- intake
- assumption precheck
- boundary resolution
- workflow gate
- receipt issue
- receipt verify
- replay run
- proof create/read/export
- no-bind
- halt
- refuse
- escalate
- admit
- verifier action
- admin/key action
- tenant-scope violation
- authorization denial

## Ledger Integrity

The candidate ledger records chained event hashes using prior-hash linkage.

Verification checks whether each event remains consistent with the prior event hash and stored event details.

## Failure Behavior

Expected failures:

- Missing prior-hash continuity returns invalid ledger.
- Changed event details return invalid ledger.
- Removed event in chain returns invalid ledger.
- Tenant mismatch prevents cross-tenant event exposure unless explicitly approved and audited.

## Reviewer Verification

```bash
PYTHONPATH="$PWD" pytest -q tests/test_a_plus_api_runtime_controls.py
```

Runtime endpoint under configured auth:

```text
GET /audit/verify
```

## Customer Gate

A customer deployment must still approve:

- audit retention period
- log export destination
- monitoring integration
- audit access policy
- incident evidence policy
- administrative review cadence

## Allowed Claim

```text
Persistent audit-ledger candidate contract is implemented and visible for audit review.
```

## Forbidden Claims

```text
certified immutable audit ledger
customer monitoring approved
regulatory audit certification
customer security approved
```
