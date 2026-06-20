# Demo Runbook

## Purpose

This runbook lets a reviewer verify the MACI-Elyria consequence-boundary demo without private runtime access.

## Core Rule

```text
MACI may inform.
MACI may not bind.
Nothing becomes protected consequence until Elyria/VERITA admits formation.
1. Install
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
2. Run Tests
pytest

Expected:

all tests pass
3. Generate Proof Transcripts
python3 scripts/generate_ai_agent_proofs.py

Expected output includes:

missing_authority.json => REFUSE / NO_BIND
uncertain_language.json => ESCALATE / NO_BIND
insufficient_evidence.json => HOLD / NO_BIND
scope_too_broad.json => NARROW / NARROWED
admit_allowed.json => ADMIT / ADMITTED
4. Run API
python -m api.app

Open:

http://127.0.0.1:8080/
http://127.0.0.1:8080/viewer
5. Buyer Verification Path

In the proof viewer:

Submit default valid packet.
Confirm CONDITIONALLY_ADMISSIBLE / CONDITIONALLY_ADMITTED.
Load missing authority case.
Confirm REFUSE / NO_BIND.
Confirm receipt exists.
Confirm replay shows same-condition, changed-condition, and tamper modes.
6. Boundary Tests

A reviewer should verify:

MACI cannot bind consequence.
Workflow cannot bypass boundary.
Refusal produces no-bind.
Hold blocks execution.
Escalation blocks execution.
Narrow does not execute original scope.
Admission is the only automatic protected-effect path.
Replay detects changed conditions.
Replay detects tampered packets and tampered receipts.
7. Public Boundary

This repository is public-safe. It does not expose protected Elyria kernel mechanics, private admissibility geometry, production enforcement rules, legal advice, medical advice, financial advice, or certification authority.
