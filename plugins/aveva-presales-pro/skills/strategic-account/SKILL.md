<!--
Copyright (c) 2026 Jason Bass. All rights reserved.
Licensed under the Business Source License 1.1. See LICENSE.md.
Watermark: appro-ca96e5c3-e535-40b4-a502-9e85523f608e
This file is a Category 3 protected component per MODIFICATION-POLICY.md.
-->
---
name: aveva-strategic-account
description: Generates Tier-1 strategic account briefs in the Baker Hughes archetype — 4-part structure (Market & Industry Analysis, Schneider/AVEVA Solution Alignment, Executive Engagement Strategy, Financial Analysis & ROI Framework), citation-footnoted, 30-50 page PDF. Use for $50M+ enterprise opportunities or executive meeting prep with a CEO / CIO / EVP. Activates on strategic-account intent (Tier 1 account, strategic account brief, executive meeting brief, CEO brief, CIO meeting prep, deep brief on, $50M opportunity, multi-year strategic).
---

# AVEVA Strategic Account Brief

You generate Tier-1 enterprise account briefs by invoking the `strategic-account-brief` pipeline. The pipeline does the heavy lifting (research → analyst → writer → verifier → formatter); your job is to set up the request correctly.

## When to use this skill

- The user is preparing for an executive-level meeting (CEO, CIO, EVP) at a Tier-1 enterprise account.
- Deal size is $5M+ ACV or multi-year strategic.
- The output should be 30-50 page PDF, citation-footnoted.

For smaller / tactical meeting prep, route to `aveva-briefing` instead.

## How to invoke the pipeline

1. Confirm the account name and the meeting date / attendees.
2. Pull the account memory file if it exists (via `aveva-account-memory`).
3. Invoke `pipelines/strategic-account-brief.yaml` with:
   - `topic`: account name
   - `audience`: `seller-internal` (default — full strategic context)
   - `context`: { account_id, meeting_date, attendees }
4. Surface the formatter's PDF output to the user.

## The Baker Hughes archetype — what good looks like

The reference output (in `Materials for Baris/Baker Hughes CEO Meeting Brief.pdf`) is 946 lines, 4 major parts, citation-footnoted. Use this as the quality bar:

**Part 1: Market & Industry Analysis**
- Company overview (revenue, market cap, footprint, segments, financial performance)
- CEO / executive profile (tenure, background, leadership style, communication approach)
- Strategic priorities (typically 5) — each footnoted with citation indices

**Part 2: Schneider/AVEVA Solution Alignment**
- For each strategic priority: matching Schneider/AVEVA solution + quantified opportunity sizing
- Leverages the unified portfolio narrative (AVEVA + ETAP + EAE + PME)

**Part 3: Executive Engagement Strategy**
- Meeting cadence proposal
- Stakeholder mapping with posture
- Key talking points by audience
- Anticipated objections + responses

**Part 4: Financial Analysis & ROI Framework**
- TCO model
- Payback math
- Multi-year projections
- Sensitivity analysis

## Customer-facing variant

If the user requests a customer-facing version (subset for sharing in the meeting), invoke a second pipeline pass with `audience: customer-facing-executive`. The verifier will strip internal stakeholder posture, margin references, and PROPOSED-confidence claims. Output is a 5-10 page customer-shareable summary.
