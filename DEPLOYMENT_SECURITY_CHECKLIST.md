# Deployment Security Checklist

## Status

Root reviewer-grade artifact for production-runtime candidate evaluation.

This file is intentionally present at the repository root so public reviewers can find the deployment security checklist without navigating into nested folders.

It complements the nested checklist at:

```text
production/security/PRODUCTION_SECURITY_CHECKLIST.md
```

This checklist does not approve or certify production deployment.

## Review Purpose

This artifact lets a reviewer confirm that the public-safe candidate shell has visible security review categories for:

- identity and access
- tenant isolation
- receipt and replay evidence
- persistent storage
- signing and key lifecycle
- API hardening
- monitoring and incident response
- release and supply chain

## Identity and Access

Required checks:

- API authentication enabled.
- Tenant ID required where tenant isolation is enabled.
- Role mapped to every protected endpoint.
- Unknown role fails closed.
- Unauthorized role/action pair fails closed.
- Admin role reviewed and assigned.
- Service-account access reviewed.

## Tenant Isolation

Required checks:

- Tenant ID attached to packets.
- Tenant ID attached to receipts.
- Tenant ID attached to proofs.
- Tenant ID attached to audit events.
- Cross-tenant receipt lookup denied.
- Cross-tenant proof read denied.
- Cross-tenant replay denied.

## Receipt and Replay Evidence

Required checks:

- Receipts are signed.
- Receipt key ID is present.
- Replay token is preserved.
- Packet digest is preserved.
- Verification failure is fail-closed.
- Tampered packet detection is tested.
- Tampered receipt detection is tested.
- Changed-condition replay detection is tested.

## Persistent Storage

Required checks:

- Receipt persistence candidate control is present.
- Audit persistence candidate control is present.
- Backup policy is defined by customer deployment.
- Restore policy is defined by customer deployment.
- Retention policy is defined by customer deployment.
- Evidence preservation policy is defined by customer deployment.

## Signing and Keys

Required checks:

- Production key is not committed to the repository.
- Demo key is blocked in production.
- KMS/HSM or customer-approved secret manager is selected.
- Key ID is set.
- Key rotation lifecycle is documented.
- Key revocation lifecycle is documented.
- External verifier has a key verification path.

## API Hardening

Required checks:

- Request-size limit enabled.
- Rate limiting enabled.
- Idempotency required for state-changing calls.
- Replay protection enabled.
- Security headers emitted.
- Strict CORS reviewed.
- Validation failure returns a non-binding response.

## Monitoring and Incident Response

Required checks:

- Liveness check defined.
- Readiness check defined.
- Audit verification endpoint reviewed.
- Alert triggers defined.
- Incident owner assigned by customer deployment.
- Rollback owner assigned by customer deployment.
- Evidence preservation process defined.

## Release and Supply Chain

Required checks:

- Tests pass.
- Review bundle generated.
- Receipts verify.
- Proof bundle verifies.
- External verifier package verifies.
- Secret scan passes.
- SBOM generated.
- Signed candidate provenance generated.
- Supply-chain readiness passes.
- Deployment preflight passes.

## Go Condition

All checks must be satisfied by the customer deployment owner and customer security owner before production certification can be claimed.

## No-Go Conditions

No-go if any of the following are true:

- Demo key is used in production.
- Private boundary adapter is missing.
- Tenant scope is unclear.
- Receipt or audit persistence is absent.
- Verifier depends only on live runtime memory.
- Customer policy pack is not approved.
- Customer security approval is not recorded.
- External audit or customer approval is incomplete.

## Allowed Claim

```text
Deployment security checklist is present as a root reviewer-grade artifact for customer-security and external-review evaluation.
```

## Forbidden Claims

```text
customer security approved
external audit approved
production certified
regulatory certified
commercial deployment rights without written scope
public exposure of private Elyria/VERITA kernel
```
