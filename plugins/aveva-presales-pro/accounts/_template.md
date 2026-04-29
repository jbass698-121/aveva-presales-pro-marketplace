---
account: "<<Customer name>>"
account_id_dynamics: "<<CRM record ID>>"
industry: "<<vertical from distributor.config.verticals>>"
sub_segment: "<<>>"
tier: "<<cost_conscious | mid_market | enterprise>>"
region: "<<>>"
distributor_se_owner: "<<email or username>>"
distributor_ae_owner: "<<email or username>>"
isolation: "per_ae"                          # per_ae | per_team | shared
shared_with: []                              # ["team-gulf-coast"] — opt-in only
deal_status: "active"                        # active | dormant | closed-won | closed-lost
last_updated: "2026-04-29T00:00:00Z"
created: "2026-04-29T00:00:00Z"
retention_state: "active"                    # active | archive_pending | archived
sensitive_data_redacted: true
---

# Account Memory: <<Customer name>>

> **Privacy boundaries.** This file contains internal-only context. The orchestrator and verifier strip raw quotes, posture annotations, and margin references from any customer-facing artifact. Memory is per-AE-isolated by default.

## Account snapshot

<<3-5 sentences: who they are, what they do, scale, current SCADA / DCS landscape, why they're in our pipeline.>>

## Stakeholder map

| Name | Role | Posture | Last contacted | Source | Notes |
|---|---|---|---|---|---|
| <<>> | <<>> | <<champion / supporter / neutral / detractor / unknown>> | <<date>> | <<CRM, Fireflies, email>> | <<>> |

## Pain points known

(Tracked across meetings; chronological order, latest first.)

- **<<2026-04-15>>** [SOURCE: fireflies meeting]: <<pain>>
- **<<2026-04-01>>** [SOURCE: email thread with VP Operations]: <<pain>>

## Decision criteria revealed

(What we know about how they buy.)

- <<criteria 1>> [SOURCE: <<>>]
- <<criteria 2>> [SOURCE: <<>>]

## Competitive landscape

- **Primary competitor of record:** <<name>>
- **Last competitor move:** <<>>
- **Our last counter:** <<>>

## History (chronological event log)

### 2026-04-15 — Fireflies meeting (90 min)
- Attendees: <<>>
- Key points: <<>>
- Action items: <<>>

### 2026-04-01 — Email thread, VP Operations
- Subject: <<>>
- Headline: <<>>

### 2026-03-15 — Discovery call
- <<>>

## Lessons learned (post-close — populated by win-loss-loop skill)

(Empty for active accounts. Populated when deal closes.)

## Sensitive data scrub log

(Auto-maintained. Records what was scrubbed and why.)

- 2026-04-29: Sensitive pattern detected and removed from history entry [redacted: SSN-shaped string].

## Retention state

- **Active retention:** indefinite
- **Next review:** <<set per distributor.config.account_memory.retention rules>>
