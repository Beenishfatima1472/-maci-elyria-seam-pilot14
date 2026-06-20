
Incident Response Runbook
Severity Classes
Severity	Trigger
SEV-1	unauthorized protected consequence path
SEV-2	receipt signature mismatch
SEV-2	audit-chain break
SEV-3	failed replay verification
SEV-3	tenant mismatch
SEV-4	documentation or configuration issue
Response Steps
Freeze affected tenant.
Preserve audit chain.
Export receipts.
Verify signed receipts.
Verify audit chain.
Rotate affected keys.
Replay affected packets.
Produce incident report.
Require re-authorization before restart.
Non-Negotiable Rule

No protected effect may continue if boundary, receipt, replay, tenant, or audit integrity is uncertain.
