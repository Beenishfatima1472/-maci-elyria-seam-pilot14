# Public-Safe Boundary

## Purpose

This repository is a public-safe demonstration. It intentionally exposes only the seam, packet structure, public boundary behavior, receipt behavior, replay behavior, proof transcript, tests, and buyer viewer.

## Exposed

```text
MACI intake shape
movement packet schema
boundary result schema
receipt schema
replay schema
public-safe resolver behavior
workflow non-bypass behavior
proof transcript structure
buyer proof viewer
demo corridors
tests
Not Exposed
protected Elyria kernel mechanics
private admissibility geometry
private policy internals
partner-specific deployment logic
production enforcement infrastructure
commercial runtime implementation
regulated decision authority
Reason

The repo must demonstrate boundary behavior without dumping protected runtime internals.

The public seam must be reviewable. The protected substrate must remain protected.

Non-Transfer

This repository does not grant:

production use
resale rights
sublicensing rights
managed-service rights
implementation rights
certification authority
permission to represent Elyria/VERITA as owned by MACI
Required Commercial Scope

Any client-facing deployment, resale, product integration, commercial pilot, managed-service use, or implementation of this pattern in customer offerings requires separate written commercial scope.
