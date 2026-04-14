<!--
author:   CivicActions Security Team
email:    security@civicactions.com
version:  0.1.0
language: en
narrator: US English Female

comment:  Security Awareness Essentials — the foundational security
          training every CivicActions team member completes.
          Covers device security, identity and access, data handling,
          acceptable use and AI, incident reporting, and governance.

-->

# Security Awareness Essentials

Welcome to **Security Awareness Essentials** — the foundational security training for every CivicActions team member.

This course covers the core behaviors and responsibilities you need to protect CivicActions systems, data, and clients. Whether its keeping your laptop secure, handling data correctly, or reporting something suspicious — this training has you covered.

**Who takes this?** Everyone — full-time staff, contractors, interns, and any third party with access to CivicActions systems.

**How long?** About 30–40 minutes.

**When?** Within 30 days of onboarding, then annually, and whenever there's a major policy change.

---

Let's get started!

## Module A — Your Devices and Workspace

Your laptop and workspace are the front line of security. This module covers what you need to know about your CivicActions-managed laptop, the software you install, and how to stay secure — whether you're at home, at a coffee shop, or on the road.

### Managed Devices

CivicActions issues employees a [**managed laptop**](https://civicactions.atlassian.net/wiki/spaces/ITSM/pages/161087491/CivicActions+Laptops). This laptop comes pre-configured with:

- **Full-disk encryption** — so your data stays protected if the device is lost or stolen
- **Scanning software** that checks for any security issues or viruses
- **Firewall** enabled by default
- **Auto-lock** — your screen locks automatically after a short idle period
- **Automatic patching** — your OS and security software stay up to date

> **Important:** You must use your CivicActions laptop for all work involving Internal, Confidential, or client data. Personal (BYOD) mobile devices can only be used for MFA prompts and communication apps

> **Example:** Your CivicActions Laptop comes with the Iru Mobile Device Management (MDM) system that manages FileVault encryption, security scanning, firewall, and patching out of the box. You don't need to configure any of this yourself — IT handles it before your laptop ships to you.

> **Tip:** It's smart to keeo your personal devices protected with a strong password, an idle screen lock and attention to security updates. Also, use multi-factor authentication (MFA) whereever possible and stay alert to avoid phishing scams. More tips [here](https://ssd.eff.org/).

### Software Rules

Not all software is safe to use. CivicActions maintains an [**Approved Software Catalog**](https://docs.google.com/spreadsheets/d/1yy7xSeTmTBCCaG5B-oJI3dwMN3r7tFPQ-lw79zOAdFE/edit?gid=852934818#gid=852934818) and a [**Prohibited Hardware and Software**](https://guidebook.civicactions.com/en/latest/company-policies/prohibited-hardware-and-software/) list.

- Only install software from the Approved Catalog
- If you need something new, submit a request through the [access and authorization workflow](https://civicactions.atlassian.net/wiki/spaces/ITSM/pages/1026719753/Approval+Process+for+Software+and+Services)
- Iru will block software that isn't approved

Think of it this way: if it's not on the approved list, don't install it.

> **What's approved?** Tools like Google Drive, Slack, Zoom, 1Password, Docker and GitHub Desktop are all in the catalog. What's prohibited? Huawei/ZTE devices, TikTok, Kaspersky, consumer "free VPN" apps, and ad-ware — Iru will block these automatically if you try to install them.

### Home Workspace Security

Working from home? Here are the basics:

- Position your screen so others can't see it (especially during video calls)
- Don't print anything that is Confidential or Restricted unless you have a cross-cut shredder and **shred it the same day**
- Protect your laptop from spills, heat, pets, and other environmental hazards
- If possible, use a **surge-protected outlet** for your laptop and monitor

> **Example:** You're on a Zoom call discussing a client's infrastructure when a friend stops by. Close your laptop lid or lock the screen before answering the door — and don't forget to close any admin consoles, CI/CD dashboards, or cloud management tabs you had open in the background.

### Networks and Wi-Fi

Your network connection matters just as much as your laptop.

- Use **WPA2 or WPA3** encrypted Wi-Fi, or a wired Ethernet connection
  - If secure Wi-Fi isn't available, use your phone's **personal hotspot**
- **No VPNs** unless required by the company or a client
- **Change the default admin password** on your home router (many people skip this) and keep the firmware updated
- **Never click through TLS/SSL warnings** — they exist for a reason

> **Example:** You're at a coffee shop between meetings. The shop has open Wi-Fi — no password required. Skip it. Tether to your phone's hotspot instead. It takes 30 seconds and keeps your connection encrypted.

### Travel and Public Locations

On the go? Extra caution is needed:

- Keep your laptop **physically with you** at all times
  - Of course, leaving it lid-closed, in a locked hotel room to go out to dinner is fine
- **Lock your screen** every time you step away, even for a minute
- Avoid displaying sensitive info where others can see your screen
- Use encrypted Wi-Fi or your personal hotspot — **never connect to open public Wi-Fi**
- Avoid printing sensitive documents while traveling

> **Example:** You're at an airport waiting for a flight and need to review a client proposal. Find a seat where nobody can read over your shoulder, and use your phone's hotspot instead of the airport Wi-Fi. When you get up to grab coffee, lock the screen — don't just close the lid, since it might not trigger a lock immediately.

### Keeping Your Laptop Secure

CivicActions' Iru Mobile Device Management (MDM) system enforces minimum **OS and patch levels**. If your laptop falls behind you'll get a reminder to allow the update to occur. If you don't, your laptop may **automatically update** at a time that could be disruptive to your work.

Don't ignore update prompts — they keep you and the organization safe.

> **Example:** Iru detects your laptop is two patch versions behind. You get a notification and if you don't update within the grace period, Iru can restrict your access to CivicActions systems until you're current. A quick restart is a lot easier than being locked out mid-sprint.

### Module A Quiz

Your CivicActions laptop prompts you to install a system update. You're in the middle of a deadline. What should you do?

- [( )] Dismiss the update permanently to avoid interruption
- [(X)] Install the update at the next reasonable opportunity — don't postpone indefinitely
- [( )] Disable the Iru Mobile Device Management system so updates stop appearing
- [( )] Uninstall the update software
***

**Correct!** System updates patch security vulnerabilities. You don't need to drop everything, but you should install them as soon as reasonably possible. Never disable Iru or dismiss updates permanently — your laptop could be blocked for non-compliance.

***

## Module B — Your Identity and Access

Your digital identity is how CivicActions verifies that *you* are *you*. This module covers your CivicActions account, multi-factor authentication (MFA), passwords, and the rules around who gets access to what.

### Your CivicActions Identity

- Your **@civicactions.com account** is your primary identity for all work systems
- **Never use personal accounts** (like a personal Gmail) for CivicActions work
- CivicActions uses a `firstname.lastname@civicactions.com` naming convention — IT sets this up when you onboard. If your name matches someone else's, IT adds a middle initial or variation.

> **Example:** When you join, PeopleOps verifies your identity through Rippling. IT then creates your Google Workspace account, assigns you to the right groups and Slack channels, and issues your YubiKey — all before your first day.

### SSO and MFA

**Single Sign-On (SSO)** lets you log in once and access multiple work systems. Use SSO wherever it's available.

> **In practice:** Your Google Workspace login is the front door. When you sign in there, SSO automatically connects you to Slack, Zoom, Jira, Confluence, GitLab, and other CivicActions systems — no separate passwords needed.

**Multi-Factor Authentication (MFA)** adds a second layer of proof that you are who you say you are.

- Enroll your [**YubiKey as a Passkey**](https://civicactions.atlassian.net/wiki/spaces/ITSM/pages/732856328/Yubikey+Passkey+Setup+Process) for quick authentication to CivicActions Google Workspace
- **Phishing-resistant MFA** (hardware keys) is preferred over SMS codes or authenticator apps
- SMS and TOTP (app-based codes) are fallbacks, not the first choice

> **Why a hardware key?** They can't be phished. Even if someone tricks you into entering your password on a fake site, they can't intercept a hardware key.

If you lose your YubiKey, report it immediately to security@civicactions.com - IT will disable the lost key, verify your identity, and send you a replacement. If you are locked out of your laptop or Google Account, follow the procedure for [Internal Technical Support](https://guidebook.civicactions.com/en/latest/common-practices-tools/software-and-support/#emergency-locked-out) in the Guidebook

> **Tip:** Consider buying a second YubiKey and keep one on your keychain and store the backup in a secure spot at home.

### Password Standards

Strong passwords are your first line of defense:

- **20 characters minimum** for human accounts
- **Memorize** your primary password and use a **password manager** for everything else
- **Never reuse passwords** across different services — if one gets compromised, they all do

> **Example:** Use your password manager to generate and store unique, strong passwords for any service that doesn't support Google SSO. Your Google Workspace password is the one you memorize — make it long, unique, and keep it out of your password manager so a single breach can't unlock everything.

> **Tip:** LastPass, 1Password, BitWarden and Proton Pass are some of the best known password managers.

### Access Requests

Need access to a new system or project?

1. Submit a request through the **defined access request process** — file a ticket or use a Rippling workflow with the system name, your justification, how long you need it, and which project it's for
2. Access is granted based on **least privilege** — you get only what you need
3. If your role changes or you leave, **notify IT promptly** so access can be adjusted

> **Example:** You're joining a new federal project that uses a GitLab group and a dedicated Google Shared Drive. You'd file a ticket with the project name, the specific GitLab group and Drive folder, and your role. Your manager or the project's System Owner approves it — and IT grants only what the ticket specifies.

### Project Boundary Awareness

Your access is **scoped to your assigned projects**. This means:

- Don't access systems or data outside your current project
- When you transition between projects, your access is **automatically reviewed**
- If you think you need broader access, request it through the proper channel

> **Example:** You finish a project for Client A and move to Client B. Your manager triggers a rights review — your Client A GitLab access and Shared Drive permissions are removed, and new access for Client B is set up through a fresh ticket. This keeps client data cleanly separated.

### Module B Quiz

You're setting up MFA for your CivicActions account. Which method is the preferred primary factor?

- [( )] SMS text message code
- [( )] Voice call one-time password
- [(X)] FIDO2/WebAuthn hardware security key (e.g., YubiKey)
- [( )] Email-based one-time password
***

**That's right!** FIDO2/WebAuthn hardware keys are phishing-resistant — they physically verify the site you're logging into, so attackers can't intercept them. SMS and email codes can be intercepted or phished, which is why hardware keys are the CivicActions standard.

***

## Module C — Data Handling and Classification

Not all data is created equal. CivicActions classifies data into levels so everyone knows how to handle, store, and share it properly. This module teaches you the classification system and the rules that go with each level.

### Four Classification Levels

CivicActions uses four levels of data classification:

| Level | What it means | If mishandled |
|-------|---------------|---------------|
| **Public** | Approved for release — website content, published marketing materials, open-source code. Anyone in the organization can access and share this data. | Minimal risk. |
| **Internal** | Non-sensitive internal procedures — meeting notes, project timelines, internal process documents. Should not be shared outside the organization. | Minor operational disruptions, but no severe compliance consequences. |
| **Confidential** | High-stakes data — client contracts, Federal Contract Information (FCI), Controlled Unclassified Information (CUI), client technical drawings, sensitive contract details. Access limited to those with a legitimate business need. | Could jeopardize contract eligibility or lead to regulatory penalties. |
| **Restricted** | The most sensitive data — payroll records, login credentials, Social Security Numbers, Personal Health Information (PHI). Access strictly controlled and monitored. | Severe harm, including legal action or significant financial loss. |

> **Default rule:** All data is treated as **Internal** until someone explicitly classifies it otherwise.

### Handling Rules by Level

Each classification level has specific rules for sharing, storage, and transmission:

- **Public:** No special handling needed
- **Internal:** Keep within CivicActions systems; don't post externally
- **Confidential/Restricted:** Must be **encrypted in transit and at rest**; access on a need-to-know basis only
  - **Controlled Unclassified Information (CUI)** has additional handling controls over other Confidential data

When in doubt, treat data as Confidential and ask your manager or IT.

> **Example:** You're writing a blog post about a project approach. The blog content is Public, but the client name and contract details behind it are Confidential. Before publishing, make sure the post only references what the client has approved for public release.

### Approved Storage

Where you store data matters:

- **Use only CivicActions-managed systems:** Google Workspace, approved SaaS platforms, and managed endpoints
- **Never store work data on personal cloud accounts** (personal Google Drive, iCloud, Dropbox, etc.)

If it's work data, it belongs on work systems — period.

> **General rule:** All work related information should be stored in the cloud in the appropriate CivicActions Google Shared Drive or in GitHub/GitLab.

> **Example:** You're drafting a proposal and want to save it locally "just in case." Don't — sync it to your [**CivicActions Google Drive**](https://civicactions.atlassian.net/wiki/spaces/ITSM/pages/620462113/Google+Drive+User+Guide) instead. That way it's backed up, access-controlled, and covered by DLP monitoring. If something happens to your laptop, the file is still safe in the cloud.

> **Tip:** Learn to spot labeled files in Google Workspace — look for banners, filename tags (like `[CUI]` or `[Confidential]`), or workspace labels on documents and folders. If a file contains sensitive information but doesn't have any of these markers, flag it to your manager or IT so it can be properly labeled before anyone shares it further.

### Sharing Safely

Sharing data the wrong way is one of the most common security mistakes:

- **Google Docs:** Share by **individual email address**, not "anyone with the link"
- **Confidential files sent externally:** Use a **password-protected AES-256 archive** with a **20+ character passphrase**
- **Send the passphrase through a separate channel** (e.g., share the file by email, send the password via Slack)
- **Never use email for Confidential or Restricted data** — use Google Drive sharing instead
- **Slack is for Public, Internal and some Confidential information** — never paste or upload CUI or Restricted data (including system vulnerability scans and login credentials) in Slack channels or DMs

> **Example:** A partner organization needs a Confidential deliverable but doesn't have access to your Google Drive. Create a password-protected ZIP archive with a 20+ character passphrase, email the archive, and then send the passphrase via Slack DM — never in the same email.

### Removable Media and Printing

The general rule: **avoid both** whenever possible.

- If you must print something, **secure it and shred it the same day**
- Do not use removable media - this includes USB drives - without express permission from CISO or CTO.

### DLP and Monitoring

CivicActions uses **Data Loss Prevention (DLP)** tools that may flag unusual data transfers. Here's what to know:

- Monitoring exists to **protect the organization**, not to watch over individuals
- If a DLP tool flags something you did for a legitimate reason, just respond to the follow-up request — it's not a disciplinary action

> **Example:** Google Workspace DLP rules scan for patterns like Social Security numbers and the keyword "CUI." If you share a Google Doc containing a SSN and the sharing settings are too broad, DLP may automatically block it and notify the security team. Just explain the context when asked — it's a safety net, not a gotcha.

### Module C Quiz

You need to share a Google Doc with Internal project data with a colleague. Which sharing method is correct?

- [( )] Set the link to "anyone with the link can view"
- [(X)] Share directly with your colleague's CivicActions email address
- [( )] Email the document to your colleague's personal Gmail
- [( )] Post the link in a public Slack channel
***

**Exactly!** Always share Google Docs by individual CivicActions email address. "Anyone with the link" makes the document accessible to anyone who gets that link — intentionally or accidentally.

***

## Module D — Acceptable Use and AI

CivicActions systems are tools for getting work done. This module covers the rules around how you use those tools — including the rapidly evolving area of AI.

### Core Principles

- CivicActions systems are for **authorized business use**
- **Limited personal use is OK** — as long as it doesn't interfere with work, consume significant resources, or violate any policy
- When in doubt, ask

> **Example:** Checking personal email or reading the news during a break is fine. Storing personal photos on your CivicActions Google Drive or running a side business from your managed laptop is not.

### Prohibited Activities

Some things are never OK:

- **Circumventing security controls** (disabling firewalls, VPN bypasses, etc.)
- **Unauthorized data exfiltration** — taking work data out of approved systems
- **Using non-approved tools** for work data
- **Sharing your credentials** with anyone, for any reason

> **Example:** A colleague on a tight deadline asks for your GitLab credentials to push a fix while you're away. The answer is always no — even with good intentions. They should request their own access through the proper workflow.

### AI Tools — General Rules

AI can be a powerful productivity tool, but it comes with real risks. Here are the ground rules:

1. **Use only [CivicActions-approved AI tools](https://civicactions.atlassian.net/wiki/spaces/MGPOL/pages/582418435/AI+Usage+Policy)** with IT-managed accounts
2. **Never input sensitive, confidential, or client-internal data** into any AI tool — even approved ones
3. **Human oversight is required** for all AI-generated output
4. **Peer-review AI content** before sharing it externally

> **Think of it this way:** Anything you type into an AI tool could end up in a training dataset. Would you be comfortable seeing your input in a news article? If not, don't enter it.

### Approved AI Tool Categories

CivicActions has approved specific AI tools for different purposes:

- **General purpose:** Slack Chatbot, Gemini, ChatGPT for Teams
- **Coding:** GitHub Copilot
- **Specialist:** Grammarly, Paxton AI
- **Service integrations:** Zoom AI, Mural, Confluence/Jira, Greenhouse, Figma

> **Note:** ChatGPT's Atlas browser feature is **not approved**. Stick to the approved configurations.

### New AI Tools

Want to use an AI tool that isn't on the approved list?

- You need **CTO approval** before using it
- On client projects, you also need **client approval**
- Every new tool goes through a **risk assessment** based on the NIST AI Risk Management Framework

> **Example:** You hear about a new AI transcription tool that could save time on meeting notes. Before signing up, check with the CTO — even a free trial counts. If it touches CivicActions data, it needs vetting first.

### Client Project AI Restrictions

Different clients may have different AI rules:

- Always **comply with client-specific AI policies**
- **Never put CUI** (Controlled Unclassified Information) into any AI tool
- Check your **onboarding/wrapper docs** for project-specific restrictions

> **Example:** You're on a federal project and want to use Gemini to draft a status report. Check the project's wrapper document first — some federal clients prohibit all AI tool usage on their projects, even for general text. When in doubt, ask your project lead.

### Module D Quiz

A colleague asks you to paste a client's internal financial data into ChatGPT to summarize it. What should you do?

- [( )] Go ahead — ChatGPT is on the approved tools list
- [(X)] Refuse — never input sensitive, confidential, or client-internal data into any AI tool, even approved ones
- [( )] Ask the client for permission first, then proceed
- [( )] Use Gemini instead since it's a Google product
***

**Good call!** Even approved AI tools must never receive sensitive, confidential, or client-internal data. The "approved" status means the tool itself is OK to use for general work — it doesn't mean all data is safe to put into it. Data classification rules always apply.

***

## Module E — Recognizing and Reporting Incidents

Security incidents happen — even to careful people. What matters most is how quickly you respond. This module teaches you what to look for, how to report it, and what happens next.

### See Something, Say Something

If you observe **anything** that might be a security incident, outage, or suspicious activity — **raise a flag immediately**. Don't wait until you're sure.

**How to report:**

- Post in **Slack #general**
- **DM an IT team member** directly
- **DM your manager**
- Email **security@civicactions.com**

Use whichever channel is fastest. Speed matters more than formality.

> **Examples of things to report:** A phishing email, a lost laptop, an unfamiliar login alert, a SaaS app behaving strangely, a colleague who seems to have access they shouldn't, a physical security concern at a co-working space.

### Blame-Free Reporting

CivicActions has a **blame-free reporting culture**:

- Good-faith reporting will **never result in retaliation**
- **Speed matters more than certainty** — it's better to report something that turns out to be nothing than to stay silent about something real
- We learn more from honest reports than from silence

> **Example:** You accidentally sent a Google Doc with Internal data to the wrong email address. Report it right away — DM an IT team member or email security@civicactions.com. This kind of honest report helps the team contain the issue quickly. Nobody gets in trouble for an honest mistake reported fast.

### Lost or Stolen Devices

If a device is lost or stolen, report it **immediately** through the incident channels. Include:

- **What** device (laptop, phone, etc.)
- **When** it went missing
- **Where** you last had it
- **Which asset** (serial number or asset tag if you know it)
- **What data** might be exposed

This applies to **both CivicActions laptops and personal devices** that have authenticated to CivicActions systems (like a phone used for MFA).

> **Example:** You left your CivicActions MacBook in a rideshare. DM an IT team member on Slack right away with: "Lost my laptop in a Lyft at 3 PM, last had it at the airport, serial number XXXX, had access to Client B's Shared Drive." IT can trigger a remote wipe through Iru immediately — FileVault encryption means the data is already protected, but the wipe makes sure.

### Incident Confidentiality

When an incident is under investigation:

- Treat incident details on a **need-to-know basis**
- **Don't share details** outside the designated channels (Slack incident thread, email to security team, etc.)

> **Example:** You hear that a SaaS vendor CivicActions uses had a breach. Don't post about it in a public Slack channel or mention it to a client. Wait for the Incident Commander or Communications Officer to share approved updates through the proper channels.

### Post-Incident Participation

After an incident is resolved, you may be asked to participate in a **retrospective** (or "post-mortem"). These are learning sessions, not blame sessions:

- Share what you observed honestly
- Focus on **what happened** and **how to prevent it next time**
- Lessons learned feed back into policy improvements

### Module E Quiz

You receive a suspicious email with an attachment claiming to be an invoice. What is the correct first step?

- [( )] Open the attachment to check if it looks legitimate
- [( )] Forward it to your personal email for safekeeping
- [(X)] Report it immediately to security@civicactions.com
- [( )] Delete it and forget about it
***

**Correct!** Never open suspicious attachments. Report the email immediately so the security team can analyze it and warn others if needed. Deleting it silently means the team can't investigate — and others might fall for the same phishing attempt.

***

## Module F — Governance, Risk, and Compliance

You don't need to be a compliance expert, but it helps to understand the big picture. This module gives you a quick overview of how CivicActions policies are organized, what frameworks they align to, and what you can do to support them.

### Policy Structure

CivicActions has a layered policy structure:

- The [**Information Security Policy**](https://civicactions.atlassian.net/wiki/spaces/MGPOL/pages/703725569/Information+Security+Policy) is the umbrella — it sets the overall direction
- It delegates specifics to **subordinate policies**: Acceptable Use, Access Control, Incident Response, Data Security, and more
- All policies are accessible to you — [know where to find them](https://civicactions.atlassian.net/wiki/spaces/MGPOL/overview?homepageId=309068052) if you need them

> **Example:** Wondering what the rules are for using USB drives? You'd look at the Data Security and Handling Policy. Not sure about your MFA requirements? Check the Identification Policy. The Information Security Policy is the table of contents — it points you to the right place.

### Compliance Frameworks

CivicActions aligns to several compliance frameworks:

| Framework | What it covers |
|-----------|---------------|
| **CMMC L1/L2** | Federal contractor cybersecurity requirements (FAR/NIST 800-171) |
| **ISO 27001** | International information security management standard |
| **ISO 9001** | Quality management |
| **ITIL** | IT service management best practices |

This training satisfies security awareness requirements for CMMC and ISO 27001.

### Risk Awareness

Understanding risk doesn't have to be complicated:

- **CIA triad:** Confidentiality, Integrity, Availability — these are the three things we protect
- **3×3 risk scale:** Likelihood (Low/Medium/High) × Impact (Low/Medium/High)
- **Risk acceptance** must be explicit and approved by the right people — you can't just decide to accept a risk on your own

> **Example:** You notice that a tool your team uses doesn't support SSO. You can't just decide "that's fine" and keep using it with a local password. A risk like that needs to be formally documented in the Jira Risk Register and approved by the appropriate authority — the CISO or CTO for higher risks, or an IT team member for lower ones.

### Disaster Recovery Communications

During a major outage, normal communication tools might be down. Here's the backup plan:

1. **Primary:** Slack chat, Slack huddle, Zoom video
2. **Secondary:** Google Chat, Google Meet, telephone

Clients and partners are notified only if the outage impacts deliverables.

### Document Change Requests

Want to suggest a change to a policy or controlled document?

- Submit an [**internal IT support request**](https://civicactions.atlassian.net/wiki/spaces/ITSM/pages/607584257/Atlassian+Assist)
- Controlled Documents are **reviewed annually**
- Access to documents is managed via **security groups**

> **Example:** You spot an outdated link in the Acceptable Use Policy. Create a ticket on the Compliance Jira board describing the change. The Document Controller reviews it, and if approved, a new minor version (e.g., 2.1 → 2.2) is published. You don't need to edit the document yourself.

### Maintenance and Patching

You don't need to manage these programs — but you should know they exist:

- CivicActions IT manages [**configuration management**](https://civicactions.atlassian.net/wiki/spaces/MGPOL/pages/767983618/Configuration+Management+Policy), [**change enablement**](https://civicactions.atlassian.net/wiki/spaces/MGPOL/pages/768114689/Change+Enablement+Policy), [**vulnerability and patch management**](https://civicactions.atlassian.net/wiki/spaces/MGPOL/pages/768344065/Vulnerability+and+Patch+Management+Policy)
- Think of these as **guardrails, not gates** — they run in the background to keep everything secure
- Your part: install updates when prompted and report anything that seems off

### Third-Party Awareness

CivicActions works with outside vendors and partners. Here's what you should know:

- **No supplier** may be procured or granted system access until due diligence is complete
- If you have concerns about a vendor's security practices, **report them to IT**

> **Example:** A project lead wants to try a new design collaboration tool. Before signing up, it needs to go through supplier intake and Confidentiality, Integrity, Availability, and eXpense (CIAX) scoring for SaaS, SSO/MFA validation, data residency review. Even a free-tier tool that touches CivicActions data must be vetted first.

### Module F Quiz

During a major SaaS outage, Slack is unavailable. What is the secondary communication channel per the Disaster Recovery Plan?

- [( )] Personal text messages
- [(X)] Google Chat
- [( )] Twitter/X direct messages
- [( )] Wait until Slack comes back
***

**Right!** The DR communication hierarchy is: Primary (Slack/Zoom), Secondary (Google Chat/Meet or telephone). Knowing these backups means you can stay connected and coordinated even when the primary tools are down.

***

## Bonus Quiz

You've completed all six modules — nice work! Here's one final question that covers an important topic from the course.

What is the **default classification level** for all CivicActions data that hasn't been explicitly classified?

- [( )] Public
- [(X)] Internal
- [( )] Confidential
- [( )] Restricted
***

**Correct!** All data is treated as **Internal** by default until it is explicitly classified otherwise. This means you should handle any unclassified data as Internal — keep it within CivicActions systems and share it only with CivicActions team members. If you think data should be treated at a higher (or lower) level, work with your manager to get it properly classified.

***

## Course Complete

Congratulations — you've finished **Security Awareness Essentials**!

Here's what you covered:

1. **Devices and workspace** — managed laptops, approved software, home and travel security
2. **Identity and access** — SSO, MFA with hardware keys, passwords, least-privilege access
3. **Data handling** — classification levels, approved storage, safe sharing
4. **Acceptable use and AI** — approved tools, data restrictions, human oversight of AI
5. **Incident reporting** — see something say something, blame-free culture, lost devices
6. **Governance and compliance** — policy structure, frameworks, risk, DR communication

**Remember the basics:**

- Use your CivicActions laptop with approved software
- Protect your identity with hardware MFA keys and strong passwords
- Handle data according to its classification level
- Never put sensitive data into AI tools
- Report anything suspicious — fast

Questions? Reach out to **security@civicactions.com** or post in **Slack #general**.
