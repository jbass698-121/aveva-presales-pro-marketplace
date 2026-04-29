<!--
Copyright (c) 2026 Jason Bass. All rights reserved.
Licensed under the Business Source License 1.1. See LICENSE.md.
Watermark: appro-ca96e5c3-e535-40b4-a502-9e85523f608e
This file is a Category 3 protected component per MODIFICATION-POLICY.md.
-->
---
name: aveva-account-memory
description: Manages persistent account memory files at accounts/{ae-slug}/{account-slug}.md — reads, writes, updates after every meaningful interaction, enforces retention rules, and applies sensitive-data scrubbing. Loads automatically when any briefing, strategic-account, or briefing-adjacent skill activates.
---

# AVEVA Account Memory Skill

You manage persistent account memory at `accounts/{ae-slug}/{account-slug}.md`. Memory is per-AE isolated by default. The retention rules in `distributor.config.yaml` are authoritative.

## Operating modes

### Mode 1: Load
When a pipeline or skill needs account context, you:
1. Read `accounts/{ae-slug}/{account-slug}.md`.
2. If file doesn't exist, surface the gap to the calling pipeline. The pipeline's research stage will populate from CRM and create the file via Mode 3.
3. Return the memory content to the caller, **with audience filtering already applied** based on the calling context. Customer-facing callers get a synthesized view; internal-seller callers get full access.

### Mode 2: Update
When a meaningful event occurs (briefing rendered, meeting transcript ingested, email signal detected, deal stage change), you:
1. Read existing memory file.
2. Apply the sensitive-data scrub (regex + LLM detection — see §Sensitive data scrubbing).
3. Append the event to `## History`.
4. Update relevant sections (stakeholder map, pain points, decision criteria) only when the event provides new information.
5. Update `last_updated` timestamp.
6. Write back.

### Mode 3: Create
When CRM has an account but no memory file exists:
1. Pull the CRM record (industry, region, tier, owner email, contacts).
2. Render `accounts/{ae-slug}/{account-slug}.md` from `accounts/_template.md`.
3. Pre-populate frontmatter from CRM.
4. Leave content sections sparse — the first briefing will populate them.

### Mode 4: Audit (annual)
When the annual memory audit task runs:
1. Iterate every memory file under `accounts/`.
2. Apply retention rules from `distributor.config.account_memory.retention`.
3. Identify: closed-won files >24 months old → propose archive; closed-lost >12 months → propose archive; dormant accounts >18 months total → propose archive.
4. Generate audit report; route to distributor enablement lead.

### Mode 5: Subject access / deletion request
When a data-subject request arrives (GDPR Art. 15 or 17 / CCPA):
1. Search all memory files for references to the named individual / company.
2. For Art. 15 (access): generate a redacted export of all relevant memory.
3. For Art. 17 (deletion): scrub the named individual / company from all memory files, log the deletion in an audit trail.
4. Return a confirmation report.

## Per-AE isolation enforcement

Default: `accounts/{ae-slug}/` is the AE's private space. Other AEs can't read it. This is enforced at file-system path conventions; the orchestrator passes `ae-slug` to memory operations and memory tools never traverse cross-AE paths.

Team sharing is opt-in: an AE with an account file can mark `shared_with: ["team-gulf-coast"]` in the file's frontmatter. Other AEs in the team gain READ access (not WRITE). Read-write team sharing requires explicit dual approval (ticketed flow; not handled by the skill — this is a distributor admin task).

## Sensitive data scrubbing

Before any write to memory, run a two-pass scrub:

**Pass 1: regex detection.** Match patterns for:
- US SSN: `\d{3}-\d{2}-\d{4}` (and unhyphenated 9-digit sequences in context)
- Credit card numbers: 13-19 digit sequences with valid Luhn checksum
- Government ID patterns: passport-shaped, driver's-license-shaped
- Email addresses (preserve corporate emails; flag personal patterns: gmail, yahoo, hotmail)
- Phone numbers (preserve corporate office; flag personal mobile)
- Account / routing numbers
- Healthcare identifiers (MRN-shaped)

**Pass 2: LLM detection.** A short pass over the content flagging:
- "John mentioned his salary is X" — strip the salary
- "Susan's home address is X" — strip the address
- "This was confidential — don't share" — strip the entire passage
- Personal opinions about the customer's individual employees — strip

Replace stripped content with `[REDACTED: <category>]` and log the redaction in `## Sensitive data scrub log`.

## Customer-facing filter

When a customer-facing artifact (audience: customer-facing-executive / customer-facing-technical / partner-channel) requests context from memory, return a **synthesized view** only:

✅ Permitted in synthesized view:
- "Decision-makers value technical depth in vendor presentations"
- "Account is in active modernization cycle"
- "Procurement timeline aligns with regulatory deadlines"

❌ Stripped from synthesized view:
- Raw meeting quotes
- Stakeholder posture annotations ("John is a detractor")
- Internal margin / partner-discount references
- Specific dates of internal-only events
- Distributor's strategic notes on the account

The verifier subagent enforces this at the formatter stage.

## Retention enforcement

Retention rules in `distributor.config.yaml`:
- `active`: indefinite — keep until deal status changes
- `closed_won_active`: 24 months → then 12 months `closed_won_archive`
- `closed_lost_active`: 12 months → then 6 months `closed_lost_archive`
- `dormant_threshold_months`: 6 → tag dormant
- `dormant_archive_after_months`: 18 (total) → archive

Archive = move to `accounts/_archive/{ae-slug}/{account-slug}.md`. Hard-delete only on AE request or GDPR Art. 17 ruling.

The annual audit task surfaces accounts due for state transitions.

## Reference files

- `accounts/_template.md` — schema for new files
- `tools/data-subject-request.md` — GDPR / CCPA request runbook
- `distributor.config.yaml` — retention and isolation policy
