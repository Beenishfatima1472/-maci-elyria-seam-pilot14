# Deployment Readiness

## Status

This file is the root deployment-readiness package for the MACI / Elyria public-safe production-runtime candidate shell.

The repository is not production certified.

Certification remains gated by customer security approval or external audit.

## Current Lane

```text
A+ audit-ready production-runtime candidate shell with decomposed reviewer-grade artifacts, fail-closed runtime gate, protected Elyria/VERITA private-kernel adapter, auth/RBAC candidate controls, tenant-isolation candidate controls, persistent receipt/audit contracts, production signing adapter, independent verifier, deployment readiness package, and certification gated by customer security approval or external audit.
```

## Reviewer-Grade Root Artifacts

The deployment-readiness package requires these root reviewer artifacts:

- `AUTH_RBAC.md`
- `TENANT_ISOLATION.md`
- `PERSISTENT_RECEIPT_STORE.md`
- `PERSISTENT_AUDIT_LEDGER.md`
- `PRODUCTION_SIGNING_ADAPTER.md`
- `DEPLOYMENT_SECURITY_CHECKLIST.md`
- `OPERATIONS_RUNBOOK.md`
- `DEPLOYMENT_READINESS.md`

## Production-Candidate Architecture

The public repository exposes the review-safe production-candidate shell:

1. API/runtime gate.
2. Auth/RBAC candidate surface.
3. Tenant-isolation candidate surface.
4. Signed receipts.
5. Replay verification.
6. Independent proof-bundle verification.
7. Persistent receipt-store contract.
8. Append-only audit-ledger contract.
9. KMS/HSM-ready signing contract.
10. Deployment readiness and claim lock.

The private Elyria/VERITA kernel remains protected behind adapter contracts.

## Implemented Public-Safe Candidate Controls

Implemented for reviewer evaluation:

- structured intake
- assumption precheck
- workflow non-bypass gate
- no-bind behavior
- receipt generation
- replay verification
- proof transcript generation
- external verifier package
- secret scan
- SBOM generation
- signed candidate provenance
- supply-chain readiness check

## Public-Safe Candidate Contracts

Visible contract files:

- auth/RBAC candidate model
- tenant isolation candidate model
- persistent receipt-store contract
- persistent audit-ledger contract
- production signing adapter contract
- deployment security checklist
- operations runbook

## Customer/Audit-Gated Production Controls

A customer deployment must still approve:

- customer IAM / identity provider
- production KMS/HSM or approved secret manager
- customer tenant isolation architecture
- durable storage approval for receipts and audit
- monitoring and alerting stack
- incident response owner
- rollback owner
- deployment network boundary
- written commercial scope

## Deployment Prerequisites

Before any production deployment, require:

- production environment selected
- auth required
- tenant ID required
- audit enabled
- API credentials configured outside the repository
- signing key configured outside the repository
- receipt key ID configured
- private boundary engine selected
- private boundary module configured
- customer storage backend approved
- customer monitoring backend approved

## Security Approval Checklist

Customer security must review:

- auth/RBAC model
- tenant isolation
- receipt persistence
- audit ledger persistence
- customer-controlled signing keys
- verifier separation from runtime trust
- rate limiting/API hardening
- endpoint permission matrix
- production policy pack
- private adapter integration

## External Audit Checklist

External reviewers should verify:

- proof bundle verifier operates without live app trust
- tampered receipt is detected
- tampered packet is detected
- changed-condition replay is detected
- missing signature is detected
- wrong key ID is detected
- no-bind, halt, refuse, escalate, and admit events are audited
- key rotation/revocation procedure is documented

## Go Criteria

Go only when:

- CI is passing.
- Deployment preflight is passing.
- Customer secrets are configured outside the repo.
- Customer tenant boundary is approved.
- Production signing backend is approved.
- Verifier separation is approved.
- Rollback owner is assigned.
- Incident response owner is assigned.
- Customer security or external audit approval is recorded.

## No-Go Criteria

No-go if:

- Demo key is used in production.
- Private adapter is missing.
- Tenant boundary is unclear.
- Audit/receipt persistence is absent.
- Verifier depends on live runtime trust.
- Customer policy pack is not approved.
- Commercial scope is not written.

## Rollback Plan

Rollback is controlled by the deployment owner:

1. Disable production traffic.
2. Preserve audit ledger and receipts.
3. Snapshot proof bundle state.
4. Revoke affected key material if needed.
5. Restore prior approved deployment.
6. Run verifier on affected receipts.
7. Document incident and corrective action.

## Production Certification Gate

The repository cannot self-certify.

Production certification requires customer security approval or external audit.

## Forbidden Claims

```text
production certified
regulatory certified
customer security approved
external audit approved
customer-managed production runtime without approval
commercial deployment rights without written scope
public exposure of private Elyria/VERITA kernel
```
