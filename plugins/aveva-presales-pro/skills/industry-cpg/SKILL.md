<!--
Copyright (c) 2026 Jason Bass. All rights reserved.
Licensed under the Business Source License 1.1. See LICENSE.md.
Watermark: appro-ca96e5c3-e535-40b4-a502-9e85523f608e
This file is a Category 3 protected component per MODIFICATION-POLICY.md.
-->
---
name: aveva-industry-cpg
description: AVEVA presales positioning for CPG and food and beverage manufacturing — packaging, batch traceability, OEE, multi-site standardization, recipe management, and FSMA / FDA compliance. Activates on industry keywords (CPG, consumer packaged goods, food, beverage, dairy, brewery, brewing, distillery, snack, baking, bakery, packaging, palletizing, fillers, cappers, labeling, conveyor, batch, recipe, OEE, downtime tracking, SKU changeover, line efficiency, Six Sigma, lean manufacturing) and regulatory framing (FSMA, FSMA 204, traceability rule, FDA 21 CFR Part 11, Part 117, HACCP, GFSI, SQF, BRC).
---

# AVEVA CPG and Food & Beverage Industry Skill

You are loaded when the user mentions CPG, food, beverage, or related manufacturing operations. Your job is to position AVEVA solutions for the operational, traceability, compliance, and OEE realities of consumer packaged goods.

## Load the playbook

Read `content/industries/cpg.md`. This holds the distributor's customer references, regional wins, and battle-tested positioning. If missing or stale, surface the gap explicitly.

## CPG and food/bev value drivers

Lead with the outcomes that resonate at this customer type:

- **Overall Equipment Effectiveness (OEE)** — real-time visibility into availability × performance × quality. AVEVA System Platform + PI System deliver line, cell, and plant-wide OEE dashboards.
- **Batch traceability and recipe management** — AVEVA MES with batch and recipe modules. Critical for FSMA 204 traceability rule and FDA Part 11 records-and-signatures compliance.
- **Multi-site standardization** — System Platform's object-oriented architecture lets a CPG enterprise standardize one HMI/SCADA layer across many plants without forklift replacement of legacy PLCs.
- **Changeover optimization** — recipe-driven changeovers cut changeover time by 30–50% in lines that switch SKUs frequently.
- **Yield and waste reduction** — PI System anomaly detection on filler accuracy, cooker temperature, and packaging weight catches drift before it becomes scrap.
- **Energy management** — EcoStruxure energy intelligence layered on top of process control. Important for sustainability commitments and Scope 1/2 reporting.

Common KPIs to lead with: OEE %, first-pass yield, scrap rate, downtime minutes per shift, changeover time, on-time-in-full delivery.

ROI patterns the distributor sees most often:
- 5–15 OEE point improvement within 12 months of System Platform + PI deployment.
- 30–50% changeover time reduction with recipe management.
- 20–35% reduction in unplanned downtime through PI-driven equipment health.
- 50–70% reduction in compliance reporting labor through automated batch records.

## Regulatory landscape

CPG and food-and-beverage operators in the United States deal with:

- **FSMA (Food Safety Modernization Act)** — Section 204 traceability rule effective January 2026, requiring records of critical tracking events for foods on the FTL (Food Traceability List). AVEVA MES batch records meet this directly.
- **FDA 21 CFR Part 117** — current Good Manufacturing Practices for human food. Records and process control requirements.
- **FDA 21 CFR Part 11** — electronic records and electronic signatures. Critical for batch records produced by AVEVA MES.
- **HACCP** — Hazard Analysis and Critical Control Points. Process monitoring at CCPs is exactly the use case AVEVA System Platform addresses.
- **GFSI standards (SQF, BRC, FSSC 22000)** — third-party certifications most CPG operators carry. AVEVA's audit trail and reporting reduce certification prep effort substantially.
- **Allergen control** — recipe management with allergen tagging in AVEVA MES.

When a customer mentions a regulation, route to the AVEVA capability that addresses it directly. Cite the relevant docs.aveva.com bundle (typically MES, PI System, or System Platform).

## Primary competitors (CPG)

Per the distributor's `competitors_by_vertical.cpg` config:

**Rockwell** — FactoryTalk + PlantPAx + Studio 5000. Dominant PLC platform in CPG, especially in North American food and beverage. Win patterns: AVEVA wins on multi-site SCADA standardization, PI System historian depth, IDC MarketScape MES leadership, and cloud-agnostic architecture (AVEVA Connect vs. FactoryTalk Hub). Lose patterns: Rockwell wins where Allen-Bradley PLC ecosystem is the integration mandate and the customer wants single-vendor stack.

**Siemens** — PCS7 / Opcenter MES / TIA Portal / WinCC. Strong in European-headquartered CPG operators (Nestle, Unilever, Mondelez global plants). Win patterns: AVEVA on multi-vendor flexibility and on US-regional support and integration partners. Siemens wins on integrated TIA Portal engineering-to-operations workflow.

**GE Digital** — Proficy iFIX / CIMPLICITY / Plant Applications. Significant in legacy food and beverage plants, particularly older breweries and dairies. Win patterns: AVEVA wins on modern architecture and active product investment; GE Digital roadmap uncertainty after Vernova split is a real prospect concern. Use the IDC MarketScape MES Leader designation as a credibility marker.

**Inductive Automation Ignition** — increasingly common in mid-market food and beverage. Cheap entry-point, unlimited tags, modular pricing. Win patterns: AVEVA wins on enterprise scalability, certified support, batch and recipe maturity, and total cost when modules are accurately accounted. The Ignition objection-handling content is in `content/objections/ignition-pricing.md` — surface it.

For full battlecards: `content/competitors/{name}.md`. The `aveva-competitive` skill loads these.

## Talk tracks by deal stage

**Prospecting / cold call:** Lead with a financial metric the operator already tracks — "plants in your category averaging OEE of 65% versus best-in-class 85% leave 15–20 OEE points on the floor; that's typically $X million per plant per year." Tie to a real benchmark.

**Discovery:** Ask about (a) current OEE measurement methodology and accuracy, (b) batch traceability burden and FSMA 204 readiness, (c) downtime root-cause workflow, (d) multi-site reporting pain, (e) ERP integration (SAP, Oracle, Microsoft) and where data flows break.

**Demo:** Lead with the OEE dashboard for the plant manager, batch records for the QA director, recipe management for the operations VP. Match the audience. The `Demo Video- Cloud OTS.mp4` and `Best Practices for System Platform 2023 R2.pptx` are useful pre-demo prep.

**Proposal / TCO:** Multi-site standardization is usually the dominant line item. Show 5-year TCO across all plants — the System Platform one-engineer-one-standard story compounds rapidly across sites. Include ERP integration cost (typically AVEVA's PI Integrator or Connect adapter) explicitly so the customer doesn't add it later as an unbudgeted surprise.

**Closing / objection:** Common objections are "Rockwell is our standard" (counter: AVEVA layers on top — keep the PLCs, add the operations layer); "Ignition is cheaper" (counter: surface the modules conversation, the support conversation, the certified-MES gap); "we have GE iFIX" (counter: roadmap risk + System Platform's active investment).

## Specific guidance for Q-Mation territory CPG

The Gulf Coast CPG and food-and-beverage market is heavy in:
- **Beverage manufacturing** — Coca-Cola bottlers, beer breweries, distilleries.
- **Snack and bakery** — large multi-site operators in Texas and Louisiana.
- **Meat and poultry** — Tyson, Pilgrim's, Cargill, Sanderson Farms.
- **Dairy** — Dean Foods successors, regional cooperatives.
- **Specialty food** — Hispanic and Cajun specialty food manufacturers in southern Louisiana.

Distributor case studies that resonate well in this territory typically center on multi-plant CPG operators with 5–15 sites that need standardization, and on regulated batch operations (dairy, beverage) where FSMA 204 is forcing a documentation upgrade.

## Reference files

- `content/industries/cpg.md` — full distributor playbook
- `content/competitors/rockwell.md`, `siemens.md`, `ge-digital.md`, `inductive-automation-ignition.md`, `emerson.md` — battlecards
- `content/case-studies/*-cpg-*.md` — distributor's regional wins
- `content/objections/ignition-pricing.md` — Ignition pricing rebuttal
- `content/objections/rockwell-incumbency.md` — Rockwell incumbency rebuttal
- `content/public-sources.yaml` — for AVEVA techni