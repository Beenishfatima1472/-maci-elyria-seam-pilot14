# Operations Runbook

## Status

Reviewer-grade operations and incident-response runbook for the production-runtime candidate shell.

Customer production approval remains gated.

This runbook documents the operational posture expected around the public-safe MACI / Elyria candidate runtime.

It is not a customer operations approval.

## Required Operational Owners

A customer deployment must assign:

- deployment owner
- security owner
- incident response owner
- rollback owner
- key-management owner
- audit/evidence owner

## Routine Health Checks

Required checks:

```text
GET /health
GET /ready
GET /runtime/status
GET /security/status
GET /audit/verify
```

Expected behavior:

- liveness responds
- readiness only passes when configured requirements are satisfied
- runtime status exposes candidate lane and gate status
- security status exposes production gate posture
- audit verification reports ledger integrity

## Alert Triggers

Alert on:

- missing_api_key
- invalid_api_key
- role_not_permitted
- tenant_scope_violation
- missing_idempotency_key
- duplicate_idempotency_key
- rate_limit_exceeded
- request_too_large
- receipt_not_found_for_tenant
- proof_not_found_for_tenant
- signature_mismatch
- wrong_key_id
- missing_signature
- production_gate_failed
- private_boundary_adapter_failure
- audit_ledger_invalid

## Incident Response Procedure

1. Stop affected traffic path if active.
2. Preserve receipts, proofs, replay outputs, audit ledger, SBOM, provenance, and deployment configuration.
3. Identify affected tenant scope.
4. Verify affected receipts using `scripts/verify_receipts.py`.
5. Verify proof bundles using `scripts/verify_proof_bundle.py`.
6. Run the external verifier package outside live runtime trust.
7. Rotate affected keys or credentials if required by customer policy.
8. Snapshot current runtime database and logs.
9. Restore prior approved deployment if required.
10. Record incident timeline, evidence, remediation, and approval trail.

## Rollback Procedure

1. Disable production ingress.
2. Preserve evidence.
3. Restore prior approved image or commit.
4. Restore approved configuration.
5. Re-run deployment preflight.
6. Re-run receipt/proof verification.
7. Obtain customer-security approval before returning to production traffic.

## Key Rotation Procedure

1. Generate new key in customer-approved key manager.
2. Assign new key ID.
3. Update verifier key registry.
4. Preserve old key for allowed historical verification window.
5. Issue audit event for rotation.
6. Re-run preflight and external verifier.

## Key Revocation Procedure

1. Mark affected key ID as inactive according to customer policy.
2. Identify affected receipt time range.
3. Preserve affected receipts and audit trail.
4. Apply verifier deny behavior for inactive keys according to customer policy.
5. Reissue or quarantine affected artifacts when required.
6. Record customer-security approval.

## Evidence Bundle

A complete incident or audit evidence bundle should include:

- receipts
- proof bundles
- replay outputs
- audit-ledger export
- SBOM
- release provenance
- deployment configuration
- key-ID history
- verifier output
- incident timeline

## Allowed Claim

```text
Operations runbook is documented for reviewer and customer-operations evaluation.
```

## Forbidden Claims

```text
customer operations approved
incident response certified
customer security approved
external audit approved
production certified
```
