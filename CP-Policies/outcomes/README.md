# Security Policy Training Program

## Overview

This folder contains training outcome tables derived from CivicActions security policies. The goal is to minimize the number and length of trainings while satisfying compliance requirements.

### Compliance targets

| Timeline | Framework | Key training requirements |
|----------|-----------|--------------------------|
| Now | CMMC Level 1 (FAR 52.204-21) | Basic safeguarding awareness for all personnel handling FCI; signed acknowledgment as evidence |
| Near-term | CMMC Level 2 (NIST 800-171) | Role-based awareness training (AT.L2-3.2.1, AT.L2-3.2.2); documented program with completion records |
| Near-term | ISO 27001:2022 | Competence, awareness, and documented training proportional to role (Annex A 6.3, 7.2, 7.3) |

## Training structure

Two trainings cover all outcomes from the seventeen completed policies. Professional Development Policy is excluded (no training requirement).

### Training 1 — Security Awareness Essentials

- **Audience:** All Staff (every team member, contractor, intern, third party with system access)
- **Target duration:** ~30 minutes
- **Covers:** every "All Staff" row from all outcome tables
- **Key topics:** acceptable use principles, prohibited activities, device rules (managed + BYOD), data handling and sharing, reporting obligations, access request process, SSO/MFA, project boundary awareness, data classification and labeling, encryption basics, hardware key enrollment and protection, identity and account naming, approved storage locations, DLP awareness, removable media and printing, see-something-say-something incident reporting (Slack #general / DM / security@civicactions.com), risk awareness (CIA matrix, 3x3 risk scales), approved software catalog and prohibited technology, non-compliant device blocking, home workspace security and travel precautions, lost/stolen device reporting, DR communication hierarchy (Slack → Google Chat → fallbacks), ISMS governance and core security principles, compliance framework awareness, AI approved tools and prohibited inputs, CUI definition and handling, CUI Security Boundary locations, document change request process
- **Satisfies:** CMMC L1 basic safeguarding awareness · CMMC L2 AT.L2-3.2.1 (general user awareness) · ISO 27001 A.6.3 / 7.2 / 7.3

### Training 2 — Role-Based Access & Privileged Operations

- **Audience:** Managers, IT / Service Desk, Developers, Privileged Users, System / Data Owners
- **Target duration:** ~20 minutes
- **Covers:** every role-specific row from all outcome tables
- **Key topics:** privileged access six-question test, access lifecycle (approve, grant, review, revoke), NPI management, periodic access reviews, break-glass procedures, developer CI/CD pipeline rules, third-party access, CUI cryptography (FIPS 140), key management, media sanitization and destruction, DevSecOps data handling gates, admin authenticator issuance (two hardware keys), logging and auditability metrics, governance and evidence collection, SIRT roles and IRP phases, incident declaration and severity assignment, incident communications and client notifications, evidence preservation and forensics, recovery objectives and emergency changes, post-incident retrospectives and risk integration, risk assessment methodology and CIA matrix, risk register and POA&M management, treatment options and authority, change classes (Standard/Normal/Significant/Emergency), change record content, vulnerability discovery and remediation targets, anti-malware management, drift detection, baseline management, staged patch deployment, MDM posture and remote wipe evidence, device sanitization/ITAD chain of custody, DR incident classification and system-specific recovery plans, backup ownership, secure engineering shift-left practices, supplier risk tiering (CIAX/SBOM/access scope), SCRM tracks (DS/S/PS), mandatory due diligence and contracting clauses, FOSS supply-chain management, prohibited technology screening, CUI document markings, Controlled Document identification and versioning
- **Satisfies:** CMMC L2 AT.L2-3.2.2 (role-based training for privileged users) · ISO 27001 A.8.2

### Delivery

- **Format:** short written module + quiz (acknowledgment doubles as compliance evidence)
- **Cadence:** onboarding (within 30 days) + annual refresher + ad-hoc on material policy change
- **Records:** completion + signed acknowledgment stored in HRIS/LMS per existing policy requirements

## Audience tiers

| Tag | Who |
|-----|-----|
| All Staff | Every team member, contractor, intern, third party with system access |
| Managers | People managers + project managers who approve access or manage teams |
| Developers | Engineers, DevOps, anyone writing or deploying code |
| IT / Service Desk | IT operations, access management, MDM administrators |
| Privileged Users | Anyone with admin, root, elevated, or break-glass access |
| System / Data Owners | Individuals responsible for a platform, dataset, or CUI boundary |

## Outcome tables

| Policy | File |
|--------|------|
| Acceptable Use Policy | [acceptable-use-outcomes.md](acceptable-use-outcomes.md) |
| Access Control Policy | [access-control-outcomes.md](access-control-outcomes.md) |
| Identification Policy | [identification-outcomes.md](identification-outcomes.md) |
| Data Security and Handling Policy | [data-security-outcomes.md](data-security-outcomes.md) |
| Incident Response Policy | [incident-response-outcomes.md](incident-response-outcomes.md) |
| Risk and Security Assessment Policy | [risk-security-outcomes.md](risk-security-outcomes.md) |
| Maintenance Policy | [maintenance-outcomes.md](maintenance-outcomes.md) |
| Configuration Management Policy | [config-mgmt-outcomes.md](config-mgmt-outcomes.md) |
| Change Enablement Policy | [change-enablement-outcomes.md](change-enablement-outcomes.md) |
| Vulnerability and Patch Management Policy | [vuln-patch-outcomes.md](vuln-patch-outcomes.md) |
| Physical Security Policy | [physical-security-outcomes.md](physical-security-outcomes.md) |
| Disaster Recovery Plan | [disaster-recovery-outcomes.md](disaster-recovery-outcomes.md) |
| Information Security Policy | [info-security-outcomes.md](info-security-outcomes.md) |
| AI Usage Policy | [ai-usage-outcomes.md](ai-usage-outcomes.md) |
| Document and Record Control Policy | [doc-record-control-outcomes.md](doc-record-control-outcomes.md) |
| Third-Party Management Policy | [third-party-mgmt-outcomes.md](third-party-mgmt-outcomes.md) |
| CUI Policy | [cui-outcomes.md](cui-outcomes.md) |

## Sample quiz questions

### Training 1 — Security Awareness Essentials

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

5. **A colleague asks you to classify a document containing a client's internal project plans. Which classification level applies?**
   - a) Public
   - b) Internal
   - c) Confidential ✅
   - d) No classification needed

6. **You need to send a Confidential file to an external partner who cannot access Google Drive. What is the correct method?**
   - a) Email the file as a plain attachment
   - b) Upload it to your personal Dropbox and share the link
   - c) Send it as a password-protected AES-256 archive with a 20+ character passphrase, transmitted via a separate channel ✅
   - d) Post it to a shared Slack channel

### Training 2 — Role-Based Access & Privileged Operations

1. **A team member is transferring from Project A to Project B. As their manager, what must you do regarding their access?**
   - a) Nothing — their access will sort itself out
   - b) Wait for the quarterly access review to clean up permissions
   - c) Trigger an immediate rights review to remove Project A access and request Project B access ✅
   - d) Ask the team member to manage their own access changes

2. **You have admin access to a production cloud environment. Which practice is required?**
   - a) Use your admin account for all daily work for convenience
   - b) Share admin credentials with a trusted colleague as backup
   - c) Use a separate privileged account for admin work and a standard account for daily tasks ✅
   - d) Store your admin password in a sticky note on your monitor

3. **A service account (NPI) for a CI/CD pipeline has a static API key. How often must it be rotated at minimum?**
   - a) Never, as long as it works
   - b) Annually
   - c) Quarterly (or immediately on exposure) ✅
   - d) Only when the service account owner leaves the company

4. **You discover that a former team member's Google Workspace account is still active two days after their departure. What should you do?**
   - a) Wait for the next quarterly access review to catch it
   - b) Report it to IT/Service Desk immediately so access can be disabled within the 24-hour policy requirement ✅
   - c) Deactivate the account yourself using your admin credentials
   - d) Assume PeopleOps will handle it eventually

5. **A CivicActions laptop is being decommissioned. The hard drive cannot be physically retrieved immediately. What is the approved sanitization method?**
   - a) Simply delete all files and folders
   - b) Perform cryptographic erasure by destroying the escrowed FileVault/LUKS key via MDM ✅
   - c) Format the drive using the default OS utility
   - d) Leave it until the device can be physically retrieved

6. **As an admin, you receive two hardware security keys at onboarding. Why?**
   - a) One is a spare in case the first battery dies
   - b) One is for your personal accounts
   - c) Admins need a primary and backup key to ensure continued access and meet privileged-access requirements ✅
   - d) The second key is for a colleague to share

### Incident Response, Risk & Change (Training 2)

1. **You notice unusual login attempts on a system you manage. What should you do first?**
   - a) Investigate thoroughly and fix the issue yourself before telling anyone
   - b) Report the suspected incident immediately using IRP-designated channels ✅
   - c) Delete the suspicious logs to prevent further access
   - d) Wait to see if it happens again before reporting

2. **You receive a notification that a SaaS service used by CivicActions has experienced a data breach. What is the correct first step?**
   - a) Immediately cancel the SaaS subscription
   - b) Report the vendor incident to security@civicactions.com so it can be escalated under the IR Policy ✅
   - c) Post about it in a public Slack channel so everyone is aware
   - d) Wait for the vendor to contact CivicActions directly

3. **A vulnerability scan identifies a Critical severity flaw in a production system. What is the remediation target?**
   - a) Best effort during the next scheduled update
   - b) 60 days
   - c) 15 days ✅
   - d) 30 days

4. **You need to change a Google Workspace security setting that affects all CivicActions users. How should this change be classified?**
   - a) Standard — it's just a settings toggle
   - b) Significant — it affects a company-wide service and requires a formal Change Record and Change Authority approval ✅
   - c) No classification needed for SaaS configuration changes
   - d) Emergency — all company-wide changes are emergencies

5. **MDM reports that a team member's laptop is running an outdated OS version and has missed two patch cycles. What happens?**
   - a) Nothing — the team member can update whenever convenient
   - b) The device is flagged as non-compliant, a ticket is generated, and access to protected resources is automatically blocked until remediation ✅
   - c) The laptop is remotely wiped immediately
   - d) The team member receives a disciplinary warning

6. **A risk assessment identifies a High residual risk. Who must approve acceptance of this risk?**
   - a) The System Owner
   - b) The CISO alone
   - c) The CEO (or CTO as backup) ✅
   - d) Any manager can accept it

### Physical Security & Disaster Recovery (Training 1 + Training 2)

1. **You are working from a coffee shop and need to step away for a moment. What must you do?**
   - a) Leave your laptop open — you'll only be gone a minute
   - b) Ask a nearby stranger to watch your things
   - c) Lock your screen and take your laptop with you (or secure it out of sight) ✅
   - d) Close the lid but leave it on the table

2. **Your CivicActions laptop is stolen from your car. What is the correct first action?**
   - a) Buy a replacement and set it up yourself
   - b) File a police report and wait for further instructions
   - c) Report it immediately via Incident Response channels, providing what/when/where/which asset/suspected exposure ✅
   - d) Post about it in Slack so colleagues know

3. **During a major SaaS outage, Slack is unavailable. What is the secondary communication channel per the Disaster Recovery Plan?**
   - a) Personal text messages
   - b) Google Chat ✅
   - c) Twitter/X direct messages
   - d) Wait until Slack comes back

4. **Google Workspace experiences a prolonged outage. Why is this classified as the highest-priority recovery?**
   - a) It has the most storage
   - b) It is the SSO/identity provider — all other services depend on it for authentication ✅
   - c) Email is the most-used feature
   - d) It's the cheapest to restore

### AI Usage & Information Security (Training 1)

1. **A colleague asks you to paste a client's internal financial data into ChatGPT to summarize it. What should you do?**
   - a) Go ahead — ChatGPT is on the approved tools list
   - b) Refuse — never input sensitive, confidential, or client-internal data into any AI tool, even approved ones ✅
   - c) Ask the client for permission first, then proceed
   - d) Use Gemini instead since it's a Google product

2. **You want to use a new AI tool you discovered for project work. What is required before using it?**
   - a) Nothing — just start using it
   - b) CTO approval (and client approval if on a client project), including a risk assessment ✅
   - c) Ask a colleague if they've used it
   - d) Check if it's free

3. **Which of the following best describes CivicActions' security policy structure?**
   - a) Each policy is independent with no hierarchy
   - b) The Information Security Policy is the umbrella policy that delegates specifics to subordinate policies ✅
   - c) The Acceptable Use Policy is the top-level policy
   - d) There is no defined hierarchy

### CUI & Third-Party Management (Training 2)

1. **You need to share a document containing CUI with a federal client. Which marking must appear in the document header?**
   - a) "CONFIDENTIAL"
   - b) "FOR OFFICIAL USE ONLY"
   - c) "CONTROLLED UNCLASSIFIED INFORMATION" or "CUI" ✅
   - d) No marking required for federal clients

2. **Where may CUI be stored? (Select the best answer.)**
   - a) Any CivicActions Google Drive folder
   - b) Only within the CUI Security Boundary: secured client network, access-controlled CivicActions Google Workspace Shared Drives marked "CUI", or managed CivicActions workstations ✅
   - c) Personal cloud storage with a strong password
   - d) Any encrypted USB drive

3. **A new SaaS vendor is proposed that will process CivicActions data. What must happen before procurement?**
   - a) Nothing — just sign up and start using it
   - b) Tier-appropriate due diligence must be completed, including intake form and evidence review, before the vendor is procured, deployed, or granted access ✅
   - c) Only a cost comparison is required
   - d) The vendor just needs to sign an NDA

4. **An open-source library used in a project has not received any updates in over a year. What does the Third-Party Management Policy require?**
   - a) Continue using it — open source is always safe
   - b) Treat it as unmaintained: isolate or replace the component and assess maintainer health ✅
   - c) Fork it and maintain it yourself
   - d) No action needed until a vulnerability is discovered

## Repeatable process for remaining policies

Use this process when adding training outcomes for additional policies:

1. **Extract sections** — read the policy; list every headed section
2. **Write outcomes** — for each section, write one verb-led outcome ("Explain…", "Identify…", "Apply…", "Report…")
3. **Assign audience** — tag each outcome with the narrowest audience tier that needs it
4. **Merge into trainings** — add "All Staff" outcomes to Training 1; add role-specific outcomes to Training 2 (create a new module only if the topic is large and distinct, e.g., Incident Response tabletop exercise)
5. **Add quiz questions** — write 2–3 scenario-based questions per policy
6. **Review** — CISO validates completeness against compliance framework crosswalk

## Coverage

All seventeen security policies have outcome tables. Professional Development Policy is excluded per organizational decision (no training requirement). The outcome tables collectively address:

- **CMMC L1 (FAR 52.204-21):** all 15 basic safeguarding requirements
- **CMMC L2 (NIST 800-171):** awareness and training (AT), access control (AC), identification and authentication (IA), incident response (IR), risk assessment (RA), system and communications protection (SC), configuration management (CM), maintenance (MA), media protection (MP), physical and environmental protection (PE), contingency planning / system and information integrity (SI), supply chain risk management (SR)
- **ISO 27001:2022:** Annex A 5–8 controls, with emphasis on A.5 (organizational), A.6 (people), A.7 (physical), A.8 (technological)
