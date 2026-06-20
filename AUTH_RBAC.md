# Auth / RBAC Candidate Model

## Status

Implemented as production-runtime candidate controls for reviewer evaluation.

Customer production approval remains gated.

This artifact documents the visible authentication and role-based access-control model used by the MACI / Elyria seam pilot.

It does not certify customer production use.

## Runtime Evidence

Code and tests:

- `maci_elyria/rbac.py`
- `api/app.py`
- `tests/test_a_plus_api_runtime_controls.py`
- `scripts/check_deployment_readiness.py`
- `scripts/production_preflight.py`

## Role Surface

The candidate role surface includes:

- requester
- reviewer
- verifier
- admin
- auditor
- service_account
- tenant_admin

Unknown roles fail closed.

## Permission Model

Runtime actions are mapped to explicit role permissions.

Covered actions include:

- packet intake
- assumption precheck
- boundary resolution
- workflow gate execution
- receipt issuance
- receipt verification
- receipt export
- replay execution
- proof read
- proof export
- audit read
- key administration
- system administration

## Endpoint Mapping

Protected API endpoints map to named permissions.

The endpoint permission matrix is implemented in:

```text
maci_elyria/rbac.py
```

The runtime middleware enforcement path is implemented in:

```text
api/app.py
```

## Enforcement Behavior

The candidate model enforces:

1. Missing role denies.
2. Unknown role denies.
3. Unknown action denies.
4. Unauthorized role/action pair denies.
5. Tenant mismatch denies unless an explicitly permitted platform-admin override applies.
6. Protected endpoint without API key denies.
7. Protected endpoint without tenant context denies when tenant requirement is enabled.

## Production Boundary

This repository shows the candidate control implementation and tests.

A customer deployment must still approve:

- identity provider integration
- credential storage
- session lifecycle
- administrator assignment
- break-glass procedure
- access-review cadence
- audit-retention requirements

## Reviewer Verification

```bash
PYTHONPATH="$PWD" pytest -q tests/test_a_plus_api_runtime_controls.py
PYTHONPATH="$PWD" python3 scripts/check_deployment_readiness.py
```

## Allowed Claim

```text
Auth/RBAC candidate controls are implemented and visible for reviewer evaluation.
```

## Forbidden Claims

```text
customer IAM approved
production access model certified
regulatory access-control certification
customer security approved
```
