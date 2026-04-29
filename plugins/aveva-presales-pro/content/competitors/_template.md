---
competitor: "<<COMPETITOR NAME>>"
threat_tier: "<<primary | secondary | niche>>"
verticals_active_in: ["<<vertical1>>", "<<vertical2>>"]
last_validated: "2026-04-29"
confidence_default: "<<HIGH | MEDIUM | LOW>>"
sources:
  - url: ""
    type: "competitor_official | analyst_report | distributor_internal"
    date: "YYYY-MM-DD"
---

# Battlecard: <<Competitor Name>>

> **How to use this template.** Copy this file to `content/competitors/<competitor-name-kebab-case>.md` (e.g., `rockwell.md`, `siemens.md`, `inductive-automation-ignition.md`) and fill in every section. Keep claims to one to three sentences. Cite a source for every numeric claim, every spec, and every "we win when" pattern. Date every section. The orchestrator surfaces stale claims (>90 days) automatically.

## Threat Profile

- **Market position:** <<#1 / #2 / #3 / niche in vertical>>
- **Revenue (most recent year):** <<$X.X B>> [SOURCE: <<>>]
- **Core strength:** <<one sentence>>
- **Target markets they pursue most actively:** <<verticals>>
- **Threat tier for this distributor:** <<primary / secondary / niche>>

## Product Portfolio (the products you'll be compared against)

- **Modern HMI/SCADA:** <<product name + GA date if recent>>
- **Site-wide SCADA:** <<>>
- **DCS:** <<>>
- **Historian:** <<>>
- **MES:** <<>>
- **Cloud platform:** <<>>
- **Engineering software:** <<>>

## Their Competitive Advantages (what they will try to win on)

1. <<one sentence + evidence>> [SOURCE: <<>>]
2. <<one sentence + evidence>> [SOURCE: <<>>]
3. <<one sentence + evidence>> [SOURCE: <<>>]

## AVEVA Counter-Strategy (what we lead with)

- **Primary positioning:** <<one sentence>>
- **Top differentiator #1:** <<>> [SOURCE: <<docs.aveva.com path>>]
- **Top differentiator #2:** <<>> [SOURCE: <<>>]
- **Top differentiator #3:** <<>> [SOURCE: <<>>]
- **Cloud / cloud-readiness story:** <<AVEVA Connect vs. their cloud>>
- **Energy / sustainability story:** <<EcoStruxure vs. their offering>>

## When AVEVA Wins (the patterns)

- <<deal pattern + characteristic + evidence>>
- <<deal pattern + characteristic + evidence>>
- <<deal pattern + characteristic + evidence>>

## When the Competitor Wins (be honest)

- <<scenario>> — gap-closure: <<what we offer to recover>>
- <<scenario>> — gap-closure: <<>>

## Top Objections + Responses

### Objection: <<verbatim phrase the customer says>>
**Response:** <<2-3 sentences>>
**Gap-closure:** <<concrete offer the seller can make>>
**Source:** <<>>

### Objection: <<>>
**Response:** <<>>
**Gap-closure:** <<>>
**Source:** <<>>

### Objection: <<>>
**Response:** <<>>
**Gap-closure:** <<>>
**Source:** <<>>

## Recommended Proof Points

- **Customer reference:** <<customer + outcome>> [SOURCE: <<distributor case study | AVEVA case study library>>]
- **Analyst marker:** <<Gartner / IDC / ARC / Forrester quote or rating>> [SOURCE: <<>>]
- **Demo asset:** <<file in content/assets/ or AVEVA library>>

## Recent Changes (review monthly)

- **<<YYYY-MM-DD>>:** <<significant product release / pricing change / acquisition / leadership move>>
- **<<YYYY-MM-DD>>:** <<>>

## Monitoring queries (used by scheduled tasks)

- "<<competitor name>> vs AVEVA <<product>> <<vertical>>"
- "<<competitor name>> pricing <<year>>"
- "<<competitor name>> announcement <<latest quarter>>"

## Internal Notes (distributor-only — do not share with customers)

<<Margin notes, deal patterns, named SE preferences, customer-specific context. This section is filtered out of customer-facing outputs by the orchestrator.>>
