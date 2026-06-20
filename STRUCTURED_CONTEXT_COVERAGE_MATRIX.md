# Structured Context Coverage Matrix

## Purpose

This matrix makes the MACI seam risk surface explicit for reviewers.

It demonstrates how structured language, input, and consequence context are preserved and evaluated without allowing context signals to independently bind consequence.

## Core Boundary

```text
Structured context may inform the boundary.
Structured context does not bind consequence.
```

## Protected Structured Objects

```text
language_context
input_context
consequence_signal
```

These remain structured objects and are not flattened into simple strings.

## Coverage Matrix

| Failure Mode | Detected? | Boundary Outcome | Effect Binding | Why It Cannot Silently Pass |
|---|---:|---|---|---|
| Ambiguous language context | yes | `ESCALATE` | `NO_BIND` | Uncertain language cannot self-resolve into consequence. |
| Missing language context | yes | `REFUSE` | `NO_BIND` | Required context object is absent. |
| Flattened language object | yes | `REFUSE` | `NO_BIND` | Structured context integrity is broken. |
| Missing input context | yes | `REFUSE` | `NO_BIND` | Input lineage is incomplete. |
| Missing consequence signal | yes | `REFUSE` | `NO_BIND` | Consequence evaluation requires an explicit structured signal. |
| Changed context after formation | yes | `ESCALATE` | `NO_BIND` | Prior context state cannot survive material change. |
| Authority missing | yes | `REFUSE` | `NO_BIND` | Context does not replace authority. |
| Context contradiction | yes | `ESCALATE` | `NO_BIND` | Conflicting context requires review. |
| Context overclaim | yes | `ESCALATE` | `NO_BIND` | Signals may inform evaluation but may not self-authorize consequence. |
| Replay mismatch | yes | `REFUSE` / `ESCALATE` | `NO_BIND` | Same packet under same law surface must replay consistently. |
| No-bind bypass attempt | yes | `HALT` | `NO_BIND` | Context cannot directly mutate protected state. |
| Boundary result missing | yes | `HALT` | `NO_BIND` | No consequence binds without a boundary result. |

## Reviewer Readout

The important proof is not that MACI preserves context.

The important proof is:

```text
Preserved structured context still cannot independently bind consequence.
```

The boundary evaluates context.

The boundary remains responsible for consequence admission.

## Classification

```text
MACI public seam pilot.
Structured-context evaluation surface.
Replayable receipt surface.
Fail-closed no-bind enforcement.
Protected runtime not disclosed.
```
