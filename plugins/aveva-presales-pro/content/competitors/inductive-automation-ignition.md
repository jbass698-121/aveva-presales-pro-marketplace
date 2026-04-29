---
competitor: "Inductive Automation (Ignition)"
threat_tier: "primary"
verticals_active_in: ["water-wastewater", "cpg", "oil-gas-upstream"]
audience_signals:
  cost_sensitive: "Surface modules math + AVEVA Operations Control — Edge subscription option below 3-year Ignition fully-loaded TCO"
  enterprise_inclined: "Lead with one-company portfolio + certified support: AVEVA, part of Schneider Electric, with ISO 27001 + SOC 2 Type II + ISA/IEC 62443 + Customer FIRST 24/7"
their_AI_offering: "Ignition Vision AI module (machine vision focus). Cloud-edition AI features in development. Inductive Automation has been adding AI capabilities; the gap to AVEVA Industrial AI Assistant (GA Jan 2026) is real but narrowing."
last_validated: "2026-04-29"
confidence_default: "MEDIUM"
provenance: "Pricing changes regularly; verify against inductiveautomation.com/pricing each month."
sources:
  - url: "https://inductiveautomation.com/"
    type: "competitor_official"
    date: "2026-04-29"
  - url: "https://inductiveautomation.com/pricing"
    type: "competitor_official"
    date: "2026-04-29"
---

# Battlecard: Inductive Automation (Ignition)

## Threat Profile

- **Market position:** growing fast in light manufacturing, water/wastewater, mid-market CPG, system-integrator-led deployments.
- **Revenue:** privately held; estimated >$50M and growing.
- **Core strength:** transparent pricing, unlimited-tag licensing, SQL-based architecture, strong SI community.
- **Threat tier (this distributor):** primary in cost-conscious water/wastewater and mid-market CPG; secondary in upstream pad operators.

## Product Portfolio

- Ignition (unified HMI/SCADA/MES platform)
- Vision module (computer vision AI)
- Reporting, Voice Notification, MQTT, SQL Bridge, Web Browser, OPC-UA, etc. (modular pricing)
- Ignition Edge (smaller, edge-first deployments)
- Enterprise licensing tiers

## Their Competitive Advantages

1. Transparent published pricing on the website — easy to comparison-shop. Resonates with budget-anxious municipal and small-mid customers.
2. Unlimited-tag licensing message is simple to understand and pitch.
3. SQL-based historian creates accessibility for IT teams familiar with traditional databases.
4. Strong SI partner community; many SIs are deeply Ignition-fluent.
5. Active development cadence and engaged user community.
6. Free fully-functional trial / development version lowers buyer barrier.

## AVEVA Counter-Strategy

- **Primary positioning:** enterprise platform with bundled support and security certification vs. open-architecture platform with SI-dependent customization.
- **Top differentiator #1:** AVEVA InTouch Unlimited and Operations Control include enterprise drivers, integrated reporting, integrated historian, and 24/7 Customer FIRST support — Ignition equivalents are modular and add up.
- **Top differentiator #2:** AVEVA's enterprise certification posture — **ISO 27001, SOC 2 Type II, ISA/IEC 62443 (since 2019), ISASecure SDLA** — is the floor for water utilities under CISA/AWIA/CIRCIA scrutiny, CPG under FDA Part 11, and midstream under TSA Pipeline Cybersecurity Directive. Independent verification matters when a customer's auditor asks.
- **Top differentiator #3:** AVEVA Industrial AI Assistant is GA in CONNECT (January 2026) — natural-language query across operations data, role-based permissions, never trained on customer data. AVEVA Operations Control — Edge / Supervisory / Enterprise are cloud-native subscription models. Ignition Vision and Cloud Edition are real but require more assembly to match this maturity.
- **MES depth:** AVEVA MES is IDC MarketScape Leader-rated; Ignition MES is younger and lighter.

## When AVEVA Wins

- Enterprise deployments and regulated industries (CPG with FDA, water with CISA/EPA, O&G with PHMSA).
- Multi-site standardization where one platform across many sites is the goal.
- Customers prioritizing certified support over community-supported architecture.
- PI System integration requirements — AVEVA's PI System breadth is hard to match.
- Customers concerned about cybersecurity audit posture.

## When Ignition Wins

- Cost-sensitive small operators and special-purpose districts where headline price drives the decision.
- SI-led implementations where the SI is Ignition-fluent and recommends what they know best.
- Customers with strong internal IT/development capability who want to customize the platform.
- Cloud-greenfield deployments by buyers who treat the SCADA layer as commodity.

## Top Objections + Responses

### Objection: "Ignition is only $5,000 vs your $12,000."
**Response:** *(See `content/objections/ignition-pricing.md` for the full sequence — this is the highest-leverage script in the distributor's playbook.)* The short version: surface the modules conversation, then pivot to the support-and-cybersecurity conversation, then offer the staged-deployment gap-closure.

### Objection: "Ignition has unlimited tags out of the box."
**Response:** "InTouch Unlimited is also unlimited-tag — that's why it's named Unlimited. The licensing model is different (perpetual vs. modular) but tag count isn't actually a differentiator."
**Gap-closure:** Direct comparison sheet showing tag licensing on both sides.

### Objection: "Our SI prefers Ignition."
**Response:** "We'd love to partner with them. AVEVA has a strong SI program, certified training, and consistent integration revenue for the SI. They keep their billing and you get an enterprise platform. Win-win."
**Gap-closure:** Co-sell motion with the SI; offer joint training credits.

### Objection: "Ignition feels more modern / cloud-native."
**Response:** "AVEVA was first SCADA on AWS. AVEVA CONNECT is the cloud layer. Operations Control — Edge, Supervisory, and Enterprise are cloud-native subscription models. AVEVA Industrial AI Assistant is GA in CONNECT today (January 2026), AVEVA + Databricks integration via Delta Sharing is in production (Manufacturing ISV Partner of the Year 2025) — modern architecture is exactly the AVEVA story."
**Gap-closure:** Demo of AVEVA Connect Vision AI and cloud architecture.

## Recommended Proof Points

- Cybersecurity certification documentation for AVEVA (vs. Ignition's largely self-asserted posture).
- IDC MarketScape MES Leader designation (where MES is in scope).
- Customer reference: enterprise water utility on AVEVA Operations Control vs. comparable utility on Ignition — pull from `content/case-studies/` if available.

## Recent Changes (review monthly)

- Watch monthly: Ignition module pricing changes; new module releases; Ignition Cloud Edition feature additions.
- Inductive Automation has been adding cloud and AI capabilities; the "AVEVA is cloud, Ignition is on-prem" framing is no longer fully accurate — the comparison is more nuanced now.

## Monitoring Queries (used by scheduled tasks)

- "Inductive Automation Ignition pricing changes 2026"
- "Ignition Cloud Edition vs AVEVA Connect"
- "Ignition new modules last 90 days"

## Internal Notes (do not share with customers)

- The Ignition battle is more about *positioning* than *capability* — Ignition is a real product. Win on enterprise discipline, support, and integration depth, not on dismissive talking points.
- Distributor SEs should be Ignition-fluent enough to demo it credibly. Customers respect competitors who know the alternatives well.
