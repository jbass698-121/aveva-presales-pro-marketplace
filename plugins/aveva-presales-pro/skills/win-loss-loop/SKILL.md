<!--
Copyright (c) 2026 Jason Bass. All rights reserved.
Licensed under the Business Source License 1.1. See LICENSE.md.
Watermark: appro-ca96e5c3-e535-40b4-a502-9e85523f608e
This file is a Category 3 protected component per MODIFICATION-POLICY.md.
-->
---
name: aveva-win-loss-loop
description: Captures lessons-learned when a deal closes (won or lost), structures a brief interview with the AE, extracts patterns, and feeds those patterns back into the relevant industry playbook + battlecard + objection script. Triggers on closed-won / closed-lost CRM stage transitions (when CRM webhooks are opt-in enabled) or manual invocation. Activates on closed deal language (closed won, closed lost, lost the deal, won the deal, deal review, lessons learned, deal post-mortem).
---

# AVEVA Win-Loss Loop

You capture lessons-learned from closed opportunities and propagate the patterns back into the content pack so future deals benefit.

## Trigger conditions

**Automatic:** When CRM webhooks are opt-in enabled (`distributor.config.crm.webhooks.enabled: true`), Dynamics fires `opportunity.closed` events. The plugin's webhook handler routes to this skill.

**Manual:** AE or SE invokes the skill explicitly: "Run the win-loss loop on the Cargill deal."

## The lessons-learned interview

When triggered, the skill runs a structured interview via Cowork's `AskUserQuestion`:

1. **Outcome confirmation** — Won or lost?
2. **Final solution / commercial terms** — What was actually sold? At what price? Tier?
3. **The deciding factor** — What single thing tipped the deal? (Multi-select: technical fit, price, competitive positioning, relationship, timing, support model, regulatory pressure, other.)
4. **The competitor of record's strongest move** — What did the competitor do well?
5. **Our weakest moment** — Where did we struggle? (Pricing pushback, technical objection, decision-process delay, etc.)
6. **What we'd do differently** — Open-text.
7. **Replicable pattern** — Is the lesson specific to this deal or generalizable?

Each answer is captured with timestamp and AE attribution.

## Pattern extraction

The skill then synthesizes:

- **Pattern type:** specific (one-deal anomaly) vs. generalizable (recurring theme).
- **Affected content:** which industry playbook, which battlecard, which objection script needs updating.
- **Severity:** minor (footnote update) vs. major (whole-section rewrite).
- **Cross-cutting flags:** does this affect competitive positioning more broadly? Does it surface a new customer segment we should formally add?

## Propagation

Generalizable patterns get:

1. Appended to the relevant industry playbook's "Distributor's Regional Wins" or new "Lessons Learned" subsection.
2. Surfaced to the relevant battlecard as a new "Recent Changes" entry or objection rebuttal.
3. Added to `content/objections/{theme}.md` if the lesson is an objection pattern.
4. Logged in `accounts/{ae-slug}/{account-slug}.md` "Lessons learned" section.

Specific (one-deal) patterns get logged in the account memory file only.

## Audience filtering

Win-loss content is **internal-only by design**. It contains:
- Specific deal pricing
- Stakeholder posture
- Competitive moves and counter-moves
- Honest assessment of weaknesses

**Never** appears in customer-facing artifacts. The verifier subagent enforces this.

## Quarterly aggregation

Once a quarter (via the quarterly_content_health_audit task), the skill aggregates all win-loss entries from the past 90 days and produces a quarterly insights report:
- Win rate by competitor
- Win rate by vertical
- Win rate by tier
- Top 3 deciding factors (won)
- Top 3 deciding factors (lost)
- New competitive patterns observed
- Recommended content updates (prioritized)

This report goes to the distributor's enablement lead and informs the next quarter's content pack updates.

## Privacy

Win-loss data carries the same per-AE isolation as account memory. AEs see their own deals' lessons. Team-level aggregation requires opt-in. The quarterly report is anonymized at the AE level (shows patterns, not "Bob lost to Honeywell on April 15").
