# Verify No-Bind Behavior

## Purpose

This document shows how to verify that proposed movement does not become protected consequence unless the boundary runtime admits formation.

## Rule

```text
No movement binds merely because MACI structured it.
No workflow executes protected effect merely because a packet exists.
No consequence forms unless Elyria/VERITA admits formation.
Run Tests
pytest

Relevant test files:

tests/test_workflow_non_bypass.py
tests/test_fullstack_runtime_expansion.py
tests/test_proof_transcripts.py
tests/test_api_smoke.py
Verify Refusal
curl -X POST http://127.0.0.1:8080/boundary/resolve \
  -H "Content-Type: application/json" \
  -d @corridors/ai-agent-action/packets/missing_authority.json

Expected:

boundary_result = REFUSE
formation_status = NO_BIND
reason_code = MISSING_AUTHORITY
Verify Hold
curl -X POST http://127.0.0.1:8080/boundary/resolve \
  -H "Content-Type: application/json" \
  -d @corridors/ai-agent-action/packets/insufficient_evidence.json

Expected:

boundary_result = HOLD
formation_status = NO_BIND
reason_code = INSUFFICIENT_EVIDENCE
Verify Escalation
curl -X POST http://127.0.0.1:8080/boundary/resolve \
  -H "Content-Type: application/json" \
  -d @corridors/ai-agent-action/packets/uncertain_language.json

Expected:

boundary_result = ESCALATE
formation_status = NO_BIND
reason_code = LANGUAGE_UNCERTAINTY
Verify Narrow
curl -X POST http://127.0.0.1:8080/boundary/resolve \
  -H "Content-Type: application/json" \
  -d @corridors/ai-agent-action/packets/scope_too_broad.json

Expected:

boundary_result = NARROW
formation_status = NARROWED
protected effect at original scope = blocked
Verify MACI Bind Attempt Refusal
curl -X POST http://127.0.0.1:8080/boundary/resolve \
  -H "Content-Type: application/json" \
  -d @corridors/ai-agent-action/packets/maci_bind_attempt.json

Expected:

boundary_result = HALT
formation_status = NO_BIND
reason_code = MACI_CANNOT_BIND_CONSEQUENCE
Verify Admission
curl -X POST http://127.0.0.1:8080/boundary/resolve \
  -H "Content-Type: application/json" \
  -d @corridors/ai-agent-action/packets/admit_allowed.json

Expected:

boundary_result = ADMIT
formation_status = ADMITTED

Admission is the only automatic protected-effect path.
