# Release Checklist

## Before Release

- [ ] `pytest` passes locally.
- [ ] `python3 scripts/generate_ai_agent_proofs.py` runs successfully.
- [ ] `python3 scripts/build_review_bundle.py` creates `dist/maci-elyria-review-bundle.zip`.
- [ ] `dist/maci-elyria-review-bundle.zip.sha256` is generated.
- [ ] Screenshot exists at `screenshots/04-replay-modes-visible.png`.
- [ ] README shows badges and review path.
- [ ] Commercial boundary is visible.
- [ ] Public-safe boundary is visible.

## GitHub Checks

- [ ] CI workflow passes.
- [ ] Review Bundle workflow passes.
- [ ] Review bundle artifact is downloadable from GitHub Actions.
- [ ] Artifact contains `MANIFEST.json`.
- [ ] Artifact contains `SHA256SUMS.txt`.
- [ ] Artifact contains proof transcripts.
- [ ] Artifact contains reviewer docs.

## Release Tag

Recommended first public review tag:

```text
v0.1.0-public-review
Release Title
MACI–Elyria Public-Safe Review Build v0.1.0
Release Description
Public-safe full-stack consequence-boundary demo showing MACI as the customer-facing domain/context layer and Elyria/VERITA as the protected boundary runtime.

MACI may inform. MACI may not bind. Workflow may not bypass. Receipts prove. Replay verifies. Commercial use requires separate written scope.
Do Not Claim
 Do not claim production certification.
 Do not claim regulatory approval.
 Do not claim legal, medical, or financial authority.
 Do not claim protected Elyria kernel disclosure.
 Do not claim commercial deployment rights.
