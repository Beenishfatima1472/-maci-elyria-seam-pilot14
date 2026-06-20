# API Reference

Base URL:

```text
http://localhost:8080
GET /health

Returns API health.

curl http://localhost:8080/health
POST /maci/intake

Receives customer/domain input and returns a structured movement packet.

MACI may structure context. MACI may not bind consequence.

curl -X POST http://localhost:8080/maci/intake \
  -H "Content-Type: application/json" \
  -d '{
    "proposed_action": "send_customer_impacting_email",
    "intended_consequence": "customer-impacting communication",
    "authority": { "status": "VALID" },
    "evidence": { "status": "SUFFICIENT" },
    "scope": { "status": "VALID" },
    "custody": { "status": "VALID" },
    "maci_can_bind": false
  }'
POST /boundary/resolve

Resolves the boundary result and formation status.

curl -X POST http://localhost:8080/boundary/resolve \
  -H "Content-Type: application/json" \
  -d @corridors/ai-agent-action/packets/missing_authority.json

Expected result:

REFUSE / NO_BIND
POST /receipt/create

Creates deterministic receipt for packet and boundary result.

curl -X POST http://localhost:8080/receipt/create \
  -H "Content-Type: application/json" \
  -d '{"movement_packet": {}}'

Receipt binds:

packet_hash
result_hash
policy_version
formation_status
no_bind_status
receipt_hash
witness_digest
POST /replay/run

Runs replay proof.

Replay modes:

SAME_CONDITIONS
CHANGED_AUTHORITY
CHANGED_EVIDENCE
CHANGED_SCOPE
CHANGED_CUSTODY
TAMPERED_PACKET
TAMPERED_RECEIPT
POST /proof/create

Creates full proof transcript.

Transcript includes:

movement_packet
boundary_result
receipt
workflow
replay
final_claim
GET /proof/<proof_id>

Returns stored proof transcript from current API runtime memory.

UI Routes
/              Buyer demo
/buyer-demo    Buyer demo
/viewer        Proof viewer

