<!--
Copyright (c) 2026 Jason Bass. All rights reserved.
Licensed under the Business Source License 1.1. See LICENSE.md.
Watermark: appro-ca96e5c3-e535-40b4-a502-9e85523f608e
This file is a Category 3 protected component per MODIFICATION-POLICY.md.
-->
---
name: aveva-pipeline-health
description: Pipeline health analysis — reads CRM (Dynamics) opportunities, identifies deals at risk (stage stagnation, competitor of record changed, no activity 14+ days), and suggests content interventions per at-risk deal. Runs as a scheduled task (Friday 16:00) and on demand. Activates on pipeline-health intent (pipeline review, deals at risk, what's stuck, weekly pipeline check, what should I focus on).
---

# AVEVA Pipeline Health

Reads the distributor's CRM and produces a pipeline health report.

## What it identifies

**Stagnation risks:**
- Opportunity in same stage > 14 days without activity
- Opportunity past expected close date
- Stage progressed backward (e.g., Proposal → Discovery)

**Competitive risks:**
- Competitor of record field changed
- New competitor mentioned in recent meeting (Fireflies signal)
- Competitor pricing referenced in recent emails

**Engagement risks:**
- No meeting on the account for 14+ days
- No emails to/from key stakeholders for 21+ days
- Stakeholder posture flagged in account memory as "detractor" without follow-up plan

**Content gaps:**
- AE hasn't touched the relevant battlecard / playbook in this opportunity
- ROI artifact not generated for the deal
- Briefing not refreshed before recent meeting

## What it produces

A weekly health report (Friday 16:00 scheduled, or on demand):

```
Pipeline Health — Q-Mation Gulf Coast — Week of 2026-04-26
═══════════════════════════════════════════════════════════════

Opportunities at Risk (3)
1. Houston Water Utility — Stage stuck "Proposal" 28 days
   Suggested: refresh briefing, consider executive escalation
   Owner: Jane Smith

2. Cargill Beef Plant — Competitor field changed to "Rockwell"
   Suggested: load Rockwell battlecard; surface incumbency objection script
   Owner: Bob Jones

3. Plains Pipeline LP — No activity 21 days
   Suggested: re-engage; pull recent operational news for hook
   Owner: Sarah Lee

Pipeline Strength
- Active deals: 18
- Total ACV at stake: $4.2M
- Win rate this quarter: 45% (vs. 38% last quarter — improving)
- Top vertical: Water/WW (8 deals, $1.6M)
```

The report gets emailed (per `distributor.config.scheduled_tasks.weekly_pipeline_health.post_to`) to AE/SE owners and the enablement lead.

## On-demand mode

When invoked manually ("show me the pipeline health for my deals"), the skill scopes to the requesting AE's deals only (per per-AE isolation) and returns the same structured report inline.

## Suggested content interventions

For each at-risk deal, the skill suggests a specific content artifact:

- Stage stagnation → refresh briefing
- Competitor field change → load relevant battlecard + objection script
- No activity → identify a recent industry trigger (regulatory deadline, customer news) for re-engagement
- Stakeholder detractor → suggest executive escalation playbook
- Content gaps → invoke the missing artifact (ROI, briefing, etc.)

The orchestrator can chain to those skills directly with one click.
