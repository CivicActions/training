# Policies : Data Security and Handling Policy

Created by Owen Barton , last modified by Sammy De La O on Dec 23, 2025

[https://civicactions.atlassian.net/browse/CPDOC-34?atlOrigin=eyJpIjoiMDA4ODFmYTZjOTQ0NGM1ZTllYmY2OTFkNDdhMThjYmEiLCJwIjoiaiJ9](https://civicactions.atlassian.net/browse/CPDOC-34?atlOrigin=eyJpIjoiMDA4ODFmYTZjOTQ0NGM1ZTllYmY2OTFkNDdhMThjYmEiLCJwIjoiaiJ9)

# Purpose

The purpose of this policy is to set guidelines for all CivicActions team members for protecting company and client information (also identified as "data" in this and other documentation). This policy covers all stages of the data lifecycle: creation, access, updating, storing, sharing, archiving, and destruction.

# Scope

This policy applies to all CivicActions team members, contractors, and third-party partners and vendors handling any CivicActions or client information. This policy covers CivicActions-managed systems, client-furnished systems, approved cloud/SaaS, or physical media.

This policy works in conjunction with client-project data that is stored in CivicActions systems. Any client data that is accessed within a client-managed system will follow client-specific policies.

# Roles and Responsibilities

- CEO / CTO (Approvers): Approve this policy. Resource baselines/automation for managed devices and cloud security.
- CISO (Policy Owner): Maintain this policy; set and verify standards (cryptography, DLP rules, labeling schemas); oversee evidence and audit.
- Document Controller (Compliance): Control this Controlled Document in Confluence/Jira (versioning, approvals, change log).
- Managers / Data Owners / System Owners: Classify data; ensure approved locations and encryption; maintain data and asset inventories; ensure backup/DR; ensure logs/monitoring; support risk exceptions.
- Team Members: Handle data per classification; use only approved services and managed endpoints; avoid email for Confidential/Restricted; report incidents.

# Definitions

- FCI: Federal Contract Information safeguarded under FAR 52.204-21
- CUI: Controlled Unclassified Information requiring safeguarding/delivery controls per federal rules; CivicActions has a dedicated CUI Policy
- Data Owner: Business lead accountable for classification, labeling, retention, and release decisions for a dataset or service
- System Owner: Technical lead accountable for control implementation, monitoring, and proof of compliance for a system or service
- Managed Endpoint: Company-managed laptop or mobile device under MDM with enforced baseline
- Cryptographic Erasure: Rendering data irretrievable by securely destroying encryption keys on fully-encrypted media

# References

- FAR Clause 52.204-21: b.1.iv (Control public information), b.1.vii (Media sanitization/destruction).
- NIST SP 800-171 Rev. 3: 03.08.08 (Media Disposal/Sanitization), 03.13.08 (Transmission and Storage Confidentiality), 03.13.11 (Cryptographic Protection), 03.14.08 (Information Management and Retention).
- CMMC Assessment Guide L2 v2.13: MP.L2-3.8.3 (Media sanitization), SC.L2-3.13.11 (Cryptographic Protection).
- ISO/IEC 27002:2022: 5.12 (Classification of information), 5.34 (Privacy and protection of PII), 8.12 (Data leakage prevention), 8.24 (Use of cryptography).
- Internal: Controlled Unclassified Information (CUI) Policy.

# Policy

## Data Classification and Labeling

CivicActions classifies all information before storage or external sharing using four levels.

| **Level**        | **Description**                                                 | **Examples**                                  | **Minimum handling**                                                                                                |
|------------------|-----------------------------------------------------------------|-----------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| **Public**       | Approved for public access/release                              | Website content, public docs                  | May be stored/shared openly; confirm no secrets/PII; follow open-data release check.                                |
| **Internal**     | Non-sensitive, internal-only                                    | Internal policies/procedures, AHC             | Store in Google Workspace Internal areas; share to named accounts; no public links.                                 |
| **Confidential** | Sensitive, need-to-know; includes FCI and CUI (Basic/Specified) | Client docs, proposals, PII, **CUI**          | Approved systems only; encryption at rest & in transit; no email; access control & audit; CUI extra controls apply. |
| **Restricted**   | Highest sensitivity; severe harm if disclosed                   | HR/personnel, payroll, financial, credentials | Stronger access (role + CISO approval), stricter logging/DLP, compartmentalization, minimal copies.                 |

- Labeling: All Confidential/Restricted items must carry an electronic label (document banner/filename tag or Workspace label) and a data owner. Google Workspace auto-tagging for "CUI" assists but does not replace owner responsibility. Physical media (rare) must be marked accordingly.
- Data minimization: Collect, keep, and copy only what's necessary; avoid local copies when cloud sharing suffices.
- CUI: CUI, when present, is treated as Confidential with additional CUI-specific safeguards covered in the [CUI Policy](https://civicactions.atlassian.net/wiki/x/RoANJQ) .

## Approved Locations and Boundaries

- Public/Internal: CivicActions Google Workspace, approved repositories, and approved SaaS.
- Confidential/Restricted (incl. FCI): Same, but only in access-controlled areas; no personal drives; audit logging required. FCI handling also requires basic safeguarding at boundaries.
- CUI: Only within authorized CUI boundaries (e.g., designated Google Workspace Shared Drives marked "CUI", FedRAMP-equivalent client environments, CivicActions managed endpoints). External CSPs that store/process/transmit CUI must meet FedRAMP Moderate equivalency.

## Encryption Requirements

- In transit (all data): TLS 1.2+ (or successor) using strong cipher suites. Network segmentation and boundary protections must be in place for publicly accessible components.
- At rest (all data): Enable provider-native encryption for cloud/SaaS; enable full-disk encryption on all endpoints; server/database encryption for services that store Confidential/Restricted data.
- CUI cryptography: Only FIPS 140-2/140-3 validated modules for protecting CUI at rest and in transit; Security maintains an Approved Crypto Modules &amp; Configurations standard and validates FedRAMP equivalency for cloud services before CUI use.
- Key management: Use cloud KMS/HSM or platform-managed keys with restricted roles, rotation, and logging. Key access is Restricted.

## Endpoints and Remote-First

- Managed endpoints are required for Confidential/Restricted access. Personal laptops are not permitted for Confidential; BYOD phones may be used for MFA/communications only under MDM with profile isolation. Baseline: FDE, EDR, host firewall, auto-lock, patching SLAs.
- Local storage: Keep data in cloud; if temporary local storage is unavoidable (e.g., offline work), it must remain on encrypted volumes and be purged promptly.
- Travel/home networks: Use secure, encrypted connections and zero-trust posture (identity + device posture).

## Software Development and Testing (DevSecOps)

- No production Confidential/CUI data in dev/test. Use synthetic or properly de-identified/masked datasets; masking scripts must be approved and codified (IaC/pipeline).
- Secrets management: No secrets in source code; use vaults/secret stores; rotate on exposure.
- Supply chain: Use SCA/SBOM; remediate vulnerable components before release.
- Shift-left: Data handling checks (classification, authN/Z, logging, retention) are required gates in CI/CD.

## Sharing and Communication Channels

- Default: Share via Google Drive to named accounts (no "anyone with link") for Internal, Confidential, and/or Restricted.
- Email is not permitted for Confidential/Restricted content. If a partner cannot access Drive: send as a password-protected archive using AES-256 (e.g., 7-Zip/Keka/SecureZIP); use a 20+ character passphrase and transmit it via a separate channel (e.g., Slack DM/call).
- CUI: Follow CUI Policy; no Slack for CUI data; use only approved CUI boundaries and channels.
- Public release: Requires Data Owner approval and the open-data release checks.

## Data Loss Prevention (DLP) and Monitoring

- Google Workspace DLP rules must protect labels/keywords (e.g., SSNs, "CUI"), blocking risky sharing and exfiltration.
- Endpoint controls: CIS-level baselines; forced encryption.
- Monitoring and Events: Access anomalies, DLP events, and boundary alerts are triaged under Monitoring and Event Management and escalated to IR if needed.

## Removable Media and Printing

- Discouraged by default. Use only when business-necessary and approved.
- If used for Confidential/Restricted: encrypt media, scan for malware before first use, keep chain-of-custody, and record in the asset register. CUI on removable media is exception-only.

## Backup and Recovery

- SaaS-first: Rely on vendor-managed backups/DR where contractually appropriate; confirm provider RTO/RPO against business needs.
- Endpoints: Sync project work to approved cloud (Google Drive/approved repos). Do not backup credentials to cloud.
- Testing: System Owners must test restore for critical datasets at least annually and record evidence.

## Retention and Legal Holds

- Data Owners define retention schedules for each dataset/type; minimize retention by default; records retention follows Document &amp; Records Control. Legal holds override normal deletion.

## Open Data and Public Release Controls

- Prior to any public release (docs, datasets, code artifacts):
    1. Classification confirmed as Public; 2) Automated scans (secrets/PII) pass; 3) Owner approval; 4) License reviewed; 5) If derived from client data, confirm contract permits release.

## Media Sanitization and Destruction

To meet FAR 52.204-21(b)(1)(vii) and CMMC MP requirements remotely:

- Company-managed devices:
    - Prefer cryptographic erasure by destroying the escrowed FileVault/LUKS key via MDM workflow, with a sanitization record linked to the asset.
    - If device is returned/reused: perform validated wipe per Security standard and retain tool certificate/log.
- External media (USB/SSD): Use approved wiping tools producing sanitization certificates; upload certificates to the asset record.
- Mail-in destruction: For failed media, use an approved shredding vendor with chain-of-custody and certificate of destruction; log in asset system.
- Full-disk encryption is mandatory so that cryptographic key destruction renders data irrecoverable if physical destruction is delayed.
- Compliance is tracked in the CMDB/asset register; Security audits a sample each quarter.

## Third-Party Management

Vendors that touch our or client data must meet baseline safeguards and incident obligations by contract; annual reviews recorded. This follows the guidelines in the [3rd Party Management Policy](https://civicactions.atlassian.net/wiki/x/DoBtL) .

For CUI, cloud providers must be FedRAMP Moderate-equivalent; delegated controls must be captured in SSP/agreements. Guidelines are in alignment with the [CUI Policy](https://civicactions.atlassian.net/wiki/x/RoANJQ) .

## Incident Response and Contingency

Suspected data incidents (loss, exposure, mis-send, DLP block) must be reported immediately and handled under the IR Plan (NIST SP 800-61r3 aligned). Post-incident learning updates controls and documentation; contingencies follow the [Contingency Plan](https://guidebook.civicactions.com/en/latest/common-practices-tools/security/contingency-plan/) .

## Governance, Evidence and Continuous Improvement

This policy implements NIST CSF 2.0 outcomes, including Govern, Identify, Protect, Detect, Response, and Recover. Evidence includes:

- classification attestations
- DLP configs
- encryption posture
- backup tests
- sanitization certificates
- vendor reviews

ITIL 4 continual improvement: track DLP incidents, restore test success, time-to-revoke access, % managed endpoints, and close POA&amp;Ms via the improvement register.

Risk exceptions are managed per risk policy, with explicit owner, compensating controls, and review dates.

# Compliance and Enforcement

Violations may result in remedial actions up to and including access revocation, disciplinary action, or contract remedies. Sanctions follow PeopleOps processes and applicable standards.

# Training

- Onboarding (30 days): Users and managers receive training on Classification &amp; labeling, approved channels, encryption basics/FIPS for CUI, DLP behaviors, secure dev/test data, remote media sanitization, incident reporting.
- Annual refresher: role-based refreshers for Data/System Owners and engineers handling CUI, sales/contract team members handling FCI.

# Review

This policy is reviewed annually by the CISO and the Document Controller. Ad-hoc reviews may take place upon major legal and/or technical changes. Changes, reviews, and approvals are recorded in Confluence and Jira, following the [Document and Records Control Policy](https://civicactions.atlassian.net/wiki/x/AYCQCw) .

# Exceptions

Exceptions for this policy are rare and time-boxed. Exceptions must include business justification, compensating controls, and risk assessment. Exceptions require approval by CISO (and CEO/CTO if residual risk is High). All exceptions are logged in the Risk Register (Jira), and reviewed at least quarterly.

Document generated by Confluence on Mar 18, 2026 09:50

[Atlassian](http://www.atlassian.com/)