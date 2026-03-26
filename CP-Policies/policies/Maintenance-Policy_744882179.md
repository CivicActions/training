# Policies : Maintenance Policy

Created by Owen Barton , last modified on Mar 04, 2026

[https://civicactions.atlassian.net/browse/CPDOC-40?atlOrigin=eyJpIjoiNWYyOWY0NDBmOWM5NDhiYThmNGEyYTZlYWMzZTNjZGQiLCJwIjoiaiJ9](https://civicactions.atlassian.net/browse/CPDOC-40?atlOrigin=eyJpIjoiNWYyOWY0NDBmOWM5NDhiYThmNGEyYTZlYWMzZTNjZGQiLCJwIjoiaiJ9)

# Purpose

The purpose of this policy is to establish a unified, automated, and auditable maintenance system that integrates configuration management, change enablement, and vulnerability and patch management. A unified maintenance program will help to keep CivicActions systems secure, reliable, and compliant while minimizing disruption.

# Scope

This policy applies to all CivicActions Team Members, contractors, and partners who build, operate, or support CivicActions systems. These systems include:

- All CivicActions-managed endpoints, cloud platforms, networks, software, and any client-furnished systems where CivicActions has maintenance duties
- Third-party and open-source software used in CivicActions services, and SaaS providers under shared-responsibility arrangements

# Roles and Responsibilities

- CTO (Approver): Approve this policy and high-risk exceptions
- CISO (Policy Owner): Maintains this policy and oversees metrics, audits, and regulatory alignment
- CTO / Head of IT: Operates the integrated maintenance program and sponsors automation and configuration as code
- Change Authority (delegated): Approves Normal and Emergency changes within remit and maintains the Standard change catalog
- System Owners / Product Owners: Maintain CI inventories and baselines, define maintenance windows, and accept residual risk within authority
- SRE/Engineering / DevOps: Build pipelines and guardrails, remediate vulnerabilities, manage SBOMs, and produce evidence
- Security Team: Runs vulnerability management, sets remediation targets, validates host protection posture
- Service Desk / IT Operations: Runs MDM/EDR, patch orchestration, allow/deny lists, and user communications
- Procurement / Vendor Managers: Flow down maintenance obligations to suppliers and monitor provider posture
- Document Controller (Compliance): Controls this Controlled Document and related records in Confluence and Jira per Document and Record Control Policy

# Definitions

- Configuration Item (CI): Any component managed to deliver a service and recorded in the configuration management system
- Configuration Management Database (CMDB) / Configuration Management System (CMS): The system of record for CIs and their relationships (for CivicActions, a combination of version control for configuration-as-code and Jira/Confluence for service asset records)
- Baseline: The approved, secure configuration for a CI, defined as code where feasible

# References

- FAR Clause 52.204-21: b.1.viii (Limit physical access during maintenance), b.1.xii (Timely flaw correction), b.1.xiii (Malicious code protection)
- NIST SP 800-171 Rev. 3: 03.04 (Configuration Management), 03.07 (Maintenance), 03.14.01 (Flaw Remediation)
- CMMC Assessment Guide L2 v2.13: CM.L2-3.4.1 (System Baselining), MA.L2-3.7.1 (Controlled Maintenance), SI.L2-3.14.1 (Flaw Remediation)
- ISO/IEC 27002:2022: 7.13 (Equipment maintenance), 8.8 (Management of technical vulnerabilities), 8.9 (Configuration management), 8.32 (Change management)
- ITIL 4: Change Enablement, Service Configuration Management, Monitoring and Event Management practices

# Policy

## Governance and Integrated Model

- CivicActions maintains one integrated maintenance program composed of configuration management, change enablement, and vulnerability/patch management. This is implemented through automation and continuous verification where feasible. "Guardrails, not gates" apply: pre-approved Standard changes and CI/CD guardrails satisfy control intent; manual approvals are used only when risk warrants.
- Major changes on critical services require a documented plan and approval by a delegated Change Authority. Routine patching of supported systems runs as Standard changes on a published schedule. SaaS and cloud services follow the shared-responsibility model, with vendor notices and material changes recorded and assessed for impact.

## Configuration Management

- Maintain complete, accurate CI inventories and relationships. Baselines are defined as configuration code where practical. Configuration drift is detected, ticketed, and resolved or put through change workflow. Evidence includes baselines, change histories, and drift reports managed as Controlled Records.
- The guidelines for baseline configurations and maintenance can be found in the [Configuration Management Policy](https://civicactions.atlassian.net/browse/CPDOC-40?atlOrigin=eyJpIjoiNWYyOWY0NDBmOWM5NDhiYThmNGEyYTZlYWMzZTNjZGQiLCJwIjoiaiJ9) .

## Change Enablement

- All production modifications follow a documented lifecycle aligned to risk: Standard, Normal, Significant, and Emergency. Peer review, automated tests and scans, and progressive rollouts act as approvals for low-risk code changes; high-risk changes require delegated approval with rollback plans. Maintenance windows and a change calendar minimize disruption. Post-implementation reviews are required for Normal and Emergency changes.
- The guidelines for the change enablement and management process are captured in the [Change Enablement Policy](https://civicactions.atlassian.net/wiki/x/AYDILQ) .

## Vulnerability and Patch Management

- Vulnerabilities are discovered on a defined cadence and after material change, prioritized by severity and business criticality, remediated within targets, and verified by re-scan. Anti-malware protections are maintained and updated with both periodic and real-time scanning where applicable. Evidence consists of scan reports, tickets, and verification records.
- The process for monitoring vulnerabilities and patch management are found in the [Vulnerability and Patch Management Policy](https://civicactions.atlassian.net/wiki/x/AQDMLQ) .

## Endpoints and Mobile Devices

- Company-managed laptops are required for access to Internal, Confidential, or client data. Baselines include full-disk encryption, EDR, host firewall, auto-lock, and automated patching.
- Limited BYOD mobile use is permitted for MFA and communications with MDM profile isolation; non-compliant devices are automatically blocked until remediated.

## Software Management and Prohibited Technology

- CivicActions maintains an Approved Software Catalog and a [Prohibited Hardware and Software list](https://guidebook.civicactions.com/en/latest/company-policies/prohibited-hardware-and-software/) . MDM blocks installation of unapproved or prohibited software where feasible, and violations are enforced. Requests for new software follow the access and authorization workflow and include security review.

## Scheduling, Communication, and Freezes

- Maintenance work is planned and tracked in Jira. Routine manual tasks are scheduled via automation; automated tasks have runbooks and change records. Windows are published per service. Emergency changes follow Incident Response communications and retrospective requirements. Change freezes may be instituted when error budgets are exceeded or during critical delivery periods.

## Evidence, Monitoring, and Metrics

- Controlled Records include change tickets, approvals, pipeline and scan results, CMDB entries, standard change catalogs, maintenance calendars, and metrics. Monitoring and event management routes vulnerability, drift, anti-malware, and deployment signals for triage and escalation. Program metrics are reviewed quarterly and include patch-SLA compliance, mean time to remediate, drift rate, emergency change volume and success, MDM violations, and SBOM coverage.

# Compliance and Enforcement

Violations may result in remedial actions up to and including access revocation, disciplinary action, or contract remedies. Sanctions follow PeopleOps processes and applicable standards.

# Training

- Onboarding (30 days): IT training on maintenance, configuration management, change enablement, vulnerability monitoring, and patch management.
- Annual refresher: Policy changes, including changes to the tools and systems to manage configurations. Include lessons learned from change controls and vulnerability incidents.

# Review

This policy is reviewed annually by the CISO and the Document Controller. Ad-hoc reviews may take place upon major legal and/or technical changes. Changes, reviews, and approvals are recorded in Confluence and Jira, following the [Document and Records Control Policy](https://civicactions.atlassian.net/wiki/x/AYCQCw) .

# Exceptions

Exceptions for this policy are rare and time-boxed. Exceptions must include business justification, compensating controls, and risk assessment. Exceptions require approval by CISO (and CEO/CTO if residual risk is High). All exceptions are logged in the Risk Register (Jira), and reviewed at least quarterly.

Document generated by Confluence on Mar 18, 2026 09:50

[Atlassian](http://www.atlassian.com/)