<!--
author:   CivicActions Security Team
email:    security@civicactions.com
version:  0.1.0
language: en
narrator: US English Female

comment:  IT Operations: Change, Configuration & Patch Management —
          training for IT, developers, and system owners on the
          technical policies they need to execute day to day.

-->

# IT Operations: Change, Configuration & Patch Management

Welcome to **IT Operations: Change, Configuration & Patch Management** — the training for CivicActions IT staff, developers, and system/data owners.

While all staff got a high-level awareness of these programs in Training 1, this course goes deeper. You're the people who actually *run* these programs, so you need to understand the details: configuration baselines, change classifications, patch timelines, privileged access rules, and disaster recovery operations.

**Who takes this?** IT / Service Desk, Developers, System/Data Owners.

**Prerequisite:** Training 1 — Security Awareness Essentials.

**How long?** About 15–20 minutes.

**When?** Within 30 days of onboarding, then annually, and whenever there's a major policy change.

**Compliance:** CMMC L2 (CM, MA, SI controls), ISO 27001 A.8.9, A.8.32.

---

Let's get started!

## Module A — Configuration Management

Configuration management is how we make sure our systems stay in a known, approved state. If someone changes something — intentionally or not — we need to know about it.

### CI Scope

CivicActions formally tracks five classes of **Configuration Items (CIs)**:

1. **CIA "High" systems** — anything rated high for confidentiality, integrity, or availability
2. **Managed endpoints** — CivicActions laptops and other managed devices
3. **Cloud resources** — infrastructure we manage in cloud environments
4. **Production SaaS configurations** — settings for the SaaS tools we rely on
5. **Critical documentation** — policies, procedures, and architecture docs

If it falls into one of these classes, it's under formal configuration control.

> **Example:** Think about the Kandji MDM profiles that enforce FileVault encryption and auto-lock on every CivicActions laptop. Those profiles are CIs under "Managed endpoints." The Google Workspace SAML configuration that provides SSO across the company? That's a "Production SaaS configuration." Both are formally tracked.

### Configuration-as-Code

At CivicActions, **Git is the authoritative baseline** for configurations:

- Git history *is* the change history — every modification is tracked
- Jira and Confluence link to repos and pipelines for traceability
- If it's not in Git, it's not the official configuration

### Baselines and Secure Defaults

Every system starts from a **secure baseline**:

- Apply **least functionality** — remove non-essential services and components
- Include **hardening settings**, identity/access parameters, and logging hooks
- Review baselines **at least annually** to make sure they're still appropriate

> **Think of a baseline as the "factory settings" for security.** It's the known-good starting point that everything else builds from.

> **Example:** A new CivicActions laptop starts from a Kandji baseline — FileVault enabled, EDR installed, host firewall on, auto-lock at 15 minutes, and automated patching configured. That's the known-good state. If an engineer disables the firewall to troubleshoot a network issue and forgets to re-enable it, drift detection will catch it.

### Drift Detection

Sometimes systems drift away from their baseline — a setting gets changed, a package gets updated outside the process, etc. CivicActions uses **automated drift detection** to catch this:

1. The system flags the deviation
2. A ticket is automatically created
3. The ticket must be **triaged within two business days**
4. Resolution: either **reconcile back to the baseline** or **raise a formal change request** to update the baseline

Ignoring drift isn't an option.

> **Example:** Kandji detects that a developer's laptop no longer has the required EDR agent running. A Jira ticket is automatically created. The Service Desk triages it within two business days and finds the agent crashed after an OS update. They reinstall the agent, confirm compliance in Kandji, and close the ticket — reconciled back to baseline.

### Evidence and Audit

Configuration management produces records that auditors care about:

- CI inventories
- Baselines and their change histories
- Drift reports
- Approval records

All of these are **Controlled Records** — keep them organized and up to date.

### Module A Quiz

Automated drift detection flags a configuration deviation on a production system. What is the required response?

- [( )] Ignore it if the system is working
- [(X)] Triage within two business days — resolve by reconciling to baseline or raising a change request
- [( )] Immediately roll back all recent changes
- [( )] Wait for the annual baseline review
***

**Correct!** Drift must be triaged within two business days. The resolution is either to reconcile the system back to the approved baseline or to submit a formal change request to update the baseline. Ignoring drift or waiting for the annual review creates untracked risk.

***

## Module B — Change Enablement

Changes are inevitable — new features, security patches, configuration updates. Change enablement makes sure those changes happen safely, with the right reviews and approvals.

### Change Classes

CivicActions categorizes changes into four classes, each with different rules:

| Class | What it is | Approval |
|-------|-----------|----------|
| **Standard** | Fully automated, pre-approved (e.g., routine patch waves) | No manual approval needed |
| **Normal** | Peer-reviewed PR/MR with delegated approval | Peer review + automated tests |
| **Significant** | Affects High Impact services | Formal Change Record + Change Authority approval + rollback plan |
| **Emergency** | During an active incident | Incident Commander authorized + post-incident review |

> **Rule of thumb:** The bigger the blast radius, the more review it needs.

> **Example:** Monthly OS patch waves pushed through Kandji? That's a **Standard** change — automated, pre-approved, no manual sign-off needed. A developer opening a PR to update a service's Terraform config? **Normal** — peer review plus CI tests. Changing the Google Workspace password policy for all CivicActions users? **Significant** — you need a formal Change Record, Change Authority approval, and a rollback plan. Revoking a compromised API key during an active incident? **Emergency** — the Incident Commander authorizes it now, and the team does a full retrospective within 72 hours.

### Change Record Content

For Normal and Significant changes, the change record should include:

- Description of the change
- Impacted services and CIs
- Impact and urgency assessment
- Risk assessment
- Test results
- Implementation plan
- **Backout plan** (how to undo it if something goes wrong)
- Maintenance window
- Evidence of completion

### Approvals and Guardrails

Each change class has specific guardrails:

- **Normal:** Peer review + automated tests must pass
- **Significant:** Change Authority approval + documented rollback plan
- **Emergency:** Incident Commander authorizes in the moment; full review happens afterwards

### Scheduling

Changes don't happen whenever you feel like it:

- Each service has a **weekly maintenance window**
- There's also a **monthly company calendar slot** for broader changes
- Changes outside these windows require **justification and additional approval**

> **Example:** Each user-facing service — Google Workspace, Slack, Kandji — has its own weekly maintenance window published on the company calendar. If you need to push a Significant change outside that window (say, a time-sensitive security configuration), you'll need to justify the timing and get additional approval.

### Post-Implementation Review

After a change goes live:

1. **Verify** the change worked as expected
2. **Update configuration records** to reflect the new state
3. If something didn't go well, hold a **retrospective within 5 business days**
4. Capture **lessons learned** and feed them back into the process

### Change Freezes

Sometimes the organization needs stability more than new changes:

- **Change freezes** are applied during critical delivery periods or when error budgets are exceeded
- During a freeze, only **stability-improving fixes** are permitted
- Everything else waits until the freeze is lifted

### Module B Quiz

You need to change a Google Workspace security setting that affects all CivicActions users. How should this change be classified?

- [( )] Standard — it's just a settings toggle
- [(X)] Significant — it affects a company-wide service and requires a formal Change Record and Change Authority approval
- [( )] No classification needed for SaaS configuration changes
- [( )] Emergency — all company-wide changes are emergencies
***

**Correct!** A security setting change that affects every CivicActions user is a Significant change — it has a large blast radius. It requires a formal Change Record, Change Authority approval, and a rollback plan. Just because it's "one toggle" in a SaaS admin panel doesn't make it low-risk.

***

## Module C — Vulnerability and Patch Management

Finding and fixing vulnerabilities before attackers exploit them is one of the most impactful things we do. This module covers how CivicActions discovers, prioritizes, and remediates vulnerabilities.

### Discovery Methods

We find vulnerabilities through multiple channels:

- **MDM/EDR** for endpoint vulnerabilities (OS, installed software)
- **SBOMs + SCA/SAST/DAST** for custom software (software bills of materials, static and dynamic analysis)
- **Vendor advisories** for SaaS platforms we use
- **Approved lists** for browser extensions, IDE plugins, and SaaS add-ons

> **Example:** Kandji continuously monitors laptops for missing OS patches and outdated software. Dependabot and Dependency-Track flag vulnerable libraries in your repos through pull requests. When a vendor like Atlassian publishes a security advisory for Confluence, the security team assesses it against our environment. These channels all feed into the same vulnerability management process.

### Prioritization

Not all vulnerabilities are equal. We prioritize based on:

1. **Severity + exploitability** — how bad is it, and is it being exploited in the wild?
2. **Service criticality** — how important is the affected system?
3. **Data sensitivity** — what kind of data does the system handle?

Before assigning remediation targets, confirm the vulnerability actually applies to your environment.

### Remediation Timelines

Once a vulnerability is confirmed and prioritized, here are the targets:

| Severity | Remediation target |
|----------|-------------------|
| **Critical** | 15 days |
| **High** | 30 days |
| **Medium** | 60 days |
| **Low** | Best effort |

> **Important:** These timelines **tighten during active exploitation**. If a Critical vulnerability is being actively exploited in the wild, 15 days may not be fast enough. Exceptions to timelines require **CISO approval**.

### Staged Deployment

Patches don't go straight to everyone at once:

- **Endpoint patches:** MDM alpha group → beta group → company-wide rollout
- **SaaS config changes:** Validated in test/staging tenants first
- **Patch waves** are treated as **Standard changes** (pre-approved, automated)

This staged approach catches problems before they affect the whole organization.

> **Example:** A new macOS security update is released. Kandji pushes it to the alpha group first — a small set of volunteer IT and engineering staff. They run it for a few days to catch compatibility issues. If nothing breaks, it goes to the beta group (a broader cross-section of teams). Only after beta validation does it roll out company-wide. If the alpha group hits a problem — say, the update breaks a VPN client — the rollout pauses before it affects anyone else.

### Anti-Malware

Malware protection is part of the vulnerability management program:

- Maintain **current signatures** on all endpoints
- Run **periodic system scans** on a schedule
- Enable **real-time scans** for files downloaded from external sources

### Verification

Patching isn't done until it's verified:

1. **Re-scan** the system or perform **functional validation**
2. **Attach evidence** to the remediation ticket
3. Reports and tickets are **Controlled Records** — retain them for audit

### Module C Quiz

A vulnerability scan identifies a Critical severity flaw in a production system. What is the remediation target?

- [( )] Best effort during the next scheduled update
- [( )] 60 days
- [(X)] 15 days
- [( )] 30 days
***

**Right!** Critical vulnerabilities must be remediated within 15 days. And if the vulnerability is being actively exploited, the timeline may be even shorter. High is 30 days, Medium is 60 days, and Low is best effort. Any exceptions require CISO approval.

***

## Module D — Endpoint Posture and Privileged Access

Your endpoint is a high-value target for attackers. Privileged accounts are even more valuable. This module covers how to manage both responsibly.

### Privileged Account Separation

If you need admin-level access, you must use **separate accounts**:

- **Standard account** for your daily work (email, Slack, docs)
- **Admin account** for elevated tasks (system administration, infrastructure changes)

Before requesting elevated access, apply the **six-question privilege test** — basically, ask yourself: "Do I truly need this level of access, and is there a less-privileged way to accomplish the task?"

> **Example:** You use your standard @civicactions.com account for Slack, email, and Google Docs all day. When you need to make changes in the Google Workspace Admin Console or push a Kandji configuration profile, you switch to your separate admin account. If your everyday account gets phished, the attacker can read your email — but they can't touch admin settings.

### NPI (Non-Person Identity) Management

Service accounts and API keys are "non-person identities" (NPIs). They need care too:

- Use **descriptive naming** so it's clear what the account does
- Every NPI must have a **linked human owner**
- Rotate credentials **quarterly** — or **immediately** if there's any sign of exposure

> **Example:** Your team has a GitLab deploy token that CI/CD pipelines use to push container images. That token has a named human owner (the team's SRE lead), a descriptive name like `gitlab-deploy-projectx-prod`, and a quarterly rotation schedule in Jira. If the token appears in a log file by mistake, it gets rotated immediately — don't wait for the quarterly date.

### Break-Glass Procedures

Sometimes you need emergency access to a system when normal channels fail. That's what **break-glass procedures** are for:

- Emergency credentials are **sealed** (not available for daily use)
- Access requires **dual control** (two people)
- After use: **mandatory audit** of what was done, followed by **credential rotation**

Break-glass is for genuine emergencies — not for skipping the normal process.

> **Example:** It's 2 AM and the Google Workspace admin account is locked out during an active incident. Two members of the SIRT use the sealed break-glass credentials together (dual control) to regain access. After the incident, they audit everything that was done with those credentials and rotate them immediately. The break-glass use is documented in the incident timeline.

### MDM Posture Evidence

CivicActions MDM generates records that prove device security:

- **Remote wipe records** — evidence that lost/stolen devices were wiped
- **Compliance reports** — proof that devices meet minimum security standards
- **ITAD certificates** — documentation of proper device disposal
- **Cryptographic erasure** — FileVault/LUKS key destruction via MDM to securely sanitize devices

These records are important for audits and for demonstrating that CivicActions takes endpoint security seriously.

### Module D Quiz

Why must admin accounts be separate from your daily-use account?

- [( )] It's optional — a single account is fine if you use a strong password
- [( )] Admin accounts get more storage space
- [(X)] Separating accounts limits the damage if your daily-use account is compromised — an attacker wouldn't automatically get admin privileges
- [( )] CivicActions licenses require two accounts per person
***

**Correct!** Account separation is a core principle of least privilege. If your everyday account gets phished or otherwise compromised, the attacker only gets regular access — not admin control over critical systems. Keeping admin work on a separate account significantly limits the blast radius of an incident.

***

## Module E — Disaster Recovery Operations

When critical systems go down, we need a plan. This module covers how CivicActions classifies outages, recovers systems, and learns from incidents.

### Incident Classification

Outages are classified by severity so we know how urgently to respond:

| Level | What it means | Example |
|-------|--------------|---------|
| **Low** | Minor issue, workaround available | A single SaaS feature is degraded but alternatives exist |
| **Medium** | Service unavailable, business impact | A key tool is down and work is disrupted |
| **High** | Multiple critical systems affected | Several production services are offline simultaneously |
| **Critical** | Prolonged outage, external impact | Extended downtime affecting clients or partner deliverables |

### System-Specific Recovery

CivicActions has documented recovery procedures for each critical system. You should know the **primary and fallback communication channels** and the **organizational actions** for the systems you manage, including:

- Google Workspace, Slack, Zoom
- Kandji/Iru (MDM)
- Atlassian (Jira/Confluence)
- Unanet, GitHub, GitLab
- Rippling, Culture Amp

> **Google Workspace is the highest-priority recovery** because it's the SSO/identity provider. All other services depend on it for authentication. If Google is down, virtually everything else is affected.

> **Example:** Slack goes down during a workday. The team shifts chat to Google Chat and video to Zoom — the documented fallback channels. If *Google Workspace* goes down, it's a different story: you can't authenticate to most other services. That's why Google is always recovered first. In that scenario, the primary communication fallback is Slack (chat) and Zoom (video), since they have independent authentication.

### Backup Ownership

For SaaS-based infrastructure:

- **Primary backups are managed by the SaaS providers** — that's part of what we're paying for
- **Admin access** to backup and export features must be limited and documented
- Where available, use the platform's **export or backup features** for additional protection

### Testing and Maintenance

A disaster recovery plan that's never tested is just a wish:

- The **DRP is reviewed annually**
- **Vendor DR assurances** are reviewed annually to confirm providers meet their commitments
- **Tabletop exercises** are conducted as appropriate — these are walk-throughs of "what if" scenarios

> **Example:** During an annual tabletop exercise, the team walks through: "It's Monday morning and GitHub is completely down. What do you do?" Answer: developers use their local Git clones to keep working, the Service Desk monitors GitHub's status page, and if the outage extends, the team communicates workarounds via Slack. The exercise reveals that two teams forgot they had CI/CD pipelines dependent on GitHub Actions — that gets added to the recovery runbook.

### Post-Incident Review

After a major outage is resolved:

1. Document the **timeline and impact**
2. Review the **effectiveness of the response** — what worked, what didn't
3. Track **improvement actions** and make sure they get done

This feeds directly back into the DRP to make it better for next time.

### Module E Quiz

Google Workspace experiences a prolonged outage. Why is it classified as the highest-priority recovery?

- [( )] It has the most storage
- [(X)] It is the SSO/identity provider — all other services depend on it for authentication
- [( )] Email is the most-used feature
- [( )] It's the cheapest to restore
***

**Correct!** Google Workspace is the identity backbone of CivicActions — it's the SSO provider. When Google is down, you can't authenticate to most other services either. That cascading effect is why it's always the top recovery priority.

***

## Bonus Quiz

You've completed all five modules — great work! Here's a final question covering a key concept from the course.

During a change freeze, a developer wants to deploy a new feature that's been fully tested and reviewed. Should this be allowed?

- [( )] Yes — it passed all tests, so it's safe to deploy
- [( )] Yes — but only if the developer's manager approves
- [(X)] No — during a change freeze, only stability-improving fixes are permitted; new features must wait
- [( )] Yes — change freezes only apply to infrastructure, not application code
***

**Correct!** Change freezes exist to protect stability during critical periods. Even fully tested new features must wait until the freeze is lifted. Only **stability-improving fixes** (like patches for active bugs or security vulnerabilities) are permitted during a freeze. This discipline prevents the "just one more thing" problem that can destabilize systems at the worst possible time.

***

## Course Complete

Congratulations — you've finished **IT Operations: Change, Configuration & Patch Management**!

Here's what you covered:

1. **Configuration management** — CI classes, Git as the authoritative baseline, secure defaults, drift detection, audit evidence
2. **Change enablement** — four change classes (Standard/Normal/Significant/Emergency), change records, scheduling, post-implementation review, change freezes
3. **Vulnerability and patch management** — discovery methods, prioritization, remediation timelines (Critical 15d / High 30d / Medium 60d), staged deployment, verification
4. **Endpoint posture and privileged access** — account separation, NPI management, break-glass procedures, MDM posture evidence
5. **Disaster recovery operations** — incident classification, system-specific recovery, backup ownership, testing, post-incident review

**Remember the essentials:**

- Git is the authoritative baseline — if it's not in Git, it's not official
- Classify changes properly — the bigger the blast radius, the more review required
- Patch Critical vulnerabilities within 15 days — faster if actively exploited
- Keep admin accounts separate from daily-use accounts
- Google Workspace is the #1 recovery priority because it's the identity provider

Questions? Reach out to **security@civicactions.com** or your IT lead.
