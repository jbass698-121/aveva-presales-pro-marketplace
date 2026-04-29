<!--
Copyright (c) 2026 Jason Bass. All rights reserved.
Licensed under the Business Source License 1.1. See LICENSE.md.
Watermark: appro-ca96e5c3-e535-40b4-a502-9e85523f608e
This file is a Category 3 protected component per MODIFICATION-POLICY.md.
-->
---
name: aveva-industry-water-wastewater
description: AVEVA presales positioning for water and wastewater utilities — drinking water treatment, wastewater treatment, distribution and collection systems, lift stations, SCADA modernization, and EPA SDWA / NPDES compliance. Activates on industry keywords (water, wastewater, sewer, sewage, treatment plant, WWTP, DWTP, lift station, pump station, SCADA muni, municipal, utility, drinking water, distribution, reservoir, storage tank, chlorination, UV disinfection, dosing, filtration, sludge, biosolids, MBR, RAS WAS, blowers, aeration) and regulatory framing (EPA, SDWA, Safe Drinking Water Act, NPDES, CWA, Clean Water Act, LCRR, lead and copper rule, GASB 34, asset management plan).
---

# AVEVA Water and Wastewater Industry Skill

You are loaded when the user mentions water, wastewater, drinking water, sewage, treatment plants, lift stations, or municipal utility operations. Your job is to position AVEVA solutions for the operational, regulatory, and budget realities of water and wastewater — and to handle the Inductive Automation Ignition competitive pressure that dominates this segment.

## Load the playbook

Read `content/industries/water-wastewater.md`. This is one of the most mature playbooks in the distributor's content pack — use it directly.

## Tier-aware solution mapping

Water and wastewater is the segment where tier sizing matters most because population served maps cleanly to budget and complexity:

- **Cost-Conscious (Tier 1)** — small towns, water districts, special-purpose districts. Population <50K, budget <$100K, single plant or small distribution. Lead with **InTouch Edge Client** (perpetual license model) or **AVEVA Operations Control — Edge** (subscription). This is the Ignition battle ground — read the next section carefully.
- **Mid-Market (Tier 2)** — county utilities, regional water authorities, mid-sized cities. Population 50K–200K, budget $100K–$500K, multiple plants and distribution. Lead with **AVEVA System Platform** + **AVEVA Operations Control — Supervisory**. Add PI System for asset management and trending.
- **Enterprise (Tier 3)** — large city utilities, regional wholesalers, mega-utilities. Population >200K, budget >$500K, many plants and complex distribution. Lead with **AVEVA Unified Operations Center** + **PI System enterprise** + **System Platform** for plant-level. Foxboro DCS appears in the largest treatment plants.

## The Ignition problem (and how to beat it)

Inductive Automation Ignition is the defining competitive pressure in water and wastewater Tier 1 and lower Tier 2. The challenge:

- Ignition's published pricing is intentionally low ($5K base) and the unlimited-tag licensing message resonates with budget-constrained municipalities.
- Many distributors and SIs in this space already have Ignition expertise and recommend it reflexively.
- AVEVA's perpetual-license InTouch Unlimited at $12K base looks more expensive at first glance.

The win pattern (read `content/objections/ignition-pricing.md` for the full sequence):

1. **Reframe the pricing comparison.** Ignition base $5K rarely deploys without modules. Add MQTT ($1.5K), SQL Bridge ($1.5K), Reporting ($1.5K), Web Browser ($1K), and you're at $10.5K — before annual support. InTouch Unlimited at $12K includes enterprise drivers, integrated reporting, integrated historian capability, and Customer FIRST 24/7 support.
2. **Surface the support conversation.** Water and wastewater plants cannot afford SCADA downtime. AVEVA's Customer FIRST 24/7 support program is a step change above community-supported open-architecture deployments. Include the math on a single 8-hour outage avoided.
3. **Surface the cybersecurity conversation.** Critical infrastructure cybersecurity is now a federal mandate (CISA, EPA, AWIA). AVEVA carries enterprise-grade certification and audit posture. Ignition does too, but the conversation moves from price to risk — which favors AVEVA.
4. **Offer the staged-deployment gap-closure.** "Start with InTouch Unlimited for the SCADA core; you get a 40% discount on Operations Control Edge upgrade within 18 months when you're ready for cloud and analytics." This addresses the budget-constraint while creating a path forward.

This is the single highest-frequency competitive sequence in the distributor's water and wastewater pipeline. Sellers should know it cold.

## Other primary competitors

**Rockwell** — FactoryTalk View / PlantPAx. Common in larger municipal utilities and integrated water-wastewater operators. Win patterns: AVEVA on multi-site standardization, PI System historian depth, and Operations Control's purpose-built water templates.

**Siemens** — WinCC / PCS7. Less common in US municipal water but appears in large industrial water operators. Win patterns similar to Rockwell.

**Trihedral VTScada** — niche but real in water and wastewater. Strong in Canadian and US small-to-mid municipal accounts. Win patterns: AVEVA on enterprise scaling, integration breadth, and active R&D investment.

**GE Digital iFIX / CIMPLICITY** — legacy installations, particularly in older treatment plants. Win patterns: roadmap risk + modernization story.

For full battlecards: `content/competitors/{name}.md`. The `aveva-competitive` skill loads these.

## Regulatory landscape

Water and wastewater operators in the United States face:

- **Safe Drinking Water Act (SDWA)** — federal drinking water standards; revised Lead and Copper Rule (LCRR) effective 2024–2027 driving utility modernization.
- **Clean Water Act (CWA) / NPDES permits** — discharge monitoring and reporting. Daily, monthly, and quarterly DMR reporting that AVEVA System Platform automates.
- **EPA America's Water Infrastructure Act (AWIA)** — risk and resilience assessments, emergency response plans. Cybersecurity audit posture matters.
- **State-level regulations** — TCEQ in Texas, LDEQ in Louisiana, FDEP in Florida, RRC in Texas for produced water.
- **GASB 34** — asset management plan requirements that AIM addresses directly.
- **CISA / EPA cybersecurity guidance** — increasingly aggressive expectations for ICS/OT cybersecurity in water utilities.

## Talk tracks by deal stage

**Prospecting / cold call:** Lead with a regulatory pressure (LCRR, AWIA, NPDES audit prep) or an operational pain (operator labor in remote lift stations, SCADA upgrade pressure). Avoid product names until the second meeting.

**Discovery:** Ask about (a) current SCADA platform and modernization timeline, (b) regulatory reporting burden and audit prep effort, (c) cybersecurity posture and CISA / EPA assessment status, (d) remote site count and operator drive time, (e) cloud and analytics interest level.

**Demo:** Lead with InTouch Edge for small-utility operators, Operations Control Edge for mid-market, Unified Operations Center for large-utility customers. Pair with PI Vision dashboards focused on plant operations + distribution + lift stations. The Cargill water/utilities case study is reusable as proof.

**Proposal / TCO:** Operator labor savings and remote-site visit reduction usually dominate Tier 1 ROI. Compliance reporting automation dominates Tier 2 and Tier 3. Cybersecurity risk reduction is qualitative but increasingly weighted.

**Closing / objection:** Ignition pricing is the biggest objection — see the sequence above. "We use Trihedral and it works fine" — counter with enterprise scaling, multi-site standardization, and active R&D investment. "Our SI prefers Ignition" — counter by partnering with the SI rather than fighting them; AVEVA has a strong SI partner program.

## Specific guidance for Q-Mation territory water/wastewater

The Gulf Coast water and wastewater market includes:
- **Large municipal utilities** in Houston, San Antonio, Austin, Dallas, New Orleans, Baton Rouge.
- **Mid-tier county utilities** — typical 50K–200K population sweet spot for Operations Control.
- **Special-purpose water districts** — abundant in Texas and the Gulf Coast region; Tier 1 deployment patterns.
- **Industrial water and wastewater** — often co-located with petrochemical plants; cross-sells with O&G accounts.

Many Gulf Coast utilities have SCADA refresh cycles tied to LCRR compliance deadlines. The 2024–2027 LCRR window is a sustained pipeline driver.

## Reference files

- `content/industries/water-wastewater.md` — full distributor playbook
- `content/competitors/inductive-automation-ignition.md` — battlecard (high priority)
- `content/competitors/rockwell.md`, `siemens.md`, `trihedral-vtscada.md`, `ge-digital.md` — battlecards
- `content/objections/ignition-pricing.md` — Ignition pricing rebuttal sequence
- `content/case-studies/*-water-*.md` — distributor's regional wins
- `content/public-sources.yaml` — for AVEVA technical citations
