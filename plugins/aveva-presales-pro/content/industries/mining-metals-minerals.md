---
industry: mining-metals-minerals
sub_segments: ["open-pit-mining", "underground-mining", "mineral-processing", "smelting-refining"]
last_validated: "2026-04-29"
distributor_focus: primary
provenance: "Adapted from prior consolidated MMM playbook (Nov 2025 revised edition); aligns with AVEVA + ETAP + EAE + PME unified portfolio narrative."
sources:
  - url: "https://www.aveva.com/en/industries/mining-metals-and-minerals/"
    type: "aveva_corporate"
    date: "2026-04-29"
  - url: "https://docs.aveva.com/bundle/pi-system/"
    type: "official_docs"
    date: "2026-04-29"
---

# Industry Playbook: Mining, Metals & Minerals (MMM)

## Executive Summary — Three Core Sales Truths

**1. The fragmentation crisis is real.** Mining, metals, and minerals companies operate blind to operational reality because process automation, electrical systems, and power management run in disconnected silos. SCADA, legacy DCS, separate historian platforms, and utility billing spreadsheets. The result: hidden inefficiency, reactive maintenance, energy waste, compliance risk.

Real-impact framing: a mid-size copper mine processing 100,000 tonnes/month with a milling circuit consuming 35 MW continuously sees motors and drive systems degrade invisibly across silos. Operators only know after catastrophic failure. 12-18 hours per event × 4-6 events annually = 48-108 lost production hours. At USD $250 per tonne refined copper revenue = USD 12-27M annualized opportunity loss from failures alone. [BENCHMARK · HIGH · SECONDARY]

**2. Digital integration pays measurable, immediate ROI.** Operators that unify process, automation, electrical, and power data into a single, model-driven platform see results within 90 days — not theoretical, but cash-verifiable.

Verified examples:
- **MMG Limited (multi-mine copper/cobalt):** AVEVA Production Management across 16 factories → 10-20% capacity improvement globally. Sepon mine: 12% above nameplate; Kinsevere: 34% above nameplate. Additional 29,422 tonnes copper in 2015. [VERIFIED · MEDIUM · PRIMARY: AVEVA case study]
- **Votorantim (Brazil, 16 facilities):** AVEVA Predictive Analytics → 10% reduction in recurring maintenance costs = BRL 23M year-1 savings; 6% reliability boost to 92%. [VERIFIED · MEDIUM · PRIMARY]
- **BHP Escondida Copper:** Granulometry-driven production loss reduced 70% monthly via digital twin → directly improved SAG mill throughput and ore-to-metal yield. [VERIFIED · MEDIUM · PRIMARY]
- **Rio Tinto Gudai-Darri:** Autonomous haulage + integrated digital twin → reduced operational costs, increased productivity; 150% improvement in final excavation phases. [VERIFIED · MEDIUM · PRIMARY]

**3. AVEVA + ETAP + EAE + PME is the only integrated backbone.** No competitor offers unified orchestration of process automation, electrical systems, software-defined automation, and power management in a single, secure, hardware-agnostic platform. (See `content/skills/portfolio-narrative` for the full positioning.)

## Industry Operating Environment — Five Pressures

**Declining ore grades globally.** Modern mining processes 3-10× more raw material per unit extracted metal vs. 20 years ago. Multiplies energy consumption, throughput demands, complexity. Typical open pit: ore grades declining 1-3% annually. [BENCHMARK · HIGH · SECONDARY]

**Energy / sustainability mandates clash with capital constraints.** ESG net-zero commitments demand 3% annual energy intensity cuts; capex flat or declining. Comminution alone consumes 25% of total mining energy. A 5% efficiency gain in comminution = ~30M tonnes CO2-e reduction globally. [BENCHMARK · HIGH · SECONDARY]

**Aging workforce.** Technical SMEs retiring; institutional knowledge departing. Replacement operators lack embedded historical context. Knowledge gaps worsen reactive maintenance and slow incident response.

**Capital cyclicality.** Commodity price volatility constrains long-cycle capex programs.

**Regulatory and stakeholder pressure.** ICMM principles, GISTM (tailings), MSHA, community accountability for water and emissions.

## Sub-Segment Detail

### Open-Pit Mining
**Operational profile:** primary crushing, comminution, autonomous haulage, dispatch optimization. Energy and reliability dominant.

**KPIs:** ore-to-mill throughput, mill availability, energy intensity per tonne, autonomous fleet utilization.

**Pain points → AVEVA capability:**
- Comminution unplanned downtime → PI System + ETAP integrated electrical health
- Autonomous fleet integration → System Platform + dispatch system OPC-UA
- Energy reporting for ESG → PME + AVEVA Connect data services

### Underground Mining
**Operational profile:** ventilation, hoist, drilling automation, ground control. Safety + electrical reliability dominant.

**KPIs:** development meters per shift, safety incident rate, ventilation power consumption, hoist availability.

**Pain points → AVEVA capability:**
- Ventilation power optimization → PME + ETAP for variable demand
- Hoist health monitoring → PI Asset Framework templates
- Underground SCADA → System Platform with edge nodes

### Mineral Processing
**Operational profile:** SAG / ball mills, flotation, leaching, dewatering. Energy intensity dominant.

**KPIs:** throughput, recovery, mill availability, kWh per tonne treated, reagent consumption.

**Pain points → AVEVA capability:**
- Mill drives reliability → ETAP + Schneider Altivar drives + PI Predictive Analytics
- Flotation circuit optimization → System Platform + advanced control + PI analytics
- Comminution energy → PME + EcoStruxure energy management

### Smelting / Refining
**Operational profile:** thermal processes, off-gas, environmental compliance, refinery yield.

**KPIs:** thermal efficiency, off-gas compliance, refinery recovery, energy intensity, environmental incidents.

**Pain points → AVEVA capability:**
- Off-gas environmental compliance → System Platform + automated reporting
- Thermal optimization → PI System + advanced analytics
- Energy intensity → full unified portfolio

## Regulatory Landscape

- **MSHA** (US Mine Safety and Health Administration) — federal mining safety
- **ICMM** (International Council on Mining and Metals) — voluntary 10 principles
- **GISTM** (Global Industry Standard on Tailings Management) — post-Brumadinho industry standard
- **ISO 14001** — environmental management
- **Local jurisdiction:** Texas RRC for produced-water-adjacent activities, Nevada/Utah/Arizona state mining bureaus

## Primary Competitors

(Full battlecards in `content/competitors/`.)

| Competitor | Threat Tier | Win Pattern (AVEVA) | Lose Pattern |
|---|---|---|---|
| Rockwell (FactoryTalk + PlantPAx) | Primary | Multi-vendor OPC-UA bridge to AB hardware; integrated electrical via ETAP | Strong AB ecosystem in grinding circuit automation |
| ABB (System 800xA + ABB Ability) | Primary | Foxboro DCS heritage + EcoStruxure energy + multi-vendor flexibility | Smelting incumbency; Power-Mining integrated stack |
| Siemens (PCS7 / WinCC / Opcenter) | Primary | US regional support + multi-vendor integration | European HQ multinationals with global Siemens standard |
| Honeywell (Experion) | Secondary | Multi-vendor SIS via best-in-class third-party | Refining-adjacent operators with locked Experion |
| Emerson (DeltaV / Plantweb) | Secondary | Process + electrical + energy unified | Upstream-mining with DeltaV process incumbency |
| GE Digital (Proficy iFIX) | Secondary in legacy mines | Active R&D investment | Deeply entrenched legacy iFIX users |

## Talk Tracks by Deal Stage

**Prospecting:** "Mining operators in your range typically lose USD 12-27M/year to fragmented automation between process, electrical, and power systems. MMG, Votorantim, and BHP have all unified their stack. Worth 20 minutes to walk through how the unified AVEVA + ETAP + EAE + PME approach plays in your operation?"

**Discovery (5 questions):**
1. "What's your unplanned downtime cost per event on the comminution train?"
2. "How are you tracking energy intensity per tonne — and where's that data sourced?"
3. "When you have a reactive maintenance event, how do process data, electrical telemetry, and power monitoring data tie together — or do they?"
4. "What's your ESG / Scope 2 reporting cadence — does the chain trace cleanly from mill to dashboard?"
5. "Aging workforce — how are you capturing operational know-how before the next 5-year wave of retirements?"

**Demo:** Lead with AVEVA PI Vision dashboards (on-prem) or CONNECT Visualization (cloud) showing combined process + electrical + power KPIs. For cloud customers, walk through **AVEVA Industrial AI Assistant** (GA Jan 2026) — natural-language query across mining operations data, role-based permissions, never trained on customer data. Layer the unified portfolio narrative. End with the customer references most relevant (copper → MMG/BHP/Escondida; iron ore → Rio Tinto; lithium / nickel → newer references).

**Proposal / TCO:** Energy intensity reduction is usually the most defensible line item (3-10% kWh per tonne savings). Reliability gains compound it (10-20% capacity improvement). ESG / Scope 2 reporting reduces compliance labor 50-70%.

**Closing:** Common objections are "we're a Rockwell shop" (counter: AVEVA on top of AB; multi-vendor flexibility), "energy is just utility cost" (counter: Scope 2 reporting + ICMM exposure), "too much change" (counter: phased deployment, electrical-first or process-first depending on customer).

## Recommended AVEVA Solution Tiers

- **Cost-Conscious:** Single mine, <2K tags. **AVEVA Operations Control — Edge** (InTouch Edge + AVEVA Edge) on Modicon M241 + Altivar drives.
- **Mid-Market:** Regional operator, 2-5 mines. **AVEVA Operations Control — Supervisory** (Plant SCADA + System Platform) + AVEVA PI System + ETAP integrated. PI Vision on-prem; CONNECT Visualization for cloud-evaluating customers.
- **Enterprise:** Global multi-mine. **AVEVA Operations Control — Enterprise** (Unified Operations Center capability + System Platform full) + AVEVA PI System Enterprise + ETAP + EAE + PME unified portfolio.

## Specific Guidance for Q-Mation Territory

Q-Mation's Mountain West expansion brings major mining accounts:
- **Copper / molybdenum** — Arizona (Phelps Dodge / Freeport, Asarco)
- **Gold / silver** — Nevada (Newmont, Barrick)
- **Lithium** — Nevada / Utah greenfield expansion
- **Coal** — Wyoming (declining but still large operators)
- **Iron ore** — Utah / Wyoming
- **Phosphate / potash** — Utah

These represent meaningful expansion from the Gulf Coast core. The unified portfolio narrative is especially strong here because the operators are running modernization programs explicitly tied to ESG mandates.

## Notes for Verification Subagent

- Trusted public sources: docs.aveva.com mining bundle; aveva.com case studies for MMG, Votorantim, BHP, Rio Tinto.
- Most-stale-prone: ICMM principle updates; GISTM standard revisions; commodity price impact on capex.
- Watch for: AVEVA + Schneider mining-specific customer announcements; competitor moves in mining digital.
