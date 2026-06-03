# aveva-presales-pro marketplace

Personal Cowork plugin marketplace hosting **aveva-presales-pro** — an AI presales content factory for Schneider Electric direct sellers and AVEVA distributors.

## What's here

- `aveva-presales-pro` v0.3.1 — 22 skills, 5 pipeline-stage agents, 4 interactive HTML artifacts, 12 scheduled tasks. Battlecards, ROI math, opportunity briefings, executive customer-facing decks, quick-reference cheat sheets, strategic account briefs.

## Install in Cowork

1. Open Cowork.
2. **Browse plugins → Personal tab → + Add marketplace from GitHub.**
3. Enter `jbass698-121/aveva-presales-pro-marketplace` and click Sync.
4. Click **Install** on the `aveva-presales-pro` plugin entry.
5. (If it doesn't persist across a restart, see Cowork issue #40600 — click Install again.)

## ⚠️ After install — start onboarding (Cowork doesn't do this for you)

Cowork plugins don't auto-run anything on install. The plugin's skills are registered but silent until you trigger one. **To configure the plugin for your team, open a fresh Cowork chat and type:**

> *"Set up the plugin for our team."*

That activates the `onboarding` skill — a 9-step interactive wizard (15-20 minutes) that asks about:

1. Audience type (Schneider direct / AVEVA distributor / Mixed / Just exploring)
2. Region and footprint
3. Active verticals (CPG, O&G, water/WW, mining, transportation, etc.)
4. Primary competitors per vertical
5. CRM stack (Dynamics 365 / Salesforce / HubSpot)
6. **Optional tools — Gamma (deck polishing), Wondercraft (audio podcast generation)**
7. Voice and tone preferences (forbidden phrases, persona)
8. **Pricing book override** — point at your real distributor pricing instead of the demo defaults
9. Brand assets (colors, logo, voice guide)

At the end it writes your `distributor.config.yaml`, creates 12 scheduled tasks, and runs an initial content health audit.

**Just want to try it without configuring?** Type *"just exploring"* (or *"use the example config"*) instead — the plugin loads the Q-Mation example config and you can start testing immediately. You can re-run onboarding any time later.

**Other ways to invoke onboarding** if the phrase above doesn't activate it: *"onboard me"*, *"configure the plugin"*, *"walk me through setup"*, *"first-run"*, *"getting started"*, *"customize the plugin"*.

## Why a GitHub marketplace and not local upload

Cowork's local-upload UI is broken on Windows for user-built plugins (Anthropic GitHub issues #24328, #40414, #28337, #42651). The personal-GitHub-marketplace path is the working install route on Pro accounts and doesn't require Team/Enterprise.

## License

BUSL-1.1 — see the plugin's `LICENSE.md`. Pilot evaluation use is permitted free of charge for up to 90 days. Commercial production use requires a separate license.

## Versioning

Each plugin update bumps the version in `plugins/aveva-presales-pro/.claude-plugin/plugin.json`, gets committed and pushed here. Cowork users click Update in the marketplace UI to pull the new version.
