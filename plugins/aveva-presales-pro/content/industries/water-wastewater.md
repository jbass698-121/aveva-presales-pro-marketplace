---
industry: water-wastewater
sub_segments: ["drinking-water", "wastewater-treatment", "distribution-collection", "lift-stations"]
last_validated: "2026-04-29"
distributor_focus: primary
provenance: "Starter content adapted from prior consolidated water/wastewater playbook (2025-Q4). Q-Mation should overwrite with regional / customer-specific content."
sources:
  - url: "https://www.epa.gov/dwreginfo/lead-and-copper-rule"
    type: "regulatory"
    date: "2026-04-29"
  - url: "https://docs.aveva.com/bundle/operations-control/"
    type: "official_docs"
    date: "2026-04-29"
---

# Industry Playbook: Water and Wastewater

## Executive Summary

Water and wastewater utilities face a defining 2024–2027 modernization window driven by **Lead and Copper Rule Improvements (LCRI, formerly LCRR)** compliance — finalized October 2024 with a November 1, 2027 compliance date and a 10-year mandatory lead service line replacement requirement — plus EPA AWIA cybersecurity expectations and SCADA refresh cycles deferred during the pandemic. AVEVA's tiered offering — InTouch Unlimited and AVEVA Operations Control — Edge for cost-conscious utilities, AVEVA Operations Control — Supervisory for mid-market (bundles Plant SCADA + System Platform), and AVEVA Operations Control — Enterprise (Unified Operations Center capability + System Platform full) plus AVEVA PI System for enterprise — maps cleanly to utility size and budget. The dominant competitive threat in cost-conscious and mid-market water and wastewater is Inductive Automation Ignition; the playbook below addresses that head-on.

## Tier-Aware Solution Mapping (critical for water/WW)

The single most important discipline in this segment is **routing the customer to the right AVEVA tier**. Defaulting to enterprise solutions for small utilities loses deals; defaulting to cost-conscious for large utilities under-serves them.

### Tier 1: Cost-Conscious (population <50K, budget <$100K, <2K tags)

**Primary recommendation:** AVEVA InTouch Unlimited (perpetual license)
- Approx. perpetual license: $12,000 + $2,400/year support [verify against `content/pricing/aveva-current.yaml`]
- Pre-built water/wastewater templates
- Web-based remote access, basic historian, professional drivers
- **Target:** small water plants needing core SCADA/HMI

**Secondary recommendation:** AVEVA Operations Control — Edge (subscription)
- Bundles AVEVA Edge + AVEVA InTouch HMI
- Approx. annual subscription: $20,000–$25,000 [verify against pricing book]
- AVEVA CONNECT cloud integration
- AVEVA Industrial AI Assistant included for CONNECT users (GA January 2026 — natural-language query, role-based permissions, never trained on customer data)
- Unlimited tags and clients
- **Target:** small utilities wanting cloud / AI features

### Tier 2: Mid-Market (population 50K–250K, budget $100K–$500K, 2K–10K tags)

**Primary:** AVEVA Operations Control — Supervisory (subscription)
- Bundles AVEVA Plant SCADA + AVEVA System Platform
- User-based pricing
- Approx. annual: $15,000–$40,000 [verify against pricing book]
- Full CONNECT integration + Industrial AI Assistant access

### Tier 3: Enterprise (population >250K, budget >$500K, >10K tags)

**Primary:** AVEVA Operations Control — Enterprise
- Bundles Unified Operations Center capability + System Platform full
- Approx. annual base: $90,000+ [verify against pricing book]
- Multi-site management with advanced analytics and AI/ML
- Industrial AI Assistant + CONNECT Visualization for cloud dashboards
- Unlimited architectural flexibility

## Trigger Detection — Route Customers to the Right Tier

When the user describes a customer, scan for these signals:

**Cost-Conscious triggers:** population <50K, budget <$100K, "small city," "budget-limited," "tight budget," <2K tags, <10 operators.

**Mid-Market triggers:** county or regional utility, 50K–250K population, $100K–$500K budget, multi-plant.

**Enterprise triggers:** large city, >250K population, >$500K budget, multi-site, regional wholesaler, mega-utility.

If unclear between two tiers, ask one question (typically tag count or site count) before recommending.

## Regulatory Landscape

- **Safe Drinking Water Act (SDWA)** — federal drinking water standards.
- **Lead and Copper Rule Improvements (LCRI, formerly LCRR)** — finalized October 8, 2024; effective December 30, 2024; **compliance date November 1, 2027**. Headline requirements: 10-year mandatory replacement of all lead service lines (limited exceptions), revised lead action level (10 µg/L), mandatory baseline service-line inventory by November 2027, publicly-accessible replacement plan for systems serving >50,000. Interim LCRR-era requirements (initial inventory October 16, 2024; public notification of known/potential lead service lines; Tier 1 notification for action level exceedance) are maintained until LCRI compliance date. Driving SCADA-modernization conversations across the country.
- **Clean Water Act / NPDES permits** — discharge monitoring; daily, monthly, quarterly DMR reporting that AVEVA System Platform automates.
- **AWIA** — risk and resilience assessments, emergency response plans. Cybersecurity audit posture matters.
- **State-level** — TCEQ (Texas), LDEQ (Louisiana), FDEP (Florida), state RRCs.
- **GASB 34** — asset management plan requirements. AIM addresses directly.
- **CISA / EPA cybersecurity guidance** — increasingly aggressive expectations for OT cybersecurity in water utilities.

## Primary Competitors

(See `content/competitors/<name>.md` for full battlecards.)

### Inductive Automation Ignition — the live competitive pressure

**The challenge:** Ignition's published pricing ($5K base) and unlimited-tag licensing message resonates with budget-constrained municipalities. Many SI partners in this space already favor Ignition. AVEVA's perpetual-license InTouch Unlimited at $12K base looks more expensive at first glance.

**The win pattern (full sequence in `content/objections/ignition-pricing.md`):**

1. Reframe pricing — Ignition base + commonly-required modules (MQTT $1.5K, SQL Bridge $1.5K, Reporting $1.5K, Web Browser $1K) lands at $10.5K before annual support. InTouch Unlimited at $12K includes enterprise drivers, integrated reporting, integrated historian, and Customer FIRST 24/7 support.
2. Surface the support conversation — water plants cannot afford SCADA downtime; AVEVA's 24/7 support program is a step change above community-supported deployments.
3. Surface the cybersecurity conversation — critical infrastructure cybersecurity is a federal mandate now (CISA + EPA + AWIA expectations + CIRCIA reporting). AVEVA holds **ISO 27001, SOC 2 Type II, ISA/IEC 62443 (since 2019), and ISASecure SDLA** — the certification floor for OT cybersecurity. Most Ignition deployments cannot point to equivalent independent certification.
4. Offer staged-deployment gap-closure — "Start with InTouch Unlimited; get 40% off Operations Control Edge upgrade within 18 months."

| Tier | AVEVA Advantage | Ignition Challenge |
|---|---|---|
| Cost-Conscious | InTouch Unlimited at $12K provides enterprise features at entry price vs Ignition modular add-on costs | Base Ignition $5K requires expensive modules for full functionality |
| Mid-Market | Site editions provide predictable user-based scaling vs Ignition gateway licensing complexity | Multi-site Ignition gateway licensing becomes expensive |
| Enterprise | Unified Operations Center includes AI/ML and cloud vs Ignition's third-party integration requirements | Lacks native advanced analytics and enterprise-grade support |

### Rockwell (FactoryTalk View / PlantPAx)
Common in larger municipal utilities and integrated water-wastewater operators. Win pattern: AVEVA on multi-site standardization, PI System historian depth, Operations Control's purpose-built water templates.

### Siemens (WinCC / PCS7)
Less common in US municipal water but appears in large industrial water operators. Similar win pattern to Rockwell.

### Trihedral VTScada
Niche but real, especially in Canadian and US small-to-mid municipal accounts. Win pattern: AVEVA on enterprise scaling, integration breadth, and active R&D investment.

### GE Digital (Proficy iFIX, CIMPLICITY)
Legacy installations, particularly in older treatment plants. Win pattern: roadmap risk + active modernization story.

## Talk Tracks by Deal Stage

### Prospecting / Cold Call
**Opening hook:** Tie to a regulatory pressure (LCRI, AWIA, NPDES audit prep) or operational pain (operator labor in remote lift stations, SCADA upgrade pressure). Avoid product names until the second meeting.

### Discovery
**Top 5 questions:**
1. "What's your current SCADA platform, and where does it slow you down?"
2. "Where are you on LCRI's 10-year service-line replacement timeline, and what's your service-line communication strategy?"
3. "How is your CISA / EPA cybersecurity posture? Have you done a risk assessment recently?"
4. "How many remote sites does your team drive to per week, and what's the operator cost of that?"
5. "Are you considering cloud or hybrid SCADA, or staying on-prem?"

### Demo
**Lead capability by audience:**
- **Plant manager:** Operations Control or InTouch dashboard for plant operations + lift stations.
- **IT director:** AVEVA Connect cloud architecture, cybersecurity certifications, identity integration.
- **City manager / public works director:** ROI summary tied to operator labor avoidance and compliance automation.
- **Operations supervisor:** mobile / responsive HMI for remote site visibility.

### Proposal / TCO
**Largest value driver in Tier 1:** operator labor savings and remote-site visit reduction.
**Largest value driver in Tier 2/3:** compliance reporting automation + multi-site standardization.

### Closing / Common Objections
- **"Ignition is cheaper."** → Surface the modules conversation (see `content/objections/ignition-pricing.md`).
- **"We use Trihedral and it works fine."** → Counter with enterprise scaling, multi-site standardization, and active R&D investment.
- **"Our SI prefers Ignition."** → Partner with the SI rather than fight them. AVEVA, part of Schneider Electric, has a strong SI program — co-sell. SI keeps integration revenue; you get the unified portfolio (AVEVA + ETAP + EAE + PME) under one MSA.

## Specific Guidance for Q-Mation Territory

- **Large municipal utilities** in Houston, San Antonio, Austin, Dallas, New Orleans, Baton Rouge, Tulsa, Oklahoma City, Albuquerque, Denver, Phoenix.
- **Mid-tier county utilities** — typical 50K–200K population sweet spot for Operations Control.
- **Special-purpose water districts** — abundant in Texas; Tier 1 deployment patterns.
- **Industrial water and wastewater** — often co-located with petrochemical plants; cross-sells with O&G accounts.

Many Gulf Coast utilities have SCADA refresh cycles tied to **LCRI (formerly LCRR)** compliance. With LCRI's November 1, 2027 compliance date and 10-year replacement timeline, the modernization window through 2027 is a sustained pipeline driver. Service-line inventory and public-facing replacement-plan portals are direct AVEVA opportunities.

## Notes for the Verification Subagent

- Trusted public sources: docs.aveva.com (Operations Control, InTouch, System Platform), www.epa.gov (LCRI, NPDES, AWIA), inductiveautomation.com (Ignition pricing).
- Most-stale-prone facts: Ignition module pricing (changes regularly), LCRI implementation timeline (state-level adoption variance — federal compliance date is 2027-11-01; verify state-specific timelines), AWIA cybersecurity guidance, OOOOb/c oil-gas methane (relevant for industrial water co-located with petrochem).
- Watch for: AVEVA quarterly Operations Control release updates, Inductive Automation new module releases.
