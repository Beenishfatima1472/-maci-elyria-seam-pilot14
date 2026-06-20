
Formal Proof Roadmap
Current Proof Type

This repository provides executable/demonstrative proof:

deterministic tests
boundary decision cases
workflow non-bypass checks
receipt preservation
replay verification
tamper detection
proof transcripts
Formal Proof Gap

This repository does not yet provide:

Coq proof
TLA+ model
SMT-checked invariant set
machine-checked proof kernel
complete private Elyria formalization
Candidate Formal Invariants
MACI cannot bind consequence.
Workflow cannot bypass boundary result.
No protected effect forms on REFUSE / HOLD / ESCALATE / HALT.
ADMIT / ADMITTED is the only automatic protected-effect path.
Receipt hash changes when packet or result changes.
Replay detects changed authority, changed evidence, changed scope, changed custody, and tampering.
Private engine must return public BoundaryResult contract.
Next Formalization Path
TLA+ state machine for movement formation
SMT checks for admissible transition invariants
Coq/Lean encoding for no-bind preservation
CI model-check job for public-safe state machine

