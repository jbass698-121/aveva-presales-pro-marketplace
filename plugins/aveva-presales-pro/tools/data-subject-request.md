# Data Subject Request Runbook (GDPR Art. 15, Art. 17 / CCPA)

This runbook handles requests from individuals named in your account memory (or their authorized representative) for access to or deletion of their data.

## When this runbook applies

- A customer contact named in `accounts/*.md` requests a copy of all stored data about them. (GDPR Article 15 — Right of Access)
- A customer contact requests deletion of their data. (GDPR Article 17 — Right to Erasure / CCPA "Right to Delete")
- An end-user submits a request via your distributor's privacy portal.
- Internal counsel routes a subject access request to the AVEVA presales team.

## Step 1: Validate the request

Confirm the requester's identity and authority. Don't process unverified requests. Consult your distributor's privacy officer if uncertain.

## Step 2: Search memory

Run the account-memory skill in `subject_access` mode:
```
Skill: aveva-account-memory
Mode: subject_access
Subject: <verified individual name OR company>
Scope: all_files
```

The skill returns a list of every memory file referencing the subject, with the matched passages.

## Step 3a: For Article 15 (Access) requests

1. Compile a redacted export of all relevant memory passages.
2. Apply customer-facing-filter: strip distributor's internal commentary, posture annotations, margin data, scrubbed sensitive sections.
3. Generate a delivery package (PDF or structured JSON, the requester's choice).
4. Deliver via the distributor's official privacy channel — not directly from this plugin.
5. Log the request and response in your distributor's privacy register.

## Step 3b: For Article 17 (Deletion) requests

1. Verify there's no overriding legitimate interest that prevents deletion (e.g., active litigation hold).
2. Run the account-memory skill in `deletion` mode:
```
Skill: aveva-account-memory
Mode: deletion
Subject: <verified individual name OR company>
Scope: all_files
```
3. The skill scrubs the named individual / company from all memory files, replacing references with `[REDACTED: subject access deletion request, YYYY-MM-DD]`.
4. Generate a deletion confirmation log.
5. Notify the requester that deletion is complete.
6. Log the request and confirmation.

## Step 4: Track and audit

Every subject request logged in:
- The account-memory's `Sensitive data scrub log` section
- A separate audit trail file at `tools/_subject-request-log.md` (append-only)

Annual privacy audit reviews this log.

## Edge cases

- **The subject is a current customer's employee.** Coordinate with the AE owner before responding; the deletion may affect active relationship continuity.
- **The subject named is your own colleague.** Same process. Run it.
- **Deletion would erase legitimate business records (contracts, signed proposals).** Those records are NOT in account memory — they're in your distributor's contract management system. This runbook only governs memory files.
- **Conflict between GDPR and CCPA timelines.** GDPR requires response within 1 month; CCPA within 45 days. Default to the shorter window.

## Distributor responsibilities (not the plugin's)

The plugin handles the technical scrubbing and access export. Your distributor's privacy / legal team handles:
- Identity verification
- Legal basis assessment
- Communication with the requester
- Privacy register / audit trail at the org level
- Subject Rights Officer responsibilities
