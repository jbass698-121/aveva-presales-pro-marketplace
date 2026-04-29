# aveva-presales-pro — Product Specification

**Version of this document:** v1.4 (2026-04-29; aligned to plugin v0.3.1)
**Plugin version this spec describes:** v0.3.1 (current — HTML live artifacts release on top of v0.3.0 pilot)
**Author:** Jason Bass
**Status:** Specification (design intent)
**Companion doc:** AS-BUILT.md (what actually shipped + gaps)
**Date:** 2026-04-29

---

## 1. Purpose

A Cowork plugin that turns Claude into a vendor-aware, distributor-personalized AVEVA presales expert for AVEVA distributors. Initial design partner: Q-Mation (Gulf Coast pilot scope, expanding to Mountain West and Southwest). The plugin reduces seller prep time, raises briefing quality, and accelerates competitive responses across the verticals the distributor actively sells into.

## 2. Target Users

- **Primary:** AEs and SEs at AVEVA distributors. Daily users who walk into customer meetings, write proposals, handle competitive objections, model ROI.
- **Secondary:** distributor enablement / training leads. They own content health, customize battlecards, and review pipeline quality.
- **Tertiary:** distributor RevOps. They wire the CRM integration and define field mappings.

## 3. Distribution and Licensing Model

- **Format:** Cowork plugin (`.plugin` file), installed per distributor org.
- **Pricing model (deferred — Phase 7 of modernization plan):** open between per-seat subscription, per-org annual, or hybrid.
- **Content model:** BYOC (Bring Your Own Content). Plugin ships with framework + slot definitions + public-source layer + minimal vendor-neutral starter content. Each distributor brings their own pricing book, battlecards, case studies, and objection scripts under their AVEVA partnership rights.
- **IP boundary:** framework, orchestrator, slot definitions, scheduled-task patterns, and verification subagent are author IP. Distributor-supplied content is distributor IP. Public AVEVA sources are referenced under fair-use citation, not redistributed.

## 4. Architecture

### 4.1 Layered Design

```
Layer 1: Framework (always present)
  - Plugin manifest
  - Orchestrator skill (master persona, routing, confidence)
  - 7 sub-skills (competitive, roi, 3 industry, discovery, briefing)
  - Verification subagent
  - Public-sources layer (docs.aveva.com + github.com/AVEVA)
  - Slot templates

Layer 2: Distributor configuration (per-distributor, file-based)
  - distributor.config.yaml (region, verticals, competitors, voice, stack)
  - Brand assets

Layer 3: Distributor content (BYOC)
  - content/pricing/aveva-current.yaml (REQUIRED — pricing book)
  - content/competitors/{name}.md (battlecards)
  - content/industries/{vertical}.md (industry playbooks)
  - content/case-studies/{slug}.md (win stories)
  - content/objections/{theme}.md (objection scripts)
  - content/discovery/questions.md (question bank)
  - content/products/{family}.md (product positioning)
  - content/assets/ (PDFs, PPTXs they're licensed to share)

Layer 4: External integrations (per-distributor stack)
  - CRM (Microsoft Dynamics 365 for Q-Mation; Salesforce / HubSpot for others)
  - Microsoft 365 (email, calendar, Teams, SharePoint)
  - Fireflies (meeting intelligence)
  - Slack (optional, depending on stack)
```

### 4.2 Core Skills

| Skill | Trigger | Loads |
|---|---|---|
| `aveva-presales-orchestrator` | Always-on for any AVEVA / Schneider / industrial automation / competitor mention | Persona, routing engine, confidence framework, quality gates, tier definitions |
| `aveva-competitive` | Competitor names; competitive verbs (vs, compared to); objection language | Battlecard lookup pattern, four-step competitive response, gap-closure offer pattern |
| `aveva-roi` | Financial intent (ROI, TCO, payback, pricing); tier-sizing language | Tier-based ROI structure, TCO comparison pattern, business case template, confidence tagging |
| `aveva-industry-oil-gas` | Oil/gas/petroleum/pipeline/refinery keywords; PHMSA/API regulatory framing | Upstream/midstream/downstream playbook routing |
| `aveva-industry-cpg` | CPG/food/beverage/packaging/batch/OEE/FSMA keywords | Sub-segment playbooks (food&bev, packaging, household, specialty) |
| `aveva-industry-water-wastewater` | Water/wastewater/utility/SCADA-muni/EPA/LCRR/AWIA keywords | Tier-aware solution mapping; Ignition counter-positioning |
| `aveva-discovery` | Discovery / qualification / MEDDPICC / BANT / demo prep | Question generator, qualification scorecard, account research brief, demo planner |
| `aveva-briefing` | Briefing intent (prep me, brief me, walking into a meeting) | The killer artifact — pulls CRM + meetings + emails + battlecards into one page |

### 4.3 Verification Subagent

Runs in parallel after any response containing factual claims. Verification priority order:

1. `docs.aveva.com` (HIGH confidence)
2. `github.com/AVEVA` (HIGH confidence)
3. AVEVA corporate (HIGH confidence)
4. Distributor content pack (MEDIUM-HIGH if recent)
5. Competitor official sources (MEDIUM)
6. General web search (MEDIUM at best — last resort)

Returns CONFIRMED / CORRECTED / FLAGGED per claim. Time budget 90 seconds per response.

### 4.4 Routing Engine

Every query passes through six routing stages:

1. **Industry detection** — surface verticals from prompt; load matching industry sub-skill.
2. **Competitor detection** — load competitive sub-skill on competitor names.
3. **Tier sizing** — match customer profile to Cost-Conscious / Mid-Market / Enterprise tier.
4. **ROI / pricing detection** — load roi sub-skill on financial intent.
5. **Briefing detection** — load briefing sub-skill on prep / meeting intent.
6. **Confidence check** — verify any UNKNOWN claims via verifier before sending.

### 4.5 Confidence System

Every numeric claim, spec, version, regulatory reference, or competitor claim carries a confidence tag:

- **HIGH** — official source (docs.aveva.com, AVEVA IR, distributor pricing book) ≤30 days old.
- **MEDIUM** — analyst report or competitor official source ≤90 days old.
- **LOW** — >90 days old; flag for refresh.
- **UNKNOWN** — no traceable source; verifier must confirm before response sends.

Auto-degradation: HIGH→MEDIUM at 30 days, MEDIUM→LOW at 90 days, LOW→UNKNOWN at 365 days.

## 5. Configuration Surface

`distributor.config.yaml` parameters:

- `distributor.name`, `distributor.type`, `distributor.region`, `distributor.regions_served`
- `verticals.active`, `verticals.fast_follow`, `verticals.parked`
- `competitors_by_vertical.{vertical}.{primary,secondary}`
- `product_focus.{software_primary,software_secondary,hardware_secondary}`
- `tiers.{cost_conscious,mid_market,enterprise}` profiles and primary solutions
- `stack.{crm,email_calendar,meeting_intelligence,messaging,identity}`
- `voice.{persona,tone,forbidden_phrases,confidence_display}`
- `scheduled_tasks.*` (timing for weekly briefing, biweekly GitHub watch, monthly docs diff, quarterly ROI refresh, monthly source validation)
- `brand.{primary_color,accent_color,logo_path,voice_guide_path}`

## 6. Content Slots (BYOC)

| Slot | Required? | Format | Purpose |
|---|---|---|---|
| `pricing/aveva-current.yaml` | **Required** | YAML | Authoritative pricing book |
| `pricing/competitors.yaml` | Recommended | YAML | Competitor pricing benchmarks |
| `competitors/{name}.md` | **Required for primary competitors** | Markdown | Battlecard per competitor |
| `industries/{vertical}.md` | **Required for active verticals** | Markdown | Industry playbook |
| `products/{family}.md` | Recommended | Markdown | Product positioning |
| `case-studies/{slug}.md` | Recommended | Markdown | Win stories |
| `objections/{theme}.md` | Recommended | Markdown | Objection scripts |
| `discovery/questions.md` | Optional | Markdown + YAML | Discovery question bank |
| `assets/` | Optional | Files | Licensed AVEVA / Schneider PDFs and PPTXs |
| `brand/` | Optional | Files | Logo, colors, voice guide |
| `public-sources.yaml` | **Built-in** | YAML | Framework-shipped (not BYOC) |

## 7. Scheduled Tasks (configured at install)

- **Weekly competitive-news brief** — searches for competitor news from the past 7 days; posts digest to configurable Slack/Teams channel.
- **Bi-weekly AVEVA GitHub watch** — checks `github.com/AVEVA` for new repos, releases, notable commits.
- **Monthly `docs.aveva.com` change watch** — diffs key product doc pages against last snapshot; flags meaningful changes.
- **Quarterly ROI/case-study refresh** — searches for new AVEVA case studies and benchmarks; flags stale content.
- **Monthly source-validation** — spot-checks top URLs in live sources registry.

## 8. External Integrations (Phase 3 of modernization plan)

Required MCPs for full functionality:

- **Microsoft Dynamics 365** (CRM) — opportunity, account, contact, custom fields. Auth via Azure AD / Entra ID. (Q-Mation stack.)
- **Microsoft 365** — email, calendar, Teams threads, SharePoint folders.
- **Fireflies** — meeting transcripts.
- **Slack** — only if distributor uses Slack.

The plugin runs without these — degraded but functional.

## 9. The Killer Artifact: Opportunity Briefing

Single-page briefing combining:

- CRM opportunity record (account, contact, stage, amount, competitor field).
- Recent meeting transcripts (last 60 days from Fireflies).
- Recent email threads (last 30 days from M365).
- Stakeholder map with posture annotations.
- Competitive context from the relevant battlecard.
- Recommended approach for the upcoming meeting.
- Pre-loaded objection rebuttals.
- Source citations with confidence tags.

Output as Markdown (default), HTML artifact (interactive, refreshable), Word doc, or PowerPoint slide.

## 10. Quality Gates (orchestrator-enforced)

Before any response sends:

- Source cited for every numeric claim?
- Confidence tagged on every price, percentage, spec?
- Competitive content includes gap-closure strategy?
- Lead with executive impact, not features?
- No competitor recommendation under any framing?
- All UNKNOWN claims verified or explicitly flagged?
- Voice matches `distributor.config.yaml`?

Customer-facing outputs additionally strip internal-only fields (margins, internal notes, partner discount tiers).

## 11. Roadmap (Cross-Reference to Modernization Plan)

| Phase | Status | Deliverable |
|---|---|---|
| 0: Foundation & decisions | Done | Distributor scoping, packaging decision, content slot manifest |
| 1: Plugin skeleton & core refactor | Done — v0.1.1 shipped | Manifest, 8 skills, verifier, slot templates, starter content, public sources |
| 2: Cowork-native artifacts | Partial — v0.2.0/v0.2.1 shipped pipelines + agents | Pipelines + 5-stage agents shipped. HTML live artifacts (battlecard, ROI calculator, dashboards) deferred to v0.3. |
| 2a: IP protection + native rendering | Done — v0.2.5 shipped | BSL license, watermarking, hash baseline, native PDF + PPTX rendering, populated pricing book |
| 2b: QA-fix release | Done — v0.2.6 shipped | Critical agent-frontmatter fix, hash-comparator restored, outline templates shipped, content stubs cover orphan refs, 12 referenced content slots stubbed, packaging cleaned (`__pycache__` and build script no longer ship inside plugin), in-plugin `docs/` directory so onboarding's path refs resolve |
| 2c: Content discovery (Phase 0 of improvement plan) | Done | Three canonical reference YAMLs shipped — aveva-canonical, aveva-regulatory-mapping, aveva-industry-positioning. PHASE-0-DIFF.md catalogs plugin-content drift |
| 2d: Pilot release (Phase 1 + Phase 2 of improvement plan) | Done — v0.3.0 shipped | Regulatory currency refresh (LCRR→LCRI, FSMA 204 extension to 2028-07-20, PHMSA Mega Rule three phases, OOOOb/c with deadline-extension context). AVEVA product naming standardized (Operations Control Edge / Supervisory / Enterprise; PI Vision + CONNECT Visualization dual-tracked). Industrial AI Assistant integrated. AspenTech ownership update + new aspentech.md battlecard. AVEVA-as-Schneider parent reframe across all 5 full battlecards. Honeywell secure-by-design counter. AVEVA + Databricks partnership. Verifier rule for regulatory-claim freshness. |
| 2e: HTML live artifacts | **Done — v0.3.1 shipped** | Four interactive HTML artifacts: `artifacts/roi-calculator.html` (sliders + tier/vertical selectors + 