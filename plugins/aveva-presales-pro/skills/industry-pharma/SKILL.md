<!--
Copyright (c) 2026 Jason Bass. All rights reserved.
Licensed under the Business Source License 1.1. See LICENSE.md.
Watermark: appro-ca96e5c3-e535-40b4-a502-9e85523f608e
This file is a Category 3 protected component per MODIFICATION-POLICY.md.
-->
---
name: aveva-industry-pharma
description: AVEVA presales positioning for Pharma & Life Sciences — drug manufacturing, biotech, medical devices. Activates on industry keywords (pharma, pharmaceutical, life sciences, biotech, medical device, drug manufacturing, biopharma, vaccine, batch pharma, sterile, biologics, mAb, fill finish, lyophilization) and regulatory framing (FDA 21 CFR Part 11, Part 210, Part 211, GMP, cGMP, GxP, validation, DSCSA, EU Annex 11, ICH Q9, ALCOA+).
---

# AVEVA Pharma & Life Sciences Industry Skill

You are loaded for pharmaceutical and life sciences manufacturing conversations. Vertical is fast-follow in the v2 distributor config; full content is in `content/industries/pharma-life-sciences.md` once populated.

## The Pharma thesis (executive framing)

Pharma manufacturing operates at the highest regulatory stakes in industrial automation. The AVEVA portfolio, especially MES + System Platform + PI System, is an IDC MarketScape MES Leader for exactly this audience. Three forces shape 2026:

1. **DSCSA enforcement** (Drug Supply Chain Security Act) — full traceability of pharmaceutical products through the supply chain. Driving system upgrades in serialization and electronic records.
2. **Continuous manufacturing emergence** — FDA encouraging shift from batch to continuous; new control architectures required.
3. **Biologics manufacturing scaling** — mAb, cell-and-gene therapy, vaccine production. Recipe-driven, cycle-time-sensitive, GMP-rigorous.

The unified portfolio plays particularly well: AVEVA MES for batch records + System Platform for SCADA + PI System for process analytics + EAE for software-defined automation in continuous manufacturing.

## Sub-segments

- **Small molecule pharma:** traditional batch operations, recipe management, deviation investigation.
- **Biologics / biopharma:** mAb production, fill-finish, lyophilization, sterile manufacturing.
- **Medical device:** discrete + cleanroom, FDA Quality System Regulation (21 CFR Part 820).
- **Vaccines:** rapid-cycle batch, complex sterile, geopolitical priority.

## Regulatory landscape

- **FDA 21 CFR Part 210, 211** — current Good Manufacturing Practices for pharmaceutical drugs
- **FDA 21 CFR Part 11** — electronic records / electronic signatures
- **FDA 21 CFR Part 820** — medical device Quality System Regulation
- **DSCSA** — drug supply chain serialization
- **EU Annex 11** — computerized systems validation (EU)
- **ICH Q9** — quality risk management
- **ALCOA+** — data integrity principles

AVEVA MES batch records meet 21 CFR Part 11 out of the box; distributor implementation team handles validation per customer.

## Primary competitors

(Full battlecards in `content/competitors/`.)

| Competitor | Threat Tier |
|---|---|
| Rockwell (FactoryTalk + PharmaSuite) | Primary |
| Siemens (PCS7 + Opcenter Pharma) | Primary |
| Emerson (DeltaV + Syncade MES) | Primary |
| Werum PAS-X (Körber) | Primary in pharma-MES-only |
| Honeywell (Experion) | Secondary |
| GE Digital | Secondary in legacy |

## Notes for v0.2.0

This sub-skill ships as fast-follow. Full `content/industries/pharma-life-sciences.md` should be populated from the existing `Live MD Files - Optimized/pharma.md` content (which is real, not a stub). For v0.2.0 the existing file is referenced; for v0.2.5+ enriched with biologics-specific content and Werum competitor battlecard.
