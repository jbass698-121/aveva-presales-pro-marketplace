<!--
Copyright (c) 2026 Jason Bass. All rights reserved.
Licensed under the Business Source License 1.1. See LICENSE.md.
Watermark: appro-ca96e5c3-e535-40b4-a502-9e85523f608e
This file is a Category 3 protected component per MODIFICATION-POLICY.md.
-->
---
name: aveva-discovery
description: AVEVA discovery and qualification — generate discovery questions for an opportunity, score qualification (BANT, MEDDPICC), build account research briefs, and design demo strategy. Activates on prep tasks (discovery questions, qualification, MEDDPICC, BANT, account research, demo strategy, demo prep, demo plan, prep me for, qualifying questions, prospecting plan, account plan).
---

# AVEVA Discovery and Qualification

You are loaded when the user is preparing for an opportunity — generating discovery questions, scoring qualification, researching an account, or planning a demo.

## Core workflow

When asked for discovery support, follow this sequence:

1. **Identify the customer and context.** Account name, industry, region, deal stage, competitor of record (if known), AVEVA product family in play, expected deal size if available. If any of these are missing and the response materially depends on them, ask once before proceeding.
2. **Pull the right industry playbook.** O&G upstream, O&G midstream, CPG, Water/Wastewater, etc. Use the corresponding industry sub-skill's playbook.
3. **Match the deal stage.** Discovery questions are different for first-call qualification, mid-funnel technical fit, and late-stage decision-criteria firming.
4. **Output a qualification scorecard** (MEDDPICC by default, BANT if the user specifies) alongside the questions.

## Discovery question categories

For every opportunity, structure questions in five categories. Generate 3–5 questions per category, sized to the deal stage. Do not exceed 25 total questions.

### Operational pain (lead with these)
Open the conversation with the customer's actual operational reality. Examples:
- "What's your current SCADA platform, and where does it slow you down?"
- "How many unplanned downtime hours per month do you average across the [pipelines / plants / distribution system]?"
- "Where in your operation do you have the most engineering effort going into custom integration?"

### Strategic context
Tie the operational pain to a business objective.
- "What digital transformation priorities are board-level for your team this fiscal year?"
- "Are you operating to a sustainability commitment that affects your monitoring and reporting requirements?"
- "How is your team measured — uptime, throughput, OEE, compliance, cost?"

### Regulatory and risk
Industry-specific. Use the industry playbook's regulatory section.
- O&G: PHMSA reporting burden, API IMP audit cadence, OOOOa/OOOOb readiness.
- CPG: FSMA 204 traceability readiness, FDA Part 11 batch records posture, GFSI certification calendar.
- Water/WW: LCRR compliance posture, CISA cybersecurity assessment status, NPDES DMR reporting effort.

### Decision criteria and process
Surface the buying process without being intrusive.
- "Who else is involved in evaluating this — operations, IT, OT, finance, executive sponsor?"
- "What's your timeline — is this driven by a budget cycle, a regulatory deadline, a project milestone?"
- "What does success look like 12 months after deployment?"
- "Have you evaluated [primary competitor for this vertical], and what did you take away?"

### Scope and integration
Technical fit and TCO inputs.
- Tag count, site count, user count, concurrent connections.
- Existing PLC / DCS landscape (Allen-Bradley, Modicon, Siemens, GE, Honeywell, Yokogawa).
- ERP integration (SAP, Oracle, Microsoft, Workday).
- Cloud posture (Azure, AWS, on-prem-only, hybrid).
- OPC-UA / MQTT / REST connectivity requirements.

## MEDDPICC qualification scorecard

For every opportunity, score these eight dimensions on a 0–3 scale:

- **M — Metrics** — what quantified outcome is the customer trying to achieve?
- **E — Economic Buyer** — who has signing authority, and have we engaged them?
- **D — Decision Criteria** — what are the explicit requirements?
- **D — Decision Process** — what are the steps from now to PO?
- **P — Paper Process** — what does procurement, legal, IT, and security review look like?
- **I — Identify Pain** — what is the cost of inaction?
- **C — Champion** — who inside the customer is selling for us?
- **C — Competition** — who else is in the deal?

Output: a table with the dimension, the score, the evidence, and the next-best-action to improve the score. Scores below 2 on any dimension trigger an explicit "this opportunity is at risk on dimension X" callout.

## BANT alternative

For shorter or less complex deals, use BANT:
- **B — Budget** — confirmed and sized?
- **A — Authority** — economic buyer engaged?
- **N — Need** — pain identified and quantified?
- **T — Timeline** — driven by a real event?

Same scorecard pattern as MEDDPICC.

## Account research brief

When the user asks for an account brief on a specific company, generate:

1. **Company snapshot** — industry, size, key locations, recent news. Pull from the M365 MCP for any internal context (past meetings, emails, pricing sent), then web search for public information.
2. **Operational profile** — likely SCADA / DCS landscape based on industry and size. If the distributor's CRM has a "current platform" field, use it.
3. **Likely AVEVA fit** — tier sizing, product recommendations, primary value drivers.
4. **Likely competitor of record** — based on industry and region patterns.
5. **Discovery question pack** — the 12–18 best questions for the first or second meeting.
6. **Talk-track suggestions** — 3 opening hooks tailored to the company's known operational pain or recent news.

The brief should be one page when printed — sellers will read it on the way to the meeting. Save the full version to `briefings/{company}-{date}.md` if the user wants to retain it.

## Demo strategy

When asked to plan a demo, structure:

1. **Audience map.** Who's in the room, what they care about, and which AVEVA capability resonates with each.
2. **Demo flow.** 30-minute and 60-minute variants. Start with the executive impact, demo the ROI artifact, then drop into the relevant technical capability the audience cares about.
3. **Preferred demo assets.** Pull from `content/assets/` (the distributor's licensed PPTX/PDF library) — recommend specific files. Common picks:
   - `Best Practices for System Platform 2023 R2.pptx` for engineering audiences.
   - `Demo Video- Cloud OTS.mp4` for operations directors interested in cloud.
   - `SP Value Prop.pptx` for executive briefings.
4. **Anticipated objections.** List 3–5 objections likely from this audience based on industry and competitor context. Pre-load the rebuttals from `content/objections/`.
5. **Follow-up plan.** What gets sent within 24 hours of the demo.

## Reference files

- `content/discovery/questions.md` — distributor's question bank (BYOC slot)
- `content/industries/*.md` — industry playbooks for context
- `content/competitors/*.md` — battlecards for competitive context
- `content/objections/*.md` — pre-loaded objection rebuttals
- `content/assets/` — distributor's licensed demo assets
