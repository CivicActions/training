# Access Control Policy — Training Outcomes

Source: [Access Control Policy](../policies/Access-Control-Policy_744947714.md)

| Policy | Section | Learning Outcome | Audience |
|--------|---------|-----------------|----------|
| ACP | Intent and Principles | Explain default-deny, least privilege, separation of duties, and project boundary segregation; give a workplace example of each | All Staff |
| ACP | Identity and SSO | Use corporate SSO (Google Workspace) for all supported services; explain why native passwords must be disabled or tightly controlled; use MFA per Identification Policy for non-SSO services | All Staff |
| ACP | RBAC as Baseline | Explain what role-based access control is and how it maps permissions to job duties; know where to find the RBAC Matrix | All Staff; Managers, System/Data Owners (deeper) |
| ACP | Segregation by Client/Project | Identify your project boundaries; explain why cross-boundary access requires explicit approval; describe CUI boundary rules | All Staff |
| ACP | Privileged Access Management | Determine whether a given account/role qualifies as privileged using the six-question test; use separate admin and day-to-day accounts; explain JIT elevation and logging requirements | Privileged Users; IT / Service Desk |
| ACP | Non-Person Identities (NPIs) | Create and manage service/bot accounts that are unique, least-privileged, not used for interactive login; prefer short-lived tokens; rotate static secrets quarterly | Developers; IT / Service Desk |
| ACP | Remote Access | Use strong authentication for all remote access; apply session timeouts; prefer ZTNA/identity-aware proxies over VPN | All Staff |
| ACP | Cloud and SaaS Governance | Use native cloud IAM with least-privilege roles; avoid overly permissive grants; monitor for excessive permissions | IT / Service Desk; System/Data Owners |
| ACP | Endpoint Prerequisite | Explain that managed endpoints are required for Internal/Confidential/Restricted data; know that unmanaged device access is exception-only and time-boxed | All Staff |
| ACP | Physical Safeguards Linkage | Explain that logical access depends on physical protection of devices (laptops, hardware keys); secure laptops when unattended, keep hardware keys on a keychain or secure pouch, and do not leave devices accessible to unauthorized individuals | All Staff |
| ACP | Access Lifecycle — Request | Submit a properly formatted access request (person, system, justification, duration, boundary, role) via ticket or Rippling workflow | All Staff |
| ACP | Access Lifecycle — Approve | Apply the correct approval authority based on data sensitivity (IT for Public/Internal; Data/System Owner for Confidential/Restricted; CTO for privileged); ensure approver ≠ implementer | Managers; System/Data Owners |
| ACP | Access Lifecycle — Grant | Implement access changes in IdP/target system, record evidence in the ticket, use time-bound grants where supported | IT / Service Desk |
| ACP | Access Lifecycle — Review/Change | Trigger an immediate rights review when a team member's role or project changes; right-size permissions | Managers; IT / Service Desk |
| ACP | Access Lifecycle — Revoke | Disable access immediately on separation; remove within 24 hours; revoke tokens, keys, sessions; collect evidence in offboarding ticket | IT / Service Desk; Managers |
| ACP | Periodic Access Reviews | Conduct quarterly reviews for high-criticality systems and annual reviews for others; certify, remediate excess access, and retain evidence | Managers; System/Data Owners |
| ACP | Project Boundary and CUI Segregation | Maintain strict separation between client environments and corporate systems; keep CUI inside authorized boundaries; require FedRAMP Moderate equivalence for CSPs handling CUI | All Staff working with CUI; System/Data Owners |
| ACP | Data and Secrets Access | Use named sharing (no "anyone with link") for non-Public data; store secrets in approved managers; never commit secrets to code or tickets | All Staff; Developers (deeper) |
| ACP | Logging, Monitoring, and Evidence | Understand that authentication, authorization, and privileged actions are logged and subject to audit; know the key metrics (time-to-revoke, review completion, SSO coverage) | IT / Service Desk; System/Data Owners |
| ACP | Emergency Access (Break-Glass) | Describe when break-glass accounts may be used; explain the post-use review requirement (within one business day) | IT / Service Desk; Privileged Users |
| ACP | Third-Party and Supplier Access | Ensure supplier access is least-privileged and contractually bound; apply DFARS flow-down for CUI | Managers; System/Data Owners |
| ACP | Critical Systems and Enforcement Mechanisms | Identify the critical systems requiring SSO via Google Authentication (Google Workspace, Slack, Zoom, Atlassian, Rippling, Unanet, GitLab, production cloud/CI-CD); know that non-SSO systems require ITSM tickets and explicit system approvers | IT / Service Desk; System/Data Owners |
| ACP | Change Control and Configuration Alignment | Understand that changes to access control mechanisms, roles, or RBAC mappings are subject to change enablement and must be documented; access controls must align with secure configuration baselines | IT / Service Desk; System/Data Owners |
| ACP | Compliance and Enforcement | Understand that violations can result in access revocation, disciplinary action, or contract remedies | All Staff |
