# Security Policy

## Public-Safe Repository

This repository is intentionally public-safe. It does not expose private Elyria kernel mechanics, private admissibility geometry, production enforcement internals, secrets, credentials, or customer data.

## Supported Security Review

Security review should focus on:

```text
boundary bypass prevention
receipt determinism
replay integrity
tamper detection
assumption discovery
public/private boundary separation
commercial boundary clarity
Secrets

Do not commit:

API keys
tokens
private keys
customer records
production policy packs
deployment credentials
private runtime material
Reporting

Report security concerns privately to the repository authors:

Samantha Revita
Terry Snyder

Do not disclose vulnerabilities publicly until the authors have reviewed them.

Production Security Requirements

Any production deployment requires separate written commercial scope and a deployment-specific security review.
