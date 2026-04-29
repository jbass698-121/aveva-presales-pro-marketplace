# Modification Policy — aveva-presales-pro

This document defines what you may, may not, and should-with-care modify in the plugin. It is a companion to `LICENSE.md`. Modifying protected components voids the commercial license.

## TL;DR

| Category | Files | Modification posture |
|---|---|---|
| **1. SAFE — modify freely** | `distributor.config.yaml`, `content/competitors/`, `content/industries/`, `content/case-studies/`, `content/objections/`, `content/discovery/`, `content/products/`, `content/pricing/`, `content/brand/`, `accounts/{your-ae}/` | Distributor-owned. Designed for customization. No restriction. |
| **2. CARE — modify only with intention** | `skills/industry-*/`, `skills/competitive/`, `skills/roi/`, `skills/discovery/`, `skills/briefing/`, custom additions to `pipelines/`, `scheduled-tasks.yaml` | Customizable but affects routing and behavior. Document changes. Do not weaken safety properties. |
| **3. PROTECTED — DO NOT MODIFY without license** | `skills/orchestrator/`, `skills/account-memory/`, `skills/win-loss-loop/`, `skills/content-health/`, `skills/onboarding/`, `agents/verifier.md`, `agents/researcher.md`, `agents/analyst.md`, `agents/writer.md`, `agents/formatter.md`, `pipelines/*.yaml` (built-in), `content/public-sources.yaml` | Protected IP. Hashed by the content-health audit task. Modification voids warranty and commercial license. |

## Category 1 — Safe to modify (designed for it)

These are your content. Customize freely.

- **`distributor.config.yaml`** — your organization's parameters (region, verticals, voice, retention, etc.). Re-run the onboarding skill to regenerate cleanly if needed.
- **`content/competitors/{name}.md`** — battlecards. Add new competitors, refine existing ones with regional intelligence, update pricing references.
- **`content/industries/{vertical}.md`** — industry playbooks. Refine for your customer base, add regional case studies, update regulatory framing.
- **`content/case-studies/{slug}.md`** — your win stories. Add aggressively as deals close.
- **`content/objections/{theme}.md`** — battle-tested scripts your team uses.
- **`content/discovery/questions.md`** — your team's question bank.
- **`content/products/{family}.md`** — product positioning specific to your customer base.
- **`content/pricing/aveva-current.yaml`** — your authoritative pricing book. **Highest leverage to fill in.**
- **`content/brand/`** — logo, colors, voice guide, templates.
- **`accounts/{ae-email-slug}/{account-slug}.md`** — your AE-isolated account memory.

No version-control restrictions. No hashing. Modify freely.

## Category 2 — Care zone (modify with intent, document changes)

These shape how the plugin routes and behaves. Modification is allowed but should be done thoughtfully.

- **`skills/industry-*/`** — adding a new industry skill is fine. Substantially rewriting existing industry skills is fine but expect tone drift. Document modifications in a `CHANGES.md` you maintain.
- **`skills/competitive/`, `skills/roi/`, `skills/discovery/`, `skills/briefing/`** — same pattern. Modifications change Claude's behavior; test before deploying to AEs.
- **Custom additions to `pipelines/`** — adding new pipelines for your workflows is encouraged. Modifying built-in pipelines is in Category 3.
- **`scheduled-tasks.yaml`** — adjusting cron times, disabling tasks, or adding new tasks is fine. Removing tasks the orchestrator depends on may degrade behavior.

Best practice: keep a `CHANGES.md` in your distributor copy of the plugin documenting what you've modified and why. The content-health audit will flag drift but won't block.

## Category 3 — PROTECTED (do not modify)

These components enforce safety, accuracy, audience filtering, IP protection, and compliance. Modifying them voids the commercial license and the warranty. The content-health audit task hashes these files quarterly and reports any drift to the licensor (via the watermark).

Protected files in v0.2.5:

```
.claude-plugin/plugin.json
skills/orchestrator/SKILL.md
skills/account-memory/SKILL.md
skills/win-loss-loop/SKILL.md
skills/content-health/SKILL.md
skills/onboarding/SKILL.md
skills/portfolio-narrative/SKILL.md
skills/strategic-account/SKILL.md
skills/deck-generator/SKILL.md
skills/enablement-podcast/SKILL.md
skills/quick-reference/SKILL.md
skills/pipeline-health/SKILL.md
agents/researcher.md
agents/analyst.md
agents/writer.md
agents/verifier.md
agents/formatter.md
pipelines/opportunity-briefing.yaml
pipelines/strategic-account-brief.yaml
pipelines/industry-playbook.yaml
pipelines/executive-deck.yaml
pipelines/enablement-podcast.yaml
pipelines/quick-reference.yaml
content/public-sources.yaml
LICENSE.md
MODIFICATION-POLICY.md
```

### Why these are protected

- **The orchestrator** controls routing, voice, and tier sizing — modifying it can produce inconsistent outputs and break confidence framework enforcement.
- **The verifier agent** is the line of defense against fabricated claims reaching customers. Weakening it directly affects accuracy of customer-facing artifacts and your brand exposure.
- **The audience filter (writer + verifier + formatter)** is what stops internal stakeholder posture annotations from leaking into customer-facing content. Modifying it creates real privacy and brand risk.
- **The confidence framework** (three-axis tagging in agents and orchestrator) enforces source citation discipline. Modifying it erodes trust in every output.
- **Account memory rules** include sensitive-data scrubbing and per-AE isolation. Modifying weakens privacy.
- **Pipelines** define stage sequencing and time budgets for content production. Modifying built-in pipelines may create incomplete or unverified outputs.
- **Public-sources.yaml** is the verification source-of-truth. Modifying it weakens fact-checking against canonical AVEVA references.
- **License and modification policy** are the legal contract.

If you need to modify any Category 3 file for a legitimate operational reason (e.g., adding a new source tier to public-sources.yaml), contact the licensor for a written exception or a custom build.

## Watermark integrity

Every Category 3 file (and most Category 2 files) contains the watermark identifier:

```
appro-ca96e5c3-e535-40b4-a502-9e85523f608e
```

Removal or alteration of the watermark without the Licensor's written consent is a material breach of the License. The content-health audit detects watermark drift on its quarterly run.

## Hash check (the content-health audit)

The `quarterly_content_health_audit` scheduled task runs the `aveva-content-health` skill in audit mode. As part of that audit, it computes SHA-256 hashes of all Category 3 files and compares against the v0.2.5 baseline (recorded in `.protected-files-baseline.json`). Drift is reported to the distributor enablement lead and (via licensee report) to the licensor. Drift in itself is informational; sustained drift across audits indicates intentional modification.

## Reporting modifications

If you need to make a modification to a Category 3 file for evaluation, ticket it before doing so. Send the proposed change and the rationale to the licensor. Many requests can be accommodated through configuration changes (Category 1) or new pipelines/skills (Category 2) rather than modifications to protected components.
