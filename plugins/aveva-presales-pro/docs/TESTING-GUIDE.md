# aveva-presales-pro v0.3.1 — Testing Guide

**For:** anyone evaluating the plugin (sales friend / Q-Mation / Schneider direct)
**Time required:** 30-60 minutes for first-pass evaluation
**What to bring:** a real customer or opportunity name to make scenarios concrete

---

## Before you start — set realistic expectations

**v0.3.1 is the pilot release.** It builds on v0.3.0 (regulatory + AVEVA AI conversation refresh), which itself built on v0.2.6 (a QA-fix on top of v0.2.5; v0.2.5 was the first release with native rendering and BSL licensing). v0.3.1 adds four interactive HTML artifacts (ROI calculator with sliders, content health dashboard, battlecard viewer, briefing dashboard) on top of v0.3.0's content. v0.3.0 added: refreshed regulatory framing (LCRR→LCRI, FSMA 204 compliance extension to July 2028, PHMSA Mega Rule three-phase specificity, OOOOb/OOOOc with deadline-extension context), corrected AVEVA product naming (Operations Control — Edge / Supervisory / Enterprise; PI Vision dual-tracked with CONNECT Visualization), AVEVA Industrial AI Assistant (GA January 2026) integrated into the portfolio narrative + competitive battlecards + industry playbooks, AspenTech-Emerson ownership reflected (since March 2025 take-private), and AVEVA-as-Schneider parent reframe across all 5 full battlecards. About **75% of the design works end-to-end today** (up from 60% in v0.2.0):

- ✅ Skill activation, content generation, voice, three-axis confidence tagging
- ✅ Multi-vertical playbooks (CPG, O&G, Water/WW, Mining, Transportation)
- ✅ Battlecards (5 starter), objection scripts, ROI math, discovery framework
- ✅ Unified AVEVA + ETAP + EAE + PME portfolio narrative
- ✅ **Native PDF rendering** for strategic briefs, industry playbooks, quick references
- ✅ **Native PPTX rendering** for executive decks (Mode C — works without Gamma license)
- ✅ Interactive onboarding with scheduled-task auto-installation
- ✅ Per-AE account memory with retention rules + sensitive data scrub
- ✅ License + modification policy + watermarked protected components
- ✅ **HTML live artifacts** — ROI calculator, content health dashboard, battlecard viewer, briefing dashboard (new in v0.3.1)

About **20% works in degraded mode** without integrations wired:

- ⚠️ Opportunity briefing — needs CRM + Fireflies + M365 MCPs for full fidelity
- ⚠️ Enablement podcast — produces Wondercraft script; you upload manually for MP3 (or accept the script-only output)
- ⚠️ Strategic account brief — content quality dependent on web research; full Tier-1 fidelity is a longer pipeline run

About **5% is documented but not yet running**:

- 🚧 Chrome MCP automation for Gamma + Wondercraft (Mode A) — manual handoff (Mode B) works
- 🚧 CRM webhook real-time event triggers
- 🚧 2023-2025 case study refresh (existing case studies are 2014-2016 vintage)
- 🚧 Full Pharma + Power-Utilities playbook content (stubs ship today)

**Bottom line:** v0.3.1 produces real, polished customer-facing PDFs and PPTXs without manual handoff, plus four interactive HTML artifacts you can use *with* a customer. Content is current to April 2026 (regulatory + AVEVA AI conversation). The content quality is the strongest part. Test it.

---

## Setup (5-10 minutes)

1. **Install the plugin.** Drag-and-drop `aveva-presales-pro-v0.3.1.plugin` into your Cowork tenant.
2. **Run onboarding** *(or skip — see step 2a).* Start a conversation: "set up the plugin for our team." 9 questions in 15-20 minutes. Outputs your `distributor.config.yaml`, creates 12 scheduled tasks, runs initial content-health audit.
3. **2a. Skip onboarding for a quick demo.** Say *"just exploring"* (or *"use the example config"*) — the plugin loads `distributor.config.example.yaml` (Q-Mation defaults) and you can start testing immediately.
4. **(Highly recommended for real use)** Override pricing book per `tools/load-your-pricing.md`. Without your real pricing, ROI demos run on the demo defaults.
5. **(Optional)** Connect MCPs: Microsoft Dynamics 365, Microsoft 365, Fireflies, Slack/Teams.
6. **(For native rendering)** Ensure your Cowork tenant has Python with `weasyprint`, `markdown`, `pyyaml`, `python-pptx` installed. If not, the plugin falls back to Markdown output.

---

## Test Scenario 1 — Single battlecard (~3 min)

**Prompt:** *"Show me the Honeywell battlecard for an upstream O&G opportunity."*

**What you should see:**

- Activation of `aveva-competitive` skill
- Loading of `content/competitors/honeywell.md`
- Structured response: threat profile → product portfolio → AVEVA counter → when we win → when they win → top objections + responses → gap-closure offer
- Three-axis confidence tags on numeric claims
- Distributor's voice block applied (no forbidden phrases)

**Evaluate:** content accuracy; voice fit; gap-closure concreteness.

---

## Test Scenario 2 — Multi-skill chain (~5 min)

**Prompt:** *"I'm walking into a meeting with a 100K-population municipal water utility evaluating AVEVA vs Ignition. Pricing is the lead objection. Brief me."*

**Expected:**

- Industry detection → water-wastewater playbook
- Competitor detection → Ignition battlecard
- Tier sizing → mid-market
- Objection chain → ignition-pricing rebuttal sequence
- Coherent integrated response with reframe → evidence → pivot → gap-closure

**This is the highest-leverage test for water/WW distributors.** Get it right and the value prop is obvious.

---

## Test Scenario 3 — Executive deck (Native PPTX render) (~5 min)

**Prompt:** *"Generate a CPG executive deck on FSMA 204 readiness — 20 slides, customer-facing."*

**Expected:**

- Activation of `aveva-deck-generator` skill, routes to `executive-deck` pipeline
- Pipeline: research → analyst → writer → verifier → formatter
- **Native render produces an actual .pptx file** in `outputs/executive-decks/{topic}-{date}.pptx`
- 20 slides with brand colors, accent bars, consistent typography
- Audience filter applied: no PROPOSED claims, no internal terminology

**If Gamma is licensed in your stack** (set `optional_tools.gamma_app.enabled: true`), the plugin uses Gamma manual handoff (Mode B) for higher polish.

**Quality bar:** open it like a customer would. Does the narrative arc work (problem → implications → solution → outcome → call to action)? Visual quality on par with a Salesforce industry brief or a Deloitte client deck — better, worse, or comparable?

---

## Test Scenario 4 — Enablement podcast script (~5 min)

**Prompt:** *"Build a 15-minute enablement podcast script on the AVEVA + ETAP + EAE + PME unified portfolio for Mining."*

**Expected:**

- Two-host conversational script (Alex + Jamie default)
- Segment markers, Q&A pacing, ~2,250 words
- Real customer references woven in (MMG, Votorantim, BHP)
- Wondercraft handoff message

**If Wondercraft is licensed:** upload, generate MP3. If not: the script alone is a useful enablement asset.

---

## Test Scenario 5 — Quick reference (Native PDF render) (~3 min)

**Prompt:** *"Quick reference cheat sheet for Water Treatment, branded for {your distributor name}."*

**Expected:**

- 5-section structure (TLDR, sub-segments, discovery, pains, ROI, objections, proof points, competitive matrix)
- **Native PDF render** — actual `.pdf` file with brand colors, footer, page numbering
- 1-page or compressed format scannable in 60 seconds

**Quality bar:** if you handed this to a rep walking into a meeting, would they have what they need in 60 seconds? If you handed it to a customer as leave-behind, would it pass the smell test?

---

## Test Scenario 6 — HTML live artifacts (v0.3.1 — ~5-8 min)

Four interactive HTML artifacts ship in `artifacts/`. Try one or two:

**ROI calculator (sliders):** ask the plugin *"open the ROI calculator"* (or *"show me the ROI calculator with sliders"*, *"play with the numbers"*). Should present `artifacts/roi-calculator.html` as a Cowork artifact. Move the sliders for tag count, site count, OEE baseline / target. Watch Year-1 / 3-year / 5-year totals + 5-year ROI % update in real time. Tier (Cost-Conscious / Mid-Market / Enterprise) and vertical (CPG / O&G / Water/WW / Mining / Transportation) selectors load different benchmark sets.

**Battlecard viewer:** ask *"browse the battlecards"* or *"show me the battlecards"*. Should present `artifacts/battlecard-viewer.html`. Pick a competitor; toggle audience-signals (multi-vendor / single-vendor / cost-sensitive / enterprise-inclined) — battlecard framing changes per buyer posture. Note the AVEVA Industrial AI Assistant counter callout on each.

**Content health dashboard:** ask *"show me the content health audit"* or *"content health dashboard"*. Reads `artifacts/content-health-snapshot.json` and renders KPI strip + per-category slot tables with full/stub status and last_validated freshness pills.

**Briefing dashboard:** ask *"open the briefing dashboard for [account]"*. Connector-aware: shows red/green status for Dynamics / M365 / Fireflies. In degraded mode (no connectors), still produces a usable brief from manual context.

**Evaluate:** do the artifacts feel like real interactive tools, or like static templates dressed up? Would your team use them in a meeting?

---

## Test Scenario 7 — Strategic account brief (Tier-1 deep dive) (~10-15 min)

**Prompt:** *"Strategic account brief for [a real Tier-1 customer name from your pipeline]. Four-part Baker Hughes structure."*

**Expected:**

- Pipeline: deep research → multi-source synthesis → 4-part structure → citation footnoting → verification → PDF render
- 4 parts: Market & Industry Analysis (CEO profile, strategic priorities, financial performance) → Schneider/AVEVA Solution Alignment → Executive Engagement Strategy → Financial Analysis & ROI Framework
- **Native PDF render** with footnoted claims, brand cover, page numbers
- ~30-50 pages

**Quality bar:** would a CEO respect this brief walking into a meeting? Are the financial alignment claims footnoted and traceable? Does the four-part structure read as one synthesized brief or four sections stapled together?

**Note on time:** the deep research + multi-source synthesis pipeline can run 10-15 minutes for full Tier-1 fidelity. Shorter prompts (e.g., *"Tier-2 brief, 5-10 pages"*) route to a faster pipeline.

---

## What good looks like

| Output | What "good" feels like |
|---|---|
| Battlecard | Reads like a sales rep wrote it. Win/lose patterns are plausible. Gap-closure offer is concrete enough to actually do in a deal. |
| Multi-skill brief | One coherent narrative — not three articles glued together. Reframe → evidence → pivot → gap-closure flows naturally. |
| Executive deck | Visual quality on par with a Gong customer deck or a Salesforce industry brief. Audience-filter applied (no internal jargon, no PROPOSED claims). |
| Quick reference | Scannable in 60 seconds. AE walking into a meeting has what they need. |
| Account brief | Footnoted claims, traceable sources. Briefing format helps rather than asking the wrong questions. |
| HTML artifact | Feels like a real interactive tool, not a static template dressed up. You'd use it sitting *with* a customer. |

---

## What to evaluate (in priority order)

1. **Content quality (most important).** Would a seller trust the artifact in a meeting? Are claims sourced or honestly tagged as estimates? Does voice match what your team would write?
2. **Workflow fit.** Does routing feel intuitive? Do skills activate when expected? Would AEs use this daily?
3. **Native rendering.** Do PDFs and PPTXs come out clean? Do brand colors apply? Is the layout customer-acceptable?
4. **Content gaps.** What's missing from starter content? Which battlecards / playbooks / case studies need filling first?
5. **License + protection.** Are the modification rules clear? Does watermarking feel intrusive or invisible?

---

## How to send feedback

Five 1-5 ratings plus one open-ended observation is plenty:

1. **Voice (1-5):** does this sound like real sales material?
2. **Trust (1-5):** would you walk into a meeting using this?
3. **Customer-facing (1-5):** would you give the deck/PDF to a customer?
4. **Friction (1-5):** how much rework would a real AE need? (1 = lots, 5 = barely any)
5. **Game-changer (1-5):** if your team had this, would it change how they work?

Plus: one specific moment that worked or fell flat. (*"Try 3 felt canned because…"* type observations are gold.)

Send via Slack / email / voice memo — whatever's easiest.

---

## If something's actually broken

| Symptom | Likely cause | What to do |
|---|---|---|
| Plugin won't install | Cowork tenant doesn't recognize plugin format | Drag the .plugin file directly into the Plugins area — not inside a chat. Send the error if it persists. |
| Plugin installs but doesn't activate on prompts | Skill descriptions not recognized as triggers | Try saying *"load the AVEVA presales plugin"* or *"use the AVEVA assistant"* explicitly. |
| Output is Markdown when expecting PDF/PPTX | Native render dependencies not installed | Run `pip install weasyprint markdown pyyaml python-pptx`. Markdown is still useful for the gut-check. |
| Briefing skill asks for everything manually | CRM / Fireflies / M365 MCPs not connected | Expected for the demo — answer inline. The briefing dashboard shows red status pills for missing connectors so it's transparent. |
| Scheduled tasks aren't running | Onboarding skipped, or task-creation step skipped | Re-run onboarding; or manually create from `scheduled-tasks.yaml`. |
| Some confidence tags missing | Model inconsistency on long outputs | Say *"verify all claims"* — verifier subagent re-tags. |
| ROI numbers feel low-confidence | Demo pricing book in use | Override per `tools/load-your-pricing.md`. |
| Voice doesn't match your team | Default voice is generic | Re-run onboarding step 7; or edit `distributor.config.yaml` voice block. |
| Hash baseline error on install | Tampered files (shouldn't happen on a fresh install) | Re-download and re-install — there shouldn't be any drift in a clean v0.3.1. |

---

*End of testing guide. ~30-60 minutes for first-pass evaluation, including the 5-question feedback. Thank you for taking the time.*
