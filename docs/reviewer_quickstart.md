# Reviewer Quickstart

## Goal

Review the MACI seam pilot without needing access to any protected runtime.

## Steps

1. Inspect the schema.
2. Review bundled example packets.
3. Run the sandbox harness.
4. Review expected outcomes.
5. Verify receipt generation.
6. Verify replay stability.

## Expected outcomes

- Valid packet -> CONDITIONALLY_ADMISSIBLE
- Missing authority -> REFUSE
- Uncertain language -> ESCALATE
- Changed context -> ESCALATE
- No-bind attempt -> HALT

## Key invariant

MACI may inform.

MACI may not independently bind consequence.
