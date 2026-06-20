# MACI–Elyria A+ Benchmark Surface

![A+ Benchmark](https://github.com/Kamanaka5502/maci-elyria-seam-pilot/actions/workflows/benchmark.yml/badge.svg)

## Buyer / Reviewer Summary

This repo demonstrates a public-safe seam between a customer-facing MACI context layer and an Elyria/VERITA consequence-boundary resolver.

The purpose is not to show another dashboard, audit trail, or policy wrapper.

The purpose is to show that structured context may inform a boundary decision while remaining incapable of binding consequence by itself.

Core invariant:

```text
MACI informs. Elyria resolves. No consequence binds without the boundary result.
```

Reviewer proof path:

1. Inspect the golden corridor packet.
2. Run the A+ bundle verifier.
3. Review no-bind transcript.
4. Review same-condition replay.
5. Review changed-condition replay.
6. Confirm digest manifest.
7. Confirm no MACI-only bind path exists.

## Quickstart

```bash
python external-verifier/verify_a_plus_bundle.py
pytest
```

Expected:

```text
RESULT: A+ BENCHMARK PASS
```
