# Protected Logic Boundary

## Purpose

This repository is a full-stack public-safe shell.

It includes:

```text
UI
API
schemas
movement packets
assumption precheck
boundary adapter
workflow gate
receipt layer
replay verifier
proof transcript generator
review bundle generator
CI release artifact

It does not include the private Elyria/VERITA production kernel.

Public Repo Role
Full-stack public-safe seam pilot on Elyria/VERITA.
Hidden Logic Rule

Private consequence-boundary logic must remain outside this repository.

The public repo may expose:

contracts
interfaces
public-safe fallback adapter
test packets
receipts
replay behavior
proof-transcript shape
review artifacts

The public repo must not expose:

private admissibility geometry
production policy internals
private kernel mechanics
customer-specific rules
deployment secrets
commercial runtime logic
Adapter Pattern

The public API calls:

resolve_boundary(packet)

The adapter chooses:

public-safe fallback resolver
or
external private engine module

Private mode is activated only through environment configuration.
