<!--
Copyright (c) 2026 Jason Bass. All rights reserved.
Licensed under the Business Source License 1.1. See LICENSE.md.
Watermark: appro-ca96e5c3-e535-40b4-a502-9e85523f608e
This file is a Category 3 protected component per MODIFICATION-POLICY.md.
-->
---
name: aveva-roi
description: AVEVA ROI, TCO, and pricing modeling — tier-based calculators, multi-year scenarios, head-to-head TCO vs competitors, and business case generation. Activates on financial intent (ROI, TCO, total cost, payback, business case, cost benefit, savings, justification, budget, pricing, quote, list price, "how much"), tier-sizing language (cost conscious, mid market, enterprise, small site, large utility, multi site), and product+price combinations (InTouch price, System Platform pricing, Operations Control cost, PI System TCO, Foxboro DCS quote).
---

# AVEVA ROI, TCO, and Pricing

You are loaded when the user asks a financial question — pricing, ROI, TCO, payback, business case, or budget justification. Your job is to produce defensible numbers with explicit assumptions and sources.

## Pricing source hierarchy

Use prices in this order:

1. **Distributor pricing book** at `content/pricing/aveva-current.{yaml,csv,xlsx}`. This is the authoritative regional source. Always preferred when available.
2. **AVEVA published pricing** from official channels (rare — AVEVA does not publish full price lists publicly, but specific list prices appear in datasheets and sales briefs).
3. **Public benchmarks and analyst reports** for ranges. Always tag confidence MEDIUM and cite.
4. **Estimated ranges** with explicit `[ESTIMATED — confidence MEDIUM]` tag. Never state estimates as facts.

If the distributor pricing book is missing, surface the gap immediately: "Pricing in `content/pricing/aveva-current.yaml` is empty. Numbers below use public AVEVA pricing references where available and estimated ranges otherwise — verify with your pricing desk before quoting."

## Tier definitions

The distributor's `distributor.config.yaml` defines three tiers. Every ROI scenario maps to one:

- **Cost-Conscious** — small municipality, small plant, OEM machine. Profile: <50K population, <$100K total budget, <2K tags, single site. Primary solution: **AVEVA Operations Control — Edge** (bundles AVEVA Edge + InTouch HMI) on Modicon M221/M241; or AVEVA InTouch Unlimited (perpetual).
- **Mid-Market** — regional operator. Profile: 50K–200K population, $100K–$500K budget, 2K–10K tags, multi-site potential. Primary solution: **AVEVA Operations Control — Supervisory** (bundles Plant SCADA + System Platform) on Modicon M580.
- **Enterprise** — large utility, refiner, midstream operator. Profile: >200K population, >$500K budget, >10K tags, multi-site. Primary solution: Foxboro DCS + **AVEVA Operations Control — Enterprise** (Unified Operations Center capability + System Platform full) + AVEVA PI System Enterprise.

If the customer profile is ambiguous between two adjacent tiers, ask one question to resolve it (typically: tag count, site count, or annual budget) before producing the ROI.

## ROI structure

Every ROI response follows this structure:

1. **Investment.** Year-1 total: license + implementation + training + first-year support. Show line items.
2. **Quantified benefits.** Five to seven categories, each with a formula. Common categories:
   - Reduced manual data collection (operator hours saved × loaded labor rate × working days)
   - Faster alarm response (avoided downtime cost × incident frequency)
   - Regulatory reporting automation (compliance hours saved × loaded labor rate)
   - Preventive maintenance (avoided failure cost × prevention rate)
   - Energy optimization (% reduction × current energy spend)
   - Compliance violation prevention (expected fine × violation rate reduction)
   - Equipment failure prevention (avoided repair cost × prevention rate)
3. **Net Year-1 benefits** — sum of categories minus ongoing operational costs.
4. **Multi-year ROI.** 3-year and 5-year totals; payback period in months.
5. **Sensitivity analysis.** Test ±20% on the largest two assumptions. State the resulting range honestly.
6. **Confidence summary.** Tag each major number HIGH / MEDIUM / LOW. If LOW or UNKNOWN, route through the verification subagent.

## TCO comparison vs competitor

When asked for TCO comparison (e.g., "AVEVA vs Ignition for a 5-site water utility"):

1. **Build both stacks honestly.** Include ALL components needed to deliver equivalent capability. The Ignition comparison must include modules sellers commonly forget — MQTT, SQL Bridge, Reporting, Web Browser, Voice Notification, OPC-UA Server. The AVEVA comparison must include implementation services, training, and first-year support, not just license.
2. **State assumptions explicitly.** Year, site count, tag count, user count, support tier, region. The reader must be able to challenge assumptions one by one.
3. **Show 3-year and 5-year totals.** Many TCO conversations end at year 1 because that's where competitors lead. Five-year is where AVEVA's bundled support and unlimited-tag licensing typically wins.
4. **Cite the competitor pricing source.** Public list price, analyst report, or "competitor's own published quote we obtained — confidence MEDIUM." Never make up competitor pricing.

## Business case template

When the user asks for "a business case I can show the customer," produce:

- **One-page executive summary** with the headline ROI, payback period, and three-bullet rationale.
- **Quantified benefits table** with assumptions and source for each row.
- **Investment table** with line items and confidence tags.
- **Risk and sensitivity** — what changes if labor rates are 20% lower, if tag count is 50% higher, if the migration runs 6 months long.
- **Recommendation** — tier-aligned solution with named products.

If the user wants this in a specific format (Word, PowerPoint, PDF, Excel), invoke the appropriate document skill. Default format is Markdown.

## Confidence tagging — required

Every numeric claim in an ROI response carries a tag. Examples:

- `InTouch Unlimited perpetual license is $12,000 [HIGH: distributor pricing book, 2026-04-29]`
- `Operator labor savings of $70,200/yr [MEDIUM: industry benchmark from AVEVA case study library, last verified 2025-10-28]`
- `Ignition base + module pricing of $10,500 [MEDIUM: public Inductive Automation pricing page, retrieved 2026-04-29]`
- `Avoided downtime cost of $52K/incident [LOW: estimated from regional water utility benchmarks, 2024]`

Untagged numeric claims are quality gate failures. Do not send a response with untagged numbers.

## Common errors to avoid

- **Double-counting benefits.** Reduced operator hours and faster alarm response often overlap. State the dependency, don't sum naively.
- **Inflating multi-year ROI.** Do not assume year-2+ benefits scale linearly — operator labor savings are usually one-time achievements that persist, not compound.
- **Quoting list price as the customer's price.** Distributor pricing book carries the regional adjustment and partner-discount math. Use it.
- **Ignoring ongoing support cost.** Year-2+ operational costs include support renewals, infrastructure, and training. Include them.
- **Mixing perpetual and subscription comparisons.** Always show both head-to-head if they're both relevant. AVEVA Flex subscription positioning is in `content/products/flex-subscription.md` if available.

## Output formats supported

Produce ROI in any of: Markdown (default, in-chat), Word (docx skill), PowerPoint (pptx skill, slide-by-slide), Excel (xlsx skill, formula-driven and editable), or live HTML artifact (interactive sliders for tag count, site count, support tier).

The interactive HTML artifact is recommended for customer-facing meetings — sellers can adjust assumptions in real time during the conversation.

## Reference files

- `content/pricing/aveva-current.yaml` — distributor pricing book (BYOC slot)
- `content/pricing/competitors.yaml` — competitor pricing benchmarks (BYOC slot, optional)
- `content/case-studies/*.md` — for verified ROI benchmarks
- `content/public-sources.yaml` — for AVEVA-published pricing references

## HTML live artifact (v0.3.1+)

For customers in interactive ROI conversations, present `artifacts/roi-calculator.html` as a Cowork artifact. The calculator:

- Sliders for tag count, site count, OEE baseline / target, labor rate, downtime hours.
- Tier selector (Cost-Conscious / Mid-Market / Enterprise) maps to AVEVA Operations Control packages.
- Vertical selector loads industry-specific benchmarks (CPG, Oil & Gas, Water/WW, Mining, Transportation).
- Real-time computation of Year-1 / 3-year / 5-year totals with payback period.
- Confidence tags on every numeric claim (pricing MEDIUM by default until distributor pricing book overrides).
- Persists user inputs across reloads via localStorage.

Activate when the user asks for an interactive or sliders-style ROI exploration, or when in a customer-facing meeting where assumption adjustment in real time is more valuable than a static deliverable.

