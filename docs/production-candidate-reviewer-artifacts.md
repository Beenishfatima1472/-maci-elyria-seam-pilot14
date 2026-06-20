# Production Candidate Reviewer Artifacts

## Purpose

This index points reviewers to the decomposed production-candidate artifacts visible in the public repository.

## Current Lane

```text
A+ audit-ready production-runtime candidate shell with decomposed reviewer-grade artifacts and customer/audit-gated production certification.
```

## Root Artifacts

- [`AUTH_RBAC.md`](../AUTH_RBAC.md)
- [`TENANT_ISOLATION.md`](../TENANT_ISOLATION.md)
- [`PERSISTENT_RECEIPT_STORE.md`](../PERSISTENT_RECEIPT_STORE.md)
- [`PERSISTENT_AUDIT_LEDGER.md`](../PERSISTENT_AUDIT_LEDGER.md)
- [`PRODUCTION_SIGNING_ADAPTER.md`](../PRODUCTION_SIGNING_ADAPTER.md)
- [`DEPLOYMENT_SECURITY_CHECKLIST.md`](../DEPLOYMENT_SECURITY_CHECKLIST.md)
- [`OPERATIONS_RUNBOOK.md`](../OPERATIONS_RUNBOOK.md)
- [`DEPLOYMENT_READINESS.md`](../DEPLOYMENT_READINESS.md)

## Code Evidence

- [`maci_elyria/rbac.py`](../maci_elyria/rbac.py)
- [`maci_elyria/tenant_isolation.py`](../maci_elyria/tenant_isolation.py)
- [`maci_elyria/sqlite_runtime_store.py`](../maci_elyria/sqlite_runtime_store.py)
- [`maci_elyria/production_signing.py`](../maci_elyria/production_signing.py)
- [`maci_elyria/api_hardening.py`](../maci_elyria/api_hardening.py)
- [`api/app.py`](../api/app.py)
- [`external-verifier/verify_bundle.py`](../external-verifier/verify_bundle.py)
- [`tests/test_a_plus_api_runtime_controls.py`](../tests/test_a_plus_api_runtime_controls.py)

## Verification Commands

```bash
PYTHONPATH="$PWD" pytest -q
PYTHONPATH="$PWD" python3 scripts/check_deployment_readiness.py
```

## Certification Boundary

This repository does not claim production certification, regulatory certification, customer security approval, or external audit approval.

Certification remains gated by customer security approval or external audit.
