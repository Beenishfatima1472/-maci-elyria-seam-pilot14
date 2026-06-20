
Key Management
Public Review Mode

Default public review key:

PUBLIC_REVIEW_DEMO_SIGNING_KEY_NOT_FOR_PRODUCTION

Override locally:

export ELYRIA_RECEIPT_SIGNING_KEY="local-review-key"
export ELYRIA_RECEIPT_KEY_ID="local-review-key-id"
Production Key Requirements

Production requires:

KMS/HSM-backed signing
key rotation
key revocation
least-privilege signer access
signer audit logs
key separation by tenant/environment
independent verifier public key path
incident response process
Do Not Commit
real signing keys
private keys
KMS credentials
tenant secrets
production verifier secrets

