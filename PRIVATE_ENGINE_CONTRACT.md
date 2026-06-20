
Private Engine Contract
Public Contract

A private Elyria/VERITA engine may be attached without committing private logic.

Environment:

ELYRIA_BOUNDARY_ENGINE=private
ELYRIA_PRIVATE_BOUNDARY_MODULE=elyria_private.engine:evaluate_boundary

The private module must export:

def evaluate_boundary(packet: dict) -> BoundaryResult:
    ...

The return type must be:

maci_elyria.models.BoundaryResult
Required Behavior

The private engine must preserve these public contract rules:

MACI cannot bind consequence.
Workflow cannot bypass boundary.
Receipts must be issued after boundary resolution.
Replay must verify same, changed, and tampered states.
No protected effect may proceed unless boundary returns ADMIT / ADMITTED.
Non-Commit Rule

Do not commit:

elyria_private/
private_engine/
private_policy_packs/
production rules
customer rules
secret configs
private keys
tokens

