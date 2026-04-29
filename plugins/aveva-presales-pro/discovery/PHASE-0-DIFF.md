# Phase 0 Discovery — Plugin vs. Canonical Diff

> ⚠️ **HISTORICAL ARTIFACT — work in this file is COMPLETE as of v0.3.0.**
>
> This document was the input punch list used to drive the v0.3.0 regulatory + naming-truth refresh. Every CRITICAL, HIGH, MEDIUM, and LOW finding listed here has been applied to the codebase. It ships in v0.3.1 as a historical record of the v0.3.0 fix scope; the findings listed below are NOT current bugs.
>
> If you're auditing v0.3.1, start with `README.md` (current state) and `docs/AS-BUILT.md` (current shipped scope). Use this file only for historical context on what changed in v0.3.0.

**Generated:** 2026-04-29
**Watermark:** appro-ca96e5c3-e535-40b4-a502-9e85523f608e
**Method:** Cross-referenced every claim in `content/industries/`, `content/competitors/`, `content/products/`, `skills/portfolio-narrative/SKILL.md`, `skills/orchestrator/SKILL.md`, and `skills/onboarding/SKILL.md` against the three Phase 0 canonical YAMLs (`aveva-canonical.yaml`, `aveva-regulatory-mapping.yaml`, `aveva-industry-positioning.yaml`).

This file was the input to Phase 1 (regulatory + naming truth release). Every row was a planned edit, and all are now applied.

---

## Severity scale

- **CRITICAL** — factually wrong; loses credibility on first contact with a current customer.
- **HIGH** — outdated framing or inaccurate detail; loses credibility within a meeting.
- **MEDIUM** — imprecise but recoverable; fix in this release for polish.
- **LOW** — drift / housekeeping; can defer if time-constrained.

---

## CRITICAL findings

### C-1. LCRR is referenced as the active regulation; LCRI replaces it

**Where the plugin says it:**
- `content/industries/water-wastewater.md` — Executive Summary, Regulatory Landscape, Discovery questions, Talk Tracks, Closing/Common Objections, "Specific Guidance for Q-Mation Territory"
- `content/discovery/questions.md` — `qual-water-discovery-01` question
- `skills/discovery/SKILL.md` — Water/WW example bullet ("LCRR compliance posture")

**Canonical truth (per `aveva-regulatory-mapping.yaml` `water_wastewater.lcri`):**
- LCRI finalized 2024-10-08, effective 2024-12-30, compliance date 2027-11-01.
- 10-year mandatory replacement; revised lead action level (10 µg/L); baseline inventory by 2027-11-01.
- LCRR is superseded — interim LCRR-era requirements (initial inventory Oct 16 2024, public notification) are maintained until LCRI compliance date.

**Phase 1 action:** Replace LCRR with LCRI throughout. Add "(formerly LCRR)" parenthetical for one cycle so muscle memory works. Update talk track to focus on LCRI 10-year timeline.

### C-2. FSMA 204 framed as Jan 2026 effective; actually extended to July 2028

**Where the plugin says it:**
- `content/industries/cpg.md` — Executive Summary, Regulatory Landscape ("FSMA 204 effective Jan 2026"), ROI patterns
- `content/discovery/questions.md` — `qual-cpg-discovery-01` ("Are you ready for FSMA 204?")
- `skills/discovery/SKILL.md` — CPG regulatory bullet
- `skills/onboarding/SKILL.md` — content health audit GREEN/YELLOW description

**Canonical truth (per `aveva-regulatory-mapping.yaml` `cpg.fsma_204`):**
- Original compliance: 2026-01-20.
- Extended via Continuing Appropriations Act (2026) to **2028-07-20**.
- FDA stance: enforcement-discretion until 2028-07-20.

**Phase 1 action:** Update the date. Add the two-track talk track (compliant program / using extension). Avoid "FSMA 204 effective January 2026" framing — it ignores the non-enforcement reality.

### C-3. Operations Control SKU naming is wrong

**Where the plugin says it:**
- `content/industries/water-wastewater.md` — Tier-Aware Solution Mapping ("Operations Control Edge Starter," "Operations Control Site Editions"), Tier triggers, Recommended AVEVA Solution Tiers
- `content/industries/cpg.md` — Recommended AVEVA Solution Tiers
- `content/industries/oil-gas.md` — Recommended AVEVA Solution Tiers
- `content/industries/mining-metals-minerals.md` — Recommended AVEVA Solution Tiers
- `content/industries/transportation.md` — Recommended AVEVA Solution Tiers
- `skills/roi/SKILL.md` — Tier definitions
- `skills/onboarding/SKILL.md` — Step 9
- `content/objections/ignition-pricing.md` — Gap-closure offer ("Operations Control Edge Starter at $22.5K/year")

**Canonical truth (per `aveva-canonical.yaml` `products.operations_control`):**
- Three packages: **Edge**, **Supervisory**, **Enterprise** (NOT Edge / Site / Supervisory).
- Edge bundles: AVEVA Edge + AVEVA InTouch HMI.
- Supervisory bundles: AVEVA Plant SCADA + AVEVA System Platform.
- Enterprise bundles: System Platform full + UOC capability.
- "Operations Control Edge Starter" is not a current SKU.
- "Operations Control Site Editions" / "Site Edition" is not a current SKU; closest equivalent is **Supervisory**.

**Phase 1 action:** Replace all references with canonical names. Maintain a `legacy_aliases` block so legacy SKU mentions in customer correspondence still resolve.

---

## HIGH findings

### H-1. Schneider-AVEVA acquisition completion date is implied as 2024; actually January 2023

**Where the plugin says it:**
- The `PRESALES-CONTENT-ANALYSIS.md` readout said "early 2024" — the plugin's content files do not state a date but treat the relationship as recent. The portfolio-narrative skill phrases it cleanly.

**Canonical truth (per `aveva-canonical.yaml` `corporate.aveva_status`):**
- Completed **2023-01-18**. Three years now under one-company structure.

**Phase 1 action:** When a date is needed (e.g., in a strategic-account brief reference), use 2023-01-18. Reframe battlecards' "AVEVA + Schneider" partnership-style language to "AVEVA, part of Schneider Electric."

### H-2. Industrial AI Assistant is missing entirely; it's GA as of January 2026

**Where the plugin says it:**
- Nowhere. There is no content/products/industrial-ai-assistant.md, no mention in portfolio-narrative, no AI counterpart in any battlecard.

**Canonical truth (per `aveva-canonical.yaml` `products.industrial_ai_assistant`):**
- GA January 2026 in CONNECT.
- Natural-language query, role-based permissions, never trained on customer data.
- Plus three other AI tools launched same wave (Generative Design AI, Predictive Design AI, Intelligent Point Cloud Framework).

**Phase 1 action (limited scope):** Add a one-paragraph mention to portfolio-narrative; add the AI Assistant one-liner to relevant industry playbook talk tracks; defer full battlecard AI-counterpart matrix to Phase 2.

### H-3. Emerson is described as having "Aspen integration via partnership"; AspenTech is now wholly owned by Emerson

**Where the plugin says it:**
- `content/competitors/emerson.md` — Product Portfolio: "Aspen simulation integration (via partnership)"
- `content/competitors/emerson.md` — Their Competitive Advantages line referencing AspenTech alongside DeltaV implies separate vendors

**Canonical truth (per industry knowledge + WebSearch):**
- Emerson completed full take-private of AspenTech 2025-03-12 ($265/share, $17B deal).
- AspenTech is wholly owned subsidiary of Emerson; ceased trading on NASDAQ.
- For chemicals/refining, expect Emerson to bundle DeltaV + Aspen products.

**Phase 1 action:** Update Emerson battlecard to reflect ownership. Add a v0.3.0+ TODO for a standalone aspentech.md battlecard. Note that the AVEVA SimSci competitive comparison disappeared from the plugin entirely — this matters for chemicals/refining.

### H-4. PHMSA generic 49 CFR 192/195 — actual conversation is the Mega Rule three phases

**Where the plugin says it:**
- `content/industries/oil-gas.md` — Regulatory Landscape table mentions "PHMSA — 49 CFR 192 (gas), 49 CFR 195 (liquid)" generically
- `content/discovery/questions.md` — `qual-og-midstream-discovery-01` references "PHMSA 49 CFR 195 reporting" generically
- `skills/discovery/SKILL.md` — O&G regulatory bullet ("PHMSA reporting burden, API IMP audit cadence, OOOOa/OOOOb readiness")

**Canonical truth (per `aveva-regulatory-mapping.yaml` `oil_gas.phmsa_gas_mega_rule`):**
- Three-phase Mega Rule: RIN1 (effective 2020-07-01), RIN2 (2023-05-24), RIN3 (2023-05-16).
- RIN2 = integrity management improvements, repair criteria, corrosion control, MoC.
- RIN3 = expanded jurisdiction over onshore gathering lines.

**Phase 1 action:** Name RIN2 and RIN3 specifically in the oil-gas playbook + discovery questions. Open with: "Mega Rule Part 2 (effective May 2023) and Part 3 (May 2023) drive the SCADA-modernization conversations in midstream now."

### H-5. EPA OOOOa/OOOOb framing — actually OOOOb/OOOOc with major timeline shifts

**Where the plugin says it:**
- `content/industries/oil-gas.md` — Regulatory Landscape: "EPA OOOOa / OOOOb — methane emissions reporting"
- `skills/discovery/SKILL.md` — same bullet

**Canonical truth (per `aveva-regulatory-mapping.yaml` `oil_gas.oooo_b_c`):**
- Final rule was OOOOb (NSPS for new sources) and OOOOc (Emission Guidelines for existing sources). OOOOa is older; current pair is OOOOb/OOOOc.
- Final rule published 2024-03-08.
- 2025-07-28 EPA extended several deadlines (interim final rule).
- 2025-11-26 final rule adopted IFR-extended deadlines.
- First annual report under Subpart OOOOb due no earlier than 2026-11-30.
- State plan submission deadline: 2027-01-22.
- 2026-04-04 reconsideration on two specific aspects.

**Phase 1 action:** Replace "OOOOa/OOOOb" with "OOOOb/OOOOc" and add the deadline-shift context. Open with: "First OOOOb annual report due no earlier than November 2026 — what's your data plan?"

### H-6. PI Vision is described as the AI/cloud demo asset; should branch by deployment

**Where the plugin says it:**
- `content/industries/cpg.md` — Demo: "PI Vision OEE dashboard"
- `content/industries/water-wastewater.md` — Demo: implied
- `content/industries/oil-gas.md` — Demo: "PI Vision dashboards focused on production health"
- `content/industries/mining-metals-minerals.md` — Demo: "PI Vision dashboards showing combined process + electrical + power KPIs"
- `content/industries/transportation.md` — Demo: "PI Vision combined dashboards"
- `skills/discovery/SKILL.md` — Demo strategy

**Canonical truth (per `aveva-canonical.yaml` `products.pi_system.deployment_paths` and `products.connect`):**
- On-prem: AVEVA PI System with PI Vision (current canonical).
- Cloud: AVEVA PI Data Infrastructure with **CONNECT Visualization**.
- Hybrid: AVEVA PI System with hybrid CONNECT data services.

**Phase 1 action:** Two-track demo guidance in every industry playbook. "If on-prem, PI Vision. If cloud-evaluating, CONNECT Visualization on AVEVA PI Data Infrastructure."

### H-7. Battlecards do not leverage AVEVA-is-Schneider parent structure consistently

**Where the plugin says it:**
- Five full battlecards (Rockwell, Siemens, Honeywell, Emerson, Ignition) treat "AVEVA + Schneider" as an alliance/partnership.
- Differentiator language: "EcoStruxure energy management capabilities Rockwell does not match natively" — implies AVEVA is bringing in EcoStruxure as an ally, not as a sister product within the same company.

**Canonical truth (per `aveva-canonical.yaml` `corporate.aveva_status`):**
- AVEVA, part of Schneider Electric. One company, one MSA, one renewal motion.
- Forbidden phrase per canonical: "AVEVA + Schneider partnership."

**Phase 1 action:** Reframe each of 5 battlecards' AVEVA Counter-Strategy section. Add a `audience_signals` block to each battlecard front-matter so the orchestrator picks framing by buyer posture.

---

## MEDIUM findings

### M-1. PI Vision branding inconsistencies across files

**Where:**
- Some references say "PI Vision" (current canonical).
- Some imply "AVEVA PI Vision" (which is correct but verbose).
- A few lean on "OSIsoft PI" historically.

**Canonical:** "AVEVA PI Vision" (full); "PI Vision" (short form acceptable). Avoid "OSIsoft PI" except when describing pre-acquisition history.

**Phase 1 action:** Standardize on "PI Vision" short form within talk tracks; "AVEVA PI Vision" in product positioning sections.

### M-2. AVEVA security certifications not cited specifically anywhere

**Where:**
- `content/objections/ignition-pricing.md` — "AVEVA's enterprise security framework" generically
- `content/competitors/inductive-automation-ignition.md` — "AVEVA's enterprise certification posture" generically

**Canonical truth (per `aveva-canonical.yaml` `security.enterprise_certifications`):**
- ISO 27001, SOC 2 Type II, IEC 62443 / ISA 99 (since 2019), ISASecure SDLA.
- Cloud (Azure + AWS): ISO 27001/27017/27018; AICPA SOC 2.

**Phase 1 action:** Cite specific certs by name with date verified in:
- `content/objections/ignition-pricing.md` cybersecurity-pivot section
- `content/competitors/inductive-automation-ignition.md` "AVEVA Counter-Strategy" section
- `content/competitors/honeywell.md` — counter to Honeywell secure-by-design (planned for Phase 2 originally, but cite worth pulling forward)

### M-3. Industrial Intelligence Platform terminology not adopted

**Where:**
- Plugin uses "industrial automation" framing throughout.

**Canonical (per `aveva-industry-positioning.yaml` `cross_cutting_themes.industrial_intelligence`):**
- AVEVA's umbrella positioning since 2024 is "Industrial Intelligence Platform."

**Phase 1 action:** Update orchestrator skill description and portfolio-narrative skill body to use "Industrial Intelligence Platform" where the umbrella framing is appropriate. Keep "industrial automation" where the specific technical layer is meant.

### M-4. AVEVA + Databricks partnership not mentioned

**Where:**
- Workspace folder has a "Presentation- AVEVA + Databricks pitch 12-24.pptx" — but no plugin content refers to it.

**Canonical (per `aveva-canonical.yaml` `partnerships.databricks`):**
- Strategic partnership announced 2024-04-03.
- AVEVA = 2025 Databricks Manufacturing ISV Partner of the Year.
- Integration via Delta Sharing — open standard.

**Phase 2 action:** Add a partnerships section to portfolio-narrative skill. Cite specifically when customer's data-fabric strategy comes up. Keep this for Phase 2 to avoid v0.2.7 scope creep.

### M-5. Mining case studies are 2014-2016 vintage

**Where:**
- `content/case-studies/mmg-limited-mining.md` (2014-2016)
- `content/case-studies/votorantim-mining.md` (2014-2015)
- `content/case-studies/bhp-escondida-mining.md` (undated — appears 2015 era)

**Phase 5 action (deferred):** Refresh with 2023-2025 published case studies. Not Phase 1 priority.

---

## LOW findings

### L-1. AVEVA case study URL pattern in front-matter
Several front-matter `sources:` blocks reference `https://www.aveva.com/en/customers/case-studies/` — the URL exists but is the index. Specific case-study URLs are deeper. **Phase 3 action:** Replace with deep links.

### L-2. "MMG Limited" vs. "MMG"
Inconsistent across files. Canonical: "MMG Limited" (per their corporate name).

### L-3. "InTouch Unlimited" branding not tagged as canonical
The product still exists and "Unlimited" is the right tag-licensing counter to Ignition. No change needed; just confirm via canonical.

### L-4. AVEVA Flex page and `flex-subscription.md` content alignment
Loose. AVEVA has continued to evolve Flex commercial terms. **Phase 2-3 action:** Confirm against partner portal.

### L-5. "OSIsoft PI" appearances
None found in current plugin — the "PI System" naming is consistently AVEVA-branded already. Confirmed clean.

---

## Summary by file (for Phase 1 work-planning)

| File | Critical | High | Medium | Low | Phase 1 work |
|---|---|---|---|---|---|
| `content/industries/water-wastewater.md` | C-1, C-3 | H-6, H-7 (via Ignition refs) | M-3 | — | Heavy |
| `content/industries/cpg.md` | C-2, C-3 | H-6 | M-3 | — | Heavy |
| `content/industries/oil-gas.md` | C-3 | H-4, H-5, H-6, H-7 | M-3 | — | Heavy |
| `content/industries/mining-metals-minerals.md` | C-3 | H-6, H-7 | M-3 | L-2 | Medium |
| `content/industries/transportation.md` | C-3 | H-6, H-7 | M-3 | — | Light |
| `content/competitors/rockwell.md` | — | H-7 | M-2 | — | Medium |
| `content/competitors/siemens.md` | — | H-7 | M-2 | — | Medium |
| `content/competitors/honeywell.md` | — | H-7 | M-2 | — | Medium |
| `content/competitors/emerson.md` | — | H-3, H-7 | M-2 | — | Medium |
| `content/competitors/inductive-automation-ignition.md` | — | H-7 | M-2 | — | Medium |
| `content/objections/ignition-pricing.md` | C-3 | — | M-2 | — | Medium |
| `content/objections/rockwell-incumbency.md` | — | H-7 | — | — | Light |
| `content/discovery/questions.md` | C-1, C-2 | H-4 | — | — | Heavy |
| `skills/discovery/SKILL.md` | C-1, C-2 | H-4, H-5, H-6 | — | — | Heavy |
| `skills/orchestrator/SKILL.md` | — | — | M-3 | — | Light |
| `skills/portfolio-narrative/SKILL.md` | — | H-2 | M-3 | — | Light |
| `skills/onboarding/SKILL.md` | — | — | — | — | Light (Step 9 update on regulations / SKUs) |
| `skills/roi/SKILL.md` | C-3 | — | — | — | Medium |
| **TOTALS** | **9 instances across 7 files** | **17 instances across 13 files** | **12 instances across 11 files** | **2 instances** | |

---

## Phase 1 entry criterion

User reviews this diff and signs off on which findings get fixed in v0.2.7 (or v0.3.0 combined Phase 1+2).
Default recommendation: fix all CRITICAL + HIGH; fix MEDIUM where the file is already being edited (no extra cost); defer LOW to Phase 3.

*End of Phase 0 diff.*
