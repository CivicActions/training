<!--
author:              CivicActions Security/compliance Team
language:            en
comment:             This CivicActions internal training course is updated and maintained by CivicActions.
controlled_document: CP7063 Access Governance, Risk and Supplier Oversight Training
-->

# Access Governance
Welcome to **Access Governance** — the training for IT and system/data owners.

While Training 3 (IT Operations) covers the technical operations, this course covers the **governance decisions** you make: approving and reviewing access. These are the "approve, review, decide" responsibilities that keep the organization running securely.

**Who takes this?** IT and System/Data Owners.

**Prerequisite:** Training 1 — Security Awareness Essentials.

**How long?** About 5-10 minutes.

**When?** Within 30 days of onboarding, then annually, and whenever there's a major policy change.

**Compliance:** CMMC L2 (AC controls), ISO 27001 A.5.15–A.5.18.

> **Note on links:** Links are sometimes provided for additional information. Following them is not required for the training.

---

Let's get started!

## Module A — Access Governance

As a manager or system owner, you're the gatekeeper for who gets access to what. This module covers your approval responsibilities, the access lifecycle, and the reviews that keep permissions current.

See also: [**Access Control Policy**](https://civicactions.atlassian.net/wiki/spaces/MGPOL/pages/744947714/Access+Control+Policy)

### Common Access Governance Themes

- **Default-Deny / Zero Trust:** No access until there's a justified reason. Every request is untrusted until proven otherwise — being on the network doesn't count.
- **SSO-First:** Google Workspace is the front door. If a tool supports SSO, native passwords get disabled. No shadow accounts, no shared logins.
- **Separation of Duties:** Requester, approver, and implementer must be three different people. You cannot approve your own access.
- **Privileged Access:** If an account can change permissions, bypass controls, access all data, alter configs, touch audit logs, or do something irreversible — it's privileged. Separate admin accounts, just-in-time elevation, two-person authorization for destructive actions.
- **Non-Person Identities:** Service accounts, bots, API keys, and tokens follow the same lifecycle as human accounts - registered, scoped, reviewed quarterly, revoked when done. Every one has a human owner on record.
- **The 24-Hour Rule:** Access is disabled the day someone separates. Full removal — accounts, tokens, group memberships - within 24 hours, no exceptions.

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

## Bonus Quiz

Great work! Here's a final question on a key governance concept.

During a quarterly access review, you discover that a former contractor still has active access to a CivicActions system. Their contract ended two months ago. What should you do?

- [( )] Leave it — they might come back for another contract
- [( )] Send them an email asking them to stop using the access
- [( )] Wait until the next quarterly review to confirm it should be removed
- [(X)] Revoke the access immediately and report it as a potential security finding
***

**Correct!** Orphaned access — permissions that belong to someone who no longer needs them — is a security risk and a common audit finding. Revoke it immediately. Don't wait, don't ask the person to self-manage, and don't assume they're not using it. The fact that it went undetected for two months is itself worth reporting so the access review process can be improved.

***

## Course Complete

Congratulations — you've finished **Access Governance**!

Here's what you covered:

Approval role, access lifecycle (approve → grant → review → revoke), quarterly reviews, third-party access, CUI access decisions

**Remember the essentials:**

- Least privilege and need-to-know guide every access decision
- Role changes, project transitions, and departures trigger immediate access reviews

Questions? Reach out to **security@civicactions.com** or the Compliance team.

---

Please take 2 minutes to fill out our [**Policy Training Feedback Form**](https://docs.google.com/forms/d/e/1FAIpQLSfYwiMB4fsg32jzzrEDnGC3DEYJyloeSy91NPVj4GuPEoFfRw/viewform?usp=header)

---

> **Tip:** Close this window to record your completion of this training in Rippling.