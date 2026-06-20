# Threat Model

## System Boundary

The public repository demonstrates a seam:

```text
MACI context input
→ movement packet
→ assumption precheck
→ boundary resolver
→ workflow gate
→ receipt
→ replay
→ proof transcript
Assets
movement packet integrity
boundary result integrity
receipt integrity
replay integrity
proof transcript integrity
public/private runtime separation
ownership and commercial boundary
Threats
Threat	Risk	Control
MACI attempts to bind consequence	Premature effect formation	seam guard + HALT / NO_BIND
Workflow bypasses boundary	Unauthorized protected effect	workflow gate
Missing authority	Invalid consequence formation	REFUSE / NO_BIND
Insufficient evidence	Unsupported movement	HOLD / NO_BIND
Uncertain language	Ambiguous operation	ESCALATE / NO_BIND
Overbroad scope	Excessive action	NARROW / NARROWED
Invalid custody	Bad provenance	REFUSE / NO_BIND
Packet tampering	Proof mismatch	replay verifier
Receipt tampering	Invalid proof	deterministic receipt hash
Private runtime leakage	IP exposure	public-safe boundary docs
Residual Risk

This is a public-safe review build. Production use requires:

authentication
authorization
persistent audit storage
secrets management
rate limiting
deployment monitoring
formal security review

