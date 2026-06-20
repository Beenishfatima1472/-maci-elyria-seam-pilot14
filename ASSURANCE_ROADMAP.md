# Assurance Roadmap

## Status

Public-safe assurance roadmap for the MACI / Elyria production-runtime candidate shell.

This roadmap defines the next trust layers without claiming production certification.

## Current Assurance Layer

Implemented and visible:

- public-safe executable review build
- fail-closed no-bind seam behavior
- protected private-kernel adapter boundary
- reviewer-grade production-candidate artifacts
- persistent receipt-store contract
- persistent audit-ledger contract
- production signing adapter contract
- external verifier package
- deployment-readiness checker
- production preflight
- SBOM generator
- signed candidate release provenance

## Next Trust Layer

The next certification/trust layer adds:

1. OpenSSF Scorecard workflow and badge.
2. SLSA provenance workflow for release artifacts.
3. SBOM generation and SBOM inclusion in release bundle.
4. CodeQL workflow and dependency review workflow badges.
5. Signed release artifact verification instructions.
6. This assurance roadmap.

## Assurance Stage 1 — Repository Security Posture

Goal:

- Make repository health visible to outside reviewers.

Controls:

- OpenSSF Scorecard workflow.
- Scorecard badge in README.
- CodeQL analysis workflow.
- Dependency review workflow.
- Dependabot configuration for GitHub Actions and Python dependencies.

## Assurance Stage 2 — Release Artifact Integrity

Goal:

- Make generated artifacts independently checkable.

Controls:

- SHA256 file for release bundle.
- SBOM generated into `dist/sbom.json`.
- SBOM included inside the review bundle.
- Candidate release provenance generated into `dist/release-provenance.json`.
- Release artifact verification instructions.

## Assurance Stage 3 — SLSA Provenance

Goal:

- Generate SLSA/in-toto provenance for release artifacts.

Controls:

- SLSA provenance workflow.
- Artifact digest subject list.
- SLSA provenance generated from GitHub Actions identity.
- Verification path documented in `RELEASE_ARTIFACT_VERIFICATION.md`.

## Assurance Stage 4 — Customer Security Approval

Goal:

- Move from public-safe candidate review to customer-approved production deployment.

Required customer approvals:

- identity provider integration
- tenant provisioning lifecycle
- KMS/HSM or secret manager
- storage backend
- monitoring and alerting
- incident response ownership
- rollback ownership
- policy-pack review
- written commercial scope

## Assurance Stage 5 — External Audit

Goal:

- Independent confirmation of the production deployment boundary.

External audit should review:

- fail-closed no-bind behavior
- tenant isolation
- RBAC enforcement
- receipt persistence
- audit ledger integrity
- signing adapter and key lifecycle
- external verifier independence
- release provenance
- SBOM and dependency posture

## Forbidden Claims

Do not claim:

```text
production certified
regulatory certified
customer security approved
external audit approved
commercial deployment rights without written scope
public exposure of private Elyria/VERITA kernel
```

## Correct Roadmap Claim

```text
The repository has an assurance roadmap for progressing from public-safe candidate review toward customer-security approval or external audit.
```
