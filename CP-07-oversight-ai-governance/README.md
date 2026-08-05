<!--
author:              CivicActions Security/compliance Team
language:            en
comment:             This CivicActions internal training course is updated and maintained by CivicActions.
controlled_document: CP7065 Third-Party Oversight and AI Governance Training
-->

# Third-Party Oversight and AI Governance

Welcome to **Third-Party Oversight and AI Governance** — a training for CivicActions management (Ops).

While Training 3 (IT Operations) covers the technical operations, this course covers the **governance decisions** you make while overseeing supplier relationships and providing AI governance.

**Who takes this?** Managerment (Ops and Program), Sales, Legal, Finance, Marketing and People.

**Prerequisite:** Training 1 — Security Awareness Essentials.

**How long?** About 10-15 minutes.

**When?** Within 30 days of onboarding, then annually, and whenever there's a major policy change.

**Compliance:** CMMC L2 (RA, SR controls), ISO 27001 A.5.19–A.5.23.

> **Note on links:** Links are sometimes provided for additional information. Following them is not required for the training.

---

Let's get started!

## Module A — Supplier and Third-Party Oversight

CivicActions relies on vendors and partners for many critical services. This module covers how to evaluate, onboard, and monitor those relationships securely.

See also: [**Third‑Party Management Policy**](https://civicactions.atlassian.net/wiki/spaces/MGPOL/pages/745373710/Third+Party+Management+Policy)

### Three SCRM Tracks

CivicActions uses three Supply Chain Risk Management tracks, depending on the type of supplier:

| Track | Supplier type | Examples |
|-------|--------------|---------|
| **SCRM-DS** | Digital services / SaaS | Google Workspace, Slack, cloud platforms |
| **SCRM-S** | Software | Open-source libraries, commercial software, containers |
| **SCRM-PS** | Professional services | Consultants, subcontractors, staffing agencies |

Know which track applies to the suppliers you manage.

> Each track has different intake requirements, evidence expectations, and monitoring cadences.

### Risk Tiering

Each supplier is categorized as **Low**, **Medium**, or **High** based on different factors:

- **SaaS (SCRM-DS):** CIAX scoring — how much confidential, integrity-critical, or availability-critical data do they handle?
- **Software (SCRM-S):** Security posture and SBOM (Software Bill of Materials) analysis
- **Professional services (SCRM-PS):** Level of access, criticality to operations, and regulatory scope

Higher-tier suppliers get more scrutiny.

> **Example:** You're evaluating a new SaaS tool for project analytics. You run the CIAX scoring: it handles Internal data (moderate C), has no integrity-critical role (low I), the team could work without it for a week (low A), and the annual cost is modest (low X). That scores as Low tier — fast-path intake with an annual review. If the same tool handled CUI or was critical to client deliverables, it would score High and require a full review with third-party evidence.

### Mandatory Due Diligence

This is a firm rule:

**No supplier may be procured, deployed, or granted access until tier-appropriate due diligence is complete.**

Due diligence includes:

- **Intake form** capturing the supplier's purpose and data handling
- **Evidence review** of security certifications, audit reports, etc.
- **Security questionnaire** for Medium and High-tier suppliers

Don't skip this because of time pressure. A vendor without due diligence is an unknown risk.

> **Example:** A project lead wants to start using a new SaaS collaboration tool next week. You walk them through the process: submit the intake form (business owner, data classification, intended use), then evidence review (does the vendor have SOC 2 or ISO 27001 certification?). For a Medium-tier tool, a SIG Lite questionnaire is also required. The tool doesn't get deployed until this is done — no exceptions, even with a deadline.

### Protecting Commercial Data in Supplier Relationships

Before granting any supplier or partner access to project data, treat the data correctly:

- **Proposals, RFPs, and technical diagrams** are **Confidential by default** — store them only in designated Shared Drives or authorized CUI enclaves, never on personal devices or unapproved platforms
- **Brief subcontractors and partners on data handling requirements before granting access** — don't rely on contract clauses alone; walk them through what's expected
- **Confirm understanding** — get written acknowledgment that the partner knows the rules before they touch project data

> **Example:** A subcontractor is joining your federal project next week. Before you approve their access to the project Shared Drive, schedule a 15-minute briefing: where CUI lives, what can and can't be shared externally, and how to report a mistake. Have them confirm they understand. Skipping this step is one of the most common ways sensitive data ends up in the wrong place.

### Data Minimization as a Management Responsibility

As a manager, you set the standard for how much data your team collects and retains:

- **Collect only what's necessary** — if your team doesn't need a data element to do the work, don't collect it
- **Grant access strictly on a need-to-know basis** — even within your own team, not everyone needs everything
- **Verify that project data stays in approved locations** — spot-check that team members aren't storing files locally or in personal cloud accounts

> **Example:** Your team is starting a new engagement and setting up a project Shared Drive. Before populating it, think about what's actually needed — don't copy over an entire folder of data from a previous project "just in case." Share only the documents required for the current scope, and limit access to the team members who need them.

### Required Contract Clauses

Every supplier contract must include specific security clauses:

- **Confidentiality** obligations
- **Least-privilege** access requirements
- **Encryption** and **MFA** requirements
- **Incident reporting** within **24 hours**
- **Right to audit**
- **Federal flow-down** clauses (FAR/DFARS) for suppliers handling FCI or CUI
- **Change notification** — the vendor must tell us before making significant changes
- **Exit and data destruction** — what happens when the contract ends

> **Example:** When negotiating a contract with a cloud storage vendor, you ensure it includes: incident reporting within 24 hours, encryption in transit and at rest, MFA for admin access, and right to audit. The vendor will also handle CUI for a federal project, so the contract adds FAR 52.204-21 flow-down, DFARS 252.204-7012, and a requirement for FedRAMP Moderate equivalence. Exit terms specify that all CivicActions data is returned or destroyed, with sanitization artifacts provided.

### Monitoring Cadence

Due diligence isn't a one-time event:

| Supplier tier | Review frequency |
|--------------|-----------------|
| **Low / Medium** | Annually |
| **High** | Semi-annually |

Additionally, trigger an **ad-hoc review** for:

- Security incidents involving the supplier
- Scope changes (the supplier starts handling more sensitive data)
- Introduction of new data classes
- Annual PM-led reviews for professional services

### Prohibited Technologies

Before onboarding any supplier or technology:

- **Screen against the prohibited technology list**
- Check for **DFARS restrictions** — some technologies cannot be used on federal projects
- Do this at intake *and* during periodic reviews — prohibitions can change

### Module A Quiz

A new SaaS vendor is proposed that will process CivicActions data. What must happen before procurement?

- [( )] Nothing — just sign up and start using it
- [(X)] Tier-appropriate due diligence must be completed, including intake form and evidence review, before the vendor is procured, deployed, or granted access
- [( )] Only a cost comparison is required
- [( )] The vendor just needs to sign an NDA
***

**Correct!** No supplier gets procured, deployed, or granted access until proper due diligence is complete. That includes an intake form, evidence review, and (for Medium/High-tier suppliers) a security questionnaire. An NDA alone doesn't address technical security requirements, and cost is not a substitute for security evaluation.

***

## Module B — AI Governance for Managers

AI tools are becoming part of how work gets done. As a manager, you have specific governance responsibilities around their use.

See also: [**AI Usage Policy**](https://civicactions.atlassian.net/wiki/spaces/MGPOL/pages/582418435/AI+Usage+Policy)

### Condensed AI Usage Policy

- **No Sensitive Data in AI Tools:** Never input confidential, proprietary, or CUI data into any AI tool — external or internal. If you wouldn't paste it into a public chat, don't paste it into a prompt.
- **IT-Managed Accounts Only:** Use CivicActions-approved AI tools through IT-managed accounts. No personal accounts, no free-tier signups, no "I just wanted to try it."
- **Label and Review:** AI-generated content must be clearly labeled as AI-assisted and peer-reviewed by a human before any business use. AI drafts it, a person owns it.
- **GitHub Copilot for Code:** Copilot is the approved tool for AI-assisted code generation. Other code-generation tools require CTO approval before use.

### AI Approval Authority

New AI tools (or significant new uses of existing tools) require approval:

- **CTO approval** is required for any new AI tool or significant new application
- On **client projects**, you also need **client approval**
- This isn't just bureaucracy — it ensures every AI tool gets a proper security and risk review

> **Example:** A manager wants to pilot a new AI-powered code review tool for their team. Even though the team already uses GitHub Copilot (approved for code), a new tool requires CTO approval. The manager submits the request, which triggers a risk assessment guided by the NIST AI Risk Management Framework: What data does the tool access? What happens if its suggestions are wrong? Does it meet CivicActions' security standards? On a client project, the client's approval is also needed before the tool touches any project code.

### Sales Restrictions

AI has specific limits when it comes to sales activities:

- **No AI tools for pricing** — pricing decisions must be human-made
- **No AI for original RFP content generation** — AI cannot write proposal content from scratch
- **AI may assist** with analysis, review, and rewriting — but a human must create the original content

> **Why?** Pricing and proposals are high-stakes, client-facing outputs. AI-generated content in these areas creates accuracy risks, contractual risks, and trust risks.

> **Example:** Your team is responding to a federal RFP. AI tools like ChatGPT for Teams can help you review and rewrite sections a human has already drafted — improving clarity or structure. But the original technical approach and pricing must be human-created. If a team member asks, "Can I just have ChatGPT write the management approach section?" the answer is no — AI can polish, but humans create the original content.

### Risk Assessment for New AI

Every new AI application requires a **risk assessment** guided by the **NIST AI Risk Management Framework**:

- Evaluate the tool's data handling practices
- Assess the risk of AI-generated errors in the intended use case
- Consider the impact if the AI tool's output is wrong

This assessment is part of the CTO approval process.

### Module B Quiz

A team lead wants to use a new AI tool to help with project planning. What approval is needed?

- [( )] No approval — project planning is internal work
- [( )] Manager approval is sufficient
- [(X)] CTO approval is required for any new AI tool or significant new application
- [( )] The team lead can approve it themselves if it's free
***

**Correct!** All new AI tools and significant new applications require CTO approval, regardless of the use case or cost. This ensures a proper risk assessment is conducted and the tool meets CivicActions' security standards. On client projects, client approval is also needed.

***

## Bonus Quiz

You've completed both modules — great work! Here's a final question that brings them together.

A project team wants to use a new AI-powered analytics SaaS tool that will ingest CUI from a federal engagement. What is required before it can be deployed?

- [( )] CTO approval only - it's an AI tool, so AI governance policy applies
- [( )] Vendor due diligence only - it's a SaaS product, so SCRM-DS intake applies
- [( )] Client sign-off only - it's their data, so their approval is all that's needed
- [(X)] CTO approval, tier-appropriate vendor due diligence (SCRM-DS, likely High tier given CUI handling), and client approval are all required - no deployment until all three are complete
***

**Correct!** This tool is simultaneously a *supplier* and an *AI tool*, so both sets of rules apply. As a SaaS product handling CUI, it goes through SCRM-DS intake — CIAX scoring would land it at High tier, requiring full due diligence including a security questionnaire and evidence review. As a new AI tool, it requires CTO approval plus client approval since it's on a federal project. And because it handles CUI, the risk assessment must also confirm the tool meets the data handling requirements of the AI Usage Policy — AI tools are not automatically cleared for sensitive data just because they've been approved for other uses.

***

## Course Complete

Congratulations — you've finished **Third-Party Oversight and AI Governance**!

Here's what you covered:

1. **Supplier oversight** — three SCRM tracks (DS/S/PS), risk tiering, mandatory due diligence before procurement, required contract clauses, monitoring cadence, prohibited technologies
2. **AI governance** — CTO approval for new tools, sales restrictions, risk assessment per NIST AI RMF

**Remember the essentials:**

- No supplier gets access without completed due diligence
- Every new AI tool requires CTO approval — and client approval on client projects — before use

Questions? Reach out to **security@civicactions.com** or the Compliance team.

---

Please take 2 minutes to fill out our [**Policy Training Feedback Form**](https://docs.google.com/forms/d/e/1FAIpQLSfYwiMB4fsg32jzzrEDnGC3DEYJyloeSy91NPVj4GuPEoFfRw/viewform?usp=header)

---

> **Tip:** Close this window to record your completion of this training in Rippling.