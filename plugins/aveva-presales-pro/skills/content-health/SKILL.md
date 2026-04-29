<!--
Copyright (c) 2026 Jason Bass. All rights reserved.
Licensed under the Business Source License 1.1. See LICENSE.md.
Watermark: appro-ca96e5c3-e535-40b4-a502-9e85523f608e
This file is a Category 3 protected component per MODIFICATION-POLICY.md.
-->
---
name: aveva-content-health
description: Content pack audit — reports completeness, freshness, and gaps in the distributor's BYOC content. Generates a Health Score per slot and an aggregate score. Runs quarterly automatically and on demand. Activates on content-health intent (content audit, content health check, what content is stale, what's missing, content pack review, audit my content).
---

# AVEVA Content Pack Health Audit

Audits the distributor's BYOC content pack and reports gaps.

## What it audits

**Per slot, four checks:**

1. **Existence.** Does the file exist in the expected slot?
2. **Freshness.** When was the file last validated (per its `last_validated:` frontmatter field)?
3. **Cross-references.** Does the file reference other content correctly?
4. **Quality signals.** Word count, section completeness against template, confidence-tag density.

**Per slot, four states:**

- **GREEN:** Exists, fresh (≤90 days), no broken cross-refs, complete sections.
- **YELLOW:** Exists, but stale (>90 days) OR missing 1-2 sections OR has broken cross-ref.
- **ORANGE:** Exists but very stale (>180 days) OR has many broken refs OR has un-tagged numeric claims.
- **RED:** Missing, expected to be present, blocking pipeline degradation.

## What it produces

```
Content Pack Health — Q-Mation — 2026-04-29
═════════════════════════════════════════════════════════

Aggregate Health Score: 72 / 100

By Slot:
GREEN (8): industries/water-wastewater.md, industries/cpg.md, ...
YELLOW (4): pricing/aveva-current.yaml [120 days old], objections/ignition-pricing.md [104 days]...
ORANGE (1): competitors/yokogawa.md [220 days, missing 2 sections]
RED (3): industries/pharma-life-sciences.md [missing], competitors/abb.md [missing], pricing/competitors.yaml [missing]

Critical gaps (block customer-facing artifacts):
- pricing/aveva-current.yaml is 120 days old — ROI math degrades to ranges
- competitors/abb.md missing — O&G upstream playbook references it

Recommended actions (prioritized):
1. Refresh aveva-current.yaml against this month's AVEVA price list (1 hour)
2. Create competitors/abb.md from template (2 hours; battlecard structure)
3. Create industries/pharma-life-sciences.md if Pharma is a fast-follow target

Stub / template files (informational):
- 14 industry stubs in stubs/ — 11 align with parked verticals (no action)
                              - 3 align with active or fast-follow (review)
```

## Run cadence

Automatic: quarterly (Jan/Apr/Jul/Oct 5 at 09:00 per `distributor.config.scheduled_tasks.quarterly_content_health_audit`).

On demand: distributor enablement lead invokes anytime.

## Health Score calculation

Aggregate Score = weighted average across slots:

- **Required slots** (pricing, primary battlecards, active industry playbooks): weight 3
- **Recommended slots** (case studies, objection scripts, secondary battlecards): weight 2
- **Optional slots** (discovery questions, brand assets): weight 1

Per slot:
- GREEN = 100
- YELLOW = 70
- ORANGE = 40
- RED = 0

Score = Σ(weight × state-value) / Σ(weight)

Distributor target: ≥85 sustained.

## Integration with other skills

- The win-loss-loop skill flags content updates needed; content-health surfaces them quarterly.
- The pipeline-health skill flags content gaps that affected at-risk deals; content-health includes them in the next audit.
- The annual memory audit task and content health audit run within the same week — distributor reviews together.

## HTML live artifact (v0.3.1+)

When the user asks for a visual content audit, present `artifacts/content-health-dashboard.html` as a Cowork artifact. The dashboard:

- Reads `artifacts/content-health-snapshot.json` (regenerated at plugin build time).
- KPI strip: watermarked files count, hash-baseline match count, full / stub content counts, total content files.
- Hash-baseline integrity table — green if all 26 protected files match, red with per-file drift listing if not.
- Per-category content slot tables: industry playbooks, competitor battlecards, case studies, objections, products, pricing, discovery, canonical references. Each row shows file path, size, full/stub status, last_validated date with green/yellow/red age indicator (<90 days fresh, <365 days stale, older = very stale).

The static dashboard runs without external connectors. To regenerate the snapshot live, run this skill in `audit` mode and re-build the snapshot JSON at build time.

