# Review Packet

## Primary Review Path

Start here:

```text
README.md
DEMO_RUNBOOK.md
REVIEWER_CHECKLIST.md
VERIFY_NO_BIND.md
API_REFERENCE.md
Architecture Review
FULLSTACK_ARCHITECTURE.md
CLAIMS_BOUNDARY.md
PUBLIC_SAFE_BOUNDARY.md
PUBLIC_POSITIONING.md
Buyer Review
BUYER_REVIEW_GUIDE.md
apps/buyer-demo/index.html
apps/proof-viewer/index.html
Regulator / Independent Reviewer Review
REGULATOR_REVIEW_GUIDE.md
proofs/proof-transcripts/ai-agent-action/
tests/test_workflow_non_bypass.py
tests/test_proof_transcripts.py
tests/test_fullstack_runtime_expansion.py
Runtime Proof Commands
pytest
python3 scripts/generate_ai_agent_proofs.py
python -m api.app

Open:

http://127.0.0.1:8080/viewer
Minimum Review Claim

A reviewer should be able to confirm:

MACI cannot bind consequence.
Workflow cannot bypass boundary.
Refusal produces no-bind.
Hold blocks protected effect.
Escalation blocks protected effect.
Narrow blocks original-scope effect.
Admission is the only automatic protected-effect path.
Receipts preserve proof.
Replay verifies same, changed, and tampered conditions.

