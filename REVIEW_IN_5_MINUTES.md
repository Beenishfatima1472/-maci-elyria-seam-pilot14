
Review in 5 Minutes
1. Read the Core Rule
MACI may inform.
MACI may not bind.
Workflow may not bypass.
Receipt must prove.
Replay must verify.
Refusal must produce no-bind.
2. Run Tests
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
3. Generate Proofs
python3 scripts/generate_ai_agent_proofs.py
4. Run the Demo
python -m api.app

Open:

http://127.0.0.1:8080/viewer
5. Verify the Claim

A reviewer should confirm:

MACI cannot bind consequence.
Workflow cannot bypass boundary.
Refusal produces no-bind.
Hold blocks protected effect.
Escalation blocks protected effect.
Narrow blocks original-scope protected effect.
Admission is the only automatic protected-effect path.
Receipts preserve proof.
Replay verifies same, changed, and tampered conditions.
6. Fast Visual Check

In the viewer, confirm these panels are visible:

MACI Intake
Boundary Resolution
Boundary Checks
Receipt
Replay
Proof Transcript

