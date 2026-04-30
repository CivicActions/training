# Policies : Information Security Policy

Created by Owen Barton , last modified by Fen Labalme on Mar 10, 2026

[https://civicactions.atlassian.net/browse/CPDOC-31](https://civicactions.atlassian.net/browse/CPDOC-31)

# Purpose

This policy establishes the overarching framework for CivicActions information security and cybersecurity program. The policy contains CivicActions leadership's commitment and authority to govern information security, align with statutory and contractual obligations, and coordinate our security program with our quality and service management systems.

This policy defines leadership intent, governance structure, security objectives, and core principles that guide the development, implementation, and enforcement of all supporting security policies, standards, and procedures. This policy ties together CivicActions technical, administrative, and physical safeguards to protect information assets while enabling a remote-first workforce to deliver services to government clients and the public.

This policy reflects CivicActions' values of Balance, Openness, and Care by taking a risk-based approach, working openly when information is classified as public, and prioritizing the protection of people and client trust.

# Scope

This policy applies to:

- All CivicActions team members, contractors, and third-party partners
- All CivicActions-managed or client-furnished information systems and cloud services
- All information CivicActions creates, stores, processes, or transmits, including Federal Contract Information (FCI), Controlled Unclassified Information (CUI), customer data, and CivicActions internal information

This policy also applies to partners where CivicActions data or systems are involved. Client-owned systems and data hosted within those systems are generally governed by client policies; however, where a client system lacks an applicable information security policy, CivicActions will follow this policy as a baseline.

This policy is superseded where applicable by laws, regulations, contractual obligations, and client-specific security or compliance requirements. In the event of a conflict, the more stringent requirement shall apply.

This policy governs information regardless of format (electronic, paper, or verbal) and applies throughout the information lifecycle.

# Roles and Responsibilities

- CEO &amp; CTO (Approvers): Provides leadership and resources; approves this policy and any material revisions; sets tone for security culture organization-wide.
- CISO (Policy Owner): Owns the ISMS ; maintains this policy; coordinates risk management, metrics, and continuous improvement; ensures alignment with NIST CSF 2.0 and contract obligations.
- CTO: Ensures secure technical architecture and DevSecOps practices; enforces secure baselines on managed devices and cloud platforms; sponsors automation of security controls.
- Document Controller (Compliance): Controls this Controlled Document in Confluence (versioning, approval records, change history, accessibility).
- Compliance &amp; Internal Audit: Maps requirements (FAR, CMMC/NIST, ISO), plans and conducts internal audits, tracks nonconformities and corrective actions ( POA&amp;Ms ).
- People Operations (HR): Ensures onboarding/offboarding steps enforce identity proofing, training, and acknowledgments.
- Managers &amp; System Owners: Ensure team compliance, implement controls relevant to their systems, maintain asset and data inventories, and accept or manage residual risks.
- Team Members: Complete required training/acknowledgments; handle data per classification; use only approved, managed devices and services; promptly report suspected incidents.
- Partners: Comply with partner specific policies and procedures, based on specific engagement scope.

# Definitions

- FCI: Non-public information provided by or for the U.S. Government under contract, requiring safeguarding per FAR 52.204-21.
- CUI: Government information that is not classified but requires safeguarding and dissemination controls per federal rules (see CivicActions CUI Policy).
- ISMS: Information Security Management System-policies, processes, and controls to manage information risks (as defined by ISO 27000/27001).
- National Institute of Science and Technology (NIST) Cyber Security Framework (CSF) 2.0 Functions: Govern, Identify, Protect, Detect, Respond, Recover-high-level outcomes for risk management.
- CMMC: Cybersecurity Maturity Model Certification
- ISO: International Standards Organization
- FAR: Federal Acquisition Regulations
- POA&amp;Ms: Plan of Actions and Milestones
- ITIL: Information Technology Infrastructure Library
- PII/PHI: Personally Identifiable Information / Personal Health Information

# References

- FAR Clause [52.204-21](https://www.acquisition.gov/far/52.204-21) : Basic Safeguarding of Covered Contractor Information Systems.
- [ISO/IEC 27001:2022](https://www.iso.org/standard/75652.html) : 4 (Context of the organization), 5 (Leadership), 6 (Planning), 7.4 (Communication).
- [ISO 9001:2015](https://www.iso.org/standard/62085.html) : 5 (Leadership), 6.2 (Quality objectives).
- NIST SP 800-171 Rev. 3: [03.15.01](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/800-171r3/NIST.SP.800-171r3.html#d30e5116-Head3) (Policy and Procedures).
- [NIST SP 800-37 R2](https://csrc.nist.gov/pubs/sp/800/37/r2/final) : Risk Management Framework (RMF).
- [NIST Cybersecurity Framework 2.0](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf) : Core Functions (Govern, Identify, Protect, Detect, Respond, Recover).
- [ITIL 4](https://www.peoplecert.org/Frameworks-Professionals/ITIL-framework) : Guiding Principles (Focus on Value, Think and work holistically).

# Policy

## Governance and Leadership Commitment

This policy is approved by the CEO and owned by the CISO. It establishes the authority for all subordinate security policies, standards, and procedures and mandates compliance by all CivicActions team members and partners handling CivicActions or client data.

CivicActions leadership is committed to maintaining an effective information security policy and cybersecurity program that aligns with CivicActions mission, values, and contractual obligations.

CivicActions will operate an ISMS guided by ISO 27001 principles and use NIST CSF 2.0 as the organizing model to Govern, Identify, Protect, Detect, Respond, and Recover from cyber risks.

Security expectations, policy changes, and program priorities will be communicated to all team members using multiple channels (e.g., Slack #announcements, All-Humans Call) and embedded in trainings.

## Security Objectives

CivicActions sets the following measurable, organization-wide objectives. Sub-program metrics and targets are defined in supporting plans:

- Safeguard Federal Contract Information (FCI) and Controlled Unclassified Information (CUI) to the requirements of FAR 52.204-21 and (as applicable) NIST SP 800-171/CMMC.
- Protect team-member PII/PHI and sensitive company information consistent with legal and contractual obligations.
- Maintain the integrity and availability of company and client systems using SRE-informed reliability practices (e.g., error budgets, incident learning).
- Enforce least privilege and need-to-know for access to sites, services, and data.
- Continuously improve the ISMS using an auditable, ITIL-aligned continual improvement approach.

## Core Security Principles

CivicActions implements security in ways that respect our values of **Openness, Balance, and Care** :

- Security by design &amp; default: We design and operate systems so that secure choices are the default and risks are considered from the outset; controls are standardized, documented, and continuously verified.
- Least privilege: We grant the minimum access necessary for the shortest duration needed to perform a task, align access to roles and duties, and promptly remove or reduce access when it's no longer required.
- Defense-in-depth &amp; monitoring: We apply layered preventive and detective controls across people, process, technology, and data; we collect and review logs and telemetry to detect anomalies and enable timely response.
- Data classification &amp; minimization: We classify information and handle it according to sensitivity; we collect, use, share, and retain only what is necessary, reduce copies and exposure, and protect data throughout its lifecycle.
- Openness with safeguards: We work and share openly-internally or publicly-whenever appropriate, while protecting confidential, regulated, or contractually restricted information through classification, access control, and review.
- Managed endpoints first: We use company-managed, configured, and monitored devices and identities as the default for accessing company or client data; any exceptions are rare, risk-assessed, time-bound, and subject to equivalent safeguards.
- Partner trust but verify: We assess and monitor vendors and services that touch our company or client data, require appropriate security and incident obligations by contract, and regularly review their performance and risk posture.

## Compliance Commitments

- Federal &amp; contractual. CivicActions will maintain basic safeguarding for FCI per FAR 52.204-21 and implement the CMMC Level 1 practices; we will align with NIST SP 800-171/CMMC Level 2 where feasible to reduce future friction.
- Standards alignment . We will continue alignment with ISO 9001 for leadership, communication, and continual improvement of policies; NIST SP 800-37 for risk management, adopt ISO 27001 concepts for ISMS governance; and use ITIL/ISO 20000 practices to integrate security into service delivery.
- Evidence and audibility. We will maintain artifacts needed to demonstrate compliance (e.g., training records, acknowledgments, asset inventories, risk registers, incident records) and support internal/external audits.

## Delegation to Subordinate Policies

This overarching policy delegates specifics to the following policies (separate Controlled Documents). Each policy states mandatory requirements without duplicating scope:

- [Acceptable Use Policy](https://civicactions.atlassian.net/wiki/x/AgAPLQ) - End-user rules for approved technology use
- [Access Control Policy](https://civicactions.atlassian.net/wiki/x/AgBnL) - Account lifecycle, role-based access, least privilege
- [Identification Policy](https://civicactions.atlassian.net/wiki/x/HABRKg) - Identify, MFA, account onboarding and off-boarding
- [Data Security and Handling Policy](https://civicactions.atlassian.net/wiki/x/HgBVKg) - Classification, encryption, retention, disposal (ties to CUI Policy ); additional policies:
    - [Controlled Unclassified Information (CUI) Policy](https://civicactions.atlassian.net/wiki/x/RoANJQ)
- [Incident Response Policy](https://civicactions.atlassian.net/wiki/x/BAAGLQ) - Roles, playbooks, notifications, post-incident learning.
- [Risk and Security Assessment Policy](https://civicactions.atlassian.net/wiki/x/EABVKg) - Risk identification, analysis, treatment.
- [Maintenance Policy](https://civicactions.atlassian.net/wiki/x/AwBmL) - Secure baselines, change enablement, vulnerability &amp; patch, CMDB/CMS; additional policies:
    - [Configuration Management Policy](https://civicactions.atlassian.net/wiki/x/AoDGLQ)
    - [Change Enablement Policy](https://civicactions.atlassian.net/wiki/x/AYDILQ)
    - [Vulnerability and Patch Management Policy](https://civicactions.atlassian.net/wiki/x/AQDMLQ)
- [Physical Security Policy](https://civicactions.atlassian.net/wiki/x/AQBrL) - Remote/home office and travel considerations
- [Disaster Recovery Plan](Disaster-Recovery-Plan_915963911.html) - Managing disruptive incidents affecting critical cloud-based systems

## Risk Management

CivicActions identifies, analyzes, treats, and monitors information risks using a process consistent with NIST SP 800-30 and NIST CSF 2.0 Govern outcomes; risk acceptance must be explicit, recorded, and by the appropriate authority, following the [Risk and Security Assessment Policy](https://civicactions.atlassian.net/wiki/x/EABVKg) . Risk decisions consider mission, stakeholder expectations, and legal/contractual requirements.

## Assets, Endpoints, and Remote-First Security

- Company-managed devices are required for CivicActions work. Personal devices are not permitted for Confidential information. Limited, pre-approved mobile exceptions may be allowed subject to MDM and control equivalency.
- Endpoints must meet baseline controls (e.g., full-disk encryption, automated patching, anti-malware, host firewall, auto-lock); changes to security configuration require authorization.
- Remote access shall use secure encrypted connections and follow Zero-Trust principles (identity + device posture + context).

## Secure Engineering, DevOps, and SRE

- DevSecOps. Shift-left: security controls are integrated into CI/CD pipelines, with pre-approved libraries for authn/crypto and automated baseline enforcement.
- Reliability + Security. We design for least privilege, zero trust, rapid, automated change, and robust rollback to support both security and availability objectives. Incident response and post-incident learning are integral to improving reliability and security together.

## Monitoring, Detection, and Incident Response

- Services and platforms must emit logs and events necessary for security and reliability operations; significant events are triaged and escalated per practice guidance.
- All team members must immediately report suspected incidents following the [Incident Response Policy](https://civicactions.atlassian.net/wiki/x/BAAGLQ) . The policy and the Response Plan governs triage, containment, eradication, recovery, communications, and lessons learned.

## Data Governance, Openness, and Classification

- Data must be classified before it is stored, shared, published, or processed outside CivicActions. Public release (e.g., open source) is permitted only for data and code explicitly classified as Public and vetted for licensing and secrets. Data classification, handling, and storage follows the [Data Security and Handling Policy](https://civicactions.atlassian.net/wiki/x/HgBVKg) .
- Any controlled unclassified information (CUI) or federal contract information (FCI) must be handled following the [Controlled Unclassified Information Policy](https://civicactions.atlassian.net/wiki/x/RoANJQ) . CUI and FCI must remain within approved security boundaries (e.g., designated Google Workspace locations, managed endpoints, client systems) and follow the CUI policy and contract rules.

## Supplier and Third-Party Management

- Partners, including vendors and subcontractors with access to CivicActions or client data/systems must meet our baseline safeguards, accept contractual security obligations (including incident reporting), and support our assessments. These must follow the [Third-Party Management Policy](https://civicactions.atlassian.net/wiki/x/DoBtL) .

# Compliance and Enforcement

Violations may result in remedial actions up to and including access revocation, disciplinary action, or contract remedies. Sanctions follow PeopleOps processes and applicable standards.

# Training

- Onboarding (30 days): Users and managers receive training on role-specific policies, updates on any recent changes, or upon role changes.
- Annual refresher: Notification on changes to policies, and role-specific policy changes.

# Review

This policy is reviewed annually by the CISO and the Document Controller. Ad-hoc reviews may take place upon major legal and/or technical changes. Changes, reviews, and approvals are recorded in Confluence and Jira, following the [Document and Records Control Policy](https://civicactions.atlassian.net/wiki/x/AYCQCw) .

# Exceptions

Exceptions for this policy are rare and time-boxed. Exceptions must include business justification, compensating controls, and risk assessment. Exceptions require approval by CISO (and CEO/CTO if residual risk is High). All exceptions are logged in the Risk Register (Jira), and reviewed at least quarterly.

Document generated by Confluence on Mar 18, 2026 09:50

[Atlassian](http://www.atlassian.com/)