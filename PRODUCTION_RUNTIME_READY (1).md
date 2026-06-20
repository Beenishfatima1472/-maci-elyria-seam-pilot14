# Production Runtime Ready

## Status

This repository now includes a production-runtime-ready candidate gate.

It is not production certified.

## Runtime-Ready Candidate Means

The runtime can fail closed unless production conditions are satisfied:

- production mode enabled
- authentication required
- tenant ID required
- audit chain enabled
- API credentials configured
- non-demo signing key configured
- receipt key ID configured
- private boundary engine selected
- private boundary module configured

## Runtime Status Endpoint

```text
GET /runtime/status
Fail-Closed Behavior

In production mode, protected routes refuse requests if the runtime is not ready.

Allowed public status routes:

/health
/live
/ready
/security/status
/runtime/status
Correct Claim
production-runtime-ready candidate with fail-closed runtime gate
Not Claimed
production certified
customer security approved
external audit approved
full private Elyria kernel exposed
Required Before Production Certification
customer security approval
external audit or equivalent formal approval
private Elyria/VERITA kernel validation
KMS/HSM signing
operational monitoring
incident response approval
written commercial scope
