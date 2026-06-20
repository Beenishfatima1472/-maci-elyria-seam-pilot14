# Rollback Runbook

## Rollback Triggers

- readiness endpoint returns 503
- receipt verification failure
- audit-chain verification failure
- tenant mismatch event
- unauthorized protected-effect attempt
- key compromise suspicion
- private boundary adapter failure

## Immediate Actions

1. Stop ingress traffic.
2. Preserve audit logs.
3. Preserve receipts and proof transcripts.
4. Revoke affected API key or signing key.
5. Roll back to prior image.
6. Run audit verification.
7. Run receipt verification.
8. Document incident.

## Rollback Command

```bash
docker compose -f deployment/docker-compose.production.yml down
docker compose -f deployment/docker-compose.production.yml up -d --build
Evidence Preservation

Do not delete:

runtime/audit/
proofs/proof-transcripts/
dist/review-bundle/
receipt exports
SHA256SUMS.txt

