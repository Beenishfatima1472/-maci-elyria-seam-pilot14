# Deployment Runbook

## Status

This is a production-candidate deployment path.

It is not production certified until customer security approval, external audit, or formal certification is complete.

## Preflight

```bash
APP_ENV=production \
ELYRIA_REQUIRE_AUTH=true \
ELYRIA_REQUIRE_TENANT=true \
ELYRIA_AUDIT_ENABLED=true \
ELYRIA_API_KEYS="admin:key-with-at-least-32-characters:admin:tenant-a" \
ELYRIA_RECEIPT_SIGNING_KEY="signing-key-with-at-least-32-characters" \
ELYRIA_RECEIPT_KEY_ID="production-key-id" \
ELYRIA_BOUNDARY_ENGINE=private \
ELYRIA_PRIVATE_BOUNDARY_MODULE=elyria_private.engine:evaluate_boundary \
PYTHONPATH=. python3 scripts/production_preflight.py
Deploy
cp deployment/.env.production.template deployment/.env.production
# edit deployment/.env.production with real secret-manager injected values
docker compose -f deployment/docker-compose.production.yml up -d --build
Health
curl -s http://127.0.0.1:8080/live
curl -s http://127.0.0.1:8080/ready
curl -s http://127.0.0.1:8080/health
Authenticated Request
curl -s http://127.0.0.1:8080/security/status \
  -H "X-Elyria-Api-Key: <api-secret>" \
  -H "X-Elyria-Tenant-Id: tenant-a"
Required Before Production Authorization
written commercial scope
customer security approval
private Elyria/VERITA kernel integration
tenant isolation test pass
KMS/HSM signing configured
audit chain verification pass
monitoring configured
rollback tested
