# Production Readiness

## Status

This repository is a public-safe production-readiness review build for the MACI public-safe seam pilot on Elyria/VERITA.

It is an audit-ready production-runtime candidate shell for reviewer evaluation.

It is not production certified.

Customer security approval or external audit remains the certification gate.

## Correct Current Lane

```text
A+ audit-ready production-runtime candidate shell with decomposed reviewer-grade artifacts, fail-closed runtime gate, protected Elyria/VERITA private-kernel adapter, auth/RBAC candidate controls, tenant-isolation candidate controls, persistent receipt/audit contracts, production signing adapter, independent verifier, deployment readiness package, and certification gated by customer security approval or external audit.
```

## Implemented Public-Safe Candidate Controls

These controls are implemented in the public-safe candidate shell for reviewer evaluation:

- Structured intake.
- Assumption precheck.
- Boundary adapter route.
- Workflow non-bypass gate.
- Fail-closed no-bind behavior.
- Deterministic signed receipts.
- Replay verification.
- Proof transcripts.
- Review bundle generation.
- External verifier package.
- Deployment-readiness checker.
- Secret scan.
- SBOM generation.
- Signed release provenance candidate.
- Supply-chain readiness check.

## Public-Safe Candidate Contracts

These contracts are visible as reviewer-grade artifacts and code contracts:

- `AUTH_RBAC.md`
- `TENANT_ISOLATION.md`
- `PERSISTENT_RECEIPT_STORE.md`
- `PERSISTENT_AUDIT_LEDGER.md`
- `PRODUCTION_SIGNING_ADAPTER.md`
- `DEPLOYMENT_SECURITY_CHECKLIST.md`
- `OPERATIONS_RUNBOOK.md`
- `DEPLOYMENT_READINESS.md`

Implementation evidence includes:

- `maci_elyria/rbac.py`
- `maci_elyria/tenant_isolation.py`
- `maci_elyria/sqlite_runtime_store.py`
- `maci_elyria/production_signing.py`
- `maci_elyria/api_hardening.py`
- `api/app.py`
- `external-verifier/verify_bundle.py`
- `tests/test_a_plus_api_runtime_controls.py`
- `scripts/check_deployment_readiness.py`
- `scripts/production_preflight.py`

## Customer/Audit-Gated Production Controls

The following are implemented as production-runtime candidate controls for reviewer evaluation; customer production approval remains gated:

- Auth/RBAC candidate controls.
- Tenant-isolation candidate controls.
- Persistent receipt-store contract.
- Persistent audit-ledger contract.
- Production signing adapter contract.
- Key rotation lifecycle.
- Key revocation lifecycle.
- API hardening posture.
- Monitoring and incident response runbook.
- Deployment security checklist.

A real customer deployment must still approve:

- customer identity provider integration
- customer tenant provisioning and lifecycle model
- customer database/storage backend
- customer KMS/HSM or secret manager
- customer monitoring and alerting stack
- customer incident response ownership
- customer rollback ownership
- customer policy-pack review
- external audit or customer security approval record
- written commercial scope

## Verification Commands

```bash
PYTHONPATH="$PWD" pytest -q
PYTHONPATH="$PWD" python3 scripts/check_deployment_readiness.py
PYTHONPATH="$PWD" python3 scripts/production_preflight.py
PYTHONPATH="$PWD" python3 external-verifier/verify_bundle.py proofs/proof-transcripts
```

Expected readiness result:

```text
ready: true
missing_files: []
```

## Forbidden Claims

Do not claim:

```text
production certified
regulatory certified
customer security approved
external audit approved
customer-managed production runtime without approval
commercial deployment rights without written scope
public exposure of private Elyria/VERITA kernel
```

## Certification Gate

The repository cannot self-certify.

Production certification requires customer security approval or external audit.
