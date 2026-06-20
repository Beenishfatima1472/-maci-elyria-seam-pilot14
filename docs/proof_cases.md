# MACI Proof Cases

This document defines the public-safe proof cases for the MACI seam pilot.

The proof surface is intentionally bounded: MACI may inform a consequence-boundary decision, but it may not bind consequence by itself.

## Proof Matrix

| Proof case | Purpose | Expected result | Effect binding |
|---|---|---|---|
| Valid structured packet | Confirms structured language, input, and consequence objects support public seam admissibility. | `CONDITIONALLY_ADMISSIBLE` | `BOUNDARY_RESULT_REQUIRED_BEFORE_BIND` |
| Uncertain language | Confirms ambiguous or low-confidence language context triggers review. | `ESCALATE` | `NO_BIND` |
| Missing authority | Confirms MACI context cannot substitute for authority. | `REFUSE` | `NO_BIND` |
| Changed context | Confirms material context drift forces review before movement continues. | `ESCALATE` | `NO_BIND` |
| No-bind attempt | Confirms MACI cannot bind consequence without boundary control. | `HALT` | `NO_BIND` |

## Critical invariant

MACI may inform.

MACI may not independently bind consequence.

Every consequence-bearing path must pass through boundary resolution.
