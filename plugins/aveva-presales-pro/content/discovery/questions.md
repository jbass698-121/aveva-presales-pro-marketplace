---
title: "Distributor Discovery Question Bank"
last_updated: "<<YYYY-MM-DD>>"
---

# Discovery Question Bank — distributor BYOC

> **How to use.** This is the master question bank the `aveva-discovery` skill draws from. Add questions that have actually worked for the distributor's team. Tag each question by industry, deal stage, and audience. The skill will pick the right ones based on opportunity context.

## Question schema

Each question entry uses this structure:

```yaml
- id: "qual-vertical-stage-NN"
  text: "<<the verbatim question>>"
  industry: ["<<>>"]                 # all | oil-gas-upstream | oil-gas-midstream | cpg | water-wastewater
  deal_stage: ["<<>>"]               # prospecting | discovery | technical-fit | proposal | closing
  audience: ["<<>>"]                 # operations | engineering | IT | finance | executive
  intent: "<<>>"                     # what insight does this surface
  follow_ups: ["<<>>"]               # adjacent questions to chain
  source: "<<>>"                     # where this question came from
```

## Starter questions (replace with the distributor's own)

```yaml
questions:

  - id: "qual-all-prospecting-01"
    text: "What's your current SCADA platform, and where does it slow you down?"
    industry: ["all"]
    deal_stage: ["prospecting", "discovery"]
    audience: ["operations", "engineering"]
    intent: "Surfaces incumbent vendor + active operational pain in one question"
    follow_ups: ["When did you last upgrade or replace it?", "What would 'faster' look like?"]
    source: "framework default"

  - id: "qual-all-discovery-01"
    text: "How is your team measured — uptime, throughput, OEE, compliance, or cost?"
    industry: ["all"]
    deal_stage: ["discovery"]
    audience: ["operations", "executive"]
    intent: "Reveals which value driver to lead the conversation with"
    follow_ups: ["Which metric is the board watching most closely?"]
    source: "framework default"

  - id: "qual-water-discovery-01"
    text: "Where are you on LCRI's (formerly LCRR) 10-year service-line replacement timeline, and what's your service-line communication strategy?"
    industry: ["water-wastewater"]
    deal_stage: ["discovery"]
    audience: ["operations", "IT"]
    intent: "LCRI (Lead and Copper Rule Improvements, finalized Oct 2024) is the dominant regulatory pressure for water utilities; compliance date Nov 1, 2027; 10-year mandatory replacement"
    follow_ups: ["What's your baseline service-line inventory state — every line identified including ownership unknowns?", "Are you on track to publish your replacement plan online by November 2027?"]
    source: "framework default; verified against EPA LCRI final rule 2024-10-08"

  - id: "qual-cpg-discovery-01"
    text: "Are you running your FSMA 204 program on the original 2026 timeline or under the extension to July 2028? What's your current state on Critical Tracking Event (CTE) capture for foods on the FTL?"
    industry: ["cpg"]
    deal_stage: ["discovery"]
    audience: ["operations", "executive"]
    intent: "FSMA 204 compliance was extended to 2028-07-20 by Congressional directive; surface whether customer is using extension or staying on original program. Both branches have AVEVA opportunities."
    follow_ups: ["How long does an audit prep currently take?", "Are your batch records electronic / Part 11 ready, or paper-based?", "Which Food Traceability List categories apply to your operation?"]
    source: "framework default; verified against FDA FSMA 204 page + extension proposal Aug 2025"

  - id: "qual-og-discovery-01"
    text: "How many unplanned downtime hours per month do you average on artificial lift across the field?"
    industry: ["oil-gas-upstream"]
    deal_stage: ["discovery"]
    audience: ["operations"]
    intent: "Surfaces the deferred-production cost that drives PI System ROI"
    follow_ups: ["What's your average response time when a well goes down?"]
    source: "framework default"

  - id: "qual-og-midstream-discovery-01"
    text: "How does your team handle PHMSA Gas Mega Rule Part 2 integrity management reporting (effective May 2023) — is it manual, semi-automated, or integrated with SCADA?"
    industry: ["oil-gas-midstream"]
    deal_stage: ["discovery"]
    audience: ["operations", "compliance"]
    intent: "PHMSA Gas Mega Rule RIN2 (May 2023) and RIN3 (May 2023, gathering lines) drive midstream SCADA-modernization conversations. Liquid pipelines: 49 CFR 195 IMP."
    follow_ups: ["What does an integrity audit prep cycle look like for your team?", "How are you tracking methane emissions for OOOOb reporting? First annual report due no earlier than November 2026."]
    source: "framework default; verified against PHMSA + EPA NSPS final rules"

  - id: "qual-all-discovery-comp-01"
    text: "Have you evaluated [primary competitor for vertical], and what did you take away?"
    industry: ["all"]
    deal_stage: ["discovery"]
    audience: ["operations", "executive"]
    intent: "Surfaces decision criteria and competitive landscape simultaneously"
    follow_ups: ["What did they do well? Where did they fall short?"]
    source: "framework default"

  - id: "qual-all-process-01"
    text: "Walk me through how a decision like this gets made at your organization — who's involved, what gates does it pass through, what's the timeline?"
    industry: ["all"]
    deal_stage: ["discovery", "technical-fit"]
    audience: ["executive"]
    intent: "MEDDPICC Decision Process + Paper Process in one question"
    follow_ups: ["Has anyone in the buying group been burned by a prior platform investment?"]
    source: "framework default"

  - id: "qual-all-economic-01"
    text: "Who would write the check for this — and have they been part of these conversations yet?"
    industry: ["all"]
    deal_stage: ["technical-fit", "proposal"]
    audience: ["champion"]
    intent: "MEDDPICC Economic Buyer access check"
    follow_ups: ["What would they need to see to feel comfortable approving this?"]
    source: "framework default"

  - id: "qual-all-pain-cost-01"
    text: "If nothing changes — if you stay on your current platform another 3 years — what does that cost you?"
    industry: ["all"]
    deal_stage: ["discovery", "technical-fit"]
    audience: ["operations", "executive"]
    intent: "Quantifies cost-of-inaction; powerful for ROI framing"
    follow_ups: ["What's the biggest risk if you don't modernize?"]
    source: "framework default"

  # Add more as the distributor's team contributes...
```

## Adding questions

Each AE who wins a deal should be encouraged to drop one or two questions that worked into this file via PR or admin tool. The distributor's enablement lead reviews monthly and curates. The plugin's content-health artifact flags this file as "stale" if no edits in 90 days.
