# Full-Stack Architecture

## Purpose

This document defines the public-safe public-safe executable seam expansion of the MACI-Elyria seam pilot.

## Stack Shape

```text
Customer / Buyer / Workflow
        ↓
MACI Surface Layer
        ↓
Structured Movement Packet
        ↓
Workflow Harness
        ↓
Elyria Consequence Boundary Runtime
        ↓
Standing / Authority / Evidence / Scope / Custody Resolver
        ↓
Result:
REFUSE / HOLD / ESCALATE / NARROW / CONDITIONALLY_ADMISSIBLE / ADMIT
        ↓
Formation Status:
NO_BIND / NON_FORMED / PENDING_REVIEW / NARROWED / CONDITIONALLY_ADMITTED / ADMITTED
        ↓
Receipt Service
        ↓
Replay Service
        ↓
Proof Viewer
```

## Service Boundaries

| Layer | Responsibility | Binding Authority |
|---|---|---:|
| MACI intake | Domain/context intake and packet creation | No |
| Workflow harness | Wraps proposed movement into proof workflow | No |
| Boundary runtime | Resolves admissibility and formation status | Yes |
| Receipt service | Emits deterministic receipt for result | No, proof only |
| Replay service | Replays same/changed conditions | No, proof only |
| Witness service | Anchors public seam witness digest | No, proof only |
| Proof viewer | Displays transcript and replay result | No |

## Boundary Rule

A workflow may not proceed to protected effect unless the boundary runtime returns `ADMIT` or an explicitly allowed `CONDITIONALLY_ADMISSIBLE` state with human review.
