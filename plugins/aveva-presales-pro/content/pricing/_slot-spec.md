# Pricing slot — distributor BYOC

This directory holds the distributor's authoritative pricing book. The `roi` skill uses these files as the single source of truth for any quote, ROI, or TCO comparison.

## Required file

`aveva-current.yaml` — the distributor's current AVEVA price list with regional adjustments and partner-discount tiers. **This is the most important BYOC file in the entire plugin.** Without it, ROI responses degrade to ranges and estimates.

## Recommended file

`competitors.yaml` — competitor pricing benchmarks. Public list prices where the competitor publishes them; verified or estimated prices where they don't. Confidence-tagged.

## Recommended schema for `aveva-current.yaml`

```yaml
metadata:
  effective_date: "2026-04-29"
  region: "north-america"
  next_review: "2026-07-29"
  pricing_source: "AVEVA Global Price List 2026.04 + distributor partner discount tiers"

products:
  intouch_unlimited:
    perpetual_license: 12000
    annual_support: 2400
    implementation_range: [8000, 15000]
    training_range: [3000, 5000]
    notes: "Standard SCADA license; perpetual; partner discount X% applies"

  ops_control_edge_starter:
    annual_subscription: 22500
    implementation_range: [12000, 18000]
    support: "Included in subscription"
    notes: "Cloud-enabled edge SCADA; subscription; 3-year minimum term"

  system_platform:
    perpetual_license_base: 30000
    perpetual_license_concurrent_users:
      "10": 45000
      "25": 70000
      "50": 105000
      "99": 145000
    annual_support_pct: 20
    notes: "Concurrent-user pricing; redundancy 50% additive"

  pi_system_data_archive:
    "<<populate>>"

  pi_af:
    "<<populate>>"

  pi_vision:
    "<<populate>>"

  unified_operations_center:
    "<<populate>>"

  mes:
    "<<populate>>"

  aveva_connect_data_services:
    "<<populate>>"

# Modicon hardware list prices (used by ROI for tier-based stack pricing)
modicon:
  m221_starter_kit: 350
  m241_with_io: 1200
  m580_base: 4500
  "<<extend>>"

# Regional adjustments
regional_adjustments:
  texas: 1.00
  louisiana: 1.00
  oklahoma: 1.00
  mountain_west: 1.02
  southwest: 1.02
  notes: "Regional adjustments are partner-program-specific; review quarterly"

# Partner discount tiers (used by ROI to show distributor margin)
partner_discount_tiers:
  authorized: 0.20
  silver: 0.25
  gold: 0.30
  platinum: 0.35
```

## Legal reminder

This file contains confidential pricing. The plugin treats it as distributor-private:

- It is read by skills but never quoted verbatim into customer-facing artifacts.
- Customer-facing outputs use the prices but cite "AVEVA channel pricing 2026" rather than the distributor's source file.
- The orchestrator strips internal-only fields (partner_discount_tiers, internal margin notes) from any output where `audience: customer` is set.

## Update cadence

- **Monthly minimum** review.
- The `monthly_source_validation` scheduled task flags pricing >180 days old as stale.
- AVEVA's annual price list refresh (typically March) drives a full re-validation.
