# Training 4 — Incident Response for Responders

| Field | Value |
|-------|-------|
| **Audience** | IT / Service Desk, SIRT members, Managers |
| **Prerequisite** | Training 1 (Security Awareness Essentials) |
| **Target duration** | 10–15 minutes |
| **Delivery** | Written module + quiz |
| **Cadence** | Onboarding (within 30 days) · annual refresher · after significant incident (lessons learned) |
| **Compliance** | CMMC L2 IR.L2-3.6.1–3.6.3 · ISO 27001 A.5.24–A.5.28 |

---

## Purpose

Training 1 teaches all staff to report incidents. This training teaches responders how to handle them: the IRP phases, evidence preservation, communications protocol, recovery objectives, and post-incident improvement. Managers attend for their responsibilities in escalation, client notifications, and communications approval.

---

## Session outline

### Module A — IRP structure and phases (3–4 min)

**Outcome sources:** IRP

1. **Document hierarchy** — IRP (principles and authority), Incident Response Checklist (step-by-step), Contingency Plan (recovery targets and DR integration)
2. **Six phases** — Breath, Document, Initiate, Assess, Remediate, Conclude; safety and containment come first
3. **Incident declaration** — Incident Commander declares incidents and assigns severity; security risks during operational outages are treated as security incidents
4. **Guiding principles** — reversible actions first, least-privilege, blast-radius-limiting; err on the side of containment

### Module B — Evidence and forensics (2–3 min)

**Outcome sources:** IRP

1. **Preservation** — preserve logs, images, and artifacts with chain of custody; do not delete, reimage, or disable logging without SIRT direction
2. **Coordination** — coordinate with SIRT before acquiring, copying, or analyzing data
3. **Controlled Records** — all incident records (logs, timelines, decisions, artifacts) are Controlled Records subject to retention policy

### Module C — Communications and escalation (2–3 min)

**Outcome sources:** IRP

1. **Communications Officer** — all external and formal internal incident communications go through the Communications Officer using approved channels and templates
2. **Update standards** — factual, time-stamped, audience-appropriate; no speculation or attribution in early updates
3. **Client and third-party notifications** — escalate supplier incidents that may affect CivicActions or client data; contracts (especially CUI/DoD) may require time-bound external reporting (typically 72 hours, some 24 hours)
4. **Need-to-know** — incident details on need-to-know basis; no disclosure outside designated channels without IC or CO approval

### Module D — Recovery and emergency changes (1–2 min)

**Outcome sources:** IRP, DRP

1. **Recovery targets** — set by system criticality and the Contingency Plan; Google Workspace (identity) is highest priority
2. **Emergency changes** — Incident Commander authorizes; document during or immediately after; formal review follows within 5 business days
3. **Service restoration** — verify system integrity before restoring access; confirm containment before closing incident

### Module E — Post-incident learning (1–2 min)

**Outcome sources:** IRP, RSAP

1. **Retrospective** — conduct within 5 business days of incident closure; blameless format; document timeline, impact, response effectiveness
2. **Risk integration** — lessons learned update the Risk Register and create POA&Ms; track through continual improvement process
3. **Personnel matters** — handled by PeopleOps separately; not part of the IR process or retrospective
4. **Compliance and enforcement** — violations may result in access revocation, disciplinary action, or contract remedies

---

## Quiz (sample — 3 questions)

1. **You notice unusual login attempts on a system you manage. What should you do first?**
   - a) Investigate thoroughly and fix the issue yourself before telling anyone
   - b) Report the suspected incident immediately using IRP-designated channels ✅
   - c) Delete the suspicious logs to prevent further access
   - d) Wait to see if it happens again before reporting

2. **You receive a notification that a SaaS service used by CivicActions has experienced a data breach. What is the correct first step?**
   - a) Immediately cancel the SaaS subscription
   - b) Report the vendor incident to security@civicactions.com so it can be escalated under the IR Policy ✅
   - c) Post about it in a public Slack channel so everyone is aware
   - d) Wait for the vendor to contact CivicActions directly

3. **During an active incident, a journalist contacts you asking for details. What do you do?**
   - a) Provide basic facts to be transparent
   - b) Refer all media inquiries to the Communications Officer — do not disclose incident details without IC/CO approval ✅
   - c) Say "no comment" and hang up
   - d) Direct them to the company website

---

## Outcome coverage

This training covers IT/SIRT/Manager rows from:

- [incident-response-outcomes.md](../outcomes/incident-response-outcomes.md) — 7 responder rows
- [disaster-recovery-outcomes.md](../outcomes/disaster-recovery-outcomes.md) — recovery/emergency change context
- [risk-security-outcomes.md](../outcomes/risk-security-outcomes.md) — post-incident risk integration
