# Third-Party Management Policy — Training Outcomes

Source: [Third-Party Management Policy](../policies/745373710.md)

| Policy | Section | Learning Outcome | Audience |
|--------|---------|-----------------|----------|
| TPM | Governance and Program Structure | Explain the three C-SCRM tracks (SCRM-DS for digital services, SCRM-S for software, SCRM-PS for professional services); understand that supplier risk is recorded in the Risk Register with POA&Ms | Managers; IT / Service Desk; System/Data Owners |
| TPM | Risk Tiering and Categorization | Describe how suppliers are risk-tiered at intake: CIAX scoring for SaaS, security posture/SBOM for software, and access/criticality/regulatory scope for professional services; identify the three tiers (Low/Medium/High) | Managers; IT / Service Desk; System/Data Owners |
| TPM | Mandatory Due Diligence — All Suppliers | Understand that no supplier may be procured, deployed, or granted access until tier-appropriate due diligence is complete (intake form, evidence review, security questionnaire) | All Staff |
| TPM | Mandatory Due Diligence — Digital Services | Explain the SCRM-DS process: CIAX scoring, SSO/MFA validation, data region and encryption review, exit strategy, FedRAMP requirement for CUI; know that OAuth app registrations are monitored to detect unapproved services | IT / Service Desk; System/Data Owners |
| TPM | Mandatory Due Diligence — Software | Explain the SCRM-S process: SBOM required at intake, SCA in CI/CD feeding Dependency-Track, remediate Critical/High before release, replace unmaintained components (no updates >1 year) | Developers; IT / Service Desk |
| TPM | Mandatory Due Diligence — Professional Services | Explain the SCRM-PS process: partner criteria (legal review, background checks, certifications), CMMC level verification for FCI/CUI work, DFARS flow-down to sub-tier suppliers | Managers; System/Data Owners |
| TPM | Contracting and Required Security Clauses | Identify the required contract clauses: confidentiality, least-privilege, encryption, MFA, incident reporting (within 24 hours), right to audit, federal flow-down (FAR/DFARS for FCI/CUI), change notification, exit/data destruction | Managers; IT / Service Desk; System/Data Owners |
| TPM | Monitoring, Reviews, and Continuous Improvement | Describe the review cadence by tier: annual for Low/Medium, semi-annual for High SaaS; CI/CD-enforced SBOM refresh for software; annual PM-led review for professional services; identify ad-hoc triggers (incidents, scope changes, new data classes) | Managers; IT / Service Desk; System/Data Owners |
| TPM | Open-Source Software (FOSS) | Treat FOSS libraries and containers as suppliers: require SBOMs, triage known vulnerabilities, verify license compliance, assess maintainer health; isolate or replace high-risk/unmaintained components | Developers |
| TPM | Prohibited and Restricted Technologies | Screen against the prohibited technology list and DFARS restrictions during intake and annual reviews | IT / Service Desk; Managers |
| TPM | Access and Identity Alignment | Ensure partners use SSO where available, enforce MFA for admin access, prohibit shared accounts; scope and rotate non-person identities per CivicActions standards | IT / Service Desk |
| TPM | Integration with Incident Response | Escalate supplier incidents or outages that may affect CivicActions data to Incident Response; follow shared responsibility model and contract SLAs for recovery | IT / Service Desk; System/Data Owners |
| TPM | Records and Evidence | Retain intake forms, tiering decisions, questionnaires, contract clauses, review results, POA&Ms, and exit attestations as Controlled Records | Managers; IT / Service Desk; System/Data Owners |
