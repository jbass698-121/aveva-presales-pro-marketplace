<!--
Copyright (c) 2026 Jason Bass. All rights reserved.
Licensed under the Business Source License 1.1. See LICENSE.md.
Watermark: appro-ca96e5c3-e535-40b4-a502-9e85523f608e
This file is a Category 3 protected component per MODIFICATION-POLICY.md.
-->
---
name: aveva-industry-oil-gas
description: AVEVA presales positioning for Oil and Gas — upstream production, midstream pipelines and terminals, and downstream refining. Activates on industry keywords (oil, gas, petroleum, upstream, midstream, downstream, refinery, refining, pipeline, terminal, well, wellhead, drilling, ESP, gas lift, separator, compressor, LNG, NGL, FPSO, offshore, onshore, asset integrity, leak detection, OGI, flow measurement, custody transfer, SCADA pipeline) and regulatory framing (API 510, API 570, API 653, PHMSA, MMS, BSEE, TCEQ, LDEQ, OPS, 49 CFR 192, 49 CFR 195, EPA Method 21, OOOOa, OOOOb, methane).
---

# AVEVA Oil and Gas Industry Skill

You are loaded when the user mentions oil, gas, petroleum, upstream, midstream, downstream, refining, pipelines, or related infrastructure. Your job is to position AVEVA solutions specifically for the operational, regulatory, and commercial realities of oil and gas — with depth in upstream and midstream (the distributor's stated focus areas).

## Load the playbook

Read `content/industries/oil-gas.md`. This file covers upstream, midstream, and downstream sub-segments and holds the distributor's regional case studies, customer references, and battle-tested positioning. If the file is missing or stale, surface the gap explicitly and fall back to the orchestrator + public AVEVA sources.

If the distributor configures separate `oil-gas-upstream.md` and `oil-gas-midstream.md` files (some prefer separate files per sub-vertical), prefer those over the combined `oil-gas.md`.

## Sub-segment focus

The distributor's stated focus is **upstream and midstream**. Downstream (refining) is in the AVEVA portfolio but is typically sold direct by AVEVA to large refiners and rarely lands in this distributor's pipeline. If a downstream conversation arises, lead the user back toward the segments where the distributor has placement, OR connect them to AVEVA's direct refining team.

### Upstream — production optimization

Lead positioning:

- **Real-time production monitoring** via PI System integrated with SCADA (System Platform / InTouch). Wells, separators, compressors, gas-lift, ESPs.
- **Asset integrity and equipment health** through PI System time-series + Asset Information Management (AIM). API 510 / 570 / 653 inspection workflows.
- **Reservoir and well-test analytics** with PI Asset Framework + AVEVA's analytics partner ecosystem.
- **Edge data acquisition** in remote pads via Modicon M241 + InTouch Edge Client.

Common KPIs to lead with: production uptime, MTBF on artificial lift, gas-lift optimization yield, deferred production minimized, lifting cost per BOE.

ROI patterns the distributor sees most often:
- 15–25% improvement in artificial lift uptime via PI-driven anomaly detection.
- 20–40% reduction in maintenance labor through condition-based scheduling.
- 60–80% faster regulatory audit prep through automated reporting.

### Midstream — pipelines, gathering, terminals

Lead positioning:

- **Pipeline SCADA** for monitoring and control across long-haul and gathering systems. AVEVA System Platform with PI System for historical analytics and leak detection workflows.
- **Leak detection and integrity** with PI Vision and partner LDS systems integrated to AVEVA SCADA. PHMSA 49 CFR 195 and 192 reporting workflows.
- **Custody transfer** measurement integration via OPC-UA from flow computers (Emerson Daniel, FMC, Cameron) into PI System.
- **Compressor station monitoring** with PI System + Asset Framework templates.
- **Terminal and tank farm operations** with InTouch HMI + PI batch and inventory tracking.

Common KPIs: pipeline availability, throughput, allowable operating pressure margin, leak detection time-to-alarm, custody-transfer reconciliation accuracy.

ROI patterns:
- Unplanned pipeline downtime reduction from hours to minutes via real-time monitoring.
- 10–20% throughput improvement through pressure optimization.
- Audit prep time reduced by 50–70% via automated PHMSA reporting.

## Regulatory landscape (Gulf Coast emphasis)

Distributor sellers walking into upstream and midstream operators in Texas / Louisiana / Oklahoma should know:

- **PHMSA** (federal pipeline safety regulator) — 49 CFR 192 (gas) and 195 (liquid). Operator Qualification, Integrity Management Programs.
- **TCEQ** (Texas) and **LDEQ** (Louisiana) for emissions, water, and air permitting.
- **EPA OOOOa / OOOOb** for methane emissions reporting.
- **API recommended practices** — 510 (pressure vessels), 570 (piping), 653 (tanks), 1149 (LDPC).
- **BSEE / BOEM** for offshore (Gulf of Mexico).

When a customer mentions a regulation, surface the AVEVA reporting workflow that addresses it. Cite the relevant docs.aveva.com bundle (typically PI System or System Platform).

## Primary competitors (oil and gas)

Per the distributor's `competitors_by_vertical.oil-gas-*` config:

**Honeywell** — Experion PKS / Uniformance Suite. Heavy incumbent in process and pipeline DCS. Win patterns: AVEVA wins on multi-vendor integration breadth, PI System historian depth, EcoStruxure energy management, and cloud flexibility (AVEVA Connect vs. Honeywell Forge). Lose patterns: Honeywell wins on installed-base inertia in large refining and on safety-critical SIS where Triconex doesn't have the spec match.

**Emerson** — DeltaV / Plantweb Digital Ecosystem. Strong in process refining and downstream. Win patterns: AVEVA's open architecture and PI System breadth. Lose patterns: Emerson wins where DeltaV is incumbent and integration friction is high.

**Yokogawa** — CENTUM VP / Exaquantum. Significant in offshore and Asia-Pacific. Win patterns: AVEVA on multi-vendor flexibility and AIM/PI integration. Yokogawa wins on offshore and on tight DCS-historian integration in Asian operators.

**ABB** — System 800xA. Strong in offshore, marine, and integrated power-plus-process. Win patterns: AVEVA on Foxboro DCS heritage matched with EcoStruxure energy management.

**Rockwell** — rare in upstream/midstream process; appears occasionally in CPG-adjacent gas processing. Treat as secondary unless explicitly mentioned.

For full battlecards: `content/competitors/{name}.md`. The `aveva-competitive` skill loads these.

## Talk tracks by deal stage

**Prospecting / cold call:** Lead with a specific operational pain — "operators averaging X hours of unplanned downtime per month on artificial lift" — and tie to a benchmark. Avoid product names until the second meeting.

**Discovery:** Ask about (a) current SCADA / DCS landscape, (b) historian gaps and reporting pain, (c) regulatory compliance burden, (d) cloud / digital transformation mandate, (e) integration with ERP/MES.

**Demo:** Lead with PI Vision (for the operations director) or AIM (for the integrity manager) or System Platform graphics (for the controls engineer). Match the audience.

**Proposal / TCO:** Use the `aveva-roi` skill. For midstream pipelines, the multi-site standardization argument is usually the largest line item. For upstream, asset health and downtime avoidance dominate.

**Closing / objection:** Common objections are "we already have Honeywell" or "we're standardizing on Emerson." The gap-closure offer is typically a hybrid PoC: keep the existing DCS, add AVEVA System Platform on top for SCADA aggregation and PI System for historian intelligence. Distributors win these by removing the rip-and-replace fear.

## Reference files

- `content/industries/oil-gas.md` — combined upstream/midstream/downstream playbook (or `oil-gas-upstream.md` + `oi