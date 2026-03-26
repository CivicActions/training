# Training 1 — Security Awareness Essentials

| Field | Value |
|-------|-------|
| **Audience** | All Staff (every team member, contractor, intern, third party with system access) |
| **Prerequisite** | None |
| **Target duration** | 30–40 minutes |
| **Delivery** | Written module + quiz |
| **Cadence** | Onboarding (within 30 days) · annual refresher · ad-hoc on material policy change |
| **Compliance** | CMMC L1 basic safeguarding awareness · CMMC L2 AT.L2-3.2.1 · ISO 27001 A.6.3 / 7.2 / 7.3 |

---

## Purpose

This is the foundational security training that every CivicActions team member completes. It covers the core behaviors and responsibilities needed to protect CivicActions systems, data, and clients — from day-to-day device security to recognizing and reporting incidents. It draws on all 17 security policies but focuses on what every individual needs to know and do.

---

## Session outline

### Module A — Your devices and workspace (8–10 min)

**Outcome sources:** AUP, MP, PSP, IdP

1. **Managed device requirement** — CivicActions-managed laptop (FDE, EDR, firewall, auto-lock, patching) is mandatory for Internal/Confidential/client work; BYOD mobile is MFA/comms only with MDM profile isolation
2. **Software rules** — use only the Approved Software Catalog; understand the Prohibited Hardware and Software list; new software requests follow the access and authorization workflow; MDM blocks unapproved installs
3. **Home workspace security** — control screen visibility, secure/shred printed material same-day, keep devices under your control, protect from environmental hazards
4. **Networks and Wi-Fi** — use WPA2/WPA3 encrypted Wi-Fi or wired Ethernet; change default router admin password; use personal hotspot if secure Wi-Fi is unavailable; never bypass TLS warnings
5. **Travel and public locations** — keep devices with you; lock screen when away; avoid screen visibility of sensitive info; use encrypted Wi-Fi or hotspot (never open public Wi-Fi); avoid printing sensitive material while traveling
6. **Non-compliant devices** — MDM enforces minimum OS and patch levels; non-compliant devices are flagged, ticketed, and automatically blocked until remediation

### Module B — Your identity and access (5–7 min)

**Outcome sources:** IdP, ACP, ISP

1. **CivicActions identity** — your @civicactions.com account is your primary identity; personal accounts are never used for CivicActions work; know the standard naming convention
2. **SSO and MFA** — use SSO wherever available; enroll two FIDO2/WebAuthn hardware keys (primary + backup); phishing-resistant MFA is preferred over SMS/TOTP
3. **Password standards** — minimum 20 characters for human accounts; memorize and use a password manager; never reuse passwords across services
4. **Access requests** — request access through the defined process; access is granted on least-privilege and need-to-know basis; notify IT promptly on role changes or departures
5. **Project boundary awareness** — access is scoped per project/client engagement; do not access systems or data outside your assigned scope; access automatically reviewed at project transitions

### Module C — Data handling and classification (5–7 min)

**Outcome sources:** DSHP, ISP, AUP

1. **Four classification levels** — Public, Internal, Confidential, Restricted; all data is Internal by default until explicitly classified otherwise
2. **Handling rules by level** — know the sharing, storage, and transmission rules for each level; Confidential/Restricted require encryption in transit and at rest
3. **Approved storage** — use only CivicActions-managed Google Workspace, SaaS platforms, and managed endpoints; never store work data on personal cloud accounts
4. **Sharing safely** — share Google Docs by individual email (not "anyone with the link"); use password-protected AES-256 archive with 20+ character passphrase for Confidential files sent externally; transmit passphrase via separate channel
5. **Removable media and printing** — avoid by default; if printed, secure and shred same-day; encrypt removable media if used
6. **DLP and monitoring awareness** — DLP tools may flag sensitive data transfers; understand that monitoring exists to protect the organization, not to surveil individuals

### Module D — Acceptable use and AI (5–7 min)

**Outcome sources:** AUP, AIP, ISP

1. **Core principles** — CivicActions systems are for authorized business use; limited personal use is acceptable if it doesn't interfere with work, consume resources, or violate policy
2. **Prohibited activities** — no circumventing security controls, no unauthorized data exfiltration, no use of non-approved tools for work data, no sharing credentials
3. **AI tools — general rules** — use only CivicActions-approved AI tools with IT-managed accounts; never input sensitive, confidential, or client-internal data; human oversight required for all AI output; peer-review AI content before external sharing
4. **Approved AI tool categories** — general purpose (Slack Chatbot, Gemini, ChatGPT for Teams), coding (GitHub Copilot), specialist (Grammarly, Paxton AI), service integrations (Zoom, Mural, Confluence/Jira, Greenhouse, Figma); know that ChatGPT Atlas browser is not approved
5. **New AI tools** — CTO approval required (plus client approval on client projects); includes risk assessment per NIST AI RMF
6. **Client project AI restrictions** — comply with client-specific AI policies; no CUI in AI tools; restrictions in onboarding/wrapper docs

### Module E — Recognizing and reporting incidents (3–5 min)

**Outcome sources:** IRP, DRP, PSP, ISP

1. **See something, say something** — if you observe anything that may be a security incident, outage, or suspicious activity, raise a flag immediately: Slack #general, DM an IT team member, DM your manager, or email security@civicactions.com
2. **Blame-free reporting** — good-faith reporting will never result in retaliation; speed matters more than certainty
3. **Lost or stolen devices** — report immediately via incident response channels: what, when, where, which asset, suspected exposure; applies to both CivicActions laptops and personal devices that authenticated to CivicActions systems
4. **Incident confidentiality** — handle incident information on need-to-know basis; don't disclose details outside designated channels
5. **Post-incident participation** — participate in retrospectives when asked; lessons learned improve policies and procedures

### Module F — Governance, risk, and compliance awareness (3–5 min)

**Outcome sources:** ISP, RSAP, DRCP, MP, DRP, VPM, TPM

1. **Policy structure** — the Information Security Policy is the umbrella; it delegates details to subordinate policies (AUP, ACP, IRP, DSHP, etc.); know where to find them
2. **Compliance frameworks** — CivicActions aligns to CMMC L1/L2 (FAR/NIST), ISO 27001, ISO 9001, ITIL; this training satisfies awareness requirements
3. **Risk awareness** — understand CIA (confidentiality, integrity, availability) and the 3×3 risk scale (likelihood × impact); risk acceptance must be explicit and approved
4. **DR communication hierarchy** — during an outage: Primary (Slack chat, Zoom video), Secondary (Google Chat), Tertiary (Slack video, Zoom chat); clients/partners notified only if deliverables impacted
5. **Document change requests** — submit through Compliance Jira board; Controlled Documents reviewed annually; understand access is managed via security groups
6. **Maintenance and patching awareness** — know that IT manages configuration, change, vulnerability, and patch management programs; these are IT-managed "guardrails, not gates"
7. **Third-party awareness** — no supplier may be procured or granted access until due diligence is complete; report concerns about vendor security to IT

---

## Quiz (sample — 6 questions)

1. **You need to share a Google Doc containing Internal project data with a colleague. Which sharing method is correct?**
   - a) Set the link to "anyone with the link can view"
   - b) Share directly with the colleague's CivicActions email address ✅
   - c) Email the document to the colleague's personal Gmail
   - d) Post the link in a public Slack channel

2. **Your CivicActions laptop prompts you to install a system update. You are in the middle of a deadline. What should you do?**
   - a) Dismiss the update permanently to avoid interruption
   - b) Disable the MDM agent so updates stop appearing
   - c) Install the update at the next reasonable opportunity (do not indefinitely postpone) ✅
   - d) Uninstall the update software

3. **You receive a suspicious email with an attachment that claims to be an invoice. What is the correct first step?**
   - a) Open the attachment to check if it looks legitimate
   - b) Forward it to your personal email for safekeeping
   - c) Report it immediately to security@civicactions.com ✅
   - d) Delete it and forget about it

4. **You are setting up MFA for your CivicActions account. Which factor is the preferred primary method?**
   - a) SMS text message code
   - b) Voice call one-time password
   - c) FIDO2/WebAuthn hardware security key (e.g., YubiKey) ✅
   - d) Email-based one-time password

5. **A colleague asks you to paste a client's internal financial data into ChatGPT to summarize it. What should you do?**
   - a) Go ahead — ChatGPT is on the approved tools list
   - b) Refuse — never input sensitive, confidential, or client-internal data into any AI tool, even approved ones ✅
   - c) Ask the client for permission first, then proceed
   - d) Use Gemini instead since it's a Google product

6. **During a major SaaS outage, Slack is unavailable. What is the secondary communication channel per the Disaster Recovery Plan?**
   - a) Personal text messages
   - b) Google Chat ✅
   - c) Twitter/X direct messages
   - d) Wait until Slack comes back

---

## Outcome coverage

This training covers All Staff rows from the following outcome tables:

- [acceptable-use-outcomes.md](../outcomes/acceptable-use-outcomes.md) — 14 rows
- [identification-outcomes.md](../outcomes/identification-outcomes.md) — 10 rows
- [access-control-outcomes.md](../outcomes/access-control-outcomes.md) — 8 rows
- [data-security-outcomes.md](../outcomes/data-security-outcomes.md) — 9 rows
- [physical-security-outcomes.md](../outcomes/physical-security-outcomes.md) — 8 rows
- [info-security-outcomes.md](../outcomes/info-security-outcomes.md) — 9 rows
- [risk-security-outcomes.md](../outcomes/risk-security-outcomes.md) — 5 rows
- [ai-usage-outcomes.md](../outcomes/ai-usage-outcomes.md) — 5 rows
- [incident-response-outcomes.md](../outcomes/incident-response-outcomes.md) — 3 rows
- [disaster-recovery-outcomes.md](../outcomes/disaster-recovery-outcomes.md) — 2 rows
- [maintenance-outcomes.md](../outcomes/maintenance-outcomes.md) — 3 rows
- [vuln-patch-outcomes.md](../outcomes/vuln-patch-outcomes.md) — 1 row
- [doc-record-control-outcomes.md](../outcomes/doc-record-control-outcomes.md) — 3 rows
- [third-party-mgmt-outcomes.md](../outcomes/third-party-mgmt-outcomes.md) — 1 row
