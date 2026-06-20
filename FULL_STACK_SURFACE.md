
Full Stack Surface
Included Public-Safe Layers
apps/buyer-demo
apps/proof-viewer
api/app.py
maci_elyria/assumptions.py
maci_elyria/boundary_engine.py
maci_elyria/resolver.py
maci_elyria/workflow.py
maci_elyria/receipt.py
maci_elyria/replay.py
maci_elyria/proof.py
packages/schemas
corridors
proofs
tests
scripts/build_review_bundle.py
.github/workflows
Runtime Flow
customer context
→ MACI intake
→ movement packet
→ assumption precheck
→ protected boundary adapter
→ public-safe or private boundary engine
→ workflow gate
→ deterministic receipt
→ replay verifier
→ proof transcript
→ buyer proof viewer
→ review bundle
Logic Boundary

The public-safe resolver proves the seam behavior.

The production/private logic stays hidden behind the protected boundary adapter.
