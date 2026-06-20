# Customer Acceptance Tests

## Gate

Production-candidate deployment may not be accepted unless all required checks pass.

## Required Tests

```text
[ ] /live returns alive
[ ] /ready returns ready only when production gates pass
[ ] missing API key is rejected
[ ] missing tenant ID is rejected
[ ] wrong tenant is rejected
[ ] valid API key + tenant is accepted
[ ] signed receipt is issued
[ ] receipt verification passes
[ ] tampered receipt verification fails
[ ] audit chain verification passes
[ ] replay detects same condition
[ ] replay detects changed authority
[ ] replay detects changed evidence
[ ] replay detects changed scope
[ ] replay detects changed custody
[ ] replay detects tampered packet
[ ] replay detects tampered receipt
[ ] private kernel remains outside public repo
[ ] rollback runbook tested
[ ] incident response runbook reviewed
Acceptance Statement

This deployment is production-candidate only until written customer security approval, external audit, or formal certification is complete.
