---
industry: oil-gas
sub_segments: ["upstream", "midstream", "downstream"]
last_validated: "2026-04-29"
distributor_focus: primary
provenance: "Starter content adapted from prior consolidated O&G playbook (2025-Q4). Q-Mation should overwrite with regional / customer-specific content."
sources:
  - url: "https://www.aveva.com/en/customers/case-studies/"
    type: "aveva_corporate"
    date: "2026-04-29"
  - url: "https://docs.aveva.com/bundle/pi-system/"
    type: "official_docs"
    date: "2026-04-29"
---

# Industry Playbook: Oil and Gas

## Executive Overview

Oil and gas operations face pressure to maximize asset utilization, ensure safety compliance, and optimize production efficiency while managing volatile market conditions. AVEVA's combined PI System + System Platform + Connect platform addresses these challenges, with broad penetration across global O&G operators. The distributor's stated focus is upstream and midstream — downstream is in the AVEVA portfolio but is typically sold direct by AVEVA to large refiners.

## Sub-Segment Detail

### Upstream — Production Optimization

**Operational profile:** wells, separators, compressors, gas-lift systems, ESPs, distributed pads, often-remote facilities. Reliability and uptime are the dominant value drivers.

**KPIs the customer tracks:** production uptime, MTBF on artificial lift, gas-lift optimization yield, deferred production, lifting cost per BOE.

**Pain points AVEVA addresses:**
- Real-time production monitoring across wells via PI System integrated with SCADA
- Asset integrity and equipment health monitoring (PI Asset Framework + AIM)
- Reservoir / well-test analytics
- Edge data acquisition at remote pads (Modicon M241 + InTouch Edge Client)
- Predictive maintenance for drilling, pumps, and rotating equipment

**ROI patterns (industry estimates — verify against distributor case studies before quoting):**
- 15–25% improvement in artificial lift uptime via PI-driven anomaly detection
- 20–40% reduction in maintenance costs through condition-based scheduling
- 60–80% faster regulatory audit prep through automated documentation

### Midstream — Pipelines, Gathering, Terminals

**Operational profile:** long-haul and gathering pipelines, compressor stations, terminals, tank farms. Regulatory and reliability pressures dominate.

**KPIs the customer tracks:** pipeline availability, throughput, allowable operating pressure margin, leak detection time-to-alarm, custody-transfer reconciliation accuracy.

**Pain points AVEVA addresses:**
- Pipeline SCADA via System Platform with PI System for historical analytics
- Leak detection and integrity workflows integrated with partner LDS
- Custody transfer measurement integration via OPC-UA from flow computers (Daniel, FMC, Cameron)
- Compressor station monitoring with PI Asset Framework templates
- Terminal and tank-farm operations with InTouch HMI + PI batch / inventory tracking
- PHMSA 49 CFR 192 (gas) and 195 (liquid) reporting automation

**ROI patterns (industry estimates):**
- Unplanned downtime reduction from hours to minutes via real-time monitoring
- 10–20% throughput improvement through pressure optimization
- Audit-prep time reduced 50–70% via automated PHMSA reporting

### Downstream — Refining (Secondary for this distributor)

**Operational profile:** refining, petrochemicals, integrated process units. Energy and yield optimization dominate.

**Pain points AVEVA addresses:** advanced process control + optimization, energy management, catalyst performance monitoring, yield optimization, integrated design-to-operations workflow.

**Note for sellers:** AVEVA tends to sell directly to large refiners. If a downstream conversation arises, the distributor's typical play is hardware (Modicon, Foxboro DCS) + selective AVEVA software pull-through. Connect to AVEVA's direct refining team for major opportunities.

## Regulatory Landscape (Gulf Coast emphasis)

- **PHMSA Gas Pipeline Mega Rule** — three phases: **RIN1** (effective July 2020, material verification + assessment expansion + recordkeeping), **RIN2** (effective May 24, 2023, integrity management improvements + repair criteria + corrosion control + management of change), **RIN3** (effective May 16, 2023, expanded jurisdiction over onshore gathering lines). RIN2 and RIN3 are the active SCADA-modernization conversation drivers in midstream right now.
- **PHMSA 49 CFR 195 (Hazardous Liquid Pipelines)** — integrity management, leak detection, custody-transfer reconciliation. Operator Qualification, IMP.
- **TCEQ** (Texas) and **LDEQ** (Louisiana) — emissions, water, air permitting.
- **EPA NSPS Subpart OOOOb / OOOOc** — methane standards for oil and gas. OOOOb = NSPS for new, reconstructed, modified sources. OOOOc = Emission Guidelines for states to develop plans for existing sources. Final rule published March 8, 2024; EPA extended several compliance deadlines via interim final rule (July 2025) and final rule (November 2025); first OOOOb annual report due no earlier than November 30, 2026; state-plan submission deadline January 22, 2027; reconsideration on two specific aspects finalized April 4, 2026.
- **API recommended practices** — 510 (pressure vessels), 570 (piping), 653 (tanks), 1149 (LDPC).
- **BSEE / BOEM** — offshore Gulf of Mexico.

When a customer mentions a regulation, surface the AVEVA reporting workflow that addresses it. PI System and System Platform have native support for most O&G compliance reporting patterns.

## Primary Competitors in Oil and Gas

(See `content/competitors/<name>.md` for full battlecards.)

| Competitor | Threat Tier | Win Pattern (AVEVA) | Lose Pattern |
|---|---|---|---|
| Honeywell (Experion / Uniformance) | Primary | Multi-vendor flexibility, PI System depth, EcoStruxure energy management, AVEVA Connect cloud-agnostic | Refining incumbency, existing Experion investments |
| Emerson (DeltaV / Plantweb) | Primary | Open architecture; PI System + System Platform breadth | Upstream incumbency, instrumentation depth |
| Yokogawa (CENTUM VP / Exaquantum) | Primary in offshore | Multi-vendor flexibility, AIM/PI integration | Offshore + Asia-Pacific incumbency |
| ABB (System 800xA) | Secondary | Foxboro DCS + EcoStruxure energy management | Marine, integrated power-plus-process |
| Rockwell | Secondary in process | Open process architecture | Discrete-adjacent gas processing |

## Talk Tracks by Deal Stage

### Prospecting / Cold Call
**Opening hook:** "Operators in your category averaging X hours of unplanned downtime per month on artificial lift — that's typically $Y in deferred production. Plus PHMSA audit cycles eating Z weeks of compliance team time. Worth 20 minutes?"
**Avoid:** product names, "AVEVA can do everything," generic "digital transformation."

### Discovery
**Top 5 questions:**
1. "What's your current SCADA / DCS landscape, and where does it slow you down?"
2. "How does your team handle PHMSA Gas Mega Rule Part 2 integrity management reporting (effective May 2023) — manual, semi-automated, or integrated with SCADA? For liquid lines: how is 49 CFR 195 IMP and leak-detection workflow integrated?"
3. "What's your average response time when a well or compressor goes down?"
4. "How is your team measured — uptime, throughput, regulatory compliance, lifting cost?"
5. "Are you operating to a sustainability commitment or OOOOb/c monitoring requirement that affects monitoring and reporting requirements? First OOOOb annual report is due no earlier than November 2026."

### Demo
**Lead capability by audience:**
- **Operations director:** AVEVA PI Vision dashboards focused on production health and downtime root cause (on-prem); CONNECT Visualization with the same data model for customers cloud-evaluating; **AVEVA Industrial AI Assistant** in CONNECT (GA Jan 2026) for natural-language query of production data, role-based permissions, never trained on customer data.
- **Integrity manager:** AIM workflows, PI Asset Framework risk-based inspection.
- **Controls engineer:** System Platform graphics, scripting, multi-vendor integration.
- **Compliance officer:** automated PHMSA reporting, audit trail.

### Proposal / TCO
**Largest value driver in upstream:** asset health and downtime avoidance.
**Largest value driver in midstream:** multi-site standardization + compliance reporting automation.

### Closing / Common Objections
- **"We already have Honeywell."** → "AVEVA, part of Schneider Electric, sits on top of your existing DCS — keep what you have, add the System Platform SCADA aggregation, PI System intelligence Experion doesn't provide natively, and EcoStruxure energy management. One company, one MSA, one renewal motion for the unified portfolio."
- **"We're standardizing on Emerson."** → Same hybrid play. PI System integrates with DeltaV; you don't have to displace anything.
- **"We tried Yokogawa overseas."** → "CENTUM is strong in Asia. In Gulf Coast operations, AVEVA's regional support footprint and the depth of US-based AVEVA-certified system integrators is a meaningful operational difference."

## Recommended AVEVA Solution Tiers

- **Cost-Conscious upstream pad operator:** **AVEVA Operations Control — Edge** (bundles AVEVA Edge + InTouch HMI) on Modicon M241; PI System Edge for historian.
- **Mid-market upstream / gathering operator:** **AVEVA Operations Control — Supervisory** (bundles AVEVA Plant SCADA + System Platform) on Modicon M580; AVEVA PI System for historian (PI Vision on-prem or CONNECT Visualization for cloud-evaluating customers).
- **Enterprise midstream / large upstream operator:** Foxboro DCS + **AVEVA Operations Control — Enterprise** (Unified Operations Center capability + System Platform full) + AVEVA PI System Enterprise + AVEVA Asset Information Management.

## Distributor's Regional Wins

(Reference `content/case-studies/<file>.md` for full stories. Add wins as they close.)

| Customer | Year | Solution | Outcome | Competitor of Record |
|---|---|---|---|---|
| <<add as cases close>> | | | | |

## Specific Guidance for Q-Mation Territory

The Gulf Coast O&G market includes:
- **Texas RRC and Permian Basin** upstream operators — distributed pad operations.
- **Louisiana and Texas Gulf Coast midstream** — major pipelines and gathering systems (Energy Transfer, Enterprise Products, Plains, Williams).
- **Offshore GoM** — independent operators and majors. Yokogawa often incumbent; AVEVA's PI System depth is the lead.
- **Texas refineries** — typically AVEVA-direct accounts; cross-sell hardware where possible.
- **Oklahoma and southwest** — gas processing, often Emerson or Honeywell incumbent.

## Notes for the Verification Subagent

- Trusted public sources: docs.aveva.com (PI System, System Platform), www.phmsa.dot.gov (regulatory), www.api.org (API standards), competitor official sites (Honeywell, Emerson, Yokogawa).
- Most-stale-prone facts: PHMSA Mega Rule phase-specific compliance milestones; OOOOb/c deadline extensions (last update Nov 2025; reconsideration Apr 2026); competitor product naming changes (Honeywell Forge / Experion roadmap; Emerson AspenTech integration since AspenTech take-private March 2025).
- Watch for: AVEVA quarterly release notes, AVEVA Connect feature additions, competitor cloud-platform announcements.
