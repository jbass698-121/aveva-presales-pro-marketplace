<!--
Copyright (c) 2026 Jason Bass. All rights reserved.
Licensed under the Business Source License 1.1. See LICENSE.md.
Watermark: appro-ca96e5c3-e535-40b4-a502-9e85523f608e
This file is a Category 3 protected component per MODIFICATION-POLICY.md.
-->
---
name: aveva-deck-generator
description: Generates Gamma.app-optimized markdown for executive decks — H1/H2/H3 hierarchy, --- slide breaks, 30-words-per-bullet max, 6-bullets-per-slide max. Drives the executive-deck pipeline. Output is either an automated render via Gamma + Chrome MCP, a paste-and-go handoff, or a python-pptx native fallback. Activates on deck intent (executive deck, customer presentation, board-level deck, industry inflection deck, slides for {customer / topic}).
---

# AVEVA Executive Deck Generator (Gamma-bound)

You produce executive-quality decks by invoking the `executive-deck` pipeline. The output format depends on what's available in the distributor's stack:

## Three operating modes

### Mode A: Gamma + Chrome MCP (preferred)
When `optional_tools.gamma_app.enabled: true` and Chrome MCP is connected:
1. Pipeline runs through writer → outputs gamma_markdown.
2. Formatter drives Chrome to gamma.app/create.
3. Pastes the markdown.
4. Waits for Gamma to render (poll for completion).
5. Exports to PPTX.
6. Saves to `outputs/executive-decks/`.
7. Surfaces the PPTX file to user.

### Mode B: Gamma manual handoff
When Gamma is enabled but Chrome MCP isn't connected:
1. Pipeline runs through writer.
2. Formatter renders a one-page handoff:
   - Gamma-optimized markdown in a copyable block.
   - One-click "Open Gamma" button.
   - 3-step instructions ("Paste → Generate → Export to PPTX → drop in `outputs/executive-decks/`").
3. User completes the manual steps; PPTX lands in the plugin's outputs.

### Mode C: python-pptx native fallback
When Gamma is not enabled:
1. Pipeline runs through writer.
2. Formatter parses the gamma_markdown into a slide structure (one `---` = slide break).
3. python-pptx renders each slide using the distributor's brand template (`content/brand/pptx-template.pptx` if exists).
4. Lower polish than Gamma but functional.
5. Output: PPTX file.

## When to use this skill

- Audience: customer-facing executive (CEO, CFO, COO, plant GM, public works director).
- Topic: industry inflection (MMM Crisis archetype), digital transformation moment (CPG archetype), or major customer briefing.
- Output target: 20-30 slides, executive narrative arc.

For shorter / tactical content, use `aveva-quick-reference`.
For internal-only material, use `aveva-briefing`.

## The MMM Inflection archetype — what good looks like

Reference output (`Materials for Baris/THE-MMM-CRISIS-MINING-AT-INFLECTION-POINT.pptx`) follows a narrative arc:

1. **The crisis** — declining ore grades, ESG mandate clash, aging workforce, capital constraints
2. **The implication** — fragmentation cost, unplanned downtime cost, reactive maintenance cost
3. **The solution** — AVEVA + ETAP + EAE + PME unified portfolio
4. **The outcome** — verified case studies (MMG, Votorantim, BHP, Rio Tinto)
5. **The call to action** — proposed engagement and next steps

Use this arc as the analyst-stage structure for industry inflection decks.

## Voice and brand

Customer-facing voice. No internal terminology. No PROPOSED-confidence claims. Brand colors and logo from `distributor.config.yaml`.

## Value-sell artifact (for distributors without Gamma)

If the user repeatedly hits Mode C and Gamma value would be high, you can generate the "Why add Gamma to your stack" value-sell document:
- Cost (~$30-100 per AE per month at standard tier)
- Benefit: 80% time reduction on deck creation, executive-quality output
- Recommend a 30-day trial to validate ROI

This is a dedicated artifact the distributor's enablement lead can use to justify the licensing case internally.
