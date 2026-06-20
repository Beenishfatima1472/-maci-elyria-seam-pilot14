# MACI–Elyria A+ Benchmark Scorecard

| Category | Required Evidence | Status |
|---|---|---:|
| Claim boundary | `CLAIM_BOUNDARY.md` | PASS |
| Golden corridor | `golden_corridor/` | PASS |
| MACI cannot bind | `proofs/NO_BIND_PROOF_TRANSCRIPT.md` | PASS |
| Elyria boundary required | `external-verifier/verify_a_plus_bundle.py` | PASS |
| Missing authority refusal | `golden_corridor/boundary_result_refuse_missing_authority.json` | PASS |
| Stale evidence refusal | `golden_corridor/boundary_result_refuse_stale_evidence.json` | PASS |
| Changed authority replay | `golden_corridor/boundary_result_refuse_changed_authority.json` | PASS |
| Changed evidence replay | `golden_corridor/boundary_result_refuse_changed_evidence.json` | PASS |
| Changed scope replay | `golden_corridor/boundary_result_escalate_changed_scope.json` | PASS |
| Bypass halt | `proofs/BYPASS_FAILURE_MATRIX.md` | PASS |
| Route closure | `proofs/ROUTE_CLOSURE_PROOF.md` | PASS |
| Receipt integrity | `proofs/RECEIPT_INTEGRITY_PROOF.md` | PASS |
| Public verifier | `external-verifier/verify_a_plus_bundle.py` | PASS |
| CI reproducibility | `.github/workflows/benchmark.yml` | PASS |
| Buyer readout | `review-bundle/BUYER_ONE_PAGE_READOUT.md` | PASS |
| Regulator checklist | `review-bundle/REGULATOR_EVIDENCE_CHECKLIST.md` | PASS |
| Kernel non-disclosure | `proofs/KERNEL_NON_DISCLOSURE_PROOF.md` | PASS |

## Acceptance Statement

```text
A+ benchmark-grade public seam system: PASS
```

This scorecard does not certify production deployment. Production certification remains gated by customer security review or external audit.
