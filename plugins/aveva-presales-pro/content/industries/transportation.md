---
industry: transportation
sub_segments: ["rail-transit", "ports-terminals", "airports", "highways-smart-mobility"]
last_validated: "2026-04-29"
distributor_focus: primary
provenance: "Adapted from prior Unified Transportation Playbook (Nov 2025); aligns with AVEVA + ETAP + EAE + PME unified portfolio."
sources:
  - url: "https://www.aveva.com/en/industries/transportation/"
    type: "aveva_corporate"
    date: "2026-04-29"
---

# Industry Playbook: Transportation Infrastructure

## Executive Summary

Transportation infrastructure operators face an inflection point: federal IIJA + state programs are unlocking unprecedented capital, but the ability to absorb it is limited by fragmented operations technology stacks. Operators who unify SCADA / historian / electrical / energy onto a single platform see 15-20% operational efficiency gains and accelerate decarbonization roadmaps simultaneously. AVEVA + ETAP + EAE + PME is the only integrated platform that addresses all four domains for transportation.

## Industry Operating Environment

**Federal capital wave.** IIJA provides $1.2T in infrastructure investment authority, much of it transportation-bound (highways, transit, rail, airports, ports). State and local agencies have larger capex than absorption capacity has historically supported.

**Decarbonization mandate.** Rail electrification (PTC was just the beginning), EV port equipment (drayage, ground power, gantry cranes), airport ground-power conversion, transit electrification. Electrical and energy systems become operationally critical, not just utility expenses.

**Operational complexity.** Multi-modal coordination (rail-port, rail-transit, transit-bus), real-time passenger and freight visibility, resilience and security overlays. Traffic Operations Centers integrate dozens of systems.

**Aging infrastructure + workforce transitions.** Same workforce challenges as other heavy industries.

## Sub-Segment Detail

### Rail and Transit

**Operational profile:** signal systems (PTC, CBTC), traction power substations, rolling stock health, station HVAC + lighting + safety, yard operations.

**KPIs:** on-time performance, MDBF (Mean Distance Between Failures), traction power energy per vehicle-mile, station availability, dwell time.

**Pain points and solutions:**
- Traction power reliability → ETAP electrical digital twin + PME real-time monitoring + System Platform integration
- Predictive maintenance for rolling stock → PI System Asset Framework templates per vehicle class
- Station environmental control → EcoStruxure Building + System Platform integration
- PTC integration with operations → System Platform with secure OPC-UA bridge

### Ports and Terminals

**Operational profile:** container terminals, bulk handling, gantry cranes, conveyors, intermodal yards, TOS integration, gate operations.

**KPIs:** TEU per hour, crane availability, energy per move (intensifies with electrification), gate turnaround time, dwell time.

**Pain points and solutions:**
- Crane health monitoring → PI System + Asset Framework
- Port electrification (shore power, electric drayage, EV ground equipment) → ETAP design + PME monitoring + EcoStruxure energy
- TOS integration → System Platform OPC-UA / REST adapters
- ESG / Scope 2 reporting → PME aggregation + AVEVA Connect data services

### Airports

**Operational profile:** baggage handling, fueling, ground power conversion, passenger boarding bridges, terminal HVAC, security infrastructure.

**KPIs:** on-time turnaround, baggage system availability, energy per passenger, fuel system reliability.

**Pain points and solutions:**
- Baggage handling system reliability → PI Predictive Analytics
- Ground power conversion (eGPU) → ETAP electrical design + PME monitoring
- Terminal energy → EcoStruxure Building + PME

### Highways and Smart Mobility

**Operational profile:** Traffic Operations Centers (TOCs), dynamic message signs, ramp metering, tolling integration, weather and incident response, ITS device fleets.

**KPIs:** travel time reliability, incident detection / response time, system availability across distributed devices.

**Pain points and solutions:**
- Multi-system TOC integration → System Platform + PI System
- ITS device fleet monitoring → System Platform with distributed edge
- Tolling system integration → System Platform secure adapter

## Regulatory Landscape

- **DOT** — broad transportation oversight
- **FRA** — rail safety, PTC enforcement
- **FAA** — airport infrastructure standards
- **FTA** — transit funding and Buy America provisions
- **FMCSA** — commercial motor carrier
- **TSA** — security overlays
- **State DOTs** — smart corridor and ITS standards

## Primary Competitors

| Competitor | Threat Tier | Win Pattern (AVEVA) | Lose Pattern |
|---|---|---|---|
| Siemens (Mobility) | Primary | US regional support; multi-vendor; integrated electrical via ETAP | European-HQ rail operators with global Siemens standard |
| Rockwell | Primary in some transit | Process-industry maturity | Discrete-AB heritage operators |
| ABB | Primary | Foxboro + EcoStruxure energy unified | Marine port + electric rail incumbency |
| Hitachi Rail | Niche | AVEVA open architecture | Hitachi-specific rolling stock contracts |
| Honeywell | Secondary | Multi-vendor SIS | Airport security incumbency |

## Talk Tracks by Deal Stage

**Prospecting:** "Transportation operators absorbing IIJA capital are running into operations-tech fragmentation that costs 15-20% in efficiency. Decarbonization roadmaps amplify the issue — every electrical conversion adds to the integration burden. Worth 30 minutes to walk through how MMG-style unified-portfolio plays in your domain?"

**Discovery:** Same 5-question framework as the SKILL.md describes.

**Demo:** Lead with AVEVA PI Vision combined dashboards (on-prem) or CONNECT Visualization (cloud) — operations + electrical + energy in one view. **AVEVA Industrial AI Assistant** (GA Jan 2026) layers on CONNECT data with natural-language query — strong for TOC operators querying multi-system status. Customer-specific examples per sub-segment.

**Proposal / TCO:** Energy intensity reduction is again the most defensible top-line metric. Reliability gains (10-20% MDBF improvement) compound it. Compliance and reporting automation reduces labor 50-70%.

**Closing:** Common objections are "Siemens is our standard" (counter: AVEVA on top of Siemens hardware, multi-vendor flexibility, US regional support); "we're already running ETAP separately" (counter: integrate ETAP with AVEVA via the Integration Service for compounding value).

## Recommended AVEVA Solution Tiers

- **Cost-Conscious:** Single station / small terminal. **AVEVA Operations Control — Edge** + Modicon.
- **Mid-Market:** Regional transit / mid-port / mid-airport. **AVEVA Operations Control — Supervisory** + AVEVA PI System + ETAP integrated. PI Vision on-prem; CONNECT Visualization for cloud-evaluating customers.
- **Enterprise:** Class I rail / major port / hub airport. **AVEVA Operations Control — Enterprise** + full unified portfolio (System Platform + PI System Enterprise + ETAP + EAE + PME).

## Specific Guidance for Q-Mation Territory

Q-Mation's Gulf Coast / Mountain West / Southwest expansion brings substantial transportation accounts:
- **Texas Gulf Coast ports:** Houston, Galveston (largest container terminals in Gulf).
- **Texas freight rail:** BNSF, Union Pacific.
- **Southwest airports:** Phoenix, Las Vegas, Salt Lake City, Albuquerque hub airports.
- **Texas / Mountain West highways:** TxDOT, NMDOT, AzDOT smart-corridor programs.
- **Transit:** Houston METRO, Dallas DART, Phoenix METRO Light Rail.

The unified-portfolio narrative is especially strong here because most of these operators are doing concurrent decarbonization + capital expansion programs.
