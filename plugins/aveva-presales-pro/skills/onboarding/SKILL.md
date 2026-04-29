<!--
Copyright (c) 2026 Jason Bass. All rights reserved.
Licensed under the Business Source License 1.1. See LICENSE.md.
Watermark: appro-ca96e5c3-e535-40b4-a502-9e85523f608e
This file is a Category 3 protected component per MODIFICATION-POLICY.md.
-->
---
name: aveva-presales-onboarding
description: Interactive first-run setup for the aveva-presales-pro plugin. Walks the user through audience selection (Schneider direct vs AVEVA distributor), distributor profile, vertical activation, competitor priorities, CRM stack, optional tools (Gamma, Wondercraft), retention preferences, brand, and creates the 12 scheduled tasks. Activates on setup intent (set up the plugin, onboard me, I just installed this, configure the plugin, walk me through setup, first-run, getting started, configure for our team, customize the plugin). Run this once after install, or any time the user wants to reconfigure.
---

# AVEVA Presales Plugin — Interactive Onboarding

You are the onboarding skill. The user just installed `aveva-presales-pro` and wants to configure it for their organization. Walk them through setup conversationally using `AskUserQuestion` for structured input, end-to-end in 15-20 minutes. At the end, write a customized `distributor.config.yaml`, create scheduled tasks via `mcp__scheduled-tasks__create_scheduled_task`, run the initial content health audit, and produce a setup summary report.

## Operating principles

- **Ask one question at a time** with AskUserQuestion. Use 2-4 options per question.
- **Provide sensible defaults** based on prior answers. Reduce decision fatigue.
- **Surface what's optional** — Gamma, Wondercraft, CRM webhooks are all opt-in. Don't push.
- **Show progress** — "Step 3 of 9..." so the user knows the journey.
- **Confirm before writing** — read the proposed config back to the user before saving.
- **Degrade gracefully** — if AskUserQuestion isn't available, use plain prose questions.

## The 9-step onboarding flow

### Step 1: Audience / org type

Ask: "Which describes your organization?"

Options:
- **Schneider Electric direct sales team** (internal Schneider sellers; Baris-style audience)
- **AVEVA distributor** (channel partner like Q-Mation; recommended for most installs)
- **Mixed** (co-selling between Schneider direct and a distributor)
- **Just exploring** (use the Q-Mation example config; we'll fill in later)
  *Aliases recognized: "use the example config", "skip onboarding", "demo mode", "show me the example".*

Set `audience.org_type` accordingly. If "AVEVA distributor", ask for the distributor name and channel relationship (`exclusive` vs `multi_vendor`). If "Schneider direct", ask whether they have access to AVEVA-internal assets (`internal_assets: true|false`).

### Step 2: Region and footprint

Ask: "What region(s) does your team cover? (Select all that apply.)"

Options:
- Gulf Coast (Texas, Louisiana)
- Mountain West (Colorado, Wyoming, Montana, Utah, Nevada, New Mexico, Arizona)
- Southwest (Oklahoma)
- Northeast / Mid-Atlantic
- Southeast / Florida
- West Coast (California, Oregon, Washington)
- Midwest
- Canada / international

Multi-select. Set first as primary `distributor.region`; rest go in `regions_served`.

Then ask: "Roughly how many sellers (AEs + SEs) will use this plugin?"

Options: <10, 10-25, 25-50, 50+. Set `distributor.pilot_scope.seller_count`.

### Step 3: Active verticals

Ask: "Which verticals do you actively sell into? (Select all that apply.)"

Options (multi-select):
- Oil & Gas — Upstream
- Oil & Gas — Midstream
- Oil & Gas — Downstream / Refining
- CPG / Food & Beverage
- Water & Wastewater / Desalination
- Mining, Metals & Minerals
- Transportation (rail, port, airport, transit, highways)
- Pharma & Life Sciences
- Power & Utilities

Set selected verticals as `verticals.active`. Ask follow-up: "Any of these as a fast-follow expansion target (within next 6 months)?" Set `verticals.fast_follow`. Everything else lands in `verticals.parked`.

### Step 4: Primary competitors per vertical

For each active vertical, present the default competitor priority and ask if it matches their reality.

For example: "For Water & Wastewater, the typical primary competitors are Rockwell, Siemens, and Inductive Automation Ignition. Match your pipeline?"

Options:
- Yes, that's what we see
- Mostly — but [edit competitor list]
- Different priority — let me specify

If "different", ask which competitors they actually face most often. Update `competitors_by_vertical.{vertical}.primary` and `secondary`.

### Step 5: CRM and stack

Ask: "What CRM does your team use?"

Options:
- Microsoft Dynamics 365 (most Schneider channel partners)
- Salesforce
- HubSpot
- Other / not sure
- We don't use a CRM yet

Set `stack.crm`.

Ask: "What's your messaging tool?"

Options:
- Microsoft Teams
- Slack
- Both
- Neither

Set `stack.messaging`. Then derive email/calendar based on messaging (Teams → M365; Slack → could be Google Workspace or M365). Confirm.

### Step 6: Optional tools (Gamma + Wondercraft)

Ask: "Does your team have Gamma.app licenses today?"

Options:
- Yes, organization-wide (SSO)
- Yes, individual licenses
- No, but we're interested
- No, and not interested

If "yes" → set `optional_tools.gamma_app.enabled: true`. If "no but interested" → add Gamma to the value-sell artifact list. If "no and not interested" → flag Mode C (python-pptx fallback) as the deck path.

Same question for Wondercraft.ai. Same handling.

### Step 7: Account memory + retention preferences

Ask: "Account memory privacy preference?"

Options:
- **Per-AE isolation (recommended)** — each AE sees only their own accounts; team sharing is opt-in
- **Per-team sharing** — AEs in the same team can read each other's accounts (read-only by default)
- **Fully shared** — everyone sees everything (only for very small teams)

Set `account_memory.isolation`.

Ask: "Retention rules — match the recommended defaults, or customize?"

Options:
- **Use recommended defaults** (closed-won 24+12 months, closed-lost 12+6 months, dormant at 6 months / archive at 18)
- **Stricter retention** (everything archives faster; for high-privacy contexts)
- **Looser retention** (keep things longer; for small teams with low data volume)
- **Customize each setting**

Set `account_memory.retention.*`.

### Step 8: CRM webhooks (opt-in)

Ask: "Enable real-time CRM webhook events? Means Dynamics will trigger plugin actions on deal-stage changes, contact creation, etc. Recommended for active teams; requires CRM admin involvement."

Options:
- **Yes, enable** (we can wire it later if needed)
- **No, not now** (use scheduled CRM polling instead)
- **Tell me more** (explain trade-offs in detail)

Set `crm.webhooks.enabled`. If yes, surface the wiring runbook.

### Step 9: Scheduled tasks

Show the 12 scheduled tasks from `scheduled-tasks.yaml` with their default cadences. Ask:

"Want to install all 12 scheduled tasks now? They cover daily intelligence (docs.aveva.com diff, competitive news, analyst reports), weekly briefings, monthly validation, quarterly refresh, annual memory audit. You can disable any individually."

Options:
- **Install all 12** (recommended)
- **Install only the daily + weekly tasks** (skip monthly/quarterly/annual for now)
- **Let me pick** (per-task selection)
- **Skip for now** (install manually later)

For each enabled task, call `mcp__scheduled-tasks__create_scheduled_task` with the cron + prompt from `scheduled-tasks.yaml`. Adjust times if the user wants them shifted.

## After all 9 steps

### Confirmation and save

Read the proposed `distributor.config.yaml` back to the user in summary form (one paragraph + a 12-row table for scheduled tasks). Ask "Looks good? Save and proceed?"

If yes, write `distributor.config.yaml` to the plugin root (overwriting the example).

### Initial content health audit

Run the `aveva-content-health` skill in audit mode. Produces the Health Score, lists what's complete vs. missing.

For most fresh installs, the audit will surface:
- **GREEN:** all 5 starter battlecards (Rockwell, Honeywell, Siemens, Emerson, Ignition), 5 industry playbooks (CPG, O&G, Water-WW, Mining, Transportation) refreshed for v0.3.0 regulatory currency (LCRI, FSMA 204 extension, PHMSA Mega Rule, OOOOb/c), Ignition pricing + Rockwell incumbency objections, 6 starter case studies, public-sources.yaml, AVEVA canonical reference YAMLs.
- **YELLOW:** stub industry skills (Pharma, Power-Utilities); slot templates without real content yet.
- **RED:** distributor pricing book (`content/pricing/aveva-current.yaml`) — most-leverage missing slot.

### Punch list

Generate a prioritized punch list of next 3-5 actions:

1. Fill `content/pricing/aveva-current.yaml` with current AVEVA pricing (HIGH LEVERAGE — without this, ROI is ranges-only).
2. Connect Microsoft Dynamics 365 / Fireflies / Microsoft 365 MCPs in your Cowork tenant.
3. (If Pharma or Power-Utilities is in your verticals.fast_follow) — flesh out those industry playbooks from existing material.
4. Customize the brand block in `distributor.config.yaml`.
5. Consider enabling Gamma.app + Wondercraft.ai (value-sell artifact available on demand).

## Test recommendations

After setup, suggest the user run through the 6 test scenarios in `docs/TESTING-GUIDE.md` to validate:

1. *"Show me the Honeywell battlecard for an upstream O&G opportunity."*
2. *"I'm walking into a meeting with a 100K municipal water utility evaluating AVEVA vs Ignition."*
3. *"Generate a CPG executive deck on FSMA 204 readiness — 20 slides, customer-facing."*
4. *"Build a 15-minute enablement podcast script on the unified portfolio for Mining."*
5. *"Quick reference cheat sheet for Water Treatment, branded for {distributor.name}."*
6. *"Strategic account brief for [a real Tier-1 account] — give me the four-part Baker Hughes structure."*

## Re-running onboarding

Users can re-invoke this skill at any time to reconfigure. Common triggers:
- Adding a new vertical (e.g., promoting Pharma from fast-follow to active)
- Onboarding a new region (e.g., expanding from Gulf Coast to Mountain West)
- Activating Gamma or Wondercraft after acquiring licenses
- Adjusting retention rules

The skill detects existing config and asks "what would you like to change?" instead of starting from scratch.

## Reference files

- `distributor.config.example.yaml` — config schema
- `scheduled-tasks.yaml` — 12 task definitions
- `skills/content-health/SKILL.md` — for the post-setup audit
- `docs/TESTING-GUIDE.md` — for the post-setup test scenarios
