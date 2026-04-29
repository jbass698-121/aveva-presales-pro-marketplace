<!--
Copyright (c) 2026 Jason Bass. All rights reserved.
Licensed under the Business Source License 1.1. See LICENSE.md.
Watermark: appro-ca96e5c3-e535-40b4-a502-9e85523f608e
This file is a Category 3 protected component per MODIFICATION-POLICY.md.
-->
---
name: aveva-quick-reference
description: Generates 1-page cheat sheets in the CPG Quick Reference archetype — TLDR table, sub-segments by urgency, 5-question discovery framework, top pain points, ROI elevator pitch, objection cheat sheet, proof points, competitive matrix. Branded PDF, scannable in 60 seconds. Drives the quick-reference pipeline. Activates on cheat-sheet intent (cheat sheet, quick reference, 1-pager, in-meeting reference, scannable summary, sales briefing card).
---

# AVEVA Quick Reference Cheat Sheet

You produce 1-page PDFs designed to scan in 60 seconds while walking into a meeting. Drives the `quick-reference` pipeline.

## When to use

- AE about to walk into a meeting and wants a single-page reference.
- Vertical-specific (CPG, Water, Mining, etc.) or competitor-specific.
- Output target: 1 page PDF, branded, dense but scannable.

For deeper content, use `aveva-strategic-account` (executive Tier-1 brief) or `aveva-briefing` (one-page opportunity brief that pulls live data).

## The CPG Quick Reference archetype

Reference output (`Materials for Baris/AVEVA CPG Sales Quick Reference.pdf`) is 5 pages — but the structure compresses well to 1 page when typeset in a denser layout. The structure:

1. **TLDR** — A "Reality" table with 5 industry-defining metrics.
2. **Sub-segments by urgency** — Pharma > Food&Bev > General CPG, with budget / timeline / deal size / key buyers per row.
3. **Discovery framework** — 5 questions, sized to a 30-min discovery call, with timing per question and "Listen for:" guidance.
4. **Top pain points to probe** — Pain → trigger questions → what to listen for → AVEVA solution table.
5. **ROI elevator pitch** — 2-minute talk track + the numbers (investment, benefits, payback, 3-year ROI).
6. **Objection handling cheat sheet** — Top 5 objections with verbatim responses + proof points.
7. **Proof points** — Customer / industry / challenge / result / ROI table.
8. **Competitive matrix** — AVEVA wins over named competitors per topic.

## Pipeline notes

The quick-reference pipeline skips the analyst stage and goes research → writer → verifier → formatter. The writer uses a fixed 5-section template (`templates/quick-reference-template.md`) and structurally compresses the source playbook.

## Output

Branded 1-page PDF saved to `outputs/quick-references/{topic-slug}-{date}.pdf`. Distributor brand colors and logo applied.
