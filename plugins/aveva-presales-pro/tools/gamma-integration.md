# Gamma.app Integration

Gamma.app turns markdown into professional presentations in 60 seconds. The plugin uses it as the preferred renderer for executive-customer-facing decks.

## When the integration applies

- The `aveva-deck-generator` skill runs.
- The `executive-deck` pipeline executes.
- Audience is `customer-facing-executive`.
- Distributor has `optional_tools.gamma_app.enabled: true` in distributor.config.

## Three modes

### Mode A — Gamma + Chrome MCP (preferred)

Requires:
- `optional_tools.gamma_app.enabled: true`
- Chrome MCP connected
- Distributor has either personal Gamma account (per-user) or org SSO (preferred for enterprise distributors)

Flow:
1. The `aveva-deck-generator` skill produces gamma-optimized markdown.
2. Formatter agent uses Chrome MCP:
   - Navigate to gamma.app/create.
   - Select "Import script."
   - Paste the markdown.
   - Click "Generate" and wait for render (poll for completion indicator).
3. After render:
   - Click "Export" → "PowerPoint (.pptx)."
   - Download to `outputs/executive-decks/{slug}-{date}.pptx`.
4. Surface the PPTX file to user.

### Mode B — Gamma manual handoff

Requires:
- `optional_tools.gamma_app.enabled: true`
- Chrome MCP NOT connected (or user prefers manual)

Flow:
1. Plugin produces gamma-optimized markdown.
2. Plugin renders a one-screen handoff:

```markdown
**Ready for Gamma**

Open Gamma → https://gamma.app/create

1. Click "Import script" or paste directly.
2. Paste the script below.
3. Click "Generate."
4. Wait ~60 seconds for render.
5. Export as PowerPoint.
6. Drop the PPTX in `outputs/executive-decks/` (or share the link with me).

```

[Then the gamma-optimized markdown in a fenced code block.]

3. User completes; plugin picks up the PPTX from outputs folder.

### Mode C — python-pptx native fallback

Requires: nothing optional — works always.

Flow:
1. Plugin parses gamma-optimized markdown into slide structure.
2. python-pptx renders each slide using `content/brand/pptx-template.pptx` if exists.
3. Lower polish than Gamma but functional.

## Why Gamma matters (for the value-sell)

Gamma's output quality vs. python-pptx is meaningfully higher for executive audiences:
- Gamma uses AI for layout suggestions and visuals.
- Gamma handles image generation and source matching automatically.
- Gamma's paginated output respects narrative arc.
- python-pptx is a great fallback but reads as "AI template" to executives who see many decks.

For distributors hesitating on the license: a single Tier-1 deal won by an executive deck pays for the license many times over. The plugin generates the value-sell artifact on demand.

## Cost reference (verify against current Gamma pricing)

- Free tier: 400 AI credits, basic features, watermarked exports.
- Plus tier (~$8/user/month): unlimited AI credits, no watermark, custom fonts, advanced export.
- Pro tier (~$15/user/month): branded templates, advanced analytics, custom domain.
- Business tier: SSO, admin controls, team libraries.

For 15-AE distributor: Business tier is typically appropriate, ~$2,700/year. Single Tier-1 win typically justifies many years.

## Limitations and watch-outs

- **Image generation can be slow.** Build expectation that Mode A takes 60-180s.
- **Gamma rate limits.** Heavy usage hits limits; Mode B handoff is the fallback.
- **Customization depth.** Gamma's branded template support is good but not perfect; complex corporate templates may need manual touch-up.
- **Audio / video embeds.** Limited; Wondercraft is a separate flow.

## Reference

- gamma.app
- gamma-script-guide.md (in original Live MD Files - Optimized — v0.1.1 reference)
