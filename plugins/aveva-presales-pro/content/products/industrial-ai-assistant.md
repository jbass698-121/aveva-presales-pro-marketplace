---
product: "AVEVA Industrial AI Assistant"
category: "ai_capability"
status: "GA"
ga_date: "2026-01"
last_validated: "2026-04-29"
confidence: "HIGH"
sources:
  - url: "https://www.aveva.com/en/connect-experience/about-connect/industrial-ai-assistant/"
    type: "aveva_official"
    date: "2026-04-29"
  - url: "https://docs.aveva.com/bundle/connect-visualization/page/1388805.html"
    type: "official_docs"
    date: "2026-04-29"
  - url: "https://www.aveva.com/en/about/news/press-releases/2026/aveva-unveils-new-artificial-intelligence-offering-across-its-unified-engineering-solution/"
    type: "aveva_press_release"
    date: "2026-04-29"
---

# AVEVA Industrial AI Assistant

## What it is

A generative-AI conversational assistant embedded in AVEVA CONNECT. Users ask industrial-specific questions in natural language; the assistant retrieves and summarizes process values, dashboards, trends, and documents from CONNECT data services.

## Status

**GA — January 2026.** Available to all users of CONNECT visualization. Not a beta or private preview.

## Capabilities

- **Natural-language query** across industrial data sources in CONNECT
- **Retrieval and summarization** of process values, dashboards, trends, documents
- **Role-based permission awareness** — respects user permissions defined in CONNECT
- **Secure data access** — never trained on customer data; processes information already stored in CONNECT
- **Minimal pre-configuration** — works against existing CONNECT data without re-architecting

## Related AVEVA AI products (same wave, January 2026)

- **Generative Design AI Assistant** — Unified Engineering. Generates layout options under user-specified constraints.
- **Predictive Design AI Assistant** — Unified Engineering. Customer-trained ML models without coding.
- **Intelligent Point Cloud Framework** — AVEVA Point Cloud Manager. Auto-import and AI-classification of point cloud data.

## Competitive context

| Vendor | AI assistant for operations data | Notes |
|---|---|---|
| AVEVA (Schneider) | Industrial AI Assistant | GA Jan 2026 — production-ready conversational AI on operations data |
| Rockwell | FactoryTalk Design Studio Copilot (Microsoft Azure OpenAI) + NVIDIA Nemotron Nano edge SLM | Available; targeted at engineering / code generation |
| Siemens | Industrial Copilot (joint with Microsoft) | Available; targeted at TIA Portal automation code, not operations data |
| Honeywell | Forge AI features | Within Honeywell stack; cybersecurity-led positioning + Quantinuum quantum-crypto roadmap |
| Emerson | DeltaV + Plantweb AI; AspenTech AI (since March 2025 take-private) | Within Emerson stack |
| Ignition (Inductive Automation) | Vision AI module; Cloud Edition AI features in development | Maturing |

## How to use in customer conversations

**For customers asking about AI:** lead with what AVEVA has GA today (Industrial AI Assistant, since January 2026), not with roadmap claims. The assistant works against the customer's existing CONNECT data — there is no big training project.

**For customers worried about data privacy:** "Never trained on customer data" is a real claim. Contrast with self-hosted competitor AI features that may train on customer-specific data without equivalent guardrails.

**For customers comparing to Microsoft + Rockwell or Microsoft + Siemens:** AVEVA + Databricks (Manufacturing ISV Partner of the Year 2025) is the comparable IT-OT data-fabric story; CONNECT + Databricks via Delta Sharing is in production today.

## Refresh policy

This file's claims should be re-verified monthly via the source-validation scheduled task. AI capabilities evolve fast; capability descriptions go stale within ~3 months.
