# aveva-presales-pro

**An AI presales content factory for Schneider Electric direct sellers and AVEVA distributors.**
v0.3.1 — HTML live artifacts release. Adds 4 interactive artifacts (ROI calculator with sliders, content health dashboard, battlecard viewer, briefing dashboard) on top of v0.3.0's regulatory + AI content refresh.

## What this plugin does

Multi-agent pipeline architecture producing six artifact archetypes from one curated content layer:
- **Strategic account briefs** (Baker Hughes archetype) — Tier-1 PDF, 30-50 pages, citation-footnoted
- **Industry sales playbooks** — version-stamped, three-axis-tagged, formal PDF/DOCX
- **Executive customer-facing decks** (MMM Inflection archetype) — PPTX (native render or Gamma-bound)
- **Sales enablement podcasts** (CPG archetype) — Wondercraft script + handoff
- **Quick reference cheat sheets** — 1-page branded PDF
- **Daily-use opportunity briefings** — pulls CRM + meetings + emails + battlecards

Plus persistent per-AE account memory, real-time intelligence routine, win-loss feedback, pipeline health, content health audit.

## What's new in v0.3.1 (current — HTML live artifacts)

Four interactive HTML artifacts now ship in `artifacts/`:

- **ROI calculator (`artifacts/roi-calculator.html`)** — sliders for tag count, site count, OEE baseline/target, labor rate, downtime hours. Tier and vertical selectors load AVEVA Operations Control packages and industry benchmarks. Real-time Year-1 / 3-year / 5-year totals + payback + 5-year ROI %. Confidence-tagged.
- **Content health dashboard (`artifacts/content-health-dashboard.html`)** — KPIs (watermarked files, hash-baseline matches, full vs. stub content), hash-baseline integrity table, per-category slot tables with last_validated freshness pills.
- **Battlecard viewer (`artifacts/battlecard-viewer.html`)** — interactive browser for all 9 competitor cards (5 full + 4 stubs). Audience-signals selector toggles framing per buyer posture. AVEVA Industrial AI Assistant counter on every card.
- **Briefing dashboard (`artifacts/briefing-dashboard.html`)** — connector-aware skeleton. Detects Cowork's MCP tool API; shows green/red per connector (Dynamics, M365, Fireflies, Slack/Teams). Generates structured briefing from live data + manual context fallback.

Five skills wired to their artifacts: `roi`, `content-health`, `competitive`, `briefing`, and the `orchestrator` (which documents the artifact-routing intents).

Snapshot files (`content-health-snapshot.json`, `battlecards-snapshot.json`) regenerated at build time.

## What was new in v0.3.0 (prior — pilot release)

- **Regulatory currency refresh:** Lead and Copper Rule Improvements (LCRI, formerly LCRR) replaces LCRR throughout the water-wastewater playbook; FSMA 204 framing acknowledges the July 20, 2028 extended compliance date; PHMSA Gas Pipeline Mega Rule called out by phase (RIN1/RIN2/RIN3); EPA OOOOa/OOOOb → OOOOb/OOOOc with deadline-extension context.
- **AVEVA Industrial AI Assistant** (GA January 2026) added to the portfolio narrative, key industry playbooks, and competitive battlecards.
- **Operations Control SKU naming** standardized: Edge / Supervisory / Enterprise (replacing legacy "Edge Starter" / "Site Edition" naming).
- **PI Vision (on-prem) and CONNECT Visualization (cloud)** dual-tracked in every industry playbook's Demo section.
- **AVEVA-as-Schneider Electric parent** reframe across all 5 full battlecards (Rockwell, Siemens, Honeywell, Emerson, Ignition). Each battlecard now carries `audience_signals:` for multi-vendor-friendly vs. single-vendor-friendly buyer framing.
- **AspenTech ownership update**: Emerson completed take-private of AspenTech March 12, 2025 ($265/share, $17B). Emerson battlecard updated; new standalone aspentech.md battlecard added.
- **Honeywell secure-by-design counter:** specific certs cited by name (ISO 27001, SOC 2 Type II, ISA/IEC 62443 since 2019, ISASecure SDLA).
- **AVEVA + Databricks partnership** (Manufacturing ISV Partner of the Year 2025) added to portfolio narrative.
- **Three new canonical reference YAMLs** ship with the plugin: `content/aveva-canonical.yaml`, `content/aveva-regulatory-mapping.yaml`, `content/aveva-industry-positioning.yaml` — single source of truth for product names, regulatory state, and AVEVA's own positioning. Phase 0 deliverable from the content improvement plan.
- **New verifier rule:** any claim mentioning a regulation listed in the regulatory-mapping YAML must carry a `last_validated` tag; older than 90 days downgrades to MEDIUM with `[refresh recommended]`.
- **New product files:** `content/products/industrial-ai-assistant.md`, `content/products/connect-visualization.md`.

## What was new in v0.2.6 (prior)

- **Critical: agent frontmatter now parses cleanly.** All 5 pipeline-stage agents (researcher, analyst, writer, verifier, formatter) and the account-memory skill had `<example>` blocks inside their YAML `description:` field that broke `yaml.safe_load`. Removed.
- **Critical: `tools/verify-protected-hashes.py` now actually verifies.** v0.2.5 shipped a copy of the build script in its place, which silently overwrote the baseline. Replaced with a read-only comparator that exits non-zero on drift.
- **Critical: outline templates ship.** The analyst stage of `opportunity-briefing.yaml` and `strategic-account-brief.yaml` referenced `templates/*.yaml` files that didn't exist. Now they do.
- "Aveva" removed from the competitive skill's trigger keyword list (was causing false-positive routing).
- 12 stub files added for previously-orphan content references (3 competitor battlecards, 2 industry playbooks, 5 product positioning pages, 1 competitor-pricing yaml, 1 pptx template).
- `__pycache__` and `build-hash-baseline.py` no longer ship inside the .plugin distribution.
- Cron expression for `biweekly_aveva_github_watch` corrected (was `3/2` which fires Wed/Fri/Sun in standard cron; now fires every Wednesday with an in-prompt parity gate).
- `docs/TESTING-GUIDE.md`, `docs/SPEC.md`, `docs/AS-BUILT.md`, `docs/DEMO-SCRIPT-FOR-FIRST-TESTER.md` now ship inside the plugin so onboarding's references resolve.
- PDF renderer switched to `string.Template` ($var) for safer custom-template handling — distributor templates with literal CSS no longer require brace doubling.
- PDF + PPTX renderers read version from `.claude-plugin/plugin.json` instead of hardcoding it.
- Orchestrator now documents intra-layer routing precedence (pipeline > sub-skill, longest match wins, artifact-format hint breaks ties).
- `pricing_claims_require_high_confidence_for_customer_facing` rule added to verifier in customer-facing pipelines.

## What was new in v0.2.5

- **Native PDF rendering** via `tools/render-pdf.py` (weasyprint) — no more manual Markdown handoff for formal documents
- **Native PPTX rendering** via `tools/render-pptx.py` (python-pptx) — Gamma-style decks even without Gamma license (Mode C)
- **Business Source License 1.1** — see `LICENSE.md`. Free for non-commercial evaluation; commercial use requires separate license. Auto-converts to Apache 2.0 on 2030-04-29.
- **Watermarked protected components** — every Category 3 file carries a unique watermark for tamper detection
- **MODIFICATION-POLICY.md** — explicit list of what's safe to modify, what's care-zone, what's protected
- **Protected-files baseline** — `.protected-files-baseline.json` records SHA-256 of all 26 protected files; quarterly content-health audit detects drift
- **Pricing book with override workflow** — `content/pricing/aveva-current.yaml` ships with publicly-derivable demo pricing; `tools/load-your-pricing.md` walks distributors through replacing it with their actual numbers

## Audience: dual-mode

`distributor.config.yaml.audience.org_type` accepts:
- **`schneider_direct`** — Schneider Electric internal sellers (Baris-style audience)
- **`aveva_distributor`** — AVEVA channel partners (Q-Mation-style)
- **`mixed`** — for co-selling situations

## License

Business Source License 1.1 (BSL). See `LICENSE.md`. TL;DR:

- **Free for non-commercial evaluation, internal research, single-user personal use, and 90-day pilots.**
- **Commercial production use** (revenue-generating sales activity using customer-facing artifacts the plugin produces) **requires a separate commercial license** from the Licensor.
- Auto-converts to Apache 2.0 on 2030-04-29 (4-year Change Date).

## Quick start

1. **Install:** drag-and-drop `aveva-presales-pro-v0.2.5.plugin` into your Cowork tenant.
2. **Onboard:** start a conversation: "set up the plugin for our team." The onboarding skill walks 9 steps in 15-20 min, writes your `distributor.config.yaml`, creates the 12 scheduled tasks, runs initial content-health audit.
3. **Override pricing:** read `tools/load-your-pricing.md`. Replace demo values with your real numbers in `content/pricing/aveva-current.yaml` before any customer-facing quote.
4. **Connect MCPs (optional):** Microsoft Dynamics 365, Microsoft 365, Fireflies, Slack/Teams. Plugin works without them; integrations unlock the briefing pipeline's full value.
5. **Test:** see `TESTING-GUIDE.md` for 6 walkthrough scenarios.

## Modification policy

Three categories, summarized:

- **Category 1 (modify freely):** all `content/` slots, `distributor.config.yaml`, `accounts/{your-ae}/`, brand assets.
- **Category 2 (care zone):** industry skills, custom additions to pipelines, scheduled-tasks.yaml.
- **Category 3 (DO NOT MODIFY):** orchestrator, account-memory, win-loss-loop, content-health, onboarding, portfolio-narrative, strategic-account, deck-generator, enablement-podcast, quick-reference, pipeline-health, all 5 pipeline-stage agents, all 6 built-in pipelines, public-sources.yaml, LICENSE.md, MODIFICATION-POLICY.md.

Modifying Category 3 voids the warranty and the commercial license. See `MODIFICATION-POLICY.md` for the full list and rationale.

## Native renderer dependencies

To use native PDF and PPTX rendering, install:

```
pip install weasyprint markdown pyyaml python-pptx
```

If these are not installed, the formatter agent gracefully falls back to Markdown output and instructions for manual handoff to Gamma / Wondercraft.

## What's NOT in v0.2.5 (v0.3+ stretch)

- Chrome MCP automation for Gamma + Wondercraft (Mode A) — manual handoff (Mode B) and native render (Mode C) work today
- HTML artifacts (live battlecard, ROI calculator with sliders, briefing dashboard, content health dashboard)
- CRM webhook handler (opt-in design documented; wiring is v0.3)
- Pharma + Power-Utilities deep content (skills shipped; full playbook content is fast-follow)

See `SPEC.md` and `AS-BUILT.md` for full design and what shipped.
