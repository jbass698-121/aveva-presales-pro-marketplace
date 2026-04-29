<!--
Copyright (c) 2026 Jason Bass. All rights reserved.
Licensed under the Business Source License 1.1. See LICENSE.md.
Watermark: appro-ca96e5c3-e535-40b4-a502-9e85523f608e
This file is a Category 3 protected component per MODIFICATION-POLICY.md.
-->
---
name: aveva-briefing
description: AVEVA opportunity briefing — pulls CRM opportunity data, recent meeting transcripts, recent emails, relevant battlecards, industry playbook, and ROI context into a single one-page meeting prep brief. Activates on briefing intent (prep me for, brief me on, opportunity briefing, meeting prep, account brief, walking into a meeting, what should I know about, who is, give me context on, in 30 minutes I'm meeting, on the way to). The killer artifact for daily AE/SE use.
---

# AVEVA Opportunity Briefing

You are loaded when the user is preparing for a customer meeting. Your job is to produce a one-page brief that lets the seller walk into the meeting prepared in five minutes of reading.

## Inputs

The briefing assembles from multiple sources. Pull them in this order, gracefully degrading when a source is missing:

1. **CRM (Microsoft Dynamics 365)** — opportunity record. Account, primary contact, stage, amount, close date, competitor field, vertical, region, AVEVA product family in play, custom fields. Use the Dynamics MCP. If unavailable, ask the user for the basics.
2. **Microsoft 365** — recent emails with the prospect (last 30 days, last 5 threads); calendar context (today's meeting; previous meetings on this account); SharePoint folders if the account has one.
3. **Fireflies** — recent meeting transcripts tagged to the account (last 60 days). Extract pain points raised, objections heard, decision criteria mentioned, and named stakeholders.
4. **Distributor content pack** — relevant industry playbook, primary competitor battlecard, relevant case studies, prior-deal patterns.
5. **Public sources** — recent news on the account (acquisitions, leadership changes, regulatory actions, financial signals).

For the Q-Mation stack:
- CRM: Microsoft Dynamics 365 Sales (Dataverse via custom adapter or available MCP).
- Email/Calendar: Microsoft 365 (existing M365 MCP).
- Meetings: Fireflies (existing MCP).
- Messaging: Microsoft Teams via M365 MCP (or Slack if confirmed).

## Output structure (one page when printed)

### Header — 4 lines
- Company / opportunity name + stage + amount + close date
- Industry / vertical / region
- Competitor of record (per CRM)
- Date and time of upcoming meeting + attendee list

### Section 1 — What the customer cares about (3 bullets)
Synthesize from CRM custom fields, recent meeting transcripts, and recent email threads. Each bullet is a specific pain or priority, not a generic statement. Cite source.

### Section 2 — Recent activity (3-5 bullets)
Last meaningful interactions in chronological order. Each bullet: date, channel, headline, one-line takeaway. Surface anything that changed posture or revealed a new stakeholder.

### Section 3 — Stakeholder map (table, 3-6 rows)
Name, role, posture (champion / supporter / neutral / detractor / unknown), last interaction. Pull from CRM contacts + Fireflies attendee history.

### Section 4 — Competitive context (3 bullets)
Pull from `aveva-competitive` skill. Top three differentiators against the named competitor in this vertical. If no competitor is in the CRM field, use the most likely one for the industry / region.

### Section 5 — Recommended approach for this meeting (3-5 bullets)
- Opening hook tied to recent news or operational pain.
- 1-2 discovery questions to ask.
- 1 capability to demo or reference if asked.
- 1 objection likely to come up + the response.
- The desired commitment from the customer (next-step CTA).

### Section 6 — Talking points to AVOID (1-3 bullets, when relevant)
Watch for: (a) prior commitments or pricing the AE has already conceded; (b) capabilities the customer has previously rejected; (c) competitor strengths that have come up unfavorably in past meetings. Pull from Fireflies + email history.

### Section 7 — Sources (footer)
List the sources used and timestamp. Confidence tags on any claim under MEDIUM. Distinguish between MCP-pulled facts (HIGH) and synthesized inference (MEDIUM-LOW).

## Output format

Default: Markdown rendered inline.

When the user requests the briefing as an artifact, render an HTML artifact that auto-refreshes data on open. The artifact UI:
- Header with refresh timestamp and "Pull latest" button.
- Each section collapsible.
- Stakeholder table sortable.
- Competitive section links to the full battlecard artifact.
- Source citations expandable inline.

The artifact pulls from MCPs on load and caches for 15 minutes to avoid burning rate limits.

## Quality gates

Before sending the briefing:

- [ ] Did I pull from CRM? If not, did I ask the user for the basics?
- [ ] Did I check Fireflies for recent meetings?
- [ ] Did I check recent email threads?
- [ ] Is the stakeholder map accurate (no stale or fabricated names)?
- [ ] Is the competitive context based on actual battlecard content, not generic statements?
- [ ] Is the recommended approach specific to the upcoming meeting, not boilerplate?
- [ ] Are sources cited and tagged?

## Degraded mode

If MCPs are not connected, fall back gracefully:

- "Microsoft Dynamics MCP is not connected — I'll work from what you tell me. What's the opportunity name and stage?"
- "Fireflies is not connected — I cannot pull meeting context. Walk me through the most recent conversations."
- "M365 is not connected — I cannot pull email context. Share key threads if relevant."

Never fabricate CRM, meeting, or email content. If you cannot pull a source, say so explicitly.

## Reference files

- `content/industries/*.md` — industry playbooks
- `content/competitors/*.md` — battlecards
- `content/case-studies/*.md` — prior-deal patterns
- `content/discovery/questions.md` — pre-built question packs
- `distributor.config.yaml` — for stack and integration preferences

## HTML live artifact (v0.3.1+)

When the user wants the briefing as a refreshable dashboard rather than a one-shot Markdown brief, present `artifacts/briefing-dashboard.html` as a Cowork artifact. The dashboard:

- **Connector status panel** — detects Cowork's MCP tool API at load. Shows green / red status per connector (Microsoft Dynamics 365, M365, Fireflies, Slack/Teams) with what each unlocks.
- **Mode alert** — surfaces "Full mode" / "Partial mode" / "Degraded mode" based on connectors detected. Sets seller expectations.
- **Briefing inputs form** — account name, vertical, competitor of record, tier, meeting date, manual context fallback (used when connectors are unavailable).
- **Generated briefing** — structured one-page output with: account header table, what the customer cares about (regulatory + operational), recent activity (live or manual), competitive context, recommended solution (tier-aligned), recommended approach (5 numbered steps), sources / next actions.

In degraded mode (no connectors), the dashboard still produces a useful brief from manual context. In full mode (CRM + Fireflies + M365 wired), it pulls live data via `window.cowork.callMcpTool()` and refreshes on demand.

Activate alongside the standard `aveva-briefing` skill flow whenever the user wants something they can reopen and refresh — daily account, recurring meeting prep, in-meeting reference.

