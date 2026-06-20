# Reviewer Checklist

## Boundary Claim

- [ ] MACI is described as the customer-facing domain/context layer.
- [ ] Elyria/VERITA is described as the consequence-boundary runtime.
- [ ] MACI is not allowed to bind consequence.
- [ ] Protected consequence requires boundary admission.

## Movement Packet

- [ ] Proposed movement is visible.
- [ ] Actor is visible.
- [ ] Intended consequence is visible.
- [ ] Affected party is visible.
- [ ] MACI context is visible.
- [ ] Boundary inputs are visible.

## Boundary Inputs

- [ ] Standing is evaluated.
- [ ] Authority is evaluated.
- [ ] Evidence is evaluated.
- [ ] Scope is evaluated.
- [ ] Custody is evaluated.
- [ ] Route closure is evaluated.

## Boundary Results

- [ ] REFUSE is supported.
- [ ] HOLD is supported.
- [ ] ESCALATE is supported.
- [ ] NARROW is supported.
- [ ] CONDITIONALLY_ADMISSIBLE is supported.
- [ ] ADMIT is supported.
- [ ] HALT is supported for MACI bind attempts.

## Formation Status

- [ ] NO_BIND is produced for refusal/blocking.
- [ ] NARROWED is produced for narrowed scope.
- [ ] CONDITIONALLY_ADMITTED is not automatic execution.
- [ ] ADMITTED is the only automatic protected-effect path.

## Receipts

- [ ] Receipt includes packet hash.
- [ ] Receipt includes result hash.
- [ ] Receipt includes policy version.
- [ ] Receipt includes formation status.
- [ ] Receipt includes no-bind status.
- [ ] Receipt includes receipt hash.
- [ ] Receipt includes witness digest.

## Replay

- [ ] Same-condition replay matches.
- [ ] Changed authority changes result.
- [ ] Changed evidence changes result.
- [ ] Changed scope changes result.
- [ ] Changed custody changes result.
- [ ] Tampered packet mismatches.
- [ ] Tampered receipt is invalid.

## Workflow Non-Bypass

- [ ] Workflow does not execute on REFUSE.
- [ ] Workflow does not execute on HOLD.
- [ ] Workflow does not execute on ESCALATE.
- [ ] Workflow does not execute original scope on NARROW.
- [ ] Workflow does not auto-execute on CONDITIONALLY_ADMISSIBLE.
- [ ] Workflow executes only on ADMIT / ADMITTED.

## UI Review

- [ ] Buyer demo opens.
- [ ] Proof viewer opens.
- [ ] Boundary result is visible.
- [ ] Receipt is visible.
- [ ] Replay is visible.
- [ ] Proof transcript is visible.
