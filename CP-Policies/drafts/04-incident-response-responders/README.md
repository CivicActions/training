<!--
author:   CivicActions Security Team
email:    security@civicactions.com
version:  0.1.0
language: en
narrator: US English Female

comment:  Incident Response for Responders — training for IT,
          SIRT members, and managers on how to handle security
          incidents from detection through post-incident learning.

-->

# Incident Response for Responders

Welcome to **Incident Response for Responders** — the training for CivicActions team members who actively handle security incidents.

Training 1 taught all staff to *report* incidents. This course teaches you how to *respond* to them: the IRP phases, evidence preservation, communications protocol, recovery objectives, and post-incident improvement.

**Who takes this?** IT / Service Desk, SIRT (Security Incident Response Team) members, and Managers.

**Prerequisite:** Training 1 — Security Awareness Essentials.

**How long?** About 10–15 minutes.

**When?** Within 30 days of onboarding, then annually, and after any significant incident (lessons learned).

**Compliance:** CMMC L2 (IR.L2-3.6.1–3.6.3), ISO 27001 A.5.24–A.5.28.

---

Let's get started!

## Module A — IRP Structure and Phases

Before you can respond to an incident effectively, you need to understand the plan that guides you. This module covers the document structure, the six response phases, and the principles that shape every decision.

### Document Hierarchy

CivicActions' incident response documentation has three layers:

| Document | Purpose |
|----------|---------|
| [**Incident Response Policy**](https://civicactions.atlassian.net/wiki/spaces/MGPOL/pages/755367940/Incident+Response+Policy) | Defines principles, authority, and roles |
| [**Incident Response Plan (IRP)**](https://guidebook.civicactions.com/en/latest/common-practices-tools/security/incident-response-plan/) | The procedures followed when responding to security incidents |
| [**Incident Response Checklist**](https://guidebook.civicactions.com/en/latest/common-practices-tools/security/incident-response-checklist/) | Step-by-step procedures for responders |
| [**Contingency Plan**](https://guidebook.civicactions.com/en/latest/common-practices-tools/security/contingency-plan/) | Recovery targets and integration with Disaster Recovery |

During an active incident, the **Checklist** is your go-to reference. The IRP provides the authority behind what you're doing, and the Contingency Plan tells you how to prioritize recovery.

> **Example:** A SIRT member gets pulled into an active phishing investigation. They don't need to re-read the full IRP — they open the Incident Response Checklist, which walks them through each step: what to document, who to notify, how to contain. The IRP is why they have authority to act; the Checklist is *how* they act.

### Six Phases

CivicActions follows six incident response phases:

1. **Breath** — Pause. Assess the situation calmly before acting.
2. **Document** — Start recording what you see, when you see it, and what you do.
3. **Initiate** — Activate the response: notify the right people, assemble the team.
4. **Assess** — Determine scope, severity, and impact. What systems are affected? What data is at risk?
5. **Remediate** — Contain the threat, eradicate it, and begin recovery.
6. **Conclude** — Close the incident, conduct the retrospective, and capture lessons learned.

> **Safety and containment always come first.** Before you investigate, make sure the situation is contained. A fire investigator doesn't start looking for causes while the building is still burning.

### Incident Declaration

The **Incident Commander (IC)** is the person who:

- **Declares** that an incident is happening
- **Assigns severity** based on impact and scope
- **Coordinates** the response team

One important rule: if a security risk is discovered during an operational outage (like a routine system failure), it gets treated as a **security incident** — not just an ops issue.

> **Example:** During a routine Jira outage investigation, the Service Desk notices that an admin account was used to export project data right before the outage. That's no longer just an ops issue — the IC declares a security incident, assigns a severity, and spins up the SIRT. The ops recovery continues in parallel, but the security investigation gets its own track.

### Guiding Principles

When making decisions during an incident, follow these principles:

- **Reversible actions first** — prefer actions you can undo over ones you can't
- **Least privilege** — limit response access to what's needed
- **Limit the blast radius** — contain the problem to the smallest possible scope
- **Err on the side of containment** — when in doubt, contain first and investigate later

> **Example:** You suspect a compromised service account is being used to access a Google Shared Drive. The reversible action is to disable the service account immediately — you can always re-enable it if it turns out to be legitimate. The *irreversible* action would be deleting the account or wiping the Drive. Contain first, investigate second.

### Module A Quiz

You notice unusual login attempts on a system you manage. What should you do first?

- [( )] Investigate thoroughly and fix the issue yourself before telling anyone
- [(X)] Report the suspected incident immediately using IRP-designated channels
- [( )] Delete the suspicious logs to prevent further access
- [( )] Wait to see if it happens again before reporting
***

**Correct!** Speed matters in incident response. Report first, then help with the investigation. Trying to investigate alone wastes precious time, and deleting logs destroys the evidence the SIRT needs. The IRP is designed to coordinate the response across the team — so get the team involved immediately.

***

## Module B — Evidence and Forensics

Evidence is what turns "we think something happened" into "we know what happened." This module covers how to preserve it properly.

### Preservation

When an incident is in progress, evidence can disappear quickly. Here's how to protect it:

- **Preserve logs, images, and artifacts** — don't modify, delete, or overwrite them
- Maintain **chain of custody** — document who had access to evidence, when, and what they did with it
- **Do not reimage, wipe, or disable logging** on affected systems without SIRT direction

> **Example:** A developer notices that their CivicActions laptop is behaving strangely — unexpected network connections, high CPU usage. Their instinct is to wipe the machine and start fresh. But that would destroy the forensic evidence the SIRT needs. Instead, they report it to security@civicactions.com, keep the laptop powered on, and wait for SIRT guidance on next steps.

> **Think of it like a crime scene.** You wouldn't clean up the evidence before investigators arrive. The same principle applies to digital incidents.

### Coordination with SIRT

Before you take action on evidence, coordinate:

- Don't **acquire, copy, or analyze** data on your own without SIRT direction
- The SIRT may have specific procedures for how evidence should be collected
- Uncoordinated evidence collection can contaminate or destroy what the team needs

If you find something relevant, **report it and wait for guidance** — unless immediate containment is needed to prevent further harm.

### Controlled Records

All incident records are **Controlled Records**, which means they're subject to retention policy:

- Incident logs and timelines
- Decision records (who decided what, and when)
- Artifacts (screenshots, log exports, configuration snapshots)
- Communication records

Keep everything organized. Auditors and legal teams may need these records long after the incident is closed.

> **Example:** During a phishing incident, the SIRT collects: the original phishing email (screenshot + headers), the Slack thread where it was first reported, the timeline of containment actions, the IC's severity assignment and decision log, and screenshots of the compromised account's recent activity. All of it goes into the incident's Jira ticket as attachments — organized and timestamped. Six months later, an auditor asks for the records. They're all in one place.

### Module B Quiz

During an incident investigation, you find a log file on an affected server that may contain key evidence. What should you do?

- [( )] Copy it to your personal laptop for review
- [( )] Delete it so it doesn't fall into the wrong hands
- [(X)] Preserve it in place and coordinate with SIRT before acquiring, copying, or analyzing it
- [( )] Email it to the entire IT team for review
***

**Correct!** Evidence must be preserved with chain of custody intact. Don't copy it to personal devices, don't delete it, and don't distribute it broadly. Coordinate with SIRT — they'll tell you how to handle it properly. Uncoordinated actions can contaminate evidence or create legal complications.

***

## Module C — Communications and Escalation

During an incident, what you say — and who you say it to — matters enormously. This module covers the communications rules that keep everyone informed without making things worse.

### Communications Officer

All external and formal internal incident communications go through the **Communications Officer (CO)**:

- The CO uses **approved channels and templates**
- No one else sends incident communications to clients, partners, media, or formal internal audiences
- If you're asked about the incident by someone outside the response team, direct them to the CO

> **Example:** During an active incident involving a client project, a project manager from another team messages you on Slack: "Hey, I heard there's a security issue on Project X — is client data affected?" Even if you know the answer, the right response is: "The incident team is handling it — the Communications Officer will send an update when there's information to share." Need-to-know applies even inside CivicActions.

### Update Standards

When you do communicate about an incident (within the response team or as directed by the CO):

- Keep updates **factual and time-stamped**
- Make them **audience-appropriate** — technical details for the response team, plain language for leadership
- **No speculation or attribution** in early updates — stick to what you know, not what you think

> **Bad example:** "We think a hacker from Country X broke in through the VPN."
>
> **Good example:** "At 14:32 UTC, unusual login activity was detected on System X. Investigation is in progress."

### Client and Third-Party Notifications

Some incidents require notification to external parties:

- **Vendor incidents** that may affect CivicActions or client data must be escalated
- Contracts — especially those involving **CUI or DoD data** — may require **time-bound external reporting** (typically 72 hours, some as short as 24 hours)
- The CO and IC determine when and how external notifications happen

> **Example:** A SaaS vendor that CivicActions uses for a federal contract notifies you of a breach on their platform. The contract requires CivicActions to notify the government client within 72 hours. The IC and CO coordinate: the CO drafts the notification using the approved template, the IC reviews it for accuracy, and it goes out within the contractual window. For CUI-related contracts, that window could be as short as 24 hours.

### Need-to-Know

Incident details are shared on a **need-to-know basis**:

- Don't discuss incident details outside designated channels (the incident Slack thread, SIRT meetings, etc.)
- No disclosure without **IC or CO approval**
- This protects the investigation and prevents misinformation

### Module C Quiz

During an active incident, a journalist contacts you asking for details. What do you do?

- [( )] Provide basic facts to be transparent
- [(X)] Refer all media inquiries to the Communications Officer — do not disclose incident details without IC/CO approval
- [( )] Say "no comment" and hang up
- [( )] Direct them to the company website
***

**Correct!** All external communications during an incident go through the Communications Officer. Even well-meaning transparency can cause problems if the information is incomplete, inaccurate, or shared too early. The CO has the training and authority to handle media and external inquiries properly.

***

## Module D — Recovery and Emergency Changes

Once the threat is contained, the focus shifts to getting systems back to normal — safely. This module covers recovery priorities and the rules around emergency changes.

### Recovery Targets

Recovery is prioritized by **system criticality**, as defined in the Contingency Plan:

- **Google Workspace** is always the highest priority — it's the identity provider, and everything else depends on it
- Other systems are prioritized based on their impact on business operations and client deliverables

The Contingency Plan defines specific recovery time objectives for each critical system. Know the ones for the systems you manage.

> **Example:** Google Workspace goes down on a Tuesday morning. Since it's the SSO provider, nobody can authenticate to Slack, Jira, or most other tools. The recovery priority is clear: Google first. The team shifts communication to Zoom (which has independent auth) and monitors the Google Workspace Status Dashboard. Once Google is restored, other services come back online as authentication resumes.

### Emergency Changes

During an incident, you may need to make changes fast — too fast for the normal change process. That's where **emergency changes** come in:

1. The **Incident Commander authorizes** the change
2. **Document** what you're doing — during the incident if possible, immediately after if not
3. A **formal review** follows within **5 business days**

Emergency authorization isn't a blank check. Document everything, and expect the review.

> **Example:** During an active incident, the IC authorizes you to revoke all API tokens for a compromised GitLab service account. You make the change, note the time, the tokens revoked, and the IC's authorization in the incident Slack thread. Within five business days, the full change goes through a formal review — just like any other change, but after the fact.

### Service Restoration

Before you declare a system "back to normal":

- **Verify system integrity** — make sure the system is clean and functioning correctly
- **Confirm containment** — verify that the threat is truly eliminated before restoring access
- Don't rush to reopen access if there's any doubt

> **The worst thing you can do is restore access to a system that's still compromised.** Take the time to verify.

> **Example:** After containing a compromised Google Workspace account, the temptation is to immediately re-enable it so the user can get back to work. But first: verify that the attacker's access is truly revoked, that all session tokens are invalidated, that the password and MFA method are reset, and that no malicious forwarding rules or OAuth grants remain. Only then do you restore access.

### Module D Quiz

During an incident, you need to make an emergency configuration change to contain a threat. What's the proper process?

- [( )] Make the change and document it at the next scheduled team meeting
- [( )] Wait for Change Authority approval through the normal process
- [(X)] Get Incident Commander authorization, document the change during or immediately after, and complete a formal review within 5 business days
- [( )] Make the change without telling anyone to avoid slowing down the response
***

**Correct!** Emergency changes follow a streamlined but accountable process: IC authorization, real-time documentation (or as close to it as possible), and a formal review within 5 business days. Never skip documentation — it's critical for the post-incident review and for maintaining trust in the change process.

***

## Module E — Post-Incident Learning

The incident is over. Now comes one of the most valuable parts: learning from it. This module covers how CivicActions turns incidents into improvements.

### Retrospective

Within **5 business days** of closing an incident, the team conducts a **retrospective**:

- The format is **blameless** — the goal is to understand *what happened*, not *who's at fault*
- Document the **timeline**, **impact**, and **response effectiveness**
- Identify what worked well and what needs improvement

> **Blameless doesn't mean accountability-free.** It means we focus on systems, processes, and conditions rather than pointing fingers. People do their best with the information they have — so we fix the conditions that led to the problem.

> **Example:** A retrospective reveals that a responder disabled a firewall rule during containment, which accidentally exposed another system for 20 minutes. The blameless discussion focuses on: "Why didn't the runbook mention this dependency? How can we add a pre-check step so future responders catch it?" That leads to an updated Incident Response Checklist — a process fix, not a blame assignment.

### Risk Integration

Lessons learned don't just sit in a document — they feed back into the organization:

- Update the **Risk Register** with new risks identified during the incident
- Create **POA&Ms** (Plans of Action & Milestones) for trackable improvement items
- Route improvements through the **continual improvement process**

> **Example:** After a phishing incident, the retrospective identifies that the team had no automated way to check if other users received the same phishing email. The improvement action becomes a POA&M ticket in the Jira Continual Improvement project: "Implement email header search capability for SIRT," with a milestone, an owner, and a due date. The Risk Register gets updated to reflect the gap until the capability is in place.

### Personnel Matters

If an incident involves personnel issues (policy violations, negligence, etc.):

- Those matters are handled by **PeopleOps separately**
- Personnel actions are **not part of the IR process or retrospective**
- This separation protects the blameless culture of the retrospective while still allowing appropriate accountability

### Compliance and Enforcement

For serious or repeated violations:

- Consequences may include **access revocation**, **disciplinary action**, or **contract remedies**
- These are determined outside the retrospective process
- The goal is always to improve — but willful or repeated violations have real consequences

### Module E Quiz

You receive a notification that a SaaS service used by CivicActions has experienced a data breach. What is the correct first step?

- [( )] Immediately cancel the SaaS subscription
- [(X)] Report the vendor incident to security@civicactions.com so it can be escalated under the IR Policy
- [( )] Post about it in a public Slack channel so everyone is aware
- [( )] Wait for the vendor to contact CivicActions directly
***

**Correct!** Vendor incidents that may affect CivicActions or client data need to be escalated through the IR process. Report it to security@civicactions.com first. Don't cancel services unilaterally (that could disrupt operations), don't broadcast it publicly (need-to-know applies), and don't wait for the vendor to reach out — some contracts have tight notification deadlines.

***

## Bonus Quiz

You've completed all five modules — well done! Here's a final question on a key incident response concept.

An incident retrospective reveals that a responder made a decision during the incident that, in hindsight, made things worse. How should this be handled?

- [( )] Name the person publicly so everyone can learn from their mistake
- [( )] Skip it in the retrospective to avoid embarrassment
- [(X)] Discuss the decision in the blameless retrospective — focus on the conditions and information that led to it, and identify process improvements
- [( )] File a complaint with PeopleOps immediately
***

**Correct!** Blameless retrospectives focus on *conditions*, not individuals. The responder made the best decision they could with the information available at the time. The retrospective should explore *why* the decision seemed reasonable, *what information was missing*, and *how the process can be improved* so future responders have better tools and information. Personnel matters, if any, are handled separately by PeopleOps — never in the retrospective.

***

## Course Complete

Congratulations — you've finished **Incident Response for Responders**!

Here's what you covered:

1. **IRP structure and phases** — three-document hierarchy, six phases (Breath → Conclude), IC authority, guiding principles
2. **Evidence and forensics** — preserve with chain of custody, coordinate with SIRT, all records are Controlled Records
3. **Communications and escalation** — Communications Officer handles external comms, factual/time-stamped updates, need-to-know rules, time-bound client notifications
4. **Recovery and emergency changes** — IC-authorized emergency changes, document everything, verify integrity before restoring access
5. **Post-incident learning** — blameless retrospective within 5 days, lessons feed into Risk Register and POA&Ms, personnel matters handled separately

**Remember the essentials:**

- Report first, investigate as a team — don't go solo
- Preserve evidence — don't delete, reimage, or modify without SIRT direction
- All external communications go through the Communications Officer
- Verify system integrity before restoring access
- Retrospectives are blameless — focus on conditions, not individuals

Questions? Reach out to **security@civicactions.com** or your SIRT lead.
