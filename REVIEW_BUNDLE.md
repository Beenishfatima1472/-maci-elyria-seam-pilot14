# Review Bundle

## Purpose

The review bundle creates one portable evidence packet for buyer, reviewer, or technical evaluation.

It collects:

```text
documents
source files
schemas
corridor packets
proof transcripts
screenshots
tests
manifest
SHA256 hashes
zip archive
```

## Build Command

```bash
python3 scripts/build_review_bundle.py
```

Output:

```text
dist/review-bundle/
dist/maci-elyria-review-bundle.zip
dist/maci-elyria-review-bundle.zip.sha256
```

## Bundle Claim

The bundle is intended to help a reviewer verify:

```text
MACI cannot bind consequence.
Workflow cannot bypass boundary.
Refusal produces no-bind.
Hold blocks protected effect.
Escalation blocks protected effect.
Narrow blocks original-scope protected effect.
Admission is the only automatic protected-effect path.
Receipts preserve proof.
Replay verifies same, changed, and tampered conditions.
```

## Integrity Files

```text
MANIFEST.json
SHA256SUMS.txt
maci-elyria-review-bundle.zip.sha256
```

## Correct Use

This bundle is for review and evaluation.

It does not grant commercial deployment rights, resale rights, sublicensing rights, certification authority, legal authority, medical authority, or financial authority.
