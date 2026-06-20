# OpenAPI Reference

## Base URL

```text
http://localhost:8080
Endpoints
Method	Path	Purpose
GET	/health	Health check and engine descriptor
GET	/engine/status	Protected boundary adapter status
POST	/maci/intake	Create movement packet from MACI context
POST	/assumptions/precheck	Surface embedded assumptions
POST	/boundary/resolve	Resolve boundary decision
POST	/workflow/harness	Verify workflow gate behavior
POST	/receipt/create	Issue deterministic signed receipt
POST	/receipt/verify	Verify signed receipt integrity
POST	/replay/run	Run replay verification
POST	/proof/create	Create proof transcript
GET	/proof/<proof_id>	Retrieve runtime proof transcript
GET	/viewer	Proof viewer UI
GET	/buyer-demo	Buyer demo UI
Receipt Verification

Example:

curl -s http://127.0.0.1:8080/receipt/verify \
  -H "Content-Type: application/json" \
  -d @receipt.json
Production Note

This API is public-safe review infrastructure.

Production deployment requires:

authentication
authorization
tenant isolation
persistent audit storage
monitoring
rate limiting
KMS/HSM-backed signing
external verifier separation
written commercial scope

