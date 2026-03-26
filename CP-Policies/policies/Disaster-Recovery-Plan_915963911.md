# Policies : Disaster Recovery Plan

Created by Sammy De La O , last modified by Fen Labalme on Feb 06, 2026

[https://civicactions.atlassian.net/browse/CPDOC-51?atlOrigin=eyJpIjoiNWI5NWY3MDhhNDA2NGUxZGI4NWI3MTIyYTI5MzMzMmMiLCJwIjoiaiJ9](https://civicactions.atlassian.net/browse/CPDOC-51?atlOrigin=eyJpIjoiNWI5NWY3MDhhNDA2NGUxZGI4NWI3MTIyYTI5MzMzMmMiLCJwIjoiaiJ9)

# Purpose

The purpose of this disaster recovery plan (DRP) is to define how CivicActions prepares for, responds to, and recovers from disruptive incidents affecting critical cloud-based systems. CivicActions is a remote-first organization with no on-premise infrastructure. Therefore, this plan relies on the disaster recovery, resilience, and business continuity capabilities of third-party cloud service providers, combined with internal coordination, communication, and deciosn-making processes.

The objective of this plan is to:

- minimize disruption to operations
- Protect the availability and integrity of organizational data
- Ensure timely communication with employees, leadership, and customers
- Support continual improvement and compliance with contractual and regulatory standards

# Scope

This plan applies to all critical cloud-based systems used by CivicActions to support business operations, including:

- Google Workspace
- Unanet
- Slack
- Zoom
- Kandji (Iru)
- Confluence
- Jira
- Rippling
- Culture Amp
- GitHub
- Organization-managed GitLab hosted on Google Cloud

This plan does not cover on-premise infrastructure, or client systems.

# Roles and Responsibilities

- CEO and CTO (Approvers): Approve this plan, defines list of critical systems and incident classification
- CISO (Plan Owner): Disaster Recovery Coordinator; Maintains this plan, and tracks metrics and audits
- System Owners: Subject matter expert and stakeholder of critical systems
- Team Members: Authorized users of critical systems
- Document Controller: Controls this Controlled Document per the Policy on Policies and Document and Records Control

# Definitions

- Availability - The ability of systems and services to be accessible and usable upon demand by authorized users
- Business Continuity (BC) - The capability of the organization to continue delivery of services at acceptable predefined levels following a disruption
- Business Impact Analysis (BIA) - A process used to determine the criticality of systems and the impact of disruptions over time
- Cloud Service Provider (CSP) - A third-party organization that delivers cloud-based services, including infrastructure, platforms, or software
- Contingency Planning - The process of developing plans to respond to and recover from system disruptions
- Disaster Recovery (DR) - The set of activities and procedures used to restore system availability and services following a disruption
- Disaster Recovery Plan (DRP) - A documented plan that defines roles, responsibilities, and actions to recover systems and services after an incident
- Incident - An occurrence that actually or potentially jeopardizes the confidentiality, integrity, or availability of an information system
- Recovery Point Objective (RPO) - The maximum acceptable amount of data loss measured in time
- Recovery Time Objective (RTO) - The maximum acceptable length of time that a system or service can be unavailable after a disruption
- Resilience - The ability of systems to withstand, adapt to, and recover from disruptions
- System Reconstitution - The restoration of systems to a secure, operational state following a disruption

# References

- FAR Clause 52.204-21: (b)(6) - Identify, report, and correct information and information system flaws.
- NIST SP 800-171 Rev. 3: 03.01 (Access Control), 03.07 (Incident Response), 03.08 (System and Information Integrity), 03.11 (Risk Assessment).
- CMMC Assessment Guide L2 v2.13: MP.L2-3.8.3 (Media sanitization), SC.L2-3.13.11 (Cryptographic Protection).
- ISO/IEC 27002:2022: 5.12 (Classification of information), 5.34 (Privacy and protection of PII), 8.12 (Data leakage prevention), 8.24 (Use of cryptography).
- Internal: Data Security and Handling Policy.

# Plan

## Incident Classification

| **Severity**   | **Description**                        | **Example**                     |
|----------------|----------------------------------------|---------------------------------|
| Low            | Minor disruption, workaround available | Brief service outage            |
| Medium         | Service unavailable, business impact   | Slack or Jira outage            |
| High           | Multiple critical systems unavailable  | Google Workspace outage         |
| Critical       | Prolonged outage with external impact  | Extended identity/email failure |

## Recovery Strategy

**General Strategy:**

- Rely on provider redundancy, geographic distribution, and automated failover
- Maintain documented understanding of each provider's DR commitments
- Use internal communication plans to manage workforce response
- Restore access and functionality rather than infrastructure

**Identity and Access Priority:**

Google Workspace is considered a critical dependency because it supports:

- Authentication (SSO)
- Email and internal communication
- File storage

## System Specific Recovery

| **System**                            | **Provider DR**                                                                           | **Organization Actions**                                                                                                                                                                                                                                                                                                                                                                                                                              |
|---------------------------------------|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Google Workspace                      | Multi-region redundancy and automated failover                                            | - Monitor Google Workspace Status Dashboard - Communicate outage status to staff - Use alternative communication channels if email is unavailable                                                                                                                                                                                                                                                                                                     |
| Slack                                 | Redundant infrastructure and data replication                                             | - Monitor Slack status page - Shift to email or Zoom chat if unavailable                                                                                                                                                                                                                                                                                                                                                                              |
| Zoom                                  | Globally distributed cloud infrastructure with regional redundancy and automated failover | - Monitor Zoom status page for outages or degradations - Shift meetings to alternate platforms (e.g., Google Meet) if Zoom is unavailable - Communicate guidance to staff on alternative meeting links and expectations - Reschedule critical external meetings if required                                                                                                                                                                           |
| Kandji (now part of Iru)              | Cloud-hosted MDM platform with vendor-managed redundancy and backups                      | - Monitor Kandji/Iru status communications for service disruptions - Prioritize restoration of device management and security enforcement capabilities - If MDM is unavailable, temporarily restrict enrollment of new devices and defer non-critical configuration changes - Coordinate with Kandji/Iru support for recovery timelines and validation of policy enforcement - Verify device compliance and security posture once service is restored |
| Atlassian Cloud - Confluence and Jira | High availability architecture with regional backups                                      | - Monitor Atlassian status page - Use documented procedures stored outside Atlassian if needed                                                                                                                                                                                                                                                                                                                                                        |
| Unanet                                | Vendor-managed backups and recovery                                                       | - Coordinate with Unanet support - Communicate time tracking or billing workarounds                                                                                                                                                                                                                                                                                                                                                                   |
| GitHub                                | Distributed architecture and regular backups                                              | - Monitor GitHub status - Use local clones as temporary workaround if needed                                                                                                                                                                                                                                                                                                                                                                          |
| GitLab (Google Cloud-hosted)          | Google Cloud regional availability and snapshot-based backups                             | - Confirm backups and recovery procedures are documented - Coordinate restoration through Google Cloud if required                                                                                                                                                                                                                                                                                                                                    |
| Rippling, Culture Amp                 | SaaS-based redundancy and vendor-managed recovery                                         | - Monitor vendor status pages - Communicate HR-related delays if applicable                                                                                                                                                                                                                                                                                                                                                                           |

## Communication Plan

**Internal Communication:**

- Primary: Slack (Chat), Zoom (Video)
- Secondary: Google Chat (Chat, Video)
- Tertiary: Slack (Chat, Video), Zoom (Chat, Video)
    - Both services support chat and video, but we normally prefer Slack for chat and Zoom for video

**External Communication:**

- Clients or partners notified only if services or deliverables are impacted
- Communications coordinated by leadership

## Backup and Data Protection Considerations

- Primary data backups are managed by service providers
- Organization ensures:
    - Administrative access is limited and documented
    - Export or backup features are used where available and appropriate
    - Critical documentation is not dependent on a single platform

## Testing and Maintenance

- DRP reviewed at least annually
- Vendor DR assurances reviewed annually
- Tabletop exercises conducted as appropriate
- Lessons learned incorporated into updates

## Post-Incident Review

- Following a significant incident:
- Document timeline and impact
- Review effectiveness of response
- Identify improvement actions
- Track actions through the continual improvement process

# Compliance and Enforcement

Violations may result in remedial actions up to and including access revocation, disciplinary action, or contract remedies. Sanctions follow PeopleOps processes and applicable standards.

# Training

- Onboarding (30 days): IT admins and system owners receive training on DR plan.
- Annual refresher: Updates to plan, role-based changes, additional to the list of critical systems or organization actions.

# Review

This policy is reviewed annually by the CISO and the Document Controller. Ad-hoc reviews may take place upon major legal and/or technical changes. Changes, reviews, and approvals are recorded in Confluence and Jira, following the [Document and Records Control Policy](https://civicactions.atlassian.net/wiki/x/AYCQCw) .

# Exceptions

Exceptions for this policy are rare and time-boxed. Exceptions must include business justification, compensating controls, and risk assessment. Exceptions require approval by CISO (and CEO/CTO if residual risk is High). All exceptions are logged in the Risk Register (Jira), and reviewed at least quarterly.

Document generated by Confluence on Mar 18, 2026 09:50

[Atlassian](http://www.atlassian.com/)