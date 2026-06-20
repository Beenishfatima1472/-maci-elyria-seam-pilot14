# Tenant Isolation Candidate Model

## Status

Implemented as production-runtime candidate controls for reviewer evaluation.

Customer production approval remains gated.

This artifact documents how tenant scope is represented, enforced, persisted, and tested in the MACI / Elyria seam pilot.

It does not certify customer production use.

## Runtime Evidence

Code and tests:

- `maci_elyria/tenant_isolation.py`
- `maci_elyria/sqlite_runtime_store.py`
- `maci_elyria/rbac.py`
- `api/app.py`
- `tests/test_a_plus_api_runtime_controls.py`

## Tenant-Scoped Resource Types

Tenant-scoped resource classes include:

- packet
- receipt
- replay
- transcript
- audit
- proof_bundle
- user

## Resource Boundary

Each tenant-scoped resource is addressed with tenant context.

Cross-tenant lookup must return no record unless a controlled administrator override is explicitly supported, approved, and audited.

## Enforcement Behavior

The candidate model enforces:

1. Missing actor tenant denies.
2. Missing resource tenant denies.
3. Matching tenant allows only when role permission also allows the action.
4. Mismatched tenant denies.
5. Tenant mismatch on receipt lookup returns not found for tenant.
6. Tenant mismatch on proof lookup returns not found for tenant.
7. Tenant mismatch on replay returns not found for tenant.

## Runtime Store Boundary

Persistent runtime tables include tenant identifiers for:

- packets
- receipts
- proofs
- audit events
- idempotency keys

Tenant ID is part of the access boundary and storage contract.

## Reviewer Verification

```bash
PYTHONPATH="$PWD" pytest -q tests/test_a_plus_api_runtime_controls.py
```

Expected tested behavior:

- Tenant B cannot verify tenant A receipt.
- Tenant B cannot export tenant A receipt.
- Tenant B cannot read tenant A proof.
- Tenant B cannot replay tenant A proof.

## Customer Gate

A customer deployment must still approve:

- tenant identity source
- tenant provisioning lifecycle
- tenant deletion/deactivation lifecycle
- data-retention policy
- backup and restore isolation
- administrator override policy

## Allowed Claim

```text
Tenant-isolation candidate controls are implemented and tested at API/runtime level for reviewer evaluation.
```

## Forbidden Claims

```text
customer tenant architecture approved
production multi-tenant certification
regulatory isolation certification
customer security approved
```
