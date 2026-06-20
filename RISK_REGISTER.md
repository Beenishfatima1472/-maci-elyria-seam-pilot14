# Risk Register

| ID | Risk | Severity | Mitigation |
|---|---|---|---|
| R-001 | Reviewer misreads repo as production-certified | High | README, release notes, production-candidate readiness doc clarify limits |
| R-002 | MACI interpreted as binding authority | High | seam guard, docs, tests, no-bind behavior |
| R-003 | Workflow bypass claim not verified | High | workflow non-bypass tests |
| R-004 | Proof transcript changes across builds | Medium | deterministic proof IDs and workflow IDs |
| R-005 | Receipt tampering not detected | High | replay tamper checks |
| R-006 | Private kernel exposure | High | public-safe boundary |
| R-007 | Commercial misuse | High | license, ownership notice, commercial boundary |
| R-008 | Screenshot treated as proof alone | Medium | README clarifies runtime proof path |
| R-009 | Deployment without security controls | High | production gate requires separate review |
