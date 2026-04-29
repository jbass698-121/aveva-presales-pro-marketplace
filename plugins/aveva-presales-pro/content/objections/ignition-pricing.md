---
theme: "ignition-pricing"
applicable_verticals: ["water-wastewater", "cpg", "oil-gas-upstream"]
last_validated: "2026-04-29"
confidence: "MEDIUM"
notes: "Ignition module pricing changes regularly. Verify against inductiveautomation.com/pricing before quoting. Distributor should refresh quarterly via the source-validation scheduled task."
---

# Objection Theme: "Ignition is cheaper than AVEVA"

## The Objection (verbatim)

> "Inductive Automation Ignition is only $5,000 versus your $12,000 — and they have unlimited tags, MQTT, and a free trial."

## Why the Customer Says It

Budget anxiety, often raised in cost-conscious water utilities, mid-market CPG operators, or upstream pad operators where the buyer is comparing list-price headlines without modeling true comparative cost. Frequently coached by an SI partner that's already Ignition-fluent.

## The Reframe (don't accept the premise)

The $5K Ignition base price almost never deploys without modules. Every real-world Ignition deployment requires several modules to match what InTouch Unlimited delivers in the box. The honest comparison adds those modules to the Ignition side of the ledger — and adds AVEVA's bundled support, certified drivers, and training to the AVEVA side. The math then runs much closer; the support-and-cybersecurity conversation tilts the rest of the way.

## The Evidence (specifics with sources — verify before quoting)

| Component | Ignition list (approximate) | AVEVA InTouch Unlimited |
|---|---|---|
| Base SCADA | $5,000 | $12,000 perpetual |
| MQTT module | $1,500 | Included |
| SQL Bridge | $1,500 | Included (HistorianDB Connector) |
| Reporting module | $1,500 | Included (basic) |
| Web Browser / Vision | $1,000 | Included (web-based view) |
| Voice notification | $500 | Optional via partner |
| Annual support / maintenance | ~20% of license | $2,400/year (20%) |
| **Year-1 fully-loaded** | **~$11,500–$12,000** | **~$14,400** (license + support) |
| **Year-3 fully-loaded** | **~$14,500–$15,000** | **~$19,200** |
| **Year-5 fully-loaded** | **~$17,500–$18,000** | **~$24,000** |

[ESTIMATE — verify against current Inductive Automation pricing at inductiveautomation.com/pricing and against `content/pricing/aveva-current.yaml` before sharing with customer.]

The math gets *closer* when modules are honestly accounted, but Ignition is still typically lower in pure license-and-modules cost. The pivot is from price to total value.

## The Three-Part Pivot

After reframing the price, the seller pivots through three angles:

### 1. Support and SLA
Water and wastewater plants cannot afford SCADA downtime. CPG plants lose six figures per hour of unplanned downtime. Upstream pads lose deferred production every hour a well is down. AVEVA Customer FIRST 24/7 support is a meaningful step up from community-supported open-architecture platforms.

> *Talk track:* "What's the cost to your operation of an 8-hour SCADA outage? Two outages per year? Customer FIRST is part of every InTouch Unlimited license — round the clock, certified, with response-time SLAs. That's not the same conversation as 'community forum.'"

### 2. Cybersecurity and compliance
Critical infrastructure cybersecurity is now under serious federal pressure — CISA, EPA AWIA for water, CIRCIA cyber-incident reporting, FDA Part 11 for CPG batch records, PHMSA Mega Rule + 49 CFR 195 for midstream, TSA Pipeline Cybersecurity Directive for hazardous-liquid pipelines. **AVEVA holds ISO 27001, SOC 2 Type II, ISA/IEC 62443 (since 2019), and ISASecure SDLA certifications** — that's the floor for OT cybersecurity audits. AVEVA's enterprise certification posture and audit trail are direct differentiators when these requirements are on the table.

> *Talk track:* "Are you doing a CISA risk assessment this year? Walk me through your audit trail and access-control posture today. AVEVA's enterprise security framework was built for this; we have the certification documentation to hand to your IT and OT directors."

### 3. Path to enterprise
The customer almost always grows. Tag count grows, sites grow, integration requirements grow. AVEVA's portfolio scales with them — Operations Control Edge → Site → Unified Operations Center — without a forklift replacement. Ignition scales too, but with module-licensing complexity at every step.

> *Talk track:* "Where do you see this system in 3 years? If you're going to add 5 more sites and a real historian, the AVEVA path keeps you on one platform. The Ignition path is more module-licensing math each step. Want to model both 5-year scenarios side-by-side?"

## The Gap-Closure Offer

Concrete commitment the seller can make this week:

> "Start with AVEVA InTouch Unlimited at $12K for the SCADA core. We'll lock in a 40% discount on **AVEVA Operations Control — Edge** upgrade if you take it within 18 months. That gets you the cloud, AI assistant, and unlimited-clients story when you're ready, while keeping today's CapEx contained."

OR, for customers genuinely budget-blocked:

> "We can do **AVEVA Operations Control — Edge** at approximately $22.5K/year — full subscription, AVEVA CONNECT cloud included, **Industrial AI Assistant** (GA January 2026, natural-language query across your CONNECT data), no upfront license. That puts AVEVA below your three-year Ignition fully-loaded cost while giving you cloud capabilities Ignition needs custom development to match."

## Verbatim Response Script

> "I hear you on the headline price. Let me show you what happens when we add the modules you'd actually need: MQTT, SQL Bridge, Reporting, Web Browser. That's another $5,500 on top of the $5,000 base — and that's before annual support. So you're at roughly $11,500 fully loaded vs. $14,400 for InTouch Unlimited including support. The pricing is much closer than the headline. The bigger question is: what's your operation's tolerance for an 8-hour SCADA outage, and how does your CISA cybersecurity audit look? Customer FIRST 24/7 support and AVEVA's enterprise security posture are part of the package — they're the conversations that matter for water utility leadership right now."

## Common Follow-Up Objections (chained)

- **"But our SI is already Ignition-fluent."** → "We'd love to partner with them. AVEVA has a strong SI program, and we provide certified training. They keep their integration revenue, you get enterprise platform."
- **"Ignition has unlimited tags out of the box."** → "InTouch Unlimited is also unlimited-tag; that's why it's named Unlimited. The license model is different (perpetual vs. modular), but tag count isn't actually a differentiator."
- **"Ignition is more cloud-native."** → "AVEVA Connect is the cloud layer; AVEVA was first SCADA on AWS. The cloud question is about your data sovereignty and integration requirements — let's walk through them."

## When This Objection Indicates Disqualification

Sometimes Ignition pricing isn't really the objection — it's a polite way to say one of the following:

- The SI already has Ignition deployed and is loyal to that ecosystem; the customer is downstream of that decision.
- The buyer has decided based on the SI's recommendation and AVEVA was added to "show competition." In this case, the gap-closure may not recover the deal — focus your time on the next opportunity.
- The customer's budget is genuinely below $10K and even the gap-closure offer doesn't fit. AVEVA may not be the right fit; consider whether the distributor's hardware-only play (Modicon + standard SCADA) is more appropriate.

Recognize these patterns; don't burn cycles on un-recoverable deals.

## Notes for the Verification Subagent

- Verify Ignition pricing monthly against: https://inductiveautomation.com/pricing
- Verify AVEVA pricing against: `content/pricing/aveva-current.yaml`
- Watch for: Ignition module re-pricing, new module bundles, perpetual-licensing changes; AVEVA InTouch Unlimited pricing updates in annual price-list refresh.
