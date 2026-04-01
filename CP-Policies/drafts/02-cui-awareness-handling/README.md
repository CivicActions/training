<!--
author:   CivicActions Security Team
email:    security@civicactions.com
version:  0.1.0
language: en
narrator: US English Female

comment:  CUI Awareness & Handling — additional training for staff
          assigned to federal contracts or projects involving
          Controlled Unclassified Information (CUI).

-->

# CUI Awareness & Handling

Welcome to **CUI Awareness & Handling** — an additional training for CivicActions team members who work on federal contracts or projects that involve **Controlled Unclassified Information (CUI)**.

This course builds on what you learned in *Security Awareness Essentials* (Training 1). It focuses specifically on the rules, boundaries, and markings that apply when you handle CUI.

**Who takes this?** Staff assigned to federal contracts or projects involving CUI.

**Prerequisite:** Training 1 — Security Awareness Essentials.

**How long?** About 10–15 minutes.

**When?** Before you're granted CUI access, then annually, and whenever there's a contract or policy change.

**Compliance:** CMMC L2 (NIST 800-171), FAR 52.204-21.

---

Let's get started!

## Module A — What Is CUI and Why It Matters

Before you can handle CUI properly, you need to understand what it is, who can access it, and why the rules exist.

### CUI Defined

**CUI** stands for **Controlled Unclassified Information**. It's government-created or government-owned information that requires safeguarding under federal regulation — specifically [**32 CFR Part 2002**](https://www.ecfr.gov/current/title-32/subtitle-B/chapter-XX/part-2002).

CUI isn't classified (like "Secret" or "Top Secret"), but it's still sensitive. At CivicActions, examples of CUI include:

- **Vulnerability scan results** from federal systems
- **Any document marked** "CUI" or "Controlled Unclassified Information"
- **Contractor bids and proposals**
- **Non-public contract data**

> **Example:** Your team runs a vulnerability scan on a federal client's infrastructure and saves the results to a Shared Drive. Those scan results are CUI — they reveal system weaknesses that could be exploited if leaked. They need to stay inside the CUI Security Boundary, not in a general project folder.

> **Key point:** CUI has its own handling rules that go beyond CivicActions' standard "Confidential" classification. Even if you already know the data handling rules from Training 1, CUI adds an extra layer.

### Need-to-Know Principle

Not everyone on a federal contract automatically gets CUI access. Access is restricted to people with a **legitimate business need** on a specific contract or project.

- If you don't need CUI to do your job, you shouldn't have access
- If you change projects, your CUI access is reviewed and may be revoked
- If you're unsure whether you should have access to something, ask your project lead

> **Example:** You're a developer on a federal contract and need access to vulnerability data stored in the CUI Shared Drive. You'd file a ticket with your justification and the specific Drive folder. Your manager and the Data Owner approve it. When you roll off the project, that access is revoked as part of the rights review — even if you're moving to another federal project.

### Compliance Context

CUI handling requirements come from federal law and regulation:

| Regulation | What it does |
|-----------|-------------|
| **DFARS** | Defense Federal Acquisition Regulation Supplement — requires CUI protection for defense contracts |
| **FAR 52.204-21** | Basic safeguarding requirements for all federal contractor information systems |
| **NIST 800-171** | The 110 security controls that define how CUI must be protected |

**Why it matters to you:** Failure to comply with these rules can affect CivicActions' contract eligibility. That means protecting CUI isn't just a best practice — it's a business requirement.

> **Example:** If a CMMC assessment finds that CUI was stored outside the Security Boundary, it could jeopardize CivicActions' ability to bid on future defense contracts. Every person on the project plays a role in maintaining compliance.

### Module A Quiz

A colleague who isn't assigned to your federal contract asks to see a CUI document for a blog post they're writing. What should you do?

- [( )] Share it — they work at CivicActions, so they have access
- [( )] Share a redacted summary only
- [(X)] Decline — CUI access is limited to personnel with a legitimate business need on the specific contract
- [( )] Ask them to sign an NDA first
***

**Correct!** CUI access is governed by the need-to-know principle. Working at CivicActions doesn't automatically grant access to all CUI. The person must have a legitimate business need tied to the specific contract or project. Point them to their project lead if they believe they need access.

***

## Module B — The CUI Security Boundary

CUI can only live in specific, approved places. This module explains exactly where CUI is allowed — and where it absolutely is not.

### Three Approved CUI Locations

CUI may only be stored or processed in these three places:

1. **Secured client network** — the client's own system, operating within their Authority to Operate (ATO) security boundary
2. **CivicActions Google Workspace** — specifically in **access-controlled Shared Drives** that are explicitly marked **"CUI"**
3. **CivicActions managed workstations** — your CivicActions-issued laptop or an approved hardened BYOD device

That's it. If a location isn't on this list, CUI doesn't belong there.

> **Example:** Your team is working on a federal project. CUI goes in the project's dedicated CUI Shared Drive in Google Workspace — not in the team's general project folder, not in Confluence, and not in a Slack channel. If you need to collaborate on a CUI document, share it by individual @civicactions.com email within that Shared Drive.

### Auto-Tagging in Google Workspace

CivicActions has set up Google Workspace to **auto-tag documents containing "CUI"** for easier discovery and audit. This means:

- Documents in CUI Shared Drives are automatically tracked
- Auditors can verify that CUI is staying where it belongs
- You benefit from this without needing to do anything extra — just use the correct Shared Drives

### Prohibited CUI Locations

CUI must **never** be stored in:

- **Personal cloud storage** (personal Google Drive, iCloud, Dropbox, OneDrive, etc.)
- **Unapproved SaaS platforms** (any tool not in the CUI Security Boundary)
- **Removable media** (USB drives, external hard drives) — unless you have explicit **CISO approval**
- **Personal email**
- **AI tools** — no CUI in ChatGPT, Gemini, Copilot, or any other AI platform
- **Slack** — do not share CUI data in any Slack channel or DM

> **Remember:** Just because a tool is on the CivicActions Approved Software Catalog doesn't mean it's approved for CUI. The CUI Security Boundary is a much tighter set of locations.

### Encryption Requirements

CUI requires **FIPS 140–validated cryptography** for protection:

- **In transit** — data must be encrypted when moving between systems (TLS, HTTPS, etc.)
- **At rest** — data must be encrypted where it's stored

Before using any SaaS platform for CUI, verify that the provider's encryption meets the FIPS 140 standard. If you're not sure, ask IT.

> **Example:** A teammate suggests storing CUI in a new cloud service that advertises "AES-256 encryption." That's not enough — for CUI, the encryption module itself must be FIPS 140-2 or 140-3 *validated*, which is a specific federal certification. The cloud provider also needs to meet FedRAMP Moderate equivalency. Check with IT before putting CUI anywhere new.

### Module B Quiz

Where may CUI be stored?

- [( )] Any CivicActions Google Drive folder
- [(X)] Only within the CUI Security Boundary: secured client network, access-controlled CivicActions Google Workspace Shared Drives marked "CUI", or managed CivicActions workstations
- [( )] Personal cloud storage with a strong password
- [( )] Any encrypted USB drive
***

**Right!** CUI has a strict Security Boundary. It can only live on the secured client network, in CivicActions Google Workspace Shared Drives that are explicitly marked "CUI" and access-controlled, or on CivicActions managed workstations. No personal cloud, no unapproved SaaS, no removable media without CISO approval, and no AI tools.

***

## Module C — CUI Handling Rules

Now that you know where CUI can live, here's how to handle it day to day. The rules are straightforward but strict.

### No Unauthorized Transfer

This is the most important rule:

**Do not copy, print, download, or move CUI outside the Security Boundary.**

That means:

- Don't download CUI to a personal device
- Don't copy it to a general-purpose Shared Drive
- Don't print it unless you have a specific, approved reason — and if you do, shred it immediately after use
- Don't email it to a non-CUI-approved address

If you need to move CUI for a legitimate reason, check with your project lead and IT first.

> **Example:** You need to reference some vulnerability data from the CUI Shared Drive while writing a status report. Don't download the file to your desktop and paste snippets into a Google Doc in the general project folder. Instead, keep the CUI document in the CUI Shared Drive and reference it from there — or write the status report within the CUI boundary too.

### Minimize Retention

Don't hold onto CUI longer than you need it.

- **Delete CUI copies** as soon as they're no longer needed for your current task
- Don't keep "just in case" copies
- The less CUI you retain, the smaller the risk if something goes wrong

> **Example:** You downloaded a contractor bid document to review on your CivicActions laptop. Once you've finished your review and added your notes to the CUI Shared Drive, delete the local copy. Don't leave it sitting in your Downloads folder.

### Project Closeout

When a CUI project ends, there's a required cleanup process:

1. Conduct a **CUI audit** as part of project closeout
2. Confirm that all CUI copies are either **returned to the client** or **securely destroyed**
3. Document the results

This isn't optional — it's a project closeout requirement.

### Incident Reporting for CUI

If you suspect CUI has been **compromised, exposed, or mishandled**:

- Report it as a **security incident immediately**
- Use the same channels: **Slack #general**, **DM an IT team member or your manager**, or email **security@civicactions.com**
- Don't try to "fix it" yourself first — speed is critical

CUI incidents may trigger notification obligations to the government client, so the security team needs to know right away.

> **Example:** You realize you accidentally shared a CUI Google Doc with someone outside the project by mistyping their email. Don't try to unshare it quietly and hope nobody notices — report it immediately to security@civicactions.com. The security team can assess the exposure, revoke access, and handle any required government notifications.

### Module C Quiz

A project involving CUI is ending. What must happen to CUI copies held by CivicActions?

- [( )] Archive them indefinitely in case they're needed later
- [(X)] Include a CUI audit in project closeout — confirm all copies are returned to the client or destroyed
- [( )] Move them to a general-purpose Shared Drive
- [( )] Nothing — CUI protections expire when the contract ends
***

**Correct!** CUI protections don't expire when a contract ends. During project closeout, all CUI copies must be accounted for through a CUI audit and either returned to the client or securely destroyed. Archiving CUI "just in case" or moving it to a general-purpose drive would violate the Security Boundary rules.

***

## Module D — CUI Document Markings

When CUI leaves the Security Boundary — for example, when shared with a partner agency or subcontractor — it must be **properly marked**. This module covers what those markings look like.

### When to Mark

Marking is **required when sharing CUI outside a security boundary**. For example:

- Sending a document to a partner agency
- Sharing with a subcontractor on the same contract
- Providing deliverables to the government client

> **Example:** Your team is submitting a security assessment report to the federal client. Before you send it, add "CUI" in the document header and "Sensitive in accordance with 32 CFR 2002" centered at the bottom of the first page. Documents that stay inside your CUI Shared Drive are already covered by the folder marking and auto-tagging.

### Header Marking

The top of the document must include:

> **CONTROLLED UNCLASSIFIED INFORMATION**

or the abbreviation:

> **CUI**

This goes in the **document header** — visible on every page if possible.

### Footer Marking

The bottom of the **first page** must include:

> **Sensitive in accordance with 32 CFR 2002**

This marking should be **centered** at the bottom of the page.

### Optional Originator Line

Some agencies or contracts require an **originator line** — a line identifying who created the document and under what authority. Include this if your contract or agency guidance requires it.

### Internal Working Documents

For documents that stay **within the CUI Shared Drive** (i.e., they don't leave the Security Boundary):

- The **folder-level marking** and **auto-tagging** already satisfy the requirement
- You don't *need* to mark each document individually — but it's **best practice** to do so

> **Tip:** When in doubt, mark it. An extra "CUI" header never hurts, and it helps anyone who opens the document understand its sensitivity immediately.

> **Example:** You're drafting a proposal response in the CUI Shared Drive. Even though the Drive itself is marked "CUI" and Google auto-tags the document, adding "CUI" to the header is a good habit. If that document is ever exported, printed, or shared outside the boundary, the marking is already in place.

### Handling Unmarked CUI

Sometimes you'll come across a file that looks like CUI but doesn't have the right markings. Don't ignore it — follow these four steps:

1. **Identify** — notice that the file appears sensitive (e.g., a technical drawing from a client or vulnerability data) but lacks a "CUI" header or label
2. **Report** — notify your manager or compliance officer about the unmarked data immediately
3. **Ensure correct marking** — work with the responsible party to apply the correct electronic labels, banners, or filename tags before any further storage or sharing
4. **Store and share securely** — once labeled, keep the data only within approved CUI boundaries (e.g., the designated CUI Shared Drive)

> **Example:** A teammate drops a client's infrastructure diagram into the general project folder. It has no "CUI" marking, but it clearly contains sensitive technical details about a federal system. Don't just move it yourself — flag it to your manager, get it properly labeled, and then store it in the CUI Shared Drive where it belongs.

### Module D Quiz

You need to share a document containing CUI with a federal client. Which marking must appear in the document header?

- [( )] "CONFIDENTIAL"
- [( )] "FOR OFFICIAL USE ONLY"
- [(X)] "CONTROLLED UNCLASSIFIED INFORMATION" or "CUI"
- [( )] No marking required for federal clients
***

**Correct!** When sharing CUI outside the Security Boundary, the header must read "CONTROLLED UNCLASSIFIED INFORMATION" or "CUI." "Confidential" is a CivicActions internal classification — it's not the same as the federally defined CUI marking. "For Official Use Only" (FOUO) was a legacy marking that has been replaced by CUI.

***

## Bonus Quiz

You've completed all four modules — well done! Here's one final question on a key CUI concept.

A teammate suggests pasting CUI data into an approved AI tool (like ChatGPT for Teams) to help draft a report. Is this allowed?

- [( )] Yes — it's an approved tool, so all data types are permitted
- [( )] Yes — as long as you delete the chat afterwards
- [(X)] No — CUI must never be entered into any AI tool, even approved ones
- [( )] Yes — but only if the project lead approves
***

**Correct!** AI tools are explicitly listed as a **prohibited CUI location**, regardless of whether the tool is on the CivicActions Approved Software Catalog. The CUI Security Boundary is limited to the secured client network, CUI-marked Google Workspace Shared Drives, and managed workstations. No exceptions for AI tools.

***

## Course Complete

Congratulations — you've finished **CUI Awareness & Handling**!

Here's what you covered:

1. **What CUI is** — government-owned sensitive info regulated under 32 CFR 2002, with access limited by need-to-know
2. **The Security Boundary** — only three approved locations: client network, CUI-marked Shared Drives, managed workstations
3. **Handling rules** — no unauthorized transfer, minimize retention, CUI audit at project closeout, immediate incident reporting
4. **Document markings** — header ("CUI"), footer ("Sensitive in accordance with 32 CFR 2002"), and when markings are required

**Remember the essentials:**

- CUI can only live within the Security Boundary
- Never put CUI in personal storage, unapproved tools, or AI platforms
- Delete CUI copies when you no longer need them
- Mark documents properly when sharing outside the boundary
- Report any suspected CUI compromise immediately

Questions? Reach out to **security@civicactions.com** or your project lead.
