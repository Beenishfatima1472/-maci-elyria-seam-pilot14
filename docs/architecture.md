# MACI Seam Architecture

## Layering

```text
Language Context
      │
Input Context
      │
Consequence Signal
      │
      ▼
MACI Seam Packet
      ▼
Validator
      ▼
Boundary Resolver
      ▼
Receipt Generator
      ▼
Replay Verification
```

## Public Boundary

The MACI seam is intentionally public-safe.

The pilot demonstrates structured context preservation and boundary evaluation.

The pilot does not expose protected runtime implementation details.

## Invariant

MACI may inform.

MACI may not independently bind consequence.

Boundary resolution remains required before consequence-bearing movement becomes admissible.
