# Runtime Seam Compliance Bridge

## Correct Public Name

Use:

```text
MACI public-safe seam pilot on Elyria/VERITA

Do not use:

MACI proof layer
Reason

“Proof layer” sounds like the repository only records proof after something else acts.

This repository demonstrates seam behavior:

customer context enters
→ MACI structures context
→ movement packet forms
→ assumption discovery precheck runs
→ Elyria/VERITA boundary evaluates
→ decision returns
→ workflow is gated
→ receipt issues
→ replay checks
→ no-bind holds unless admitted
Reviewer-Facing Runtime Requirements

This repo covers:

MACI cannot bind consequence.
Boundary must evaluate before effect.
Missing authority refuses.
Insufficient evidence holds.
Uncertain language escalates.
Overbroad scope narrows.
Invalid custody refuses.
Workflow cannot bypass.
Receipts prove the boundary result.
Replay checks same, changed, and tampered conditions.
Assumptions are surfaced before proof transcript finalization.
Terminology Bridge

Execution-style language:

EXECUTE only after valid boundary clearance.
REFUSE when authority/standing/custody fails.
HOLD when evidence is insufficient.
ESCALATE when language or material context is uncertain.
NARROW when proposed scope is too broad.
NO-BIND when proposed movement cannot become consequence.

Current repo language:

ADMIT / ADMITTED = allowed protected-effect path
REFUSE / NO_BIND = failed standing, authority, custody, or invalid scope
HOLD / NO_BIND = evidence insufficiency
ESCALATE / NO_BIND = language or context uncertainty
NARROW / NARROWED = original scope blocked; narrowed review only
HALT / NO_BIND = MACI bind attempt or invalid payload
Public Claim
This is a public-safe executable consequence-boundary seam demo.
It is not merely a proof surface.
It is not the private Elyria kernel.

