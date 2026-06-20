# Claims Boundary

## Admissible Public Claim

This repository demonstrates a public-safe MACI-on-Elyria consequence runtime where MACI operates as the customer-facing domain/context layer and Elyria/VERITA operates as the protected consequence-boundary runtime.

## Non-Negotiable Rule

```text
MACI may structure and submit domain/context signals.
MACI may not independently bind consequence.
Workflow may not bypass the boundary.
Nothing becomes protected consequence until the Elyria/VERITA boundary runtime admits formation.
```

## Current Allowed Lane

```text
A+ audit-ready production-runtime candidate shell with decomposed reviewer-grade artifacts, fail-closed runtime gate, protected Elyria/VERITA private-kernel adapter, auth/RBAC candidate controls, tenant-isolation candidate controls, persistent receipt/audit contracts, production signing adapter, independent verifier, deployment readiness package, and certification gated by customer security approval or external audit.
```

## Allowed Public Claims

The repo may claim:

- MACI can structure proposed movement into a movement packet.
- MACI preserves language, input, context, risk, and consequence signals.
- Elyria/VERITA resolves boundary status before protected consequence forms.
- Workflow cannot bypass the boundary gate.
- Refused movement produces no-bind/non-formation proof.
- Receipts bind packet, result, policy version, and replay token.
- Replay can confirm same-condition, changed-condition, and tampered states.
- Auth/RBAC candidate controls are visible for reviewer evaluation.
- Tenant-isolation candidate controls are visible for reviewer evaluation.
- Persistent receipt/audit contracts are visible for reviewer evaluation.
- Production signing adapter contract is visible for reviewer evaluation.
- Independent verifier package can verify proof evidence outside live app memory.

## Customer/Audit-Gated Claims

These may be described only as gated:

- customer production approval
- customer IAM integration
- customer tenant architecture approval
- customer KMS/HSM or secret-manager approval
- customer operations approval
- external audit approval
- commercial deployment rights

## Forbidden Claims

Do not claim:

```text
production certified
regulatory certified
customer security approved
external audit approved
customer-managed production runtime without approval
commercial deployment rights without written scope
public exposure of private Elyria/VERITA kernel
legal authority
medical authority
financial authority
```

## Commercial Boundary

Any client-facing deployment, resale, product integration, commercial pilot, managed-service use, or implementation of this pattern in customer offerings requires separate written scope.

## Certification Boundary

The repository cannot self-certify.

Production certification remains gated by customer security approval or external audit.
