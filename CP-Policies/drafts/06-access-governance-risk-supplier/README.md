<!--
author:   CivicActions Security Team
email:    security@civicactions.com
version:  0.1.0
language: en
narrator: US English Female

comment:  Access Governance, Risk & Supplier Oversight — training for
          managers, system/data owners, and document controllers on
          approving access, managing risk, overseeing suppliers, and
          controlling documents.

-->

# Access Governance, Risk & Supplier Oversight

Welcome to **Access Governance, Risk & Supplier Oversight** — the training for CivicActions managers, system/data owners, and document controllers.

While Training 3 covers the technical operations, this course covers the **governance decisions** you make: approving and reviewing access, managing risk, overseeing supplier relationships, and controlling documents. These are the "approve, review, decide" responsibilities that keep the organization running securely.

**Who takes this?** Managers, System/Data Owners, Document Controllers.

**Prerequisite:** Training 1 — Security Awareness Essentials.

**How long?** About 15–20 minutes.

**When?** Within 30 days of onboarding, then annually, and whenever there's a major policy change.

**Compliance:** CMMC L2 (AC, RA, SR controls), ISO 27001 A.5.1–A.5.23.

---

Let's get started!

## Module A — Access Governance

As a manager or system owner, you're the gatekeeper for who gets access to what. This module covers your approval responsibilities, the access lifecycle, and the reviews that keep permissions current.

### The Approval Role

When someone requests access to a system or project, you're the one who decides whether to approve it. Here's what guides that decision:

- Apply the **principle of least privilege** — grant only the minimum access needed
- Apply **need-to-know** — does this person actually need this access for their current work?
- Scope access to the specific **project, role, or task** — not broad access "just in case"

> **If you're unsure, start with less access.** It's always easier to grant more later than to clean up over-provisioned access after a problem.

> **Example:** A new team member submits a Jira ticket requesting access to the production Google Cloud environment. The ticket includes their name, the specific project, their justification, and the role they need. As the System Owner, you check: does their current assignment actually require production access, or would staging be sufficient? You approve staging access and note that production can be added later if the project scope expands.

### Access Lifecycle

Access follows a predictable lifecycle — and you have a role at every stage:

1. **Approve** — review and approve (or deny) the request
2. **Grant** — IT provisions the access
3. **Review** — periodically verify the access is still needed
4. **Revoke** — remove access when it's no longer needed

Three events should trigger an **immediate rights review**:

- **Role changes** — someone moves to a different team or function
- **Project transitions** — someone finishes one project and starts another
- **Departures** — someone leaves the organization

Don't wait for the quarterly review when someone's situation changes.

> **Example:** One of your developers finishes a federal contract and moves to an internal project. You don't wait until the next quarterly review — you trigger an immediate rights review. IT removes their access to the CUI Shared Drive, the client's cloud environment, and the project-specific GitLab group. Then you submit a new request for the access they need on their new project. Rippling's offboarding workflow handles some of this automatically, but system-specific access like Shared Drives and GitLab groups needs your attention.

### Periodic Access Reviews

Even without role changes, access should be reviewed regularly:

- Conduct **quarterly reviews** of access rights for your team
- **Verify continued need** for each permission
- **Revoke orphaned or excessive permissions** — these are permissions nobody needs anymore

Stale access is a common audit finding and a real security risk.

> **Example:** During your quarterly access review of high-criticality systems — the IdP, production cloud, CI/CD, and CUI boundary — you discover that two people who rotated off a project three months ago still have access to that project's GitLab group and Google Shared Drive. You revoke both immediately and file Jira tickets documenting the cleanup. This is exactly the kind of finding auditors look for.

### Third-Party and Contractor Access

External people — contractors, consultants, partners — need the same controls as employees. In some ways, they need more:

- Apply the **same least-privilege and need-to-know principles**
- Make access **time-bound** — set an expiration date, don't leave it open-ended
- Ensure **contractual security obligations** are in place before granting any access

> **Example:** A subcontractor needs Jira and Confluence access for a six-month engagement. You approve time-bound access that expires at the contract end date, require that their device meets CivicActions endpoint standards (or they use a managed device), and confirm that the subcontract includes the required security clauses — confidentiality, least-privilege, and incident reporting within 24 hours.

### CUI Access Decisions

Access to Controlled Unclassified Information (CUI) has extra requirements:

- CUI access requires **explicit justification** — not a blanket grant
- Access is limited to the **CUI Security Boundary** (covered in Training 2)
- As a manager, you must **verify need-to-know** for each team member before approving CUI access

> **Example:** A team member asks for access to the CUI Shared Drive for a federal project. Before approving, you verify: Are they assigned to this contract? Does their role require CUI access? You approve with an explicit justification in the ticket — "Developer assigned to Project X, needs vulnerability scan data for remediation work" — rather than a blanket "they're on the team."

### Module A Quiz

A team member is transferring from Project A to Project B. As their manager, what must you do regarding their access?

- [( )] Nothing — their access will sort itself out
- [( )] Wait for the quarterly access review to clean up permissions
- [(X)] Trigger an immediate rights review to remove Project A access and request Project B access
- [( )] Ask the team member to manage their own access changes
***

**Correct!** Project transitions are one of the three events that require an immediate rights review. Don't wait for the quarterly cycle — remove Project A access right away and request only the access needed for Project B. Leaving old access in place creates unnecessary risk and violates the principle of least privilege.

***

## Module B — Risk Management Responsibilities

Risk management can sound complicated, but at its core it's about answering three questions: *What could go wrong? How bad would it be? What are we doing about it?* This module covers your role in that process.

### Risk Assessment Participation

As a system or data owner, you contribute to risk assessments for the systems you manage:

- Understand the **CIA matrix**: Confidentiality, Integrity, and Availability — each system is rated for all three
- Understand the **3×3 risk scale**: Likelihood (Low/Medium/High) × Impact (Low/Medium/High)
- Your input matters — you know your systems better than anyone

> **Example:** During a risk assessment for a project management tool, you rate it: Confidentiality = Medium (it holds project plans and timelines, but no CUI), Integrity = Medium (corrupted data would disrupt work but is recoverable from backups), Availability = High (the team can't function without it). Those CIA ratings go into Jira assets and drive the controls that apply to the system.

### Risk Treatment Options

When a risk is identified, there are four ways to handle it:

| Option | What it means |
|--------|--------------|
| **Mitigate** | Reduce the risk by adding controls |
| **Transfer** | Shift the risk to someone else (e.g., insurance, a vendor SLA) |
| **Accept** | Acknowledge the risk and decide to live with it |
| **Avoid** | Eliminate the risk by stopping the activity |

> **Key point:** Risk acceptance must be **explicit and recorded**. You can't just ignore a risk and call it "accepted."

> **Example:** Your team identifies a risk: a SaaS tool you depend on doesn't support hardware-key MFA — only TOTP. The impact is Medium (credential theft is harder to prevent) and the likelihood is Low (the tool is internal-only). That's a Low residual risk. You accept it as the System Owner with CISO concurrence and document the rationale in a Risk Mitigation ticket in the Jira Continual Improvement project. "Ignore" is never an option — even Low risks get documented.

### Risk Acceptance Authority

Not everyone can accept every level of risk. The authority depends on severity:

| Residual risk level | Who can accept it |
|--------------------|-------------------|
| **Medium** | System Owner |
| **High** | CISO |
| **Above High** | CEO (or CTO as backup) |

If a risk is too high for your authority level, escalate it.

### Risk Register and POA&Ms

The Risk Register is the central record of all identified risks:

- Maintain awareness of **your systems' entries** in the register
- Make sure **POA&M items** (Plans of Action & Milestones) have assigned owners, realistic timelines, and tracked progress
- POA&Ms aren't just paperwork — they're commitments to fix things

> **Example:** A risk assessment finds that one of your systems doesn't have automated drift detection yet. The CISO creates a POA&M ticket in the Jira Continual Improvement board: "Implement automated configuration drift detection for System Y." It has your name as the owner, a due date in 90 days, and milestones for tool selection, testing, and deployment. The ELT sees its status in the quarterly risk report.

### Annual Risk Review

Risk isn't static — it changes as systems, threats, and business conditions evolve:

- Participate in the **annual reassessment** of risks for your systems
- **Update entries** when systems change, new threats emerge, or the business context shifts
- Don't wait for the annual cycle if something significant changes — update the register immediately

### Module B Quiz

A risk assessment identifies a High residual risk for a system you own. Who must approve acceptance of this risk?

- [( )] You (the System Owner)
- [(X)] The CISO
- [( )] Any manager on the team
- [( )] The risk is automatically accepted if documented
***

**Correct!** System Owners can accept Medium residual risk, but High residual risk requires CISO approval. Risks above High require CEO (or CTO as backup) approval. Simply documenting a risk doesn't mean it's accepted — explicit approval from the right authority level is required.

***

## Module C — Supplier and Third-Party Oversight

CivicActions relies on vendors and partners for many critical services. This module covers how to evaluate, onboard, and monitor those relationships securely.

### Three SCRM Tracks

CivicActions uses three Supply Chain Risk Management tracks, depending on the type of supplier:

| Track | Supplier type | Examples |
|-------|--------------|---------|
| **SCRM-DS** | Digital services / SaaS | Google Workspace, Slack, cloud platforms |
| **SCRM-S** | Software | Open-source libraries, commercial software, containers |
| **SCRM-PS** | Professional services | Consultants, subcontractors, staffing agencies |

Know which track applies to the suppliers you manage.

> **Example:** Google Workspace is **SCRM-DS** — it's a digital service/SaaS platform. An npm library your developers want to add is **SCRM-S** — it's software. A consulting firm providing security assessment support is **SCRM-PS** — professional services. Each track has different intake requirements, evidence expectations, and monitoring cadences.

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

### Module C Quiz

A new SaaS vendor is proposed that will process CivicActions data. What must happen before procurement?

- [( )] Nothing — just sign up and start using it
- [(X)] Tier-appropriate due diligence must be completed, including intake form and evidence review, before the vendor is procured, deployed, or granted access
- [( )] Only a cost comparison is required
- [( )] The vendor just needs to sign an NDA
***

**Correct!** No supplier gets procured, deployed, or granted access until proper due diligence is complete. That includes an intake form, evidence review, and (for Medium/High-tier suppliers) a security questionnaire. An NDA alone doesn't address technical security requirements, and cost is not a substitute for security evaluation.

***

## Module D — Document and Record Control

Controlled Documents are the policies, procedures, and records that define how CivicActions operates. This module covers how they're managed.

### Document Identification

Controlled Documents are tracked in the **Controlled Document Jira board**. Each document gets a unique ID:

**Format:** Two-character department prefix + document type digit + three-digit unique number

For example: `IT-1-001` might be an IT policy document.

> **Example:** The IT department (prefix "IT") publishes a new policy (type digit "1"), and it's the third document in the series (serial "003"). Its ID is `IT-1-003`. A security team checklist would be something like `SC-4-012` — Security (SC), checklist (4), twelfth document. These IDs live on the Controlled Document Jira board and never get reused, even if a document is retired.

### Classification

Every Controlled Document gets a data classification:

- Apply the **four-level classification** (Public, Internal, Confidential, Restricted) using the Data Classification SOP
- Record the classification in the **Document Control Change Log**
- Classification determines who can access the document and how it must be handled

### Version Control

CivicActions uses a clear versioning system:

| Version type | When to use it | Examples |
|-------------|---------------|---------|
| **Major** | Significant content or scope changes | New section added, policy requirement changed |
| **Minor** | Small corrections | Typos fixed, broken links updated, formatting improved |

One critical rule: **effective Controlled Documents are immutable**. You don't edit a live document — you create a new draft, get it approved, and publish a new version.

> **Example:** The Access Control Policy is currently at version 2.0. Someone notices that a referenced Confluence link is broken and a section heading has a typo. They don't edit version 2.0 directly — they submit a Document Change Request through the Compliance Jira board. The Document Controller creates a draft (version 2.1), the Responsible Person reviews it, and once approved, 2.1 becomes the new controlled copy. Version 2.0 is archived, not modified.

### Change Request Process

To change a Controlled Document:

1. **Submit** a request through the **Compliance Jira board**
2. The document goes through the workflow: **Draft → Feedback → Approval → Distribution**
3. The approved version becomes the new **controlled copy**

### Training Coordination

When a Controlled Document changes, people may need training on the update:

- **Management and the Responsible Person** determine training requirements for each document
- The **Document Controller** coordinates training planning
- Not every change requires training — but significant ones do

### Annual Review

All Controlled Documents are reviewed annually by default:

- The review confirms the document is still accurate and relevant
- Documents with **different review schedules** note this in their Review section
- Don't skip the annual review — even if nothing seems to have changed, the review itself is a compliance requirement

### Module D Quiz

A colleague submits a change to a Controlled Document that corrects a typo and updates a broken link. How is this version classified?

- [( )] Major version — all changes are major
- [(X)] Minor version — typos, link updates, and formatting are minor changes
- [( )] No version change needed for typos
- [( )] Emergency version — broken links need immediate fixes
***

**Correct!** Typos, broken links, and formatting corrections are minor version changes. Major versions are reserved for significant content or scope changes. And no, you can't skip versioning entirely — even small corrections create a new version because effective Controlled Documents are immutable.

***

## Module E — AI Governance for Managers

AI tools are becoming part of how work gets done. As a manager, you have specific governance responsibilities around their use.

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

### Module E Quiz

A team lead wants to use a new AI tool to help with project planning. What approval is needed?

- [( )] No approval — project planning is internal work
- [( )] Manager approval is sufficient
- [(X)] CTO approval is required for any new AI tool or significant new application
- [( )] The team lead can approve it themselves if it's free
***

**Correct!** All new AI tools and significant new applications require CTO approval, regardless of the use case or cost. This ensures a proper risk assessment is conducted and the tool meets CivicActions' security standards. On client projects, client approval is also needed.

***

## Bonus Quiz

You've completed all five modules — great work! Here's a final question on a key governance concept.

During a quarterly access review, you discover that a former contractor still has active access to a CivicActions system. Their contract ended two months ago. What should you do?

- [( )] Leave it — they might come back for another contract
- [( )] Send them an email asking them to stop using the access
- [( )] Wait until the next quarterly review to confirm it should be removed
- [(X)] Revoke the access immediately and report it as a potential security finding
***

**Correct!** Orphaned access — permissions that belong to someone who no longer needs them — is a security risk and a common audit finding. Revoke it immediately. Don't wait, don't ask the person to self-manage, and don't assume they're not using it. The fact that it went undetected for two months is itself worth reporting so the access review process can be improved.

***

## Course Complete

Congratulations — you've finished **Access Governance, Risk & Supplier Oversight**!

Here's what you covered:

1. **Access governance** — approval role, access lifecycle (approve → grant → review → revoke), quarterly reviews, third-party access, CUI access decisions
2. **Risk management** — CIA matrix, 3×3 risk scale, treatment options, acceptance authority (System Owner → CISO → CEO), Risk Register and POA&Ms, annual review
3. **Supplier oversight** — three SCRM tracks (DS/S/PS), risk tiering, mandatory due diligence before procurement, required contract clauses, monitoring cadence, prohibited technologies
4. **Document control** — identification, classification, version control (major vs. minor), change request process, training coordination, annual review
5. **AI governance** — CTO approval for new tools, sales restrictions, risk assessment per NIST AI RMF

**Remember the essentials:**

- Least privilege and need-to-know guide every access decision
- Role changes, project transitions, and departures trigger immediate access reviews
- No supplier gets access without completed due diligence
- Risk acceptance must be explicit, recorded, and approved at the right authority level
- Controlled Documents are immutable — changes create new versions

Questions? Reach out to **security@civicactions.com** or the Compliance team.
