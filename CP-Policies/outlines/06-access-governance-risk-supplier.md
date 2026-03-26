# Training 6 — Access Governance, Risk & Supplier Oversight

| Field | Value |
|-------|-------|
| **Audience** | Managers, System/Data Owners, Document Controllers |
| **Prerequisite** | Training 1 (Security Awareness Essentials) |
| **Target duration** | 15–20 minutes |
| **Delivery** | Written module + quiz |
| **Cadence** | Onboarding (within 30 days) · annual refresher · ad-hoc on material policy change |
| **Compliance** | CMMC L2 AC.L2-3.1.1–3.1.22, RA.L2-3.11.1–3.11.3, SR.L2-3.17.1–3.17.3 · ISO 27001 A.5.1–A.5.23 |

---

## Purpose

This training covers the governance decisions that managers, system/data owners, and document controllers make: approving and reviewing access, managing risk, overseeing supplier relationships, and controlling documents. These are the "approve, review, decide" responsibilities that complement the technical operations covered in Training 3.

---

## Session outline

### Module A — Access governance (4–5 min)

**Outcome sources:** ACP, IdP

1. **The approval role** — managers approve access requests using the principle of least privilege and need-to-know; access must be scoped to the specific project, role, or task
2. **Access lifecycle** — approve → grant → review → revoke; trigger immediate rights review on role changes, project transitions, and departures
3. **Periodic access reviews** — quarterly reviews of access rights; verify continued need; revoke orphaned or excessive permissions
4. **Third-party and contractor access** — apply same least-privilege and time-bound access principles; ensure contractual security obligations are in place before granting access
5. **CUI access decisions** — CUI access requires explicit justification and is limited to the CUI Security Boundary; managers verify need-to-know for each team member

### Module B — Risk management responsibilities (3–4 min)

**Outcome sources:** RSAP, ISP

1. **Risk assessment participation** — understand the CIA matrix (confidentiality, integrity, availability) and 3×3 risk scale (likelihood × impact); contribute to risk assessments for systems you own or manage
2. **Risk treatment options** — mitigate, transfer, accept, or avoid; know that risk acceptance must be explicit and recorded
3. **Risk acceptance authority** — System Owners accept Medium residual risk; CISO accepts High; CEO (or CTO as backup) accepts risks above High
4. **Risk Register and POA&Ms** — maintain awareness of your systems' entries; ensure POA&M items have owners, timelines, and tracked progress
5. **Annual risk review** — participate in annual reassessment; update entries when systems, threats, or business context change

### Module C — Supplier and third-party oversight (4–5 min)

**Outcome sources:** TPM, ISP

1. **Three SCRM tracks** — SCRM-DS (digital services/SaaS), SCRM-S (software), SCRM-PS (professional services); know which applies to your supplier relationships
2. **Risk tiering** — suppliers are categorized as Low, Medium, or High based on CIAX scoring (SaaS), security posture/SBOM (software), or access/criticality/regulatory scope (professional services)
3. **Mandatory due diligence** — no supplier procured, deployed, or granted access until tier-appropriate due diligence is complete (intake form, evidence review, security questionnaire)
4. **Required contract clauses** — confidentiality, least-privilege, encryption, MFA, incident reporting (24 hours), right to audit, federal flow-down (FAR/DFARS for FCI/CUI), change notification, exit/data destruction
5. **Monitoring cadence** — Low/Medium annually, High semi-annually; ad-hoc on incidents, scope changes, or new data classes; annual PM-led review for professional services
6. **Prohibited technologies** — screen against prohibited technology list and DFARS restrictions during intake and reviews

### Module D — Document and record control (3–4 min)

**Outcome sources:** DRCP

1. **Document identification** — Controlled Documents are tracked in the Controlled Document Jira board; ID format: two-character department prefix + document type digit + three-digit unique number
2. **Classification** — apply data classification (Public, Internal, Confidential, Restricted) using the Data Classification SOP; record in the Document Control Change Log
3. **Version control** — major versions (significant content/scope changes) vs. minor (typos, links, formatting); effective Controlled Documents are immutable; changes create a new draft
4. **Change request process** — submit through Compliance Jira board; workflow: draft → feedback → approval → distribution of controlled copy
5. **Training coordination** — Management and the Responsible Person determine training requirements for each Controlled Document; Document Controller coordinates planning
6. **Annual review** — all Controlled Documents reviewed annually by default; documents with different schedules note this in their Review section

### Module E — AI governance for managers (1–2 min)

**Outcome sources:** AIP

1. **AI approval authority** — new AI tools or significant new applications require CTO approval (and client approval for client projects)
2. **Sales restrictions** — no AI tools for pricing or original RFP content generation; AI may assist with analysis, review, and rewriting
3. **Risk assessment** — new AI applications require a risk assessment guided by the NIST AI Risk Management Framework

---

## Quiz (sample — 4 questions)

1. **A team member is transferring from Project A to Project B. As their manager, what must you do regarding their access?**
   - a) Nothing — their access will sort itself out
   - b) Wait for the quarterly access review to clean up permissions
   - c) Trigger an immediate rights review to remove Project A access and request Project B access ✅
   - d) Ask the team member to manage their own access changes

2. **A risk assessment identifies a High residual risk for a system you own. Who must approve acceptance of this risk?**
   - a) You (the System Owner)
   - b) The CISO ✅
   - c) Any manager on the team
   - d) The risk is automatically accepted if documented

3. **A new SaaS vendor is proposed that will process CivicActions data. What must happen before procurement?**
   - a) Nothing — just sign up and start using it
   - b) Tier-appropriate due diligence must be completed, including intake form and evidence review, before the vendor is procured, deployed, or granted access ✅
   - c) Only a cost comparison is required
   - d) The vendor just needs to sign an NDA

4. **A colleague submits a change to a Controlled Document that corrects a typo and updates a broken link. How is this version classified?**
   - a) Major version — all changes are major
   - b) Minor version — typos, link updates, and formatting are minor changes ✅
   - c) No version change needed for typos
   - d) Emergency version — broken links need immediate fixes

---

## Outcome coverage

This training covers Manager/System Owner/Document Controller rows from:

- [access-control-outcomes.md](../outcomes/access-control-outcomes.md) — 8 governance rows (approvals, reviews, CUI access, third-party)
- [risk-security-outcomes.md](../outcomes/risk-security-outcomes.md) — 6 rows (methodology, treatment, authority, register, annual review)
- [third-party-mgmt-outcomes.md](../outcomes/third-party-mgmt-outcomes.md) — 8 rows (governance, tiering, due diligence, contracts, monitoring, prohibited tech, records)
- [doc-record-control-outcomes.md](../outcomes/doc-record-control-outcomes.md) — 5 rows (identification, classification, versioning, change process, review)
- [identification-outcomes.md](../outcomes/identification-outcomes.md) — 1 row (admin authenticator issuance)
- [ai-usage-outcomes.md](../outcomes/ai-usage-outcomes.md) — 2 rows (approval, sales restrictions)
- [data-security-outcomes.md](../outcomes/data-security-outcomes.md) — 2 rows (classification decisions, media sanitization oversight)
