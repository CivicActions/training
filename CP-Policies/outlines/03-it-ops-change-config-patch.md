# Training 3 — IT Operations: Change, Configuration & Patch Management

| Field | Value |
|-------|-------|
| **Audience** | IT / Service Desk, Developers, System/Data Owners |
| **Prerequisite** | Training 1 (Security Awareness Essentials) |
| **Target duration** | 15–20 minutes |
| **Delivery** | Written module + quiz |
| **Cadence** | Onboarding (within 30 days) · annual refresher · ad-hoc on material policy change |
| **Compliance** | CMMC L2 CM.L2-3.4.1–3.4.9, MA.L2-3.7.1–3.7.6, SI.L2-3.14.1–3.14.7 · ISO 27001 A.8.9, A.8.32 |

---

## Purpose

This training covers the technical "guardrails" that IT, developers, and system owners operate within: configuration management, change enablement, vulnerability and patch management, endpoint posture, and disaster recovery operations. These are the policies that general staff only need awareness of — this audience needs to execute them.

---

## Session outline

### Module A — Configuration management (4–5 min)

**Outcome sources:** CMP, MP

1. **CI scope** — five CI classes under formal control: CIA "High" systems, managed endpoints, cloud resources, production SaaS configs, critical documentation
2. **Configuration-as-code** — Git is the authoritative baseline; Git history is the change history; Jira/Confluence links to repos and pipelines
3. **Baselines and secure defaults** — apply least functionality (remove non-essential services/components); include hardening, identity/access parameters, logging hooks; review at least annually
4. **Drift detection** — automated detection generates tickets triaged within two business days; resolve by reconciling to baseline or raising a change request
5. **Evidence and audit** — retain CI inventories, baselines, change histories, drift reports, and approvals as Controlled Records

### Module B — Change enablement (4–5 min)

**Outcome sources:** CEP, MP

1. **Change classes** — Standard (fully automated, pre-approved), Normal (peer-reviewed PR/MR, delegated approval), Significant (affects High Impact services, formal Change Record + Change Authority approval), Emergency (Incident Commander authorized)
2. **Change record content** — description, impacted services/CIs, impact, urgency, risk assessment, test results, implementation plan, backout plan, maintenance window, evidence
3. **Approvals and guardrails** — Normal: peer review + automated tests; Significant: Change Authority + rollback plan; Emergency: IC approval + subsequent review
4. **Scheduling** — each service has a weekly maintenance window and monthly company calendar slot; changes outside windows require justification and approval
5. **Post-implementation review** — verify changes, update config records; retrospective within 5 business days when needed; capture lessons learned
6. **Change freezes** — applied during critical delivery periods or exceeded error budgets; only stability-improving fixes permitted

### Module C — Vulnerability and patch management (3–4 min)

**Outcome sources:** VPM, MP

1. **Discovery methods** — MDM/EDR for endpoints, SBOMs + SCA/SAST/DAST for custom software, vendor advisories for SaaS, approved lists for browser/IDE/SaaS extensions
2. **Prioritization** — severity + exploitability signals, then service criticality and data sensitivity; confirm applicability before assigning targets
3. **Remediation timelines** — Critical 15 days, High 30 days, Medium 60 days, Low best effort; timelines tighten during active exploitation; exceptions require CISO approval
4. **Staged deployment** — MDM alpha → beta → company-wide for endpoint patches; SaaS config changes validated in test/staging tenants; patch waves are Standard changes
5. **Anti-malware** — maintain current signatures; periodic system scans and real-time scans of files from external sources
6. **Verification** — re-scan or functional validation; attach evidence to ticket; reports and tickets are Controlled Records

### Module D — Endpoint posture and privileged access (2–3 min)

**Outcome sources:** ACP, IdP, MP, DSHP

1. **Privileged account separation** — separate admin account for elevated work; standard account for daily tasks; apply the six-question privilege test before requesting elevated access
2. **NPI (non-person identity) management** — service accounts use descriptive naming, linked ownership, quarterly credential rotation (immediate on exposure)
3. **Break-glass procedures** — sealed emergency credentials, dual-control access, mandatory post-use audit and rotation
4. **MDM posture evidence** — remote wipe records, compliance reports, ITAD certificates, device sanitization via cryptographic erasure (FileVault/LUKS key destruction via MDM)

### Module E — Disaster recovery operations (2–3 min)

**Outcome sources:** DRP

1. **Incident classification** — Low (minor, workaround), Medium (service unavailable, business impact), High (multiple critical systems), Critical (prolonged outage, external impact)
2. **System-specific recovery** — know primary/fallback channels and org actions for each critical system (Google Workspace, Slack, Zoom, Kandji/Iru, Atlassian, Unanet, GitHub, GitLab, Rippling, Culture Amp)
3. **Backup ownership** — primary backups managed by SaaS providers; admin access limited and documented; use export/backup features where available
4. **Testing and maintenance** — DRP reviewed annually; vendor DR assurances reviewed annually; tabletop exercises as appropriate
5. **Post-incident review** — document timeline and impact; review response effectiveness; track improvement actions

---

## Quiz (sample — 4 questions)

1. **A vulnerability scan identifies a Critical severity flaw in a production system. What is the remediation target?**
   - a) Best effort during the next scheduled update
   - b) 60 days
   - c) 15 days ✅
   - d) 30 days

2. **You need to change a Google Workspace security setting that affects all CivicActions users. How should this change be classified?**
   - a) Standard — it's just a settings toggle
   - b) Significant — it affects a company-wide service and requires a formal Change Record and Change Authority approval ✅
   - c) No classification needed for SaaS configuration changes
   - d) Emergency — all company-wide changes are emergencies

3. **Automated drift detection flags a configuration deviation on a production system. What is the required response?**
   - a) Ignore it if the system is working
   - b) Triage within two business days; resolve by reconciling to baseline or raising a change request ✅
   - c) Immediately roll back all recent changes
   - d) Wait for the annual baseline review

4. **Google Workspace experiences a prolonged outage. Why is it classified as the highest-priority recovery?**
   - a) It has the most storage
   - b) It is the SSO/identity provider — all other services depend on it for authentication ✅
   - c) Email is the most-used feature
   - d) It's the cheapest to restore

---

## Outcome coverage

This training covers IT/Developer/System Owner rows from:

- [config-mgmt-outcomes.md](../outcomes/config-mgmt-outcomes.md) — 6 rows (all)
- [change-enablement-outcomes.md](../outcomes/change-enablement-outcomes.md) — 6 rows (all)
- [vuln-patch-outcomes.md](../outcomes/vuln-patch-outcomes.md) — 5 IT-specific rows
- [maintenance-outcomes.md](../outcomes/maintenance-outcomes.md) — 5 IT-specific rows
- [disaster-recovery-outcomes.md](../outcomes/disaster-recovery-outcomes.md) — 4 IT-specific rows
- [access-control-outcomes.md](../outcomes/access-control-outcomes.md) — privileged access rows (4)
- [identification-outcomes.md](../outcomes/identification-outcomes.md) — NPI/admin rows (3)
- [data-security-outcomes.md](../outcomes/data-security-outcomes.md) — encryption/key mgmt IT rows (2)
