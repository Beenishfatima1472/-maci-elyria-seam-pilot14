# A+ Acceptance Criteria

Reviewer command:

```bash
python external-verifier/verify_a_plus_bundle.py
pytest
```

Expected output:

```text
RESULT: A+ BENCHMARK PASS
```

Required surface:

- claim boundary
- golden corridor
- no-bind transcript
- changed-condition replay
- route-closure proof
- receipt-authenticity proof
- buyer readout
- regulator checklist
- external verifier

Core invariant: MACI informs. Elyria resolves. No consequence binds without the boundary result.
