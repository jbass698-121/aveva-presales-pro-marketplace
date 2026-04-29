---
theme: "rockwell-incumbency"
applicable_verticals: ["cpg", "water-wastewater-large", "discrete-adjacent-oil-gas"]
last_validated: "2026-04-29"
confidence: "MEDIUM"
---

# Objection Theme: "Rockwell is our standard — we don't want to introduce another vendor"

## The Objection (verbatim)

> "We've standardized on Allen-Bradley PLCs and FactoryTalk. Introducing AVEVA means another vendor to manage."

## Why the Customer Says It

Vendor-fatigue, often expressed by IT directors or operations VPs who've been through painful multi-vendor integrations. They've made a strategic decision to consolidate around Rockwell and aren't looking to revisit it. Sometimes coached by a Rockwell distributor / SI who positions AVEVA as competitive.

## The Reframe (don't accept the premise)

Adding AVEVA software is *not* a vendor swap. AVEVA System Platform sits on top of existing Allen-Bradley PLCs through OPC-UA, gives the customer the operations, alarming, recipe, and historian layer that FactoryTalk View doesn't natively deliver, and adds energy intelligence Rockwell doesn't match. The customer keeps every PLC investment they've made; they add the intelligence layer they're already missing.

## The Evidence (specifics with sources)

- AVEVA System Platform supports OPC-UA, Ethernet/IP, ControlNet, DH+, and direct Allen-Bradley protocols natively. Source: docs.aveva.com System Platform driver list.
- Many AVEVA customers run mixed Modicon + Allen-Bradley + Siemens + third-party PLCs through one System Platform. Source: AVEVA reference architectures.
- IDC MarketScape MES Leader designation reflects multi-vendor integration as a core competency. Source: IDC MarketScape MES report.
- Energy management capabilities (EcoStruxure) are not natively present in FactoryTalk. Source: Rockwell product pages vs. AVEVA + Schneider Electric portfolio.

## The Gap-Closure Offer

> "Let's start with one production line. We'll keep every existing Allen-Bradley PLC and FactoryTalk asset in place. We add AVEVA System Platform on top for that line — operations dashboards, recipe management, historian intelligence. Run it for 90 days. If the value isn't visible to your operations team, we walk away. If it is, we extend to the next line on your timeline."

Distributor commits to:
- 90-day pilot pricing.
- Implementation services scoped tightly to the pilot.
- All existing AB hardware and FactoryTalk software preserved.
- Joint review with the customer's operations and IT leads at day 90.

## Verbatim Response Script

> "I get the vendor-fatigue concern — you've consolidated around Rockwell intentionally and that's served you. We're not asking you to swap vendors. AVEVA System Platform sits on top of your existing Allen-Bradley PLCs through OPC-UA. Your PLC investment, your FactoryTalk investments — all preserved. What you add is the operations layer FactoryTalk View doesn't natively deliver: recipe management, multi-site standardization, integrated historian, EcoStruxure energy management. Many of our customers run AVEVA on top of pure Allen-Bradley environments. Want to see a reference architecture and propose a 90-day pilot on one line?"

## Common Follow-Up Objections (chained)

- **"We don't have budget for another platform."** → "AVEVA Operations Control — Edge at ~$22.5K/year is below most plant maintenance line items. The pilot decision isn't a multi-million dollar one."
- **"FactoryTalk is adding the cloud features we need."** → "FactoryTalk Hub is real and Rockwell-centric. AVEVA Connect has multi-vendor data services with a multi-year head start. If your stack is Rockwell-only, that's fine. If it's evolving toward multi-vendor — most are — AVEVA's vendor-agnostic position adds optionality."
- **"What about training cost?"** → "AVEVA is intentionally similar to FactoryTalk in concepts. Most engineers ramp on System Platform faster than they expect. We include training in implementation services."

## When This Objection Indicates Disqualification

If the customer is genuinely committed to single-vendor Rockwell stack as a strategic decision (not just a default), the AVEVA pitch is uphill. Don't burn cycles on customers who've explicitly committed at the executive level to vendor consolidation; redirect to opportunities where multi-vendor flexibility is at least neutral.

## Notes for the Verification Subagent

- Verify Rockwell product naming and roadmap quarterly against rockwellautomation.com.
- Verify AVEVA System Platform driver list against docs.aveva.com.
- Watch for: FactoryTalk Hub feature additions that close the cloud-vendor-agnostic gap.
