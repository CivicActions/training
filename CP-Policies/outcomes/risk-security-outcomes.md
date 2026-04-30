# Risk and Security Assessment Policy — Training Outcomes

Source: [Risk and Security Assessment Policy](../policies/Risk-and-Security-Assessment-Policy_710213648.md)

| Policy | Section | Learning Outcome | Audience |
|--------|---------|-----------------|----------|
| RSAP | Governance — Authority and Method | Explain that CivicActions follows NIST SP 800-30 and NIST CSF 2.0 for risk management; identify the CEO as final risk owner and the CISO as process owner | All Staff |
| RSAP | Governance — Risk Ownership | Identify who approves High residual risks (CEO/CTO) and who may accept Low risks (System Owners with CISO concurrence); understand that "Ignore" is never an accepted treatment | All Staff; System/Data Owners (deeper) |
| RSAP | Governance — Documentation Control | Understand that all risk assessment documentation is Controlled Records subject to the Document and Records Control Policy | All Staff |
| RSAP | Methodology | Describe the four steps of a risk assessment: define scope, identify assets/threats/vulnerabilities, rate impact and likelihood, and recommend treatments | Managers; System/Data Owners; IT / Service Desk |
| RSAP | Assessing Impact (CIA Matrix) | Use the CIA matrix (Confidentiality, Integrity, Availability × Low/Medium/High) to rate system impact; know where CIA ratings are stored (Jira assets for subscriptions/services, GitLab for internal systems) | System/Data Owners; IT / Service Desk |
| RSAP | Qualitative Risk Scales | Apply the 3×3 risk matrix (Impact × Likelihood) to classify risks as Low, Medium, or High; describe what each level means and the required response | All Staff; System/Data Owners (deeper) |
| RSAP | Scope and Cadence — Enterprise RA | Understand that an annual enterprise risk assessment covers the policy library, cloud services, vendors, and personnel/endpoint environment | All Staff |
| RSAP | Scope and Cadence — System Assessments | Explain that individual systems aim for continuous automated compliance with at least annual assessments; High-criticality systems receive quarterly health checks | System/Data Owners; IT / Service Desk |
| RSAP | Scope and Cadence — Ad-hoc Triggers | Identify the four triggers for ad-hoc risk assessments: major change to a High system, new compliance obligations, major incident, or material supply-chain event | Managers; System/Data Owners |
| RSAP | Risk Appetite and Criteria | State CivicActions' risk appetite (moderately risk-tolerant); describe the required actions at each residual risk level (High: CEO approval + POA&M, Medium: mitigate/transfer with CISO acceptance, Low: System Owner acceptance with CISO concurrence) | All Staff; System/Data Owners (deeper) |
| RSAP | Treatment Options and Authority | Distinguish five treatment options (Remediate, Mitigate, Accept, Transfer, Avoid); explain that remediation is preferred when a safe, feasible fix exists; identify the approval authority for each risk level | Managers; System/Data Owners; IT / Service Desk |
| RSAP | Risk Register and POA&M | Create and update Risk Register entries in the Jira Continual Improvement project with required fields (title, description, asset/data type, owner, due date); track treatments as POA&M tickets to closure | Managers; System/Data Owners; IT / Service Desk |
| RSAP | Integration with DevSecOps, SRE & ITSM | Embed risk checks in CI/CD (SCA/SAST/IaC); use monitoring signals to inform risk creation; apply blameless post-incident reviews to update the Risk Register; capture improvement opportunities in the Continual Improvement board | Developers; IT / Service Desk |
| RSAP | Remote-First and Endpoints | Account for distributed endpoints, home networks, and travel in risk assessments; understand that managed-device exceptions require time-bound approval and equivalent safeguards | All Staff |
| RSAP | Data Classification and Security | Ensure sensitive data risks keep data within approved boundaries per the Data Security and Handling Policy; align client-sensitive data (FCI/CUI) risks with the CUI Policy | All Staff working with CUI; System/Data Owners |
| RSAP | Third-Party Management | Include cybersecurity and risk assessment in vendor onboarding and annual reviews; record supplier risks in the Risk Register | Managers; System/Data Owners |
| RSAP | Reporting and Metrics | Understand that risk reporting occurs quarterly to ELT (heat map, risk movements, POA&M status) and annually for the enterprise risk assessment | Managers; System/Data Owners |
| RSAP | Compliance and Enforcement | Understand that violations can result in access revocation, disciplinary action, or contract remedies | All Staff |
