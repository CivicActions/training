# Policies : Incident Response Policy

Created by Owen Barton , last modified by Fen Labalme on Feb 18, 2026

[https://civicactions.atlassian.net/browse/CPDOC-48](https://civicactions.atlassian.net/browse/CPDOC-48)

# Purpose

The purpose of this policy is to define how CivicActions prepares for, detects, responds to, and learns from security incidents across company-managed systems and services. This policy establishes an incident response (IR) lifecycle that enables effective mitigation and continuous improvement.

## Scope

This policy applies to all CivicActions Team Members, contractors, and approved third parties who work with or have access to CivicActions-managed systems, client-furnished systems, or CivicActions data.

Incidents within CivicActions infrastructure includes all CivicActions-managed identities, endpoints, cloud platforms, SaaS, and data.

Client-furnished systems, procured through client projects, fall out of scope when it's required for CivicActions delivery teams to follow the client-owned Incident Response policy. Where there is no client policy, CivicActions delivery teams will follow this policy.

When regulatory, contract, client, and/or legal requirements impose policies or laws with stricter requirements than this policy, those take precedent for that engagement.

# Roles and Responsibilities

- **CEO and CTO (Approvers):** Approve this policy; accept High residual risk and material exceptions.
- **CISO (Policy Owner):** Owns the incident management program; maintains the IRP and this policy; ensures coordination with risk management and quality systems.
- **Incident Commander (per IRP):** Leads incident execution, decisions, and handoffs; ensures post-incident review and reporting.
- **Communications Officer (per IRP):** Manages internal and external communications and stakeholder updates.
- **System Owners / Data Owners:** Maintain accurate inventories, logging, and contacts; ensure playbooks and backups exist; support triage, containment, and recovery.
- **IT / Service Desk:** Operate managed endpoint baselines and remote actions; preserve logs and evidence during response; coordinate emergency changes with Maintenance.
- **Procurement / Vendor Managers:** Coordinate supplier notifications and evidence requests; enforce contract incident clauses per C-SCRM.
- **Compliance / Document Controller:** Control IR controlled documents and incident records per Document &amp; Records Control.
- **All Team Members:** Report suspected incidents immediately; follow instructions from the SIRT; preserve evidence.

# Definitions

- **Event:** An observable occurrence in a system or network.
- **Inciden t:** A confirmed adverse event that jeopardizes confidentiality, integrity, availability, or privacy, or a reasonable likelihood of such, requiring coordinated response.
- **IRP** : Incident response plan
- **Security Incident Response Team (SIRT):** The cross-functional group that performs incident response per the IRP.
- **Severity:** Tiering used to drive response and communications; our IRP defines High, Medium, and Low, with role-specific actions.

# References

- DFARS 252.204-7012: Safeguarding Covered Defense Information and Cyber Incident Reporting.
- NIST SP 800-171 Rev. 3: 03.10.02 (Incident Reporting), 03.10.03 (Incident Response Testing).
- CMMC Assessment Guide L2 v2.13: IR.L2-3.6.2 (Incident Testing), IR.L2-3.6.3 (Incident Reporting).
- NIST SP 800-61r3: Incident Response Recommendations and Considerations.
- ISO/IEC 27002:2022: 5.24-5.28 (Information security incident management controls).
- ISO 9001:2015: 10.2 (Nonconformity and corrective action).
- Internal: CivicActions Incident Response Plan (IRP), Controlled Unclassified Information (CUI) Policy.

# Policy

## Authority and Relationship to Procedures

- This policy authorizes and requires the use of the CivicActions [IRP](https://guidebook.civicactions.com/en/latest/common-practices-tools/security/incident-response-plan/) , [Incident Response Checklist](https://guidebook.civicactions.com/en/latest/common-practices-tools/security/incident-response-checklist/) , and [Contingency Plan](https://guidebook.civicactions.com/en/latest/common-practices-tools/security/contingency-plan/) as the authoritative procedures for incident handling, communications, and recovery. The policy governs principles and accountability; the IRP and Checklist define steps and roles during assessment, remediation, conclusion, and handoffs.
- The IRP's severity model and command roles apply to all security incidents; the Contingency Plan governs broader service disruptions and reconstitution.

## Report Quickly, Report Safely

- All Team Members must report suspected incidents immediately using the channels named in the IRP.
- Reporting in good faith is expected, will not result in retaliation, and any willful misconduct or repeated negligence will be handled by PeopleOps, and not by this policy.
- Do not investigate beyond basic facts unless part of the SIRT. Do not delete data, reimage systems, or disable logging without SIRT direction. Preserve potential evidence.

## Scope of incidents and declaration

- The Incident Commander may declare an incident based on the IRP criteria and assign a severity. Severity drives response time, communications, and leadership visibility.
- If there is a material confidentiality, integrity, or privacy risk, treat it as a security incident even when it coincides with an operational outage. Coordinate security and reliability response as one team to reduce harm.

## Execution Model

- Follow the IRP phases:
    1. Breath
    2. Document
    3. Initiate
    4. Assess
    5. Remediate
    6. Conclude
- Safety and containment first: prefer reversible, least-privilege, and blast-radius-limiting actions; escalate to emergency changes when needed per our maintenance process.
- When recovery activities exceed the thresholds in the Contingency Plan, activate continuity steps and reconstitution tasks.

## Communications and stakeholder updates

- All incident communications follow the IRP and are centralized through the Communications Officer.
- Use approved channels and templates; keep updates factual, time-stamped, and audience-appropriate.
- SIRT maintains an incident log and issues stakeholder updates at intervals appropriate to severity and contractual needs.

## Third-party and client notifications

- Supplier incidents that may affect CivicActions or client data must be escalated under this policy. Vendors must notify CivicActions promptly and cooperate per contract; High or Critical suppliers are required to meet accelerated timelines and provide evidence on request.
- Where contract or law requires external reporting, CivicActions will notify the client or authority within the required timeframes. For example, contracts involving CUI or DoD work may require time-bound reporting and FedRAMP-equivalent safeguards for cloud providers.
- Client-managed environments follow client notification rules; CivicActions cooperates and provides evidence and staff support as requested.

## Evidence, Logging, and Forensics

- Preserve logs, images, and relevant artifacts. Maintain chain of custody where possible; coordinate with the SIRT before acquiring, copying, or analyzing data.
- Network and system logging must support detection and reconstruction consistent with our security and network-security references.
- Incident records are Controlled Records and must be stored per the Document &amp; Records Control Policy.

## Recovery Objectives and Emergency Change

- Recovery targets are set by system criticality and the Contingency Plan. Extended unavailability beyond plan thresholds triggers continuity procedures and leadership escalation.
- Emergency changes used to restore service must be documented, reviewed after the fact, and integrated with problem management and maintenance practices.

## Post-Incident Learning and Risk Integration

- Every incident concludes with documented closure, a retrospective , and agreed corrective actions .
- Lessons learned will focus on system and process improvements. Any personnel-specific takeaways or follow-ups are handed off to PeopleOps and not handled by this policy and processes.
- Update the Risk Register and create POA&amp;Ms where needed. Track to closure, and fold lessons into standards, training, and tests.

## Confidentiality of Incident Information

- Incidents involving CUI or Restricted data must remain within approved boundaries and channels, following the CUI Policy and Data Security practices during analysis and communications.

- Incident information is shared on a need-to-know basis . Team Members must not disclose incident details outside designated channels without approval from the Communications Officer or Incident Commander.

# Compliance and Enforcement

Violations may result in remedial actions up to and including access revocation, disciplinary action, or contract remedies. Sanctions follow PeopleOps processes and applicable standards.

# Training

- Onboarding (30 days): all Team Members complete training on incident recognition and reporting, managed-device responsibilities, and their role during an incident.
- Annual refresher: updates on IRP changes, reporting routes, mock exercises, and role-specific drills for SIRT members.
    - Additional training, such as incident response test, table-top exercise, or other similar testing can be added, based on the risks and requirements of clients.

# Review

This policy is reviewed annually by the CISO and the Document Controller. Ad-hoc reviews may take place upon major legal and/or technical changes. Changes, reviews, and approvals are recorded in Confluence and Jira, following the [Document and Records Control Policy](https://civicactions.atlassian.net/wiki/x/AYCQCw) .

# Exceptions

Exceptions for this policy are rare and time-boxed. Exceptions must include business justification, compensating controls, and risk assessment. Exceptions require approval by CISO (and CEO/CTO if residual risk is High). All exceptions are logged in the Risk Register (Jira), and reviewed at least quarterly.

Document generated by Confluence on Mar 18, 2026 09:50

[Atlassian](http://www.atlassian.com/)