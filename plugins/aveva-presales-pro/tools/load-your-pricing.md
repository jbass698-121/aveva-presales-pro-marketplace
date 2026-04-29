# How to Load Your Real Pricing Into the Plugin

The framework ships with `content/pricing/aveva-current.yaml` populated with public AVEVA pricing references as a demo. **Before any customer-facing pricing or ROI artifact, you must override these with your real numbers.**

## Why this matters

The ROI skill, the strategic-account-brief pipeline, the executive deck pipeline, and the quick-reference all read from `content/pricing/aveva-current.yaml` for any quoted figure. The framework defaults are tagged confidence MEDIUM at best. Customer-facing artifacts produced from MEDIUM-confidence pricing get downgraded by the verifier — meaning they'll show ranges and disclaimers rather than firm numbers. Replace the defaults with your verified pricing and you get HIGH-confidence, defensible quotes.

## Three ways to override

### Option 1 — Direct edit (simplest)

Open `content/pricing/aveva-current.yaml` in your editor. For each product:

1. Replace numeric values with your current quoted price.
2. Update the `confidence` field to `"HIGH"` once you've verified against your AVEVA partner price list.
3. Update the file's top-level `metadata.effective_date` and `metadata.next_review`.
4. Save.

The plugin picks up your changes immediately on the next conversation.

### Option 2 — Layered override (recommended for multi-region distributors)

If you operate across multiple regions with different pricing, create per-region override files:

```
content/pricing/
├── aveva-current.yaml                  (framework defaults — keep as-is)
├── aveva-overrides-gulf-coast.yaml     (your overrides for this region)
├── aveva-overrides-mountain-west.yaml  (overrides for another region)
└── aveva-overrides-default.yaml        (catch-all)
```

The orchestrator reads the override file matching `distributor.config.distributor.region` first, falls back to `aveva-overrides-default.yaml`, and finally falls back to `aveva-current.yaml`. Override files use the same schema; they need to define only the fields they're changing.

### Option 3 — Spreadsheet import (for teams who maintain pricing in Excel)

Many distributors maintain pricing in a partner-program spreadsheet. To bridge:

1. Export the spreadsheet to CSV with columns: `product_id, list_price, partner_price, margin_pct, confidence`.
2. Place at `content/pricing/source-spreadsheet.csv`.
3. Run: `python3 tools/sync-pricing-from-csv.py` (provided in v0.3+; for v0.2.5 do this step manually).

For v0.2.5, Option 1 (direct edit) or Option 2 (layered) are the supported paths.

## What to override (priority order)

If your time is limited, override in this order — the highest-leverage products first:

1. **`intouch_unlimited`** (perpetual_license, annual_support) — entry point for water/WW Tier 1 deals
2. **`ops_control_edge_starter`** (annual_subscription) — cloud-positioned mid-market entry point
3. **`system_platform`** (perpetual_license_base + concurrent_users tiers) — backbone of mid-market and enterprise
4. **`unified_operations_center`** (annual_subscription_base) — enterprise tier
5. **`pi_data_archive` and `pi_vision`** — historian intelligence
6. **`mes_starter` and `mes_full`** — high-value but customer-specific; leave as ranges if you don't have firm numbers
7. **`aveva_connect_data_services`** — cloud add-on
8. **Modicon hardware prices** — usually well-known to distributor
9. **`partner_discount_tiers`** — your actual program tiers (DO NOT share customer-facing)
10. **`regional_adjustments`** — your regional multipliers

Override 1-5 covers ~80% of common ROI conversations. Override 1-10 covers ~98%.

## Confidence tagging guidance

For each value you override, update the `confidence` field:

- **HIGH** — verified against your current partner price list, ≤30 days
- **MEDIUM** — verified against published AVEVA references or analyst reports, ≤90 days
- **LOW** — estimate, customer-specific, or significantly outdated
- **UNKNOWN** — leave unchanged; the verifier will flag it before customer-facing use

The plugin's verifier subagent uses these tags. HIGH-confidence pricing flows through into customer-facing PDFs and decks. MEDIUM-confidence gets caveats. LOW or UNKNOWN gets blocked from customer-facing output and surfaces a warning.

## Post-override validation

After you populate your pricing:

1. **Run the ROI skill on a sample scenario** — *"Generate ROI for a mid-market water utility, 50K population, 5K tags."*
2. **Compare the quoted numbers** to what you'd actually quote in that scenario. They should match within a few percent.
3. **Run the content-health audit** — it'll confirm the pricing book is fresh and HIGH-confidence.

## Privacy reminder

`content/pricing/aveva-current.yaml` and any override files contain confidential pricing. The plugin treats this as distributor-internal:

- Customer-facing artifacts NEVER quote your `partner_discount_tiers` verbatim.
- Customer-facing artifacts use the customer-applicable price (post-discount), not your margin math.
- The audience filter at the formatter stage strips internal pricing fields before any PDF/PPTX exits to a customer.

## Update cadence

Recommended cadence:

- **Quarterly:** review against AVEVA's quarterly partner price list. The `monthly_pricing_book_validation` scheduled task flags drift > 5% automatically; review the report.
- **Annually:** AVEVA's annual price list refresh (typically March) drives a full re-validation.
- **As needed:** when AVEVA announces a major product or pricing change.

## Need help?

- Default values in `aveva-current.yaml` are publicly-derivable references; they're a starting baseline, not authoritative.
- Your AVEVA partner-program portal is the authoritative source.
- Your AVEVA channel rep can confirm program-tier-specific pricing.
- For region-specific or customer-specific deviations, consult your sales engineering team.
