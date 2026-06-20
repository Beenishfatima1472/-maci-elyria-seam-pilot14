# Interface Contract

## Purpose

This document defines the public-safe seam contract between the MACI structured-context layer and the Elyria/VERITA consequence boundary.

The contract defines what MACI may submit, what the boundary returns, and why structured context may inform but never independently bind consequence.

## Core Boundary

```text
Structured context may inform the boundary.
Structured context does not bind consequence.
```

## Integration Position

```text
MACI domain/context signal layer
→ structured MACI seam packet
→ public seam validator
→ execution-boundary resolver
→ deterministic receipt
→ replay verifier
→ no-bind enforcement
```

## Ingress Packet

```json
{
  "packet_id": "MACI-SEAM-001",
  "language_context": {
    "confidence": "high",
    "ambiguity_detected": false,
    "interpretation_basis": "bounded_domain_signal"
  },
  "input_context": {
    "source_state": "valid",
    "lineage_status": "present"
  },
  "consequence_signal": {
    "requested_motion": "domain_action",
    "effect_attempted": false
  },
  "authority_state": "valid",
  "context_state": "unchanged"
}
```

## Required Structured Objects

| Object | Required | Purpose |
|---|---:|---|
| `language_context` | yes | Preserves language confidence, ambiguity, and interpretation basis. |
| `input_context` | yes | Preserves source state and input lineage. |
| `consequence_signal` | yes | Preserves requested motion and effect attempt status. |

These objects must remain structured. They must not be flattened into strings.

## Outcome Packet

```json
{
  "packet_id": "MACI-SEAM-001",
  "boundary_decision": "CONDITIONALLY_ADMISSIBLE",
  "reason_code": "BOUNDARY_SUPPORTED",
  "effect_binding_status": "BOUNDARY_RESULT_REQUIRED_BEFORE_BIND",
  "structured_context_preserved": true,
  "context_bound_consequence": false,
  "receipt_hash": "deterministic_hash_bound_to_packet_law_and_decision"
}
```

## Decision Enums

```text
CONDITIONALLY_ADMISSIBLE
ESCALATE
REFUSE
HALT
```

## Reason Codes

```text
BOUNDARY_SUPPORTED
LANGUAGE_UNCERTAINTY
AUTHORITY_FAILURE
CHANGED_CONTEXT
NO_BIND_ENFORCEMENT
STRUCTURE_FLATTENED
INPUT_CONTEXT_FAILURE
CONSEQUENCE_SIGNAL_MISSING
REPLAY_MISMATCH
```

## Effect Binding Status

```text
BOUNDARY_RESULT_REQUIRED_BEFORE_BIND
NO_BIND
```

## Failure Semantics

| Condition | Boundary Behavior |
|---|---|
| Ambiguous language context | `ESCALATE` / `NO_BIND` |
| Missing language context | `REFUSE` / `NO_BIND` |
| Flattened language context | `REFUSE` / `NO_BIND` |
| Missing input context | `REFUSE` / `NO_BIND` |
| Missing consequence signal | `REFUSE` / `NO_BIND` |
| Authority missing | `REFUSE` / `NO_BIND` |
| Changed context | `ESCALATE` / `NO_BIND` |
| Context contradiction | `ESCALATE` / `NO_BIND` |
| Effect attempted before boundary result | `HALT` / `NO_BIND` |
| Replay mismatch | `REFUSE` or `ESCALATE` / `NO_BIND` |

## Receipt Contract

A boundary receipt should bind:

```text
packet_id
language_context hash
input_context hash
consequence_signal hash
authority state
context state
boundary decision
reason code
effect binding status
structured context preservation flag
receipt hash
```

## Non-Negotiable Rule

```text
No MACI-side context signal, interpretation, structured object, or domain conclusion may bind consequence without an Elyria/VERITA boundary result.
```

## Public Boundary

This contract is a public-safe seam contract.

It does not expose protected runtime logic, private admissibility geometry, substrate mechanics, production enforcement rules, or partner-specific deployment internals.
