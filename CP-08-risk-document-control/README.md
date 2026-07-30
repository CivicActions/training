<!--
author:              CivicActions Security/compliance Team
language:            en
comment:             This CivicActions internal training course is updated and maintained by CivicActions.
controlled_document: CP7066 Risk Management and Document Control Training
-->

# Risk Management and Document Control

Welcome to **Risk Management and Document Control** — the training for CivicActions managers, system/data owners, and document controllers.

While Training 3 (IT Operations) covers the technical operations, this course covers the **governance decisions** you make when managing risk and controlled documents. These are the "approve, review, decide" responsibilities that keep the organization running securely.

**Who takes this?** Managers (Ops), Legal and Internal Security and Compliance.

**Prerequisite:** Training 1 — Security Awareness Essentials.

**How long?** About 15–20 minutes.

**When?** Within 30 days of onboarding, then annually, and whenever there's a major policy change.

**Compliance:** CMMC L2 (RA controls), ISO 27001 A.5.1–A.5.23.

> **Note on links:** Links are sometimes provided for additional information. Following them is not required for the training.

---

Let's get started!

## Module A — Risk Management Responsibilities

Risk management can sound complicated, but at its core it's about answering three questions: *What could go wrong? How bad would it be? What are we doing about it?* This module covers your role in that process.

See also: [**Risk and Security Assessment Policy**](https://civicactions.atlassian.net/wiki/spaces/MGPOL/pages/710213648/Risk+and+Security+Assessment+Policy)

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

### Module A Quiz

A risk assessment identifies a High residual risk for a system you own. Who must approve acceptance of this risk?

- [( )] You (the System Owner)
- [(X)] The CISO
- [( )] Any manager on the team
- [( )] The risk is automatically accepted if documented
***

**Correct!** System Owners can accept Medium residual risk, but High residual risk requires CISO approval. Risks above High require CEO (or CTO as backup) approval. Simply documenting a risk doesn't mean it's accepted — explicit approval from the right authority level is required.

***

## Module B — Document and Record Control

Controlled Documents are the policies, procedures, and records that define how CivicActions operates. This module covers how they're managed.

See also: [**Document and Record Control Policy**](https://civicactions.atlassian.net/wiki/spaces/MGPOL/pages/194019329/Document+and+Record+Control+Policy)

### Document Identification

Controlled Documents are tracked in the **Controlled Document Jira board**. Each document gets a unique ID:

**Format:** Two-character department prefix + document type digit + three-digit unique number

For example: `IT1001` might be an IT policy document.

> **Example:** The IT department (prefix "IT") publishes a new policy (type digit "1"), and it's the third document in the series (serial "003"). Its ID is `IT1003`. A security team checklist would be something like `SC4012` — Security (SC), checklist (4), twelfth document. These IDs live on the Controlled Document Jira board and never get reused, even if a document is retired.

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

### Module B Quiz

A colleague submits a change to a Controlled Document that corrects a typo and updates a broken link. How is this version classified?

- [( )] Major version — all changes are major
- [(X)] Minor version — typos, link updates, and formatting are minor changes
- [( )] No version change needed for typos
- [( )] Emergency version — broken links need immediate fixes
***

**Correct!** Typos, broken links, and formatting corrections are minor version changes. Major versions are reserved for significant content or scope changes. And no, you can't skip versioning entirely — even small corrections create a new version because effective Controlled Documents are immutable.

***

## Bonus Quiz

You've completed both modules — great work! Here's a final question that brings them together.

During an annual review, a System Owner identifies a risk that exceeds the organization's tolerance. The policy document describing the mitigation controls is two years old with no version history. What are the two immediate actions?

- [( )] Accept the risk and leave the document as-is until the next scheduled review
- [( )] Update the document informally and email the team
- [(X)] Escalate the risk through the proper acceptance authority chain (or select a treatment option), and raise a Change Request to update the controlled document with a new version
- [( )] Only the document matters — fix that first, risk acceptance can wait
***

**Correct!** Both issues require action — neither can wait for the other. The risk must move through the acceptance authority chain (System Owner → CISO → CEO, depending on severity) or be assigned a treatment option; it cannot simply be left unresolved. The outdated policy document must be updated through the formal Change Request process, producing a new versioned controlled document — informal edits and email notifications are not sufficient. Handling only one of these would leave either an unaccepted risk or an inaccurate controlled document on the record.

***

## Course Complete

Congratulations — you've finished **Risk Management and Document Control**!

Here's what you covered:

1. **Risk management** — CIA matrix, 3×3 risk scale, treatment options, acceptance authority (System Owner → CISO → CEO), Risk Register and POA&Ms, annual review
2. **Document control** — identification, classification, version control (major vs. minor), change request process, training coordination, annual review

**Remember the essentials:**

- Risk acceptance must be explicit, recorded, and approved at the right authority level
- Controlled Documents are immutable — changes create new versions

Questions? Reach out to **security@civicactions.com** or the Compliance team.

---

Please take 2 minutes to fill out our [**Policy Training Feedback Form**](https://docs.google.com/forms/d/e/1FAIpQLSfYwiMB4fsg32jzzrEDnGC3DEYJyloeSy91NPVj4GuPEoFfRw/viewform?usp=header)

---

> **Tip:** Close this window to record your completion of this training in Rippling.