# Wondercraft.ai Integration

Wondercraft.ai turns scripts into multi-host AI podcasts. The plugin uses it as the preferred renderer for sales enablement audio.

## When the integration applies

- The `aveva-enablement-podcast` skill runs.
- The `enablement-podcast` pipeline executes.
- Audience is `seller-internal`.
- Distributor has `optional_tools.wondercraft_ai.enabled: true`.

## Three modes

### Mode A — Wondercraft + Chrome MCP

Flow:
1. Plugin produces wondercraft-optimized script (two-host, segment-marked, ~2,250 words for 15 min).
2. Formatter uses Chrome MCP:
   - Navigate to wondercraft.ai/create.
   - Paste script into the editor.
   - Configure host pair (default Alex + Jamie, configurable).
   - Trigger generation.
   - Poll for completion (audio render: 2-5 min typical).
   - Download MP3 to `outputs/podcasts/{topic-slug}-{date}.mp3`.

### Mode B — Wondercraft manual handoff

1. Plugin produces script.
2. Plugin renders handoff:
   ```
   **Ready for Wondercraft**

   Open Wondercraft → https://wondercraft.ai/create

   1. Paste the script below.
   2. Select host pair (recommended: Alex + Jamie).
   3. Trigger "Generate."
   4. Wait 2-5 minutes for audio render.
   5. Download MP3 → drop in outputs/podcasts/.
   ```

   [Script in fenced code block.]

3. User completes manually.

### Mode C — Text-only fallback

Plugin saves the script as Markdown with note: "Audio generation requires Wondercraft license. Script ready for upload."

## Why Wondercraft matters

For sales enablement, audio fits a different listening pattern than reading:
- Commute listening: 15-30 min daily.
- Between-meeting listening: 5-10 min slots.
- Pre-customer-meeting prep: 10-15 min.

Reading a 5-page playbook is friction. Listening to a 15-min podcast on the topic is much lower friction and tends to land better — especially for senior AEs / SEs who have less time to read.

## Cost reference (verify against current Wondercraft pricing)

- Free tier: limited credits, watermarked.
- Pro: ~$45/user/month for unlimited generation.
- Team: SSO, brand controls.
- Enterprise: custom voices, custom hosts, full API access.

For 15-AE distributor: Pro tier is typically appropriate. ~$8K/year. Often sells via the value-sell artifact ("how much would you pay to give your team access to a 15-min podcast on every major industry / customer / competitor brief, on demand?").

## Voice / host pair guidance

Default hosts (Alex and Jamie) are configurable in distributor.config.voice.podcast_hosts. Recommendations for AVEVA presales context:

- **Alex (lead host)** — frames topics, asks the questions an AE would ask. Energetic, curious tone.
- **Jamie (subject expert)** — answers, provides nuance. Authoritative, technical-but-accessible.

Distributors can substitute other Wondercraft voices if they have brand-specific preferences.

## Limitations and watch-outs

- **Audio quality varies by content type.** Highly technical content sometimes reads stiffly; Wondercraft's editing tools help.
- **Generation time.** 15-min script → 3-5 min render. Mode A pipeline budget is 6 min; Mode B is async.
- **Audio review.** Always preview before distributing internally — occasional pronunciation issues with technical terms (PI System, ETAP, Triconex). Wondercraft has a "pronunciation override" feature.
- **Custom voices** require Enterprise tier and audio samples.

## Reference

- wondercraft.ai
- The original podcast strategy: `Live MD Files - Optimized/podcast-strategy.md`
- Wondercraft API: https://wondercraft.ai/api (Enterprise tier)
