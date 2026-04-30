# Policies : Identification Policy

Created by Owen Barton , last modified by Sammy De La O on Mar 11, 2026

[https://civicactions.atlassian.net/browse/CPDOC-35](https://civicactions.atlassian.net/browse/CPDOC-35)

# Purpose

This policy outlines how CivicActions uniquely identifies and authenticates every individual and non-person entity that accesses CivicActions or client systems. Following this policy ensures accountability across CivicActions systems and data, CivicActions remote-first workforce, and fulfills leadership, client, contractual, and regulatory requirements.

# Scope

This policy applies to all CivicActions team members, contractors, third-party vendors, and client points of contacts with access to any CivicActions systems, including:

- CivicActions Google Workspace, including Gmail and Drive
- CivicActions Slack channels
- CivicActions GitHub and GitLab instance
- Other cloud services with CivicActions instances

This policy also governs non-person identities (service, bot, or API accounts) used by CivicActions systems.

# Roles and Responsibilities

- CEO/CTO (Approvers): Approve this policy; resource SSO, MFA, and device controls
- CISO (Policy Owner): Maintains IdAM standards; verifies compliance; coordinates audits and metrics under the ISMS and NIST CSF governance outcomes
- CTO: Ensures secure technical architecture, SSO integrations, and managed endpoint baselines
- People Operations (HR): Identity proofing at hire; initiates onboarding/offboarding tasks (accounts, MFA issuance, revocation)
- IT/Service Desk (IdAM): Operates IdP/SSO, MFA lifecycle, account provisioning, break-glass controls, and access logging
- Managers &amp; System Owners: Ensure team compliance; use SSO federation; minimize local accounts; maintain NPI ownership/inventory
- All Personnel: Use approved authenticators; protect credentials; report lost/stolen credentials immediately per IR Plan
- Document Controller (Compliance): Controls this Controlled Document per Document and Records Control Policy

# Definitions

- Primary Identifier: Corporate email `firstname.lastname@civicactions.com` used as username/NameID across SSO-integrated systems; a separate immutable Employee ID is maintained as a key for identity synchronization (when supported) as well as in analytics.
- Single Sign-On (SSO): Central identity provider (IdP) (e.g., Google Workspace) used to authenticate users and federate to SaaS via SAML/OIDC
- Multi-factor Authentication (MFA): Use of at least two authentication factors; approved methods include FIDO2/WebAuthn hardware security keys (e.g., YubiKey) and TOTP apps; SMS/voice are disallowed except break-glass
- Managed Endpoint: Company-managed device under MDM with enforced baseline
- Non-Person Identity (NPI): Service, bot, or workload identity used by software, not a human

# References

- FAR Clause 52.204-21: b.1.v (Identify users), b.1.vi (Authenticate users).
- NIST SP 800-171 Rev. 3: 03.05.02 (Identifier Management), 03.05.03 (Multi-factor Authentication).
- NIST SP 800-63-3: Digital Identity Guidelines.
- CMMC Assessment Guide L2 v2.13: IA.L2-3.5.1 (Unique ID), IA.L2-3.5.3 (MFA).
- ISO/IEC 27002:2022: 5.16 (Identity management), 5.17 (Authentication information).

# Policy

## Identity Foundations &amp; Account Naming

- Unique Identity Required. Every human and non-person entity that accesses CivicActions or client systems must have a unique, traceable identity-no shared human accounts. (FAR basic safeguarding)
- Standard account name. Human user accounts shall use `firstname.lastname@civicactions.com` **.** If a collision occurs, HR/IT will add a middle name/initial or other minimally invasive variation agreed with the later-joining person. When a legal name changes, the prior address becomes a permanent alias.
- Primary Identifier. The corporate email is the primary login identifier across SSO-integrated systems. Separately, HR assigns an immutable Employee ID used for identifier synchronization (when supported) as well as analytics to preserve longitudinal consistency when names change.
- Directory of Record. The IdP directory (e.g., Google Workspace) is the authoritative source for identities, attributes (role, manager, status), and MFA status; downstream apps must federate to it unless an exception is approved.

## SSO and Federation

- SSO is mandatory for workforce access to company SaaS and internal systems where available (SAML/OIDC). Local app passwords are prohibited unless exempted; if required, they must be vaulted and rotated.
- Least local accounts. System Owners must disable direct, native logins where SSO is supported and document any residual local accounts as exceptions (time-boxed; risk-assessed). (NIST CSF governance/policy outcomes).

## Authentication Requirements (MFA)

- MFA is required for all users and all systems that process CivicActions or client data, including FCI and any CUI boundary; acceptable factors/devices:
    - Preferred: FIDO2/WebAuthn hardware security key (e.g., YubiKey)
    - Backup: TOTP authenticator app
    - Not allowed (except break-glass): SMS/voice OTP Rationale: meets FAR's "authenticate users/devices" control and aligns to CMMC/CSF
- High-risk systems (IdP/Google Workspace, admin consoles, CI/CD, production cloud, client environments, and any CUI boundary) shall require a hardware key for primary sign-in and step-up re-auth.
- Passwordless trajectory. CivicActions is moving to passwordless by default (WebAuthn platform or roaming keys). Until fully deployed, any passwords in use must be long (≥14 chars), unique, and stored in an approved password manager (1Password/LastPass/Chrome store). (Best-practice posture for modern I&amp;A).

## Authenticator Issuance, Protection and Lifecycle

- Issuance: IT issues at least one hardware key at onboarding (two for admins).
- Protection: Keys must not be left inserted in laptops when traveling; keep them on a keychain or secure pouch. Users must configure at least one backup factor.
- Loss/Suspected compromise: Users must report immediately (without delay) to IT/Security; IT disables lost factors, verifies user identity, re-binds replacement keys, and documents the incident per the IR Plan (NIST SP 800-61r3).
- Revocation: All authenticators and sessions are revoked at off-boarding effective date/time; privileged and API tokens are invalidated as part of the leaver checklist.
- Break-glass accounts: Maintain the minimum practical number (≤2) of emergency admin accounts protected by hardware keys, and stored in a sealed vault process. Events are logged and reviewed.

## Session Management and Re-authentication

- IdP session lifetime: Default IdP (SSO) session is set to 20 hours. (Matches current IdP capability and balances usability with remote-first risk.)

## Managed Endpoints and Remote-First Alignment

- Managed endpoints are required to access Internal/Confidential (incl. FCI) data; any limited mobile BYOD for MFA/communications must be under MDM/profile isolation and follow endpoint baselines. For further direction, see the [Data Security and Handling Policy](https://civicactions.atlassian.net/wiki/x/HgBVKg) .

## Credentials and Secrets Hygiene

- Password managers are mandatory for any residual app passwords or recovery codes.
- No credential sharing. Shared secrets are prohibited; use NPIs or delegated access.
- Secrets in code or tickets are prohibited; store in a managed secret system; rotate on exposure. (ITIL Create/Deliver/Support and Monitoring practices reinforce operational controls.)

## Non-Person Identities (Service Account/API/Bot)

- Uniqueness and ownership: Each NPI must be unique, mapped to a System Owner, and tracked in inventory (scope/effective permissions documented).
- Authentication: Prefer OIDC client credentials, workload identity, or short-lived tokens over long-lived passwords/keys; NPIs must not be used for interactive login.
- Rotation and vaulting: NPI secrets are vaulted, rotated at least anually or on role/privilege change, and immediately upon suspected compromise; access is least-privileged and time-bound.

## Logging, Monitoring and Auditability

- Authentication events (success/failure), factor changes, admin elevation, break-glass usage, and NPI token use must be logged centrally and retained per data/logging standards; alerts are triaged under Monitoring and Event Management, with incident escalation via IR Plan.
- Network audit logging and identification safeguards support traceability across boundaries. (ISO/IEC 27033 references identification/authentication and audit logging in network security).
- Continuous improvement. Metrics (e.g., % hardware-key coverage, mean time to revoke leavers, anomalous login rate) are reviewed annually as part of the ISMS/ITIL continual improvement practice by using 3rd party vendor reports (such as Google Admin Console &gt; Reporting &amp; Monitoring &gt; Security Reports).

## Identity Proofing, On/Off-boarding and Access Changes

- Onboarding: PeopleOps verifies identity, collects legal name and contact, and triggers IdAM tasks (account creation, group/role assignment, MFA key issuance).
- Job/role change: System Owners update role-based access and NPIs promptly; privileges are minimized or removed when duties change.
- Offboarding: Access is revoked immediately upon separation; retrieve or cryptographically revoke authenticators; document evidence (Jira offboarding ticket). (QMS/Document &amp; Record Control).

## Incident Reporting &amp; Response

- Report immediately any suspected account compromise, phishing credential capture, or loss/theft of an MFA device; Security follows the IR Plan (NIST SP 800-61r3) to contain, eradicate, and recover, and initiates POA&amp;M actions if needed.
- Notification duties for client environments follow contract and CUI policies.

# Compliance and Enforcement

Violations may result in remedial actions up to and including access revocation, disciplinary action, or contract remedies. Sanctions follow PeopleOps processes and applicable standards.

# Training

- Onboarding (within 30 days): SSO usage, passwordless/MFA with hardware keys, password manager setup, device baseline, and how to report lost/compromised credentials.
- Annual refresher: Updates, phishing simulations, incident reporting rehearsals. Training records are managed per QMS and Controlled Documents processes.

# Review

This policy is reviewed annually by the CISO and the Document Controller. Ad-hoc reviews may take place upon major legal and/or technical changes. Changes, reviews, and approvals are recorded in Confluence and Jira, following the [Document and Records Control Policy](https://civicactions.atlassian.net/wiki/x/AYCQCw) .

# Exceptions

Exceptions for this policy are rare and time-boxed. Exceptions must include business justification, compensating controls, and risk assessment. Exceptions require approval by CISO (and CEO/CTO if residual risk is High). All exceptions are logged in the Risk Register (Jira), and reviewed at least quarterly.

Document generated by Confluence on Mar 18, 2026 09:50

[Atlassian](http://www.atlassian.com/)