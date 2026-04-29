---
product: "AVEVA CONNECT Visualization"
category: "visualization_software"
last_validated: "2026-04-29"
confidence: "HIGH"
sources:
  - url: "https://www.aveva.com/en/products/connect/"
    type: "aveva_official"
    date: "2026-04-29"
  - url: "https://docs.aveva.com/bundle/connect-visualization/"
    type: "official_docs"
    date: "2026-04-29"
---

# AVEVA CONNECT Visualization

## What it is

Composable browser-based dashboarding for industrial operations. Combines real-time data from AVEVA CONNECT data services with multiple data types and formats — including third-party — and presents through any browser on any device.

## How it relates to PI Vision

| | PI Vision | CONNECT Visualization |
|---|---|---|
| Deployment | On-prem (with PI System) | Cloud (with CONNECT data services) |
| Data sources | PI System Asset Framework | CONNECT data services + multiple types and formats |
| Hosting | Customer-hosted | AVEVA-hosted (CONNECT) |
| Best for | Existing on-prem PI customers | Cloud-evaluating + new builds + multi-vendor data integration |

These are complementary, not replacements. Many customers run both — PI Vision for existing on-prem users, CONNECT Visualization for browser-based composable dashboards on cloud-stored data.

## Demo positioning

**On-prem customers:** lead with PI Vision dashboards. The on-prem story is mature.

**Cloud-evaluating customers:** lead with CONNECT Visualization. Composable, browser-based, works on any device, integrates third-party data formats.

**Hybrid customers (most enterprise customers):** show both. Same Asset Framework model under the hood; visualization layer chosen by deployment context.

## Embedded AI

CONNECT Visualization is the host for AVEVA Industrial AI Assistant (GA January 2026). The natural-language query layer runs in the browser, on top of the same dashboards.

## Refresh policy

Quarterly review via source-validation scheduled task.
