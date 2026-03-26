# Policies : Configuration Management Policy

Created by Owen Barton , last modified on Mar 04, 2026

[https://civicactions.atlassian.net/browse/CPDOC-44](https://civicactions.atlassian.net/browse/CPDOC-44)

# Purpose

The purpose of this policy is to define how CivicActions identifies, baselines, tracks, and verifies the configuration of all managed components to support reliable operations, effective change, incident response, access control, and audit.

# Scope

This policy applies to all CivicActions Team Members, contractors, and partners who build, operate, or support CivicActions systems. These systems include:

- All managed components required to deliver CivicActions services, including infrastructure, platforms, applications, endpoints, cloud resources, integrations, datasets, and documentation
- All CIA "High" systems and any infrastructure they depend on
- Managed endpoints and their approved software, secure baselines, and locked configurations

# Roles and Responsibilities

- CTO (Approver): Approve this policy and high-risk exceptions
- CISO (Policy Owner): Maintains this policy and oversees metrics, audits, and regulatory alignment
- CTO / Head of IT: Operates the integrated maintenance program and sponsors automation and configuration as code
- System Owners: Maintain configuration item records, relationships, and baselines; reconcile inventory drift
- IT: Implement configuration as code, peer reviews, pipelines, and drift detection
- Document Controller (Compliance): Controls this Controlled Document and related records in Confluence and Jira per Document and Record Control Policy

# Definitions

- Configuration item: A configuration item is a managed component that delivers a service
- Baseline: The approved secure configuration for a configuration item
- Configuration Management Database (CMDB): System of record for configuration items and their relationships (Git for configuration-as-code and Jira/Confluence for service asset records)

# References

- FAR Clause 52.204-21: b.1.ii (Limit functions/transactions), b.1.xii (Flaw correction/Integrity).
- ISO 9001:2015: 7.5 (Documented information), 8.5.2 (Identification and traceability).
- NIST SP 800-171 Rev. 3: 03.04.01 (Baseline Configuration), 03.04.02 (Configuration Settings), 03.04.06 (Least Functionality).
- CMMC Assessment Guide L2 v2.13: CM.L2-3.4.1 (System Baselining), CM.L2-3.4.3 (Configuration Change Control), CM.L2-3.4.6 (Least Functionality).
- ISO/IEC 27002:2022: 5.9 (Inventory of information and other associated assets), 8.9 (Configuration management).
- ITIL 4: Service Configuration Management practice.

# Policy

## Configurable item Scope and Granularity

- CivicActions places the following configuration item classes under formal configuration control:
    - CIA "High" systems and their dependent infrastructure
    - Managed endpoints and their approved software catalogs and managed device baselines
    - Cloud resources, platform services, and network components
    - Production SaaS configurations when feasible via API or documented snapshots; otherwise maintained through ticketed before/after states linked to the service asset record
    - Critical documentation such as runbooks and recovery procedures

## CMDB Architecture and Tooling

- Configuration-as-Code in Git is the authoritative baseline for infrastructure, platform, and application configuration. Git history is the change history; pull or merge requests are the mechanism for proposed changes and continuous integration/deployment is the records of testing and rollout.
- Jira/Confluence link service asset records to code repositories, deployment pipelines, and operational runbooks. When configuration cannot be managed as code, change tickets capture the approved before/after state.

## Baselines and Secure Defaults

- Secure baselines apply least functionality and remove non-essential services and components. Baselines include hardening guidance, identity and access parameters, logging, and monitoring hooks. Baselines are reviewed at least annually or upon major change.

## Change Governance and Traceability

- For CIA "High" systems and dependent infrastructure, peer review on pull/merge requests is mandatory. Automated policy checks, tests, and scans run in pipelines.
- All deployed configuration changes must be traceable to an approved change record (Standard catalog entry or Normal/Significant/Emergency change) and to the configuration item record.

## Continuous Verification and Drift Management

- Automated discovery and drift detection are implemented where feasible. Drift generates tickets that are triaged within two business days and resolved by either reconciling to baseline or raising a change request. Monitoring and event management feed this process with actionable signals.

## Evidence and Audit

- CivicActions retains configuration item inventories, baseline definitions, change histories, drift reports, and approvals as Controlled Records subject to the Document and Record Control Policy and QMS.

# Training

- Onboarding (30 days): following the training guidelines in the [Maintenance Policy.](https://civicactions.atlassian.net/wiki/x/AwBmL)
- Annual refresher: following the training guidelines in the [Maintenance Policy.](https://civicactions.atlassian.net/wiki/x/AwBmL)

# Review

This policy is reviewed annually by the CISO and the Document Controller. Ad-hoc reviews may take place upon major legal and/or technical changes. Changes, reviews, and approvals are recorded in Confluence and Jira, following the [Document and Records Control Policy](https://civicactions.atlassian.net/wiki/x/AYCQCw) .

# Exceptions

Exceptions for this policy are rare and time-boxed. Exceptions must include business justification, compensating controls, and risk assessment. Exceptions require approval by CISO (and CEO/CTO if residual risk is High). All exceptions are logged in the Risk Register (Jira), and reviewed at least quarterly.

Document generated by Confluence on Mar 18, 2026 09:50

[Atlassian](http://www.atlassian.com/)