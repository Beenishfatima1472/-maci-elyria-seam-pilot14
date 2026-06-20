# Worked MACI Corridor

## Purpose

This document provides one concrete, end-to-end MACI seam corridor.

It demonstrates how structured language, input, and consequence context may inform a boundary decision without independently binding consequence.

## Core Claim

```text
Structured context may inform the boundary.
Structured context does not bind consequence.
```

## Scenario

A MACI packet contains valid structured objects but the language context becomes uncertain after signal formation.

The packet remains structurally valid, yet the boundary cannot safely admit movement under the current context state.

## Input Packet

```json
{
  "packet_id": "MACI-CORRIDOR-001",
  "language_context": {
    "confidence": "low",
    "ambiguity_detected": true
  },
  "input_context": {
    "source_state": "valid"
  },
  "consequence_signal": {
    "requested_motion": "domain_action"
  },
  "authority_state": "valid"
}
```

## Evaluation

| Check | Result | Reason |
|---|---:|---|
| Structured language object | pass | Object preserved. |
| Structured input object | pass | Object preserved. |
| Structured consequence object | pass | Object preserved. |
| Authority state | pass | Authority present. |
| Language certainty | fail | Ambiguity detected. |
|

## Boundary Resolution

```text
ESCALATE
LANGUAGE_UNCERTAINTY
NO_BIND
```

## Outcome

The packet remains reviewable.

No consequence is admitted.

No consequence binds.

## Reviewer Conclusion

The MACI seam preserves structure across language, input, and consequence dimensions.

The boundary proves that structured context may influence evaluation while remaining incapable of independently binding consequence.
