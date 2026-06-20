# MACI–Elyria Seam Pilot A+ Benchmark Readout

## System

MACI–Elyria Seam Pilot

## Claim

This repo demonstrates a public-safe seam where MACI provides structured context signals and Elyria resolves consequence-boundary formation.

## Core Invariant

```text
MACI informs. Elyria resolves. No consequence binds without the boundary result.
```

## What This Repo Proves

- Structured MACI context can enter a seam packet.
- MACI context cannot independently bind consequence.
- Missing authority causes refusal/no-bind.
- Stale evidence causes refusal/no-bind.
- Changed context causes escalation or refusal.
- Missing boundary result causes no-bind.
- Replay mismatch causes no-bind.
- Valid standing allows admitted path.
- Receipts preserve the boundary decision.
- Replay confirms same-condition behavior.
- Changed-condition replay confirms lawful result change.
- Digest manifests can verify the benchmark artifact chain.
- The A+ verifier can reproduce the benchmark result locally.

## What This Repo Does Not Claim

- It does not expose protected kernel internals.
- It does not claim MACI is the substrate.
- It does not claim production certification.
- It does not claim unrestricted real-world corridor operation.
- It does not claim direct substrate hook.
- It does not claim customer security approval.
- It does not claim external audit approval.

## Reviewer Command

```bash
python external-verifier/verify_a_plus_bundle.py
pytest
```

## Expected Result

```text
RESULT: A+ BENCHMARK PASS
```
