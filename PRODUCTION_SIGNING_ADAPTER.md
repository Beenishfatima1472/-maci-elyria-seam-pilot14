# Production Signing / KMS-HSM Adapter Contract

## Status

Implemented as a KMS/HSM-ready production-signing candidate contract for reviewer evaluation.

Customer production approval remains gated.

This artifact documents the signing adapter boundary for the MACI / Elyria production-runtime candidate shell.

It does not claim custody of production keys.

## Runtime Evidence

Code and tests:

- `maci_elyria/production_signing.py`
- `maci_elyria/signing.py`
- `scripts/production_preflight.py`
- `scripts/generate_release_provenance.py`
- `scripts/verify_receipts.py`
- `external-verifier/verify_bundle.py`

## Contract Fields

The production signing contract exposes:

- key_id
- key_backend
- verifier_separation_required
- rotation_required
- revocation_required
- failed_signature_behavior
- external_verification_required

## Required Runtime Behavior

The candidate model requires:

1. Production mode declared by environment.
2. Receipt key ID present.
3. Signing backend not set to demo/public-review mode.
4. Signing key supplied outside the repository.
5. External verification path available.
6. Verifier separation maintained.
7. Failed signature handled fail-closed.
8. Key rotation required.
9. Key revocation required.

## KMS/HSM Boundary

The public repo does not include production key custody.

It defines the adapter contract a customer deployment must bind to:

- customer KMS
- customer HSM
- approved secret manager
- approved signing service

## Key Rotation Lifecycle

A production deployment must define:

1. active key ID
2. prior key IDs still accepted for verification
3. key creation authority
4. rotation interval
5. emergency rotation trigger
6. verifier update procedure
7. receipt validation across old and new keys
8. audit event for each key lifecycle action

## Key Revocation Lifecycle

A production deployment must define:

1. compromised key detection
2. revocation authority
3. revocation timestamp
4. affected receipt range
5. verifier-deny behavior for revoked keys
6. customer-security approval record
7. remediation evidence bundle

## Failure Behavior

Expected failures:

- Missing key ID fails preflight.
- Demo backend in production fails preflight.
- Missing signing key fails preflight.
- Bad signature fails verification.
- Wrong key ID fails verification.
- Revoked key fails verification in customer deployment.

## Reviewer Verification

```bash
APP_ENV=production \
ELYRIA_RECEIPT_SIGNING_KEY="signing-key-with-at-least-32-characters" \
ELYRIA_RECEIPT_KEY_ID="ci-production-key" \
ELYRIA_SIGNING_BACKEND="KMS_OR_HSM_CI_PLACEHOLDER" \
PYTHONPATH="$PWD" python3 scripts/production_preflight.py
```

## Allowed Claim

```text
Production signing adapter contract is KMS/HSM-ready and externally gated.
```

## Forbidden Claims

```text
customer KMS approved
customer HSM approved
production key custody certified
regulatory signing certification
customer security approved
```
