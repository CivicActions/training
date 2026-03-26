# Identification Policy — Training Outcomes

Source: [Identification Policy](../policies/Identification-Policy_709951516.md)

| Policy | Section | Learning Outcome | Audience |
|--------|---------|-----------------|----------|
| IdP | Identity Foundations & Account Naming | Explain why every person and service must have a unique, traceable identity (no shared human accounts); identify your primary identifier (corporate email) and know that an immutable Employee ID exists for system synchronization | All Staff |
| IdP | SSO and Federation | Use corporate SSO (Google Workspace SAML/OIDC) for all supported services; explain why local app passwords are prohibited unless exempted, and that any exceptions must be vaulted and rotated | All Staff |
| IdP | Authentication Requirements (MFA) | Enroll in MFA using approved factors (preferred: FIDO2/WebAuthn hardware key; backup: TOTP app); explain why SMS/voice OTP is disallowed; identify which high-risk systems require a hardware key for primary sign-in | All Staff |
| IdP | Authentication Requirements — Passwordless Trajectory | Understand CivicActions is moving toward passwordless-by-default; until then, use passwords that are ≥14 characters, unique, and stored in an approved password manager | All Staff |
| IdP | Authenticator Issuance, Protection and Lifecycle | Protect hardware keys (keychain or secure pouch, not left in laptops while traveling); configure at least one backup factor; report loss or suspected compromise immediately to IT/Security | All Staff |
| IdP | Authenticator Issuance — Admin Requirements | Receive and secure two hardware keys at onboarding; understand that all authenticators and sessions are revoked at offboarding | Privileged Users; IT / Service Desk |
| IdP | Session Management and Re-authentication | Understand the default IdP session lifetime (20 hours) and that re-authentication is required after session expiry | All Staff |
| IdP | Managed Endpoints and Remote-First Alignment | Explain that managed endpoints are required for Internal/Confidential (including FCI) data access; understand BYOD limitations (MFA/communications only, under MDM/profile isolation) | All Staff |
| IdP | Credentials and Secrets Hygiene | Use an approved password manager for any residual app passwords or recovery codes; never share credentials; store secrets only in managed secret systems, never in code or tickets | All Staff; Developers (deeper) |
| IdP | Non-Person Identities (NPIs) | Create unique NPIs mapped to a System Owner and tracked in inventory; prefer OIDC/workload identity/short-lived tokens over long-lived keys; rotate NPI secrets at least annually and immediately on compromise; never use NPIs for interactive login | Developers; IT / Service Desk |
| IdP | Logging, Monitoring and Auditability | Understand that authentication events, factor changes, admin elevation, break-glass usage, and NPI token use are logged and auditable; know that metrics (hardware-key coverage, time-to-revoke, anomalous login rate) are reviewed annually | IT / Service Desk; System/Data Owners |
| IdP | Identity Proofing — Onboarding | Complete identity verification with PeopleOps; receive account, group/role assignment, and MFA key issuance as part of onboarding | All Staff |
| IdP | Identity Proofing — Role Changes | Expect prompt access updates when duties change; privileges are minimized or removed when no longer needed | All Staff; Managers |
| IdP | Identity Proofing — Offboarding | Understand that all access is revoked immediately on separation; authenticators are retrieved or cryptographically revoked; evidence is documented in a Jira offboarding ticket | IT / Service Desk; Managers |
| IdP | Incident Reporting & Response | Report immediately any suspected account compromise, phishing credential capture, or loss/theft of an MFA device; know that Security follows the IR Plan to contain, eradicate, and recover | All Staff |
| IdP | Compliance and Enforcement | Understand that violations can result in access revocation, disciplinary action, or contract remedies | All Staff |
