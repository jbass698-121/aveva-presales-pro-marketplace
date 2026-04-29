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

## Why a GitHub marketplace and not local upload

Cowork's local-upload UI is broken on Windows for user-built plugins (Anthropic GitHub issues #24328, #40414, #28337, #42651). The personal-GitHub-marketplace path is the working install route on Pro accounts and doesn't require Team/Enterprise.

## License

BUSL-1.1 — see the plugin's `LICENSE.md`. Pilot evaluation use is permitted free of charge for up to 90 days. Commercial production use requires a separate license.

## Versioning

Each plugin update bumps the version in `plugins/aveva-presales-pro/.claude-plugin/plugin.json`, gets committed and pushed here. Cowork users click Update in the marketplace UI to pull the new version.
