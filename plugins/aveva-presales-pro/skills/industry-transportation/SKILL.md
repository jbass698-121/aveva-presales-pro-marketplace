<!--
Copyright (c) 2026 Jason Bass. All rights reserved.
Licensed under the Business Source License 1.1. See LICENSE.md.
Watermark: appro-ca96e5c3-e535-40b4-a502-9e85523f608e
This file is a Category 3 protected component per MODIFICATION-POLICY.md.
-->
---
name: aveva-industry-transportation
description: AVEVA presales positioning for transportation infrastructure — rail, transit, ports, airports, highways, smart mobility, traffic operations centers. Activates on transportation keywords (transportation, transit, rail, light rail, metro, subway, port, airport, terminal, highway, motorway, intelligent transportation system, ITS, traffic operations center, TOC, mobility, fleet, freight, logistics) and regulatory framing (DOT, FRA, FAA, FMCSA, FTA).
---

# AVEVA Transportation Industry Skill

You are loaded for transportation infrastructure conversations. Drives the unified portfolio narrative across rail, ports, airports, transit, and highways.

## The transportation thesis

Transportation infrastructure operators face a defining moment. Three forces:

1. **Aging infrastructure + capital backlog.** Federal IIJA / state programs are unlocking capital but capacity to absorb it lags.
2. **Decarbonization.** Rail electrification, EV port equipment, airport ground-power conversion. Electrical and energy systems become operationally critical.
3. **Operational complexity.** Multi-modal coordination, real-time passenger / freight visibility, security and resilience.

The unified Schneider + AVEVA story plays particularly well in transportation because:
- **AVEVA System Platform** consolidates SCADA across rail signal, station, and yard.
- **PI System** provides historian intelligence for asset reliability across rolling stock and fixed infrastructure.
- **ETAP** is critical for traction power, station electrical reliability, and microgrid design.
- **PME** addresses station-and-facility energy management plus sub-metering for ESG reporting.
- **EAE (EcoStruxure Automation Expert)** offers software-defined automation portable across station deployments.

## Sub-segments

### Rail and Transit
**Operational profile:** signal systems, traction power, vehicle monitoring, station HVAC and safety, yard operations.
**KPIs:** on-time performance, mean distance between failures, energy per vehicle-mile, station availability.
**Pain points → AVEVA capability:**
- Traction power reliability → ETAP + PME + System Platform
- Predictive maintenance for rolling stock → PI System + AIM
- Station HVAC and safety → System Platform + EcoStruxure Building

### Ports and Terminals
**Operational profile:** container terminals, bulk handling, gantry cranes, conveyor systems, terminal operating system integration.
**KPIs:** TEU per hour, crane availability, energy per move, gate turnaround.
**Pain points → AVEVA capability:**
- Crane health monitoring → PI System + Asset Framework
- Energy intensity (port electrification, shore power) → ETAP + PME + EcoStruxure
- TOS integration → System Platform OPC-UA / REST

### Airports
**Operational profile:** baggage handling, fueling systems, ground power, passenger boarding bridges, terminal HVAC.
**KPIs:** on-time aircraft turnaround, baggage system availability, energy per passenger.
**Pain points → AVEVA capability:**
- Baggage handling system reliability → PI System + System Platform
- Ground power conversion → ETAP electrical design + PME monitoring
- Terminal energy → EcoStruxure Building + PME

### Highways and Smart Mobility
**Operational profile:** traffic operations centers, dynamic message signs, ramp metering, tolling, weather and incident response.
**KPIs:** travel time reliability, incident response time, system availability.
**Pain points → AVEVA capability:**
- Multi-system traffic operations → System Platform + PI System
- ITS device monitoring → System Platform with edge nodes
- Energy management at facilities → PME + ETAP

## Regulatory landscape

- **DOT** (US Department of Transportation) — broad transportation oversight
- **FRA** (Federal Railroad Administration) — rail safety, PTC mandate
- **FAA** (Federal Aviation Administration) — airport infrastructure
- **FTA** (Federal Transit Administration) — transit funding and standards
- **FMCSA** — commercial motor carrier safety
- **State and local DOTs** — smart corridor and ITS programs
- **TSA** — security overlays at airports and rail / transit

## Primary competitors

| Competitor | Threat Tier | Win Pattern (AVEVA) |
|---|---|---|
| Siemens (Mobility) | Primary | US regional support; multi-vendor flexibility |
| Rockwell | Primary in some transit | Process-industry maturity for traction + station |
| ABB | Primary | Foxboro + EcoStruxure energy management combined |
| Honeywell | Secondary | Multi-vendor SIS via third-party |
| Hitachi (Rail) | Niche | AVEVA's open architecture |

## Talk tracks

**Prospecting:** "Transportation operators are wrestling with capital backlog and decarbonization at the same time. The fragmentation between operations, electrical, and energy systems is costing 15-20% in efficiency. Worth 30 minutes to walk through how the unified Schneider + AVEVA stack plays?"

**Discovery (5 questions):**
1. "What's your asset reliability dashboard look like — single view across rolling stock, fixed infrastructure, and traction power?"
2. "How is your traction-power / ground-power / facility-power energy data flowing into ESG reporting?"
3. "When PTC / signal / terminal systems all generate alarms, how are operators correlating them?"
4. "What's your decarbonization roadmap — where are the electrical conversions happening?"
5. "Workforce — how are you preserving operational know-how through fleet refresh cycles?"

## Recommended Solution Tiers

- **Cost-Conscious:** Single station / small terminal. InTouch + Modicon.
- **Mid-Market:** Regional transit / mid-sized port. System Platform + PI System + ETAP.
- **Enterprise:** Class I rail / major port / hub airport. Unified Operations Center + full unified portfolio.

## Reference files

- `content/industries/transportation.md`
- Public sources: docs.aveva.com transportation bundle; aveva.com transportation case studies; FTA / DOT public reports.
