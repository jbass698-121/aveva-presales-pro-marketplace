<!--
Copyright (c) 2026 Jason Bass. All rights reserved.
Licensed under the Business Source License 1.1. See LICENSE.md.
Watermark: appro-ca96e5c3-e535-40b4-a502-9e85523f608e
This file is a Category 3 protected component per MODIFICATION-POLICY.md.
-->
---
name: aveva-enablement-podcast
description: Generates Wondercraft.ai-optimized podcast scripts for sales enablement audio — two-host conversational format (Alex and Jamie default), segment markers, ~15-min pacing, Q&A flow. Drives the enablement-podcast pipeline with three operating modes (Wondercraft + Chrome MCP, Wondercraft manual handoff, text-only fallback). Activates on podcast intent (enablement podcast, audio briefing, podcast for the team, audio for AEs).
---

# AVEVA Enablement Podcast (Wondercraft-bound)

You produce sales enablement podcasts by invoking the `enablement-podcast` pipeline. Like the deck generator, output format depends on stack:

## Three operating modes

### Mode A: Wondercraft + Chrome MCP (preferred)
1. Pipeline runs through writer → outputs `wondercraft_script` (two-host conversational, segment-marked, ~2,250 words for 15 min at 150 wpm).
2. Formatter drives Chrome to wondercraft.ai/create.
3. Pastes script, configures host pair (Alex / Jamie), triggers generation.
4. Polls for completion (audio render takes 2-5 minutes typical).
5. Downloads MP3 to `outputs/podcasts/`.

### Mode B: Wondercraft manual handoff
When Wondercraft enabled but Chrome MCP not connected:
1. Pipeline runs through writer.
2. Formatter renders handoff: script in copyable block, "Open Wondercraft" link, 4-step instructions, Wondercraft host pair recommendation.
3. User completes manually; MP3 lands in `outputs/podcasts/`.

### Mode C: Text-only script fallback
When Wondercraft is not enabled:
1. Pipeline runs through writer.
2. Formatter saves the script as Markdown with explicit "Audio generation requires Wondercraft license" note.
3. Recommend evaluating Wondercraft in the value-sell artifact.

## When to use this skill

- Sales enablement waves (quarterly enablement, new product launch, major industry inflection).
- AE / SE listening during commute, between meetings, before customer calls.
- Multi-vertical or multi-product topics where reading a 2-page summary is too much friction.

For tactical 1-page reference content, use `aveva-quick-reference`.

## The CPG enablement archetype

Reference output (`Materials for Baris/CPG-Sales-Enablement-AVEVA-EAE-ETAP.pptx` plus matching MP3) follows:

1. **[INTRO]** Hosts welcome, set context, name the topic.
2. **[SEGMENT 1: WHAT'S DRIVING THIS]** Industry inflection (FSMA 204 deadline, OEE gap, sustainability mandate).
3. **[SEGMENT 2: WHAT WE OFFER]** AVEVA + ETAP + EAE + PME unified portfolio for CPG.
4. **[SEGMENT 3: WHO'S WINNING]** Real customer references (Kellogg's, Maple Leaf, Nestlé Powder).
5. **[SEGMENT 4: HOW TO SELL IT]** Discovery questions, top objections, gap-closure offers.
6. **[OUTRO]** Recap, calls to action (ask about FSMA 204, run the OEE assessment).

Use this segment structure as the analyst-stage outline for enablement podcasts.

## Voice and pacing

Conversational. Two hosts trading insights. Real questions, real answers. Avoid jargon dumps. Pause cues for emphasis. ~150 words per minute (so 15 min ≈ 2,250 words).

Default host pair: Alex (lead host, frames topics) and Jamie (subject-matter expert, answers). Configurable in distributor.config.

## Reference files

- `pipelines/enablement-podcast.yaml`
- Existing podcast strategy: `Live MD Files - Optimized/podcast-strategy.md`
- Wondercraft documentation: `tools/wondercraft-integration.md`
