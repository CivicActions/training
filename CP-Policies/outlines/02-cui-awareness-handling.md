# Training 2 — CUI Awareness & Handling

| Field | Value |
|-------|-------|
| **Audience** | Staff assigned to federal contracts or projects involving CUI |
| **Prerequisite** | Training 1 (Security Awareness Essentials) |
| **Target duration** | 10–15 minutes |
| **Delivery** | Written module + quiz |
| **Cadence** | Before CUI access is granted · annual refresher · ad-hoc on contract/policy change |
| **Compliance** | CMMC L2 (NIST 800-171 3.1.22, 3.8.1–3.8.9) · FAR 52.204-21 |

---

## Purpose

This training covers the additional responsibilities that apply when handling Controlled Unclassified Information (CUI). It builds on the data classification and handling foundations from Training 1 and focuses on the specific boundaries, markings, and restrictions for CUI.

---

## Session outline

### Module A — What is CUI and why it matters (3–4 min)

**Outcome sources:** CUI Policy, ISP, AUP

1. **CUI defined** — government-created or -owned information that requires safeguarding per 32 CFR Part 2002; examples at CivicActions include vulnerability scan results, contractor bids/proposals, non-public contract data
2. **Need-to-know principle** — CUI access is restricted to personnel with a legitimate business need on the specific contract or project
3. **Compliance context** — CUI handling is mandated by DFARS, FAR 52.204-21, and NIST 800-171; failure to comply can affect contract eligibility

### Module B — The CUI Security Boundary (3–4 min)

**Outcome sources:** CUI Policy, DSHP, ACP

1. **Three approved CUI locations:**
   - Secured client network (per client's ATO/security boundary)
   - CivicActions Google Workspace — access-controlled Shared Drives explicitly marked "CUI"
   - CivicActions Workstations — managed laptop or approved hardened BYOD
2. **Auto-tagging** — Google Workspace auto-tags documents containing "CUI" for discovery and audit
3. **Prohibited locations** — personal cloud storage, unapproved SaaS, removable media (without explicit CISO approval), personal email, AI tools
4. **Encryption requirements** — CUI requires FIPS 140–validated cryptography in transit and at rest; verify SaaS provider encryption meets this standard

### Module C — CUI handling rules (2–3 min)

**Outcome sources:** CUI Policy, DSHP, RSAP

1. **No unauthorized transfer** — do not copy, print, download, or move CUI outside the Security Boundary
2. **Minimize retention** — delete CUI copies as soon as no longer needed for the task
3. **Project closeout** — include CUI audit in project closeout procedures; confirm all copies returned or destroyed
4. **Incident reporting** — report suspected CUI compromise as a security incident immediately (Slack #general, DM IT/manager, security@civicactions.com)

### Module D — CUI document markings (2–3 min)

**Outcome sources:** CUI Policy

1. **When to mark** — required when sharing CUI outside a security boundary (e.g., with a partner agency or subcontractor)
2. **Header marking** — "CONTROLLED UNCLASSIFIED INFORMATION" or "CUI" in the document header
3. **Footer marking** — "Sensitive in accordance with 32 CFR 2002" centered at the bottom of the first page
4. **Optional originator line** — include per agency/contract guidance if required
5. **Internal working documents** — within the CUI Shared Drive, the folder marking and auto-tagging satisfy the requirement; explicit per-document marking is best practice

---

## Quiz (sample — 3 questions)

1. **You need to share a document containing CUI with a federal client. Which marking must appear in the document header?**
   - a) "CONFIDENTIAL"
   - b) "FOR OFFICIAL USE ONLY"
   - c) "CONTROLLED UNCLASSIFIED INFORMATION" or "CUI" ✅
   - d) No marking required for federal clients

2. **Where may CUI be stored?**
   - a) Any CivicActions Google Drive folder
   - b) Only within the CUI Security Boundary: secured client network, access-controlled CivicActions Google Workspace Shared Drives marked "CUI", or managed CivicActions workstations ✅
   - c) Personal cloud storage with a strong password
   - d) Any encrypted USB drive

3. **A project involving CUI is ending. What must happen to CUI copies held by CivicActions?**
   - a) Archive them indefinitely in case they're needed later
   - b) Include CUI audit in project closeout; confirm all copies are returned to the client or destroyed ✅
   - c) Move them to a general-purpose Shared Drive
   - d) Nothing — CUI protections expire when the contract ends

---

## Outcome coverage

This training covers CUI-specific rows from the following outcome tables:

- [cui-outcomes.md](../outcomes/cui-outcomes.md) — 5 rows (all)
- [data-security-outcomes.md](../outcomes/data-security-outcomes.md) — 2 CUI-specific rows
- [access-control-outcomes.md](../outcomes/access-control-outcomes.md) — 1 CUI-specific row
- [risk-security-outcomes.md](../outcomes/risk-security-outcomes.md) — 1 CUI-specific row
- [info-security-outcomes.md](../outcomes/info-security-outcomes.md) — 1 CUI reference (data governance)
