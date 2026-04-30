# Policies : Change Enablement Policy

Created by Owen Barton , last modified by Bentley Hensel on Mar 11, 2026

[https://civicactions.atlassian.net/browse/CPDOC-43](https://civicactions.atlassian.net/browse/CPDOC-43)

# Purpose

The purpose of this policy is to ensure production changes proceed safely and efficiently with evidence, using automation and delegated authority aligned to risk.

# Scope

Applies to all production changes across infrastructure, platforms, applications, SaaS configurations under CivicActions control, and endpoint policies delivered through MDM.

# Roles and Responsibilities

- CTO (Approver): Approve this policy and high-risk exceptions
- CISO (Policy Owner): Maintains this policy and oversees metrics, audits, and regulatory alignment
- CTO / Head of IT: Operates the integrated maintenance program and sponsors automation and configuration as code
- Change Authority: Delegated approvers for Normal and Significant changes; maintains Standard change catalog
- System Owners and Implementers: Prepare change records, perform testing and rollback planning, implement, verify, and update configuration records
- Incident Commander: Authorizes Emergency changes and leads the retrospective per Incident Response Plan

# Definitions

- Standard change: Low-risk, pre-approved, repeatable change using a documented runbook
- Normal change: Assessed and peer-reviewed change with delegated approval based on impact
- Significant change: Manual or broad-impact change, change to High Impact systems, or change that cannot be easily rolled back
- Emergency change: Time-critical change to resolve or prevent a major incident

# References

- ISO 9001:2015: 8.5.6 (Control of changes).
- NIST SP 800-171 Rev. 3: 03.04.03 (Configuration Change Control), 03.04.04 (Impact Analyses).
- CMMC Assessment Guide L2 v2.13: CM.L2-3.4.4 (Security Impact Analysis), CM.L2-3.4.5 (Access Restrictions for Change).
- ISO/IEC 27002:2022: 5.37 (Documented operating procedures), 8.9 (Configuration management), 8.32 (Change management).
- ITIL 4: Change Enablement practice.

# Policy

## Change Classes and Criteria

- Standard (fully automated changes)
    - Examples: monthly OS patch waves via MDM; routine DNS updates from runbooks; rotating credentials using automated workflows
    - Logged automatically; no additional approvals when executed within the cataloged procedure and window
- Normal (manual change)
    - Meets all: managed in code, automated tests, peer-reviewed PR/MR, progressive rollout to test or staging
    - Or: affects a Low or Moderate Impact service and is easily reversible
    - Approval: delegated Change Authority based on impact assessment
- Significant (manual change)
    - Any configuration change that could affect confidentiality, data integrity or availability for a High Impact service that is applied to the entire company
    - Requires creation of a Change Record and formal approval step in Jira.
- Emergency
    - Time-critical to mitigate or resolve a major incident; Incident Commander authorization; full documentation and retrospective within 72 hours.

## Required Content for Change Records

- Description, impacted services and configurable items, impact, urgency, risk assessment, test results, implementation plan, change reason, communications plan, backout plan, test plan, maintenance window, and evidence attachments (screenshots etc). The Jira workflow and fields must be completed.

## Approvals and Guardrails

- For Normal changes, peer review in PR/MR plus passing automated tests, SAST/DAST/SCA, and environment validation act as the primary approval guardrails.
- Significant changes require delegated Change Authority approval and a rollback plan.
- Emergency changes require Incident Commander approval with rapid communication and subsequent review/retrospective.

## Scheduling and Communication

- Each user-facing service directly maintained by CivicActions maintains a weekly maintenance window and participates in a monthly company maintenance calendar. External services Changes outside windows require justification and delegated approval. Impacting changes require stakeholder notifications before and after implementation.

## Post-Implementation Review

- Normal, Significant and Emergency changes require verification and configuration records updated. If needed, a post-implementation retrospective should be conducted within five business days to capture lessons learned in the improvement register.

## Change Freezes

- Change freezes may be applied by the Change Authority during critical delivery periods or when services exceed error budgets; only fixes that improve stability are permitted until recovery.

# Training

- Onboarding (30 days): following the training guidelines in the [Maintenance Policy.](https://civicactions.atlassian.net/wiki/x/AwBmL)
- Annual refresher: following the training guidelines in the [Maintenance Policy.](https://civicactions.atlassian.net/wiki/x/AwBmL)

# Review

This policy is reviewed annually by the CISO and the Document Controller. Ad-hoc reviews may take place upon major legal and/or technical changes. Changes, reviews, and approvals are recorded in Confluence and Jira, following the [Document and Records Control Policy](https://civicactions.atlassian.net/wiki/x/AYCQCw) .

# Exceptions

Exceptions for this policy are rare and time-boxed. Exceptions must include business justification, compensating controls, and risk assessment. Exceptions require approval by CISO (and CEO/CTO if residual risk is High). All exceptions are logged in the Risk Register (Jira), and reviewed at least quarterly.

Document generated by Confluence on Mar 18, 2026 09:50

[Atlassian](http://www.atlassian.com/)