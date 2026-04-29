# aveva-presales-pro — As-Built Documentation

**Latest version:** v0.3.1 (2026-04-29 — HTML live artifacts release on top of v0.3.0 pilot)
**Phase 0 status:** Done. Three canonical reference YAMLs shipped inside the plugin at `content/aveva-canonical.yaml`, `content/aveva-regulatory-mapping.yaml`, `content/aveva-industry-positioning.yaml`. PHASE-0-DIFF.md cataloging plugin-content drift saved to workspace + plugin's `discovery/` directory.
**Phase 1 + Phase 2 status:** Done — shipped as v0.3.0. Regulatory currency refresh (LCRR→LCRI, FSMA 204 extension to 2028-07-20, PHMSA Mega Rule three phases, OOOOb/c with deadline-extension context), AVEVA product naming (Operations Control Edge / Supervisory / Enterprise; CONNECT Visualization), Industrial AI Assistant integrated, AspenTech ownership update, Schneider parent reframe across all 5 battlecards.
**Companion docs:** SPEC.md (intended design), DESIGN-V2.md (v2 architecture), MODERNIZATION-PLAN-v1.md (full roadmap), TESTING-GUIDE.md (tester walkthrough), DEMO-SCRIPT-FOR-FIRST-TESTER.md (sales-friend onboarding)

## Plugin file artifacts in workspace

| Version | File | Size | Purpose |
|---|---|---|---|
| v0.1.1 | `aveva-presales-pro.plugin` | 90 KB | Original v0.1.1 build — preserved for comparison |
| v0.2.0 | `aveva-presales-pro-v0.2.0.plugin` | 160 KB | First v2 architecture release |
| v0.2.1 | `aveva-presales-pro-v0.2.1.plugin` | 165 KB | Added interactive onboarding skill — **preserved untouched at user's request** |
| v0.2.5 | `aveva-presales-pro-v0.2.5.plugin` | 199 KB | Native rendering + BSL license + watermarking + pricing book |
| v0.2.6 | `aveva-presales-pro-v0.2.6.plugin` | 234 KB | QA-fix release — agent frontmatter parses, hash comparator works, outline templates ship, content stubs cover orphan refs |
| v0.3.0 | `aveva-presales-pro-v0.3.0.plugin` | 269 KB | Pilot release. Regulatory currency refresh + AVEVA product naming + Industrial AI Assistant + AspenTech update + Schneider parent reframe + 3 canonical reference YAMLs. |
| **v0.3.1** | **`aveva-presales-pro-v0.3.1.plugin`** | **300 KB** | **Latest. HTML live artifacts: ROI calculator (sliders, real-time computation), content health dashboard (KPIs + slot-by-slot status), battlecard viewer (audience-signals selector), briefing dashboard (connector-aware skeleton). 5 skills wired to their artifacts.** |

## What v0.3.1 delivers vs. v0.3.0 (the latest delta — HTML live artifacts)

v0.3.1 is content-additive on top of the v0.3.0 pilot. Four interactive HTML artifacts now ship in `artifacts/`. Each is self-contained (no external CDN), persists user input via localStorage, and either runs standalone or activates Cowork's `window.cowork.callMcpTool()` API when connectors are wired.

- **`artifacts/roi-calculator.html`** — interactive ROI/TCO calculator. Sliders for tag count, site count, OEE baseline / target, labor rate, downtime hours. Tier selector (Cost-Conscious / Mid-Market / Enterprise) maps to current AVEVA Operations Control packages. Vertical selector loads industry-specific benchmarks (CPG, O&G, Water/WW, Mining, Transportation). Real-time Year-1 / 3-year / 5-year totals with payback period and 5-year ROI %. Confidence tags on every claim (pricing MEDIUM by default; HIGH when distributor pricing book overrides).
- **`artifacts/content-health-dashboard.html`** — content audit dashboard. KPI strip (watermarked files, hash-baseline matches, full vs. stub content counts). Hash-baseline integrity table — all-green pass or per-file drift listing. Per-category content slot tables (industry playbooks, battlecards, case studies, objections, products, pricing, discovery, canonical references) with full/stub status and last_validated freshness pills (green <90d, yellow <365d, red older). Reads `artifacts/content-health-snapshot.json` regenerated at build time.
- **`artifacts/battlecard-viewer.html`** — interactive battlecard browser. Picker for all 9 competitor cards (5 full + 4 stubs); audience-signals selector toggles framing per buyer posture (multi-vendor / single-vendor / cost-sensitive / enterprise-inclined). Each card surfaces: threat tier, verticals, "their AI offering" with AVEVA Industrial AI Assistant counter, recent corporate change banner (e.g., AspenTech-Emerson), Cybersecurity counter section (Honeywell), full body sections collapsible, sources with click-to-open.
- **`artifacts/briefing-dashboard.html`** — opportunity briefing dashboard with connector-aware skeleton. Detects Cowork's MCP tool API at load; shows green/red status per connector (Microsoft Dynamics 365, M365, Fireflies, Slack/Teams). "Full mode" / "Partial mode" / "Degraded mode" alert sets seller expectations. Form for account / vertical / competitor / tier / meeting date + manual context fallback. Generates structured one-page brief with what-the-customer-cares-about, recent activity (live or manual), competitive context, recommended solution (tier-aligned), 5-step recommended approach, sources / next actions.

**Skills wired to artifacts:**
- `skills/roi/SKILL.md` knows about roi-calculator.html and offers it on interactive-ROI intent.
- `skills/content-health/SKILL.md` offers content-health-dashboard.html on visual-audit intent.
- `skills/competitive/SKILL.md` offers battlecard-viewer.html on browse-battlecards intent.
- `skills/briefing/SKILL.md` offers briefing-dashboard.html when user wants something refreshable.
- `skills/orchestrator/SKILL.md` documents the artifact-routing intents (the 4 patterns that map to each artifact).

**Snapshots:**
- `artifacts/content-health-snapshot.json` (regenerated at build time from the actual file tree)
- `artifacts/battlecards-snapshot.json` (regenerated at build time from the 9 competitor MD files)

**Briefing dashboard scope clarification:**
The briefing dashboard ships as a connector-aware skeleton because v0.3.1 is content-additive — connector wiring (Dynamics, Fireflies, M365) is environment-specific and lives in your Cowork tenant configuration, not the plugin. Once those MCPs are connected, the dashboard's "Full mode" path activates automatically; until then, "Degraded mode" still produces a usable brief from manual context.

## What v0.3.0 delivered vs. v0.2.6 (prior delta — pilot release)

v0.3.0 is the pilot release built on the content improvement plan. Phase 0 (docs.aveva.com discovery) preceded it; Phase 1 (regulatory + naming truth) and Phase 2 (AI + competitive freshness) were combined into this single release because Phase 2 on stale Phase 1 content would have been a worse plugin.

**Phase 0 outputs (reference data, no architectural change)**
- `content/aveva-canonical.yaml` — single source of truth for product names, current SKUs, AI capabilities, security certifications, partner pillars (ETAP / EAE / PME), partnership context (Databricks), Schneider parent context. 22 source URLs cited.
- `content/aveva-regulatory-mapping.yaml` — current state of every regulation referenced in the plugin: LCRI (Lead and Copper Rule Improvements, Oct 2024 final, 2027-11-01 compliance), FSMA 204 (extended to 2028-07-20), PHMSA Mega Rule three phases, OOOOb/c with all extension context, AWIA, CIRCIA, ISA/IEC 62443, etc.
- `content/aveva-industry-positioning.yaml` — AVEVA's official per-industry positioning, used as the credibility floor.
- `discovery/PHASE-0-DIFF.md` — diff between plugin content and canonical truth, severity-ranked. Drove Phase 1 + 2 work.

**Regulatory currency**
- `LCRR` → `LCRI` throughout water-wastewater playbook, discovery questions, and skill bodies. Parenthetical "(formerly LCRR)" retained for muscle-memory cycle. Compliance date Nov 1 2027 named explicitly; 10-year service line replacement detail surfaced.
- FSMA 204: original Jan 20 2026 compliance acknowledged + extended to **July 20, 2028** per Congressional directive. Two-track talk track (compliant program / using extension).
- PHMSA generic 49 CFR 192/195 → specific Gas Pipeline Mega Rule with three phases (RIN1 effective Jul 2020, RIN2 May 2023, RIN3 May 2023). Discovery questions and oil-gas playbook updated.
- EPA OOOOa/OOOOb → OOOOb/OOOOc with deadline-extension context (first OOOOb annual report due no earlier than 2026-11-30; state plans 2027-01-22).

**AVEVA product nami