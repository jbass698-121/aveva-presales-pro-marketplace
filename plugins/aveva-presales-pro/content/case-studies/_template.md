---
customer: "<<Customer name (or anonymized identifier)>>"
customer_visible: "<<true | false>>"           # if false, all customer-identifying details get redacted in customer-facing outputs
industry: "<<>>"
sub_segment: "<<>>"
region: "<<>>"
year_deployed: "<<YYYY>>"
deal_size_band: "<<<$50K | $50K-$250K | $250K-$1M | $1M+>>"
solution_components: ["<<AVEVA System Platform>>", "<<>>"]
competitor_of_record: "<<name or 'greenfield'>>"
distributor_owned: "<<true | false>>"          # was this our deal or was it AVEVA-direct?
last_validated: "<<YYYY-MM-DD>>"
sources:
  - type: "internal_postmortem | customer_quote | published_case_study | analyst_writeup"
    reference: "<<file path or URL>>"
    date: "YYYY-MM-DD"
---

# Case Study: <<Customer Name or Anonymized ID>>

> **How to use this template.** Copy to `content/case-studies/<descriptive-slug>.md` (e.g., `houston-water-utility-2024.md`, `gulf-coast-refiner-anonymized.md`). Mark `customer_visible: false` if the customer hasn't given press permission — the orchestrator will redact identifiers in customer-facing outputs.

## Customer Profile

- **Industry:** <<>>
- **Sub-segment:** <<>>
- **Size:** <<population served | tag count | site count | annual revenue>>
- **Region:** <<>>
- **Prior platform:** <<what they had before AVEVA>>

## The Pain (what they came to us with)

<<2-4 sentences describing the operational, regulatory, or commercial problem. Quote the customer if you have permission.>>

## The Solution (what we deployed)

- **AVEVA software:** <<>>
- **Schneider hardware:** <<>>
- **Implementation timeline:** <<>>
- **Distributor role:** <<full implementation | hardware + software resale | services partner>>

## The Outcome (the numbers)

| Metric | Before | After | Improvement | Source |
|---|---|---|---|---|
| <<>> | <<>> | <<>> | <<>> | <<>> |
| <<>> | <<>> | <<>> | <<>> | <<>> |
| <<>> | <<>> | <<>> | <<>> | <<>> |

**Headline ROI:** <<X-year payback | Y% Y1 ROI | $Z annual savings>>

## Why It Worked (the non-obvious factors)

- <<>>
- <<>>
- <<>>

## What We Did Differently (vs. competitor pitch)

<<If a competitor was in the deal — what swung it.>>

## Reusable Talking Points

(Stripped of customer-identifying details. Safe for use in customer-facing material.)

- <<>>
- <<>>
- <<>>

## Reference Pack

- Demo screenshots: <<file path>>
- Customer quote (with permission): <<>>
- Anonymized version: <<>>

## Distributor Internal Notes (do not share)

<<Margin, deal context, named SE who led, lessons learned, what we'd do differently next time.>>
