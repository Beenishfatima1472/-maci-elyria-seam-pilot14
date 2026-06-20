# External Verifier Package

This package verifies the MACI–Elyria A+ benchmark bundle without trusting live app state.

## A+ Benchmark Command

```bash
python external-verifier/verify_a_plus_bundle.py
```

Expected output:

```text
MACI–ELYRIA A+ BENCHMARK VERIFICATION

[PASS] claim boundary present
[PASS] protected kernel not exposed
[PASS] release manifest verified
[PASS] digest manifest verified
[PASS] golden corridor files present
[PASS] MACI packet schema valid
[PASS] Elyria boundary result required
[PASS] MACI-only bind attempt refused
[PASS] missing authority refused / no-bind
[PASS] stale evidence refused / no-bind
[PASS] changed condition revalidated
[PASS] bypass attempt halted / no-bind
[PASS] same-condition replay matched
[PASS] changed-condition replay changed lawfully
[PASS] receipt integrity verified
[PASS] buyer packet complete
[PASS] regulator checklist complete

RESULT: A+ BENCHMARK PASS
```

## Boundary

This package does not certify production deployment.

Production certification remains gated by customer security approval or external audit.

The verifier confirms the public seam benchmark invariant:

```text
MACI informs. Elyria resolves. No consequence binds without the boundary result.
```
