# aveva-presales-pro — As-Built Documentation

**Latest version:** v0.3.2 (2026-06-03 — bug-fix + 2026-H1 content-refresh release on top of v0.3.1 HTML live artifacts)
**Distribution:** Personal GitHub marketplace at https://github.com/jbass698-121/aveva-presales-pro-marketplace (added 2026-04-29 after Cowork's local upload UI was confirmed broken — see Distribution Architecture below)
**Phase 0 status:** Done. Three canonical reference YAMLs shipped inside the plugin at `content/aveva-canonical.yaml`, `content/aveva-regulatory-mapping.yaml`, `content/aveva-industry-positioning.yaml`. PHASE-0-DIFF.md cataloging plugin-content drift saved to workspace + plugin's `discovery/` directory.
**Phase 1 + Phase 2 status:** Done — shipped as v0.3.0. Regulatory currency refresh (LCRR→LCRI, FSMA 204 extension to 2028-07-20, PHMSA Mega Rule three phases, OOOOb/c with deadline-extension context), AVEVA product naming (Operations Control Edge / Supervisory / Enterprise; CONNECT Visualization), Industrial AI Assistant integrated, AspenTech ownership update, Schneider parent reframe across all 5 battlecards.
**Companion docs:** SPEC.md (intended design), DESIGN-V2.md (v2 architecture), MODERNIZATION-PLAN-v1.md (full roadmap), TESTING-GUIDE.md (tester walkthrough), DEMO-SCRIPT-FOR-FIRST-TESTER.md (sales-friend onboarding)

## What v0.3.2 delivers vs. v0.3.1 (the latest delta — bug-fix + 2026-H1 content refresh)

v0.3.2 closes the gaps found in the 2026-06-03 gap/bug audit (`GAP-AND-BUG-ANALYSIS-v0.3.1.md`) and brings reference material current to 2026 H1. No architectural change; the skeleton (22 skills, 5 agents, 6 pipelines, 4 artifacts) is unchanged.

**Bug fixes**
- **Regulatory currency reached the skill bodies (HIGH-1).** v0.3.0 refreshed the `content/` playbooks but left the *skill bodies* stale — they still said "LCRR effective 2024–2027" and "FSMA 204 effective January 2026," contradicting the canonical `aveva-regulatory-mapping.yaml`. Fixed in `skills/industry-water-wastewater/SKILL.md` (LCRI / formerly LCRR, Nov 1 2027 compliance, 10-yr LSL replacement), `skills/discovery/SKILL.md`, and `skills/industry-cpg/SKILL.md` (FSMA 204 → July 20 2028, two-track).
- **HTML artifacts are now genuinely self-contained (HIGH-2).** `battlecard-viewer.html` and `content-health-dashboard.html` previously `fetch()`-ed a sibling snapshot JSON, which fails when rendered via Cowork's `create_artifact` (a single self-contained HTML page — no sibling file to fetch). Both now inline their snapshot at build time between `/*__SNAPSHOT_INLINE_START__*/ … /*__SNAPSHOT_INLINE_END__*/` markers; the `fetch()` calls are removed. (ROI calculator + briefing dashboard already inlined and were unaffected.)
- **Battlecard count corrected** to 6 full + 3 stub (AspenTech is a full card; prose previously said "5 full + 4 stub"). `skills/onboarding/SKILL.md` updated.

**2026 H1 reference updates** (verified, with sources + confidence; full record in `content/whats-new-2026H1.md` and `recent_developments_2026:` in `aveva-canonical.yaml`)
- **Regulatory contradictions corrected** in `aveva-regulatory-mapping.yaml`: EPA methane **Waste Emissions Charge repealed** (CRA; Part 99 revoked) and **OOOOb/OOOOc materially weakened** (2026 reconsideration rule, eff. 2026-06-08) → posture shifted from "federal mandate" to operator-elected / state-driven; **PHMSA 2025 LDAR final rule withdrawn** (no current LDAR deadline; RIN1–3 remain in effect); FSMA 204 strengthened to a statutory enforcement bar + FDA lot-level-traceability re-examination; LCRI litigation-watch (AWWA v. EPA, oral argument Fall 2026) with Nov 1 2027 confirmed; AWIA 2026-06-30 recertification; CIRCIA final-rule status flagged unverified.
- **Competitor cards refreshed** (`competitors/`): Emerson **AspenTech AVA** agentic-AI launch (2026-05-11); Ignition **8.3 LTS** (through 8.3.6, Apr 2026; "no 8.5"); Rockwell FactoryTalk edge GenAI (Nemotron Nano, Design Studio AI Copilot, ResilientEdge); Honeywell Q1 2026 reorg (Process Automation and Technology segment; aerospace spin-off ~2026-06-29).
- **AVEVA product news** (`aveva-canonical.yaml`, `whats-new-2026H1.md`): AVEVA World 2026 (CONNECT + Snowflake/ServiceNow, Flows via Crosser, knowledge graph + agentic twin builder, MCP roadmap, Operations Control unified visualization from June 2026, PI Audit Reporter), AVEVA Unified Engineering AI (2026-01-14), Microsoft Customer-Hosted SaaS. Unverified items (System Platform point-release number; NVIDIA Nemotron is Rockwell not AVEVA) explicitly flagged `unverified_do_not_assert`.

**Tooling + hygiene**
- Added **`build.py`** (marketplace repo root): one command bumps version in plugin.json + marketplace.json, regenerates both snapshots from the file tree / competitor frontmatter, **inlines** them into the artifacts, and recomputes `.protected-files-baseline.json`. Replaces the manual multi-step release that caused drift.
- **Hash baseline regenerated** at v0.3.2 (26/26 OK, includes the edited onboarding skill + new plugin.json).
- **In-plugin `docs/` synced** to the canonical workspace SPEC.md / AS-BUILT.md (they had drifted to 199-line / 58-line stale copies).
- Inventory deltas: watermarked files now **45** (added `whats-new-2026H1.md`); new dev tool `build.py` lives at repo root (not shipped inside the plugin payload).

**Still pending (unchanged):** Phase 3 MCP integration (Dynamics/M365/Fireflies) — the briefing dashboard remains a connector-aware skeleton until those are wired, so SPEC §13 acceptance criterion #2 (live briefing data) is still not met.

## Distribution Architecture (current — added 2026-04-29)

**Primary install path: Personal GitHub Marketplace.**

The plugin lives in a public GitHub repo: **https://github.com/jbass698-121/aveva-presales-pro-marketplace**. Users install in Cowork via:

> Browse plugins → Personal tab → + Add marketplace from GitHub → `jbass698-121/aveva-presales-pro-marketplace` → Sync → Install on the `aveva-presales-pro` entry.

**Repo structure:**

```
.claude-plugin/marketplace.json       — marketplace registration
plugins/aveva-presales-pro/           — the plugin itself
  .claude-plugin/plugin.json          — plugin manifest (name, version, author, license)
  skills/                             — 22 skills
  agents/                             — 5 pipeline-stage agents
  artifacts/                          — 4 HTML live artifacts
  content/, pipelines/, templates/, tools/, docs/
  scheduled-tasks.yaml, distributor.config.example.yaml
  LICENSE.md, MODIFICATION-POLICY.md, README.md
README.md                             — top-level marketplace README
```

**marketplace.json required schema** (Cowork's validator is strict here):

- `name` (string) — must match the repo name
- `owner` (object with `name` field) — string-form `owner` is rejected
- `plugins` (array) — each entry needs `name`, `description`, `version`, `source` (relative path string from marketplace.json's location)

**Iteration workflow:**

1. Edit files locally in `local-marketplace/plugins/aveva-presales-pro/...`
2. Bump `version` in both `plugins/aveva-presales-pro/.claude-plugin/plugin.json` AND `.claude-plugin/marketplace.json`'s plugin entry
3. `git push origin main` — Cowork polls GitHub on focus; users see Update button when version changes
4. Users click Update; new version pulls down

**OneDrive caveat:** the working `.git/` cannot live inside an actively-syncing OneDrive folder — OneDrive locks `.git/objects/` mid-write. Either pause OneDrive sync before each push session, or move the working git copy to a non-OneDrive folder (e.g., `C:\repos\aveva-presales-pro-marketplace`).

**Why GitHub marketplace, not local upload:**

Cowork's local upload UI (`Customize → Personal plugins → + → Upload plugin`) is broken on Windows for user-built plugins as of 2026-04-29. The "plugin validation failed" toast fires regardless of file extension (.plugin OR .zip), structure (full plugin OR aggressively-stripped to mirror Anthropic's Operations / HR plugins exactly), or content. No log entry is written for the rejection (`main.log` shows `[LocalPluginsReader] Found 0 enabled local plugins (0 installed)`; `claude.ai-web.log` has zero matches for plugin/validation/upload/zip/manifest). Tracked as open Anthropic GitHub issues:

- **#24328** — `getPlugins` schema validation bug (the underlying blocker)
- **#40414** — Windows: `.plugin` extension rejected; `.zip` rename claimed to fix but did not in our build
- **#28337** — same root cause as #40414, marked stale
- **#42651** — macOS variant
- **#40600** — Personal-marketplace installs sometimes don't persist across Claude Desktop restarts (workaround: click Install again in marketplace UI)
- **#38185** — Personal tab can fail to load on macOS (not blocking on Windows)

The personal-GitHub-marketplace path bypasses the broken upload UI entirely and works on Cowork Pro (no Team/Enterprise required).

## Historical plugin file artifacts in workspace

These are the historical .plugin file builds, preserved for archival comparison. **None are in active use** — distribution moved to GitHub marketplace at v0.3.1. The current source of truth is the GitHub repo.

| Version | File | Size | Purpose |
|---|---|---|---|
| v0.1.1 | `aveva-presales-pro.plugin` | 90 KB | Original v0.1.1 build — preserved for comparison |
| v0.2.0 | `aveva-presales-pro-v0.2.0.plugin` | 160 KB | First v2 architecture release |
| v0.2.1 | `aveva-presales-pro-v0.2.1.plugin` | 165 KB | Added interactive onboarding skill — **preserved untouched at user's request** |
| v0.2.5 | `aveva-presales-pro-v0.2.5.plugin` | 199 KB | Native rendering + BSL license + watermarking + pricing book |
| v0.2.6 | `aveva-presales-pro-v0.2.6.plugin` | 234 KB | QA-fix release — agent frontmatter parses, hash comparator works, outline templates ship, content stubs cover orphan refs |
| v0.3.0 | `aveva-presales-pro-v0.3.0.plugin` | 269 KB | Pilot release. Regulatory currency refresh + AVEVA product naming + Industrial AI Assistant + AspenTech update + Schneider parent reframe + 3 canonical reference YAMLs. |
| **v0.3.1** | `aveva-presales-pro-v0.3.1.plugin` + `aveva-presales-pro-v0.3.1.zip` | 300 KB | HTML live artifacts release. **The .plugin / .zip files are kept in `Pilot Phase 0 Package/` as a fallback only — Cowork's local upload UI rejects them (see Distribution Architecture above). Active distribution is the GitHub marketplace.** |

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

**AVEVA product naming**
- Operations Control SKU naming standardized to canonical: **Edge / Supervisory / Enterprise** (replaces "Operations Control Edge Starter" / "Operations Control Site Editions"). Updated across all 5 industry playbooks, ROI skill, orchestrator, onboarding skill, water-wastewater skill body, Ignition objection script, Rockwell incumbency objection, pricing book.
- PI Vision (on-prem) and CONNECT Visualization (cloud) dual-tracked in every industry playbook's Demo section.
- Schneider acquisition completion date corrected: January 18, 2023 (not 2024 as a prior assumption). Phrasing standardized: "AVEVA, part of Schneider Electric" (canonical); "AVEVA + Schneider partnership" forbidden.

**AI + competitive freshness**
- New `content/products/industrial-ai-assistant.md` — captures GA Jan 2026, capability set, related AI products (Generative Design, Predictive Design, Intelligent Point Cloud), competitive AI matrix.
- New `content/products/connect-visualization.md` — captures CONNECT Visualization vs. PI Vision deployment guidance, embedded AI host.
- New `content/competitors/aspentech.md` — full battlecard reflecting Emerson's March 12, 2025 take-private of AspenTech ($265/share, $17B). AVEVA SimSci competitive comparison restored.
- All 5 full battlecards (Rockwell, Siemens, Honeywell, Emerson, Ignition) now have:
  - `audience_signals:` block in front-matter (multi-vendor-friendly vs. single-vendor-friendly framing)
  - `their_AI_offering:` field (Rockwell FactoryTalk Copilot + NVIDIA Nemotron, Siemens Industrial Copilot, Honeywell Forge AI + Quantinuum, Emerson + AspenTech AI, Ignition Vision module)
  - "AVEVA, part of Schneider Electric" framing in AVEVA Counter-Strategy section
- Honeywell battlecard: new "Cybersecurity counter (Honeywell secure-by-design / Quantinuum)" section citing AVEVA's specific certs (ISO 27001, SOC 2 Type II, ISA/IEC 62443 since 2019, ISASecure SDLA).
- Ignition objection script: cybersecurity pivot now cites the same specific certs by name with date verified.
- Emerson battlecard updated for AspenTech ownership (no more "via partnership" language).
- Portfolio narrative skill: AI competitive matrix added; Industrial Intelligence Platform framing; AVEVA + Databricks partnership section added (Manufacturing ISV Partner of the Year 2025; Delta Sharing).
- Orchestrator skill: opening rephrased as "AVEVA, part of Schneider Electric — the Industrial Intelligence Platform with the only unified portfolio..."

**Verifier rule**
- `agents/verifier.md` adds a regulatory-currency rule. Any claim mentioning a regulation listed in the regulatory-mapping YAML (LCRR, LCRI, FSMA 204, OOOOa/b/c, PHMSA Mega Rule, AWIA, etc.) must carry a `last_validated` tag; if older than 90 days, claim downgrades to MEDIUM with `[refresh recommended]` note.

**QA**
- QA Expert subagent reviewed the v0.3.0 build before final ship. Found 1 Critical (YAML escape error in honeywell.md + emerson.md), 1 High (residual obsolete SKU names in 6 files), 1 Medium-High (Industrial AI Assistant missing from 4 industry playbooks). All resolved before this AS-BUILT entry. QA report saved to workspace at `QA-REPORT-v0.3.0.md`.

## What v0.2.6 fixed vs. v0.2.5 (prior delta)

QA-driven fix release. No new features — three Critical and six High defects from the v0.2.5 audit are resolved.

**Critical fixes**
- Removed `<example>` blocks from the YAML `description:` field on all 5 pipeline-stage agents and the `account-memory` skill. v0.2.5 shipped with invalid frontmatter that PyYAML rejected — the entire pipeline architecture would have failed to load.
- Rewrote `tools/verify-protected-hashes.py` as a read-only comparator. v0.2.5 shipped a verbatim copy of the build script in its place, which silently overwrote the baseline rather than verifying it.
- Added `templates/opportunity-briefing-outline.yaml` and `templates/strategic-account-outline.yaml` so the analyst stage of those two pipelines has the structures it references.

**High fixes**
- Removed "Aveva" from the competitive skill's competitor-name trigger list.
- Added stub files for 12 previously-orphan content references (3 competitor battlecards, 2 industry playbooks, 1 competitor-pricing yaml, 5 product positioning files, 1 pptx template).
- Excluded `__pycache__/` and `build-hash-baseline.py` from the .plugin distribution (build script lives in workspace, not in the install).
- Cron expression `0 8 * * 3/2` (which fires Wed/Fri/Sun in standard cron) replaced with `0 8 * * 3` plus an in-prompt biweekly parity gate.
- `docs/TESTING-GUIDE.md`, `docs/SPEC.md`, `docs/AS-BUILT.md`, `docs/DEMO-SCRIPT-FOR-FIRST-TESTER.md` ship inside the plugin so the onboarding skill's path references resolve at install location.
- AS-BUILT inventory counts re-derived from the actual file tree (see "Total v0.2.6 inventory" below).

**Selected Medium / Low fixes**
- `tools/render-pdf.py` switched from `str.format()` to `string.Template` for safer custom-template handling — distributors no longer need to double-escape CSS braces.
- Both renderers read version from `.claude-plugin/plugin.json` instead of hardcoding it.
- Dead import (`from pptx.shapes.autoshape import Shape`) removed from `render-pptx.py`.
- Orchestrator now documents intra-layer routing precedence (pipeline > sub-skill, longest match wins, artifact-format hint breaks ties).
- `pricing_claims_require_high_confidence_for_customer_facing` rule added to verifier in customer-facing pipelines (executive-deck, strategic-account-brief, quick-reference).

## What v0.2.5 added vs. v0.2.1 (prior delta)

### IP protection scaffolding (Category 1 of v0.2.5 spec)
- **`LICENSE.md`** — Business Source License 1.1. Free for non-commercial / evaluation / 90-day pilots. Commercial production use requires separate license. Auto-converts to Apache 2.0 on 2030-04-29 (Change Date).
- **`MODIFICATION-POLICY.md`** — explicit three-category framework. Category 1 (modify freely): config + content slots. Category 2 (care zone): industry skills, pipelines, scheduled tasks. Category 3 (protected): orchestrator, memory, win-loss, content-health, onboarding, portfolio, all 6 pipelines, all 5 agents, public-sources, license, modification-policy.
- **Watermark identifier:** `appro-ca96e5c3-e535-40b4-a502-9e85523f608e` embedded in 38 protected files (every Category 3 file plus key Category 2 files). Removal voids license per BSL terms.
- **Copyright headers:** every SKILL.md, agent.md, pipeline.yaml, and Category 3 YAML carries a 4-line copyright/license/watermark/policy block. Signals provenance and detects tampering.
- **`.protected-files-baseline.json`** — SHA-256 hash of all 26 Category 3 files at v0.2.5 release. The quarterly content-health audit task computes current hashes and reports drift.
- **`tools/verify-protected-hashes.py`** — distributor-runnable hash audit script.

### Native rendering (Category 2 of v0.2.5 spec)
- **`tools/render-pdf.py`** — weasyprint-based PDF rendering. Reads pdf-ready Markdown, applies brand template (`content/brand/pdf-template.html`), produces customer-ready PDF with brand colors, footnoting, page numbers, cover page. Used by formatter agent for strategic-account-brief, industry-playbook, quick-reference pipelines.
- **`tools/render-pptx.py`** — python-pptx-based PPTX rendering. Parses gamma-optimized Markdown (one `---` = slide break), produces 16:9 PPTX with brand accent bars, consistent typography, distributor footer. Mode C fallback when Gamma is not licensed.
- **`content/brand/pdf-template.html`** — default PDF template; distributors override with custom HTML if they want.
- **README.md** updated with `pip install weasyprint markdown pyyaml python-pptx` dependency note.

### Pricing book + override workflow (Category 3 of v0.2.5 spec)
- **`content/pricing/aveva-current.yaml`** — populated with publicly-derivable AVEVA list pricing (InTouch Unlimited, Operations Control Edge tiers, System Platform concurrent-user pricing, PI System, MES, Connect data services, Modicon hardware, Altivar drives, regional adjustments, partner discount tiers). Every value tagged with confidence (mostly MEDIUM, LOW where customer-specific). Marked clearly as illustrative; distributor must override before customer-facing use.
- **`tools/load-your-pricing.md`** — comprehensive override runbook. Three options (direct edit, layered override per region, future spreadsheet sync). Priority order for which products to override first. Confidence-tagging guidance. Privacy reminder. Update cadence recommendation.

### Manifest + dependencies
- Bumped to `v0.2.5`
- Added `"license": "BUSL-1.1"` field
- README updated with v0.2.5 highlights and license positioning

## Total v0.2.6 inventory

Counts derived from the actual file tree at release time.

- **95 files** in source tree (vs. 81 in v0.2.5)
- **234 KB** packaged size (vs. 199 KB v0.2.5)
- **44 watermarked files** (was 41 in v0.2.5; the 3 new template/stub additions inherit the watermark)
- **26 hashed protected files** in baseline (unchanged)
- **22 skills** — full list:
  - Cross-cutting: orchestrator, portfolio-narrative
  - Producer skills: deck-generator, enablement-podcast, quick-reference, strategic-account
  - Tactical / Q&A: competitive, roi, briefing, discovery
  - Operational: account-memory, content-health, pipeline-health, win-loss-loop, onboarding
  - Industry skills (7): industry-cpg, industry-oil-gas, industry-water-wastewater, industry-mining-metals, industry-transportation, industry-pharma, industry-power-utilities
- **5 pipeline-stage agents** (researcher, analyst, writer, verifier, formatter)
- **6 pipelines** (opportunity-briefing, strategic-account-brief, industry-playbook, executive-deck, enablement-podcast, quick-reference)
- **2 analyst outline templates** (opportunity-briefing-outline.yaml, strategic-account-outline.yaml) — new in v0.2.6
- **12 scheduled tasks** auto-installable (cron for biweekly task corrected)
- **5 full starter battlecards** + **3 stub battlecards** (Rockwell, Honeywell, Siemens, Emerson, Ignition full; ABB, GE Digital, Trihedral VTScada stubs added in v0.2.6)
- **5 full industry playbooks** + **2 stub playbooks** (CPG, oil-gas, water-wastewater, mining-metals-minerals, transportation full; pharma-life-sciences, power-utilities stubs added in v0.2.6)
- **6 starter case studies** (MMG, Votorantim, BHP Escondida, Kellogg's, Maple Leaf Foods, SCG Chemicals)
- **2 starter objection scripts** (Ignition pricing, Rockwell incumbency)
- **5 product positioning stubs** + **1 full** (flex-subscription full; aveva-pi-system, aveva-system-platform, ecostruxure-automation-expert, etap, power-monitoring-expert stubs added in v0.2.6)
- **4 in-plugin docs** (TESTING-GUIDE.md, SPEC.md, AS-BUILT.md, DEMO-SCRIPT-FOR-FIRST-TESTER.md — moved into `docs/` so the onboarding skill's path references resolve)
- **Tools** (3 Python scripts + 4 markdown integration docs): render-pdf.py (now uses string.Template; reads version from manifest), render-pptx.py (dead import removed; reads version from manifest), verify-protected-hashes.py (now a real comparator), gamma-integration.md, wondercraft-integration.md, data-subject-request.md, load-your-pricing.md
- **Build-only script** kept *outside* the plugin tree: `build-hash-baseline.py` (workspace only)

## Acceptance Criteria — v0.2.5 status

| Criterion | Status |
|---|---|
| Native PDF renders strategic briefs and quick references | ✅ |
| Native PPTX renders executive decks (Mode C fallback) | ✅ |
| Business Source License applied with watermarked protected files | ✅ |
| MODIFICATION-POLICY enforces three-category framework | ✅ |
| Pricing book ships populated; override workflow documented | ✅ |
| All v0.2.1 functionality preserved (skills, pipelines, agents, content) | ✅ |
| v0.2.1 plugin file preserved untouched for comparison | ✅ |
| README + TESTING-GUIDE updated for v0.2.5 | ✅ |
| Demo script for first tester (sales friend) provided | ✅ |
| Hash baseline computed for protected files | ✅ |

## What's NOT in v0.2.5 (next version targets)

- Chrome MCP automation for Gamma + Wondercraft (Mode A) — stretch v0.2.6 or v0.3
- HTML live artifacts (battlecard refresh, ROI calculator with sliders, briefing dashboard, content health dashboard) — v0.3 priority
- CRM webhook real-time event handler — v0.3, opt-in
- Pharma + Power-Utilities deep playbook content — v0.3, ports from existing material
- Additional starter battlecards (ABB, Yokogawa, GE Digital, Trihedral VTScada, Werum PAS-X, Aspen) — v0.3
- Hosted-service architecture for stronger IP protection — v0.4 (decision pending pilot results)

## Testing readiness — v0.2.5

Per the user's design-partner sequencing:

1. **First tester (sales friend) — sequenced first.** Demo script at `DEMO-SCRIPT-FOR-FIRST-TESTER.md`. Goal: validate that outputs *look like real sales material* without needing AVEVA domain expertise. 5 scenarios in 30-45 min. Five-question feedback form built into the script.
2. **Q-Mation** — design partner pilot, after sales-friend feedback is incorporated. TESTING-GUIDE.md is the walkthrough document.
3. **Baris (Schneider direct)** — secondary validation, after Q-Mation. Same TESTING-GUIDE applies; demo can use `audience.org_type: schneider_direct` config.

## Files delivered in workspace

See the workspace `Cowork SDA/` tree and the active distribution repo
`github.com/jbass698-121/aveva-presales-pro-marketplace` (public; mirrors
`local-marketplace/`, pushed via git). v0.3.2 adds `build.py` at the repo root
(one-command release) and `content/whats-new-2026H1.md`.

*End of AS-BUILT.md.*
