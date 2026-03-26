# Policies : Access Control Policy

Created by Owen Barton , last modified on Mar 11, 2026

[https://civicactions.atlassian.net/browse/CPDOC-37?atlOrigin=eyJpIjoiYjU4NzBmZGY4NThiNDI1NmEyOThmZjhiMjI2NmU1YzIiLCJwIjoiaiJ9](https://civicactions.atlassian.net/browse/CPDOC-37?atlOrigin=eyJpIjoiYjU4NzBmZGY4NThiNDI1NmEyOThmZjhiMjI2NmU1YzIiLCJwIjoiaiJ9)

# Purpose

The purpose of this policy is to control logical access to company and client systems and data. The policy enforces least privilege, separation of duties, and project boundary segregation across cloud, SaaS, and internal services. This policy governs logical access. Physical access safeguards are referenced where basic safeguarding requires it.

# Scope

This policy applies to all CivicActions Team Members, contractors, and approved third parties who access CivicActions-managed systems, client-furnished systems, or CivicActions data. It covers:

- Enterprise identity and SSO
- Cloud infrastructure (e.g., AWS, GCP, Azure) and CI/CD
- SaaS applications (Google Workspace, Slack, Zoom, Atlassian, Rippling, Unanet, GitLab)
- Internal servers, databases, secrets and data platforms
- Non-person identities (service, bot, API accounts)

# Roles and Responsibilities

- CEO and CTO (Approvers): Approve this policy and privileged access categories
- CISO (Policy Owner): Maintains this policy, tracks metrics and audits, ensures alignment with ISMS and NIST CSF outcomes
- IT/Service Desk (Access Management): Operates IdP/SSO, implements approved changes, manages break-glass, maintains access evidence and logs
- System Owners: Define roles, implement RBAC in their platforms, keep inventories current, run access attestations
- Data Owners: Approve access to Confidential/Restricted datasets, including any CUI boundaries
- Managers: Initiate and certify access for their teams
- Team Members: Use only authorized access and report over-privilege
- Document Controller: Controls this Controlled Document per the Policy on Policies and Document and Records Control

# Definitions

- Access Control: Policies and mechanisms intentionally implemented to enforce who may perform which actions on which systems and data
- Least Privilege: The minimum permissions required to perform a task, for the shortest time needed
- Privileged User: A user that is authorized (and therefore, trusted) to perform security-relevant functions that ordinary users are not authorized to perform
- Authorization Boundary / Project Boundary: A set of systems, identities, and data segregated by client or program; cross-boundary access requires explicit owner approval
- Managed Endpoint: Company-managed device under MDM with baseline controls
- Non-Person Identity (NPI): Service, bot, workload identity used by software; no interactive login
- SSO: Single sign-on
- SaaS: Software as-a-service

# References

- FAR Clause 52.204-21: b.1.i (Limit information system access), b.1.ii (Limit types of transactions/functions), b.1.v (Identify users), b.1.vi (Authenticate users), b.1.viii (Limit physical access).
- NIST SP 800-171 Rev. 3: 03.01.02 (Access Enforcement), 03.01.04 (Separation of Duties), 03.01.05 (Least Privilege), 03.01.12 (Remote Access), 03.05.03 (Multi-factor Authentication).
- CMMC Assessment Guide L2 v2.13: AC.L1-B.1.i (Authorized Access Control), AC.L2-3.1.4 (Separation of duties), AC.L2-3.1.5 (Least privilege), AC.L2-3.1.8 (Access reviews), IA.L2-3.5.3 (MFA).
- ISO/IEC 27002:2022: 5.3 (Segregation of duties), 5.15 (Access control), 5.18 (Access rights), 8.2 (Privileged access rights), 8.3 (Information access restriction).

# Policy

## Intent and Principles

CivicActions enforces default-deny access that is risk-based and measurable:

- Grant the least privilege necessary, for the minimum duration, aligned to role and duty.
- Enforce separation of duties for sensitive actions; requesters do not approve or implement their own access.
- Keep authorization boundaries segregated by client/project; cross-boundary access is exception-based and logged.
- Use managed endpoints for Internal/Confidential/Restricted data; limited, risk-assessed exceptions are time-boxed.
- Prefer Zero Trust patterns for remote access (identity, device posture, and context), moving toward identity-aware proxies and JIT elevation on high-criticality systems.

## Access Control Architecture

### **Identity and Single Sign-on (SSO)**

- SSO via the corporate IdP (Google Workspace SAML/OIDC) is mandatory wherever supported; native passwords must be disabled or tightly controlled.
- Groups and organizational units in the IdP are the authoritative source for SSO grants; groups that confer SAML app access must be clearly labeled and inventoried.
- Exceptions: Some services (e.g., GitLab, Unanet) may permit separate credentials; when SSO is not used, accounts must be unique, vaulted, long and unique, and rotated per standards; enable MFA consistent with the Identification Policy.

### **RBAC as Baseline, ABAC-Ready**

- CivicActions standardizes on role-based access control. Each system maintains a role catalog mapped to permissions and linked to job duties. A centrally tracked RBAC Matrix is maintained as the source of truth.
- Where risk or scale warrants, attribute/context rules (e.g., device trust, location, project tag) may narrow access further.

### **Segregation by Client/Project Boundaries**

- Client access control policies must be followed whenever client systems or data is involved.
- Access defaults to project-specific boundaries. Shared services require explicit owner approvals. CUI stays in authorized CUI boundaries; external release follows contract and policy.

### **Privileged Access Management (PAM)**

- Classify an account/role as Privileged Access if the answer is "yes" to any of these:
    - Can it change who has access (accounts, groups, roles, permissions)?
    - Can it change security controls or security monitoring/auditing?
    - Can it disable/bypass controls, or perform key management/integrity checks?
    - Can it modify security-relevant configuration like firewall rules, ACLs, or key material?
    - Can it perform system administration actions that change system behavior (patch/config/install)?
    - Can it run "privileged commands" (control/monitor/administer the system)?
- Admin work uses separate privileged accounts; day-to-day work uses non-privileged accounts. All privileged grants and sessions are logged and periodically reviewed.
- Use just-in-time elevation or time-boxed admin roles on high-criticality systems; consider multi-party authorization for irreversible actions (e.g., KMS deletes, production data export).
- Treat DevOps abilities that change production (e.g., merging to protected branches, applying IaC to prod) as privileged access subject to the same controls.

### **Non-Person Identities (NPIs)**

- Each NPI is unique, owned by a System Owner, least-privileged, and never used for interactive login. Prefer short-lived tokens, workload identity, or OIDC client credentials; vault and rotate any static secrets at least quarterly or on exposure.

### **Remote Access**

- All remote access uses strong authentication per the Identification Policy, with session logging and monitoring. Prefer ZTNA/SASE or identity-aware proxies over network-wide VPN. Idle timeouts and absolute session limits apply per data sensitivity.
- Remote sessions to sensitive systems are monitored; anomalous access is triaged under Monitoring and Event Management.

### **Cloud and SaaS Governance**

- Use native cloud IAM (e.g., AWS IAM, Azure RBAC) and deny overly permissive roles for routine tasks. Continuously monitor for excessive permissions, unused roles, and risky configurations (e.g., CSPM/SSPM).

### **Endpoint Prerequisite**

- Managed endpoints are required for access to Internal/Confidential/Restricted data. Access from unmanaged devices is exception-only, time-boxed, and risk-assessed.

### **Physical Safeguards Linkage**

- Logical access depends on physical protection of IT equipment; basic safeguarding requires limiting physical access to authorized individuals for systems and operating environments.

## Access Lifecycle

CivicActions uses a single lifecycle across all systems (request, approve, grant, review, revoke), integrated with ITSM and HR, and recorded in an RBAC Matrix . Access may be managed directly be IT, or delegated to a trained team member (e.g. Project Manager) for managing sub-system level access (e.g. Google Shared Drive).

1. **Request**
    - For IT managed system access, Team Member or Manager submits a ticket or pre-approved workflow (e.g., Rippling) specifying person, system, justification, duration, project/boundary (if sub-system or project-specific system), role (if external) . Standardized request templates are required.
    - For sub-system level access , the access manager is required to have contextual awareness with the person, system and data and the reason access is needed (e.g. a team member joining a project). If they are not confident of these, the request should be redirected to IT.
2. **Approve**
    - Public or Internal data access: IT may approve based on verified roster and role.
    - Confidential/Restricted or dataset access: Data Owner or System Owner approval is required.
    - Privileged access: CTO or delegate approval; consider multi-party authorization for high-risk. Approvers cannot be the implementer.
3. **Grant**
    - IT/Service Desk implements in IdP/target system and records evidence in the ticket. Use time-bound grants or JIT for elevated roles where supported.
4. **Review/Change**
    - Role or boundary change triggers an immediate rights review and right-sizing.
5. **Revoke**
    - Upon separation, disable all access immediately and remove within 24 hours of HR notice; revoke tokens, keys, and sessions, and collect evidence in the offboarding ticket. This closes a common gap that enables privilege creep.
    - Accounts may be suspended or revoked if unused, or if the account holder fails to comply with the Information Security Policy, Acceptable Use Policy, Rules of Behavior and cybersecurity training requirements.

## Periodic Access Reviews

- Frequency by criticality
    - High-criticality systems (including IdP, cloud prod, CI/CD, financials, and any CUI boundary): quarterly access reviews for all users and privileged roles.
    - Other systems: annual review. Triggers include major changes, incidents, or boundary shifts.
- Managers and System Owners certify access; excess or orphaned access is remediated promptly and tracked to closure. Evidence must be retained.

## Project boundary and CUI segregation

- Maintain strict segregation between client environments and corporate systems. CUI remains inside authorized boundaries; cross-boundary flows require explicit authorization and technical enforcement of approved sources and destinations. For any CSP that stores or transmits CUI, require FedRAMP Moderate equivalence by contract.

## Data and secrets access

- Google Drive and Shared Drives: default to named sharing, no "anyone with link" for Internal/Confidential/Restricted. Data Owners manage membership and labels.
- Secrets and credentials: no secrets in code or tickets; store in an approved secret manager; rotate on exposure or role change. Access to KMS/HSM is Restricted and logged.

## Logging, Monitoring, and Evidence

- Log authentication and authorization events, group/role changes, privileged elevations, break-glass usage, and NPI token use; retain per logging standard.
- Access review attestations, approvals, grants/changes/revokes, and emergency use are Controlled Records subject to audit.
- NIST CSF outcomes guide continuous improvement; metrics include time-to-revoke on leavers, completion rate of reviews, privileged JIT coverage, and SSO coverage.

## Emergency Access ("break-glass")

- Maintain the minimum practical number of emergency admin accounts. Protect with strong MFA, store hardware keys securely, and test access monthly. Any use is fully logged and reviewed within one business day; residual elevation is removed.

## Third-party and supplier access

- Supplier and partner access must meet CivicActions' baseline safeguards, be limited to least privilege, and be contractually bound to equivalent controls. DFARS 252.204-7012 flow-down and FedRAMP-equivalent requirements apply when CUI is involved.

## Critical systems and enforcement mechanisms

- Critical systems include Google Workspace, Slack, Zoom, Atlassian, Rippling, Unanet, GitLab, and production cloud and CI/CD.
- SSO via Google Authentication is required wherever available; groups that confer app access are maintained by IT and System Owners. Non-SSO systems require ITSM tickets, default approvers, and explicit system approvers as listed in asset records.

## Change control and configuration alignment

- Changes to access control mechanisms, roles, or RBAC mappings are subject to change enablement and must be documented; access controls must align with secure configuration baselines and inventories.

# Compliance and Enforcement

Violations may result in remedial actions up to and including access revocation, disciplinary action, or contract remedies. Sanctions follow PeopleOps processes and applicable standards.

# Training

- Onboarding (30 days): Users and managers receive training on least privilege, request/approval mechanics, duty to report over-privilege, and project boundary rules.
- Annual refresher: Updated expectations, CUI/FCI handling, and how to complete access reviews. Records are maintained per QMS/Controlled Documents.

# Review

This policy is reviewed annually by the CISO and the Document Controller. Ad-hoc reviews may take place upon major legal and/or technical changes. Changes, reviews, and approvals are recorded in Confluence and Jira, following the [Document and Records Control Policy](https://civicactions.atlassian.net/wiki/x/AYCQCw) .

# Exceptions

Exceptions for this policy are rare and time-boxed. Exceptions must include business justification, compensating controls, and risk assessment. Exceptions require approval by CISO (and CEO/CTO if residual risk is High). All exceptions are logged in the Risk Register (Jira), and reviewed at least quarterly.

Document generated by Confluence on Mar 18, 2026 09:50

[Atlassian](http://www.atlassian.com/)