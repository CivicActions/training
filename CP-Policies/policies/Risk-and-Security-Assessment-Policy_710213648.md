# Policies : Risk and Security Assessment Policy

Created by Owen Barton , last modified by Sammy De La O on Dec 23, 2025

[https://civicactions.atlassian.net/browse/CPDOC-33?atlOrigin=eyJpIjoiYTgzYWE0ZjM4YWQ2NGI2NDk4MTk5OTJmNDhmYWUxYWQiLCJwIjoiaiJ9](https://civicactions.atlassian.net/browse/CPDOC-33?atlOrigin=eyJpIjoiYTgzYWE0ZjM4YWQ2NGI2NDk4MTk5OTJmNDhmYWUxYWQiLCJwIjoiaiJ9)

# Purpose

The purpose of this policy is to establish a standard process to identify, analyze, treat, and monitor security risks across CivicActions. This policy helps CivicActions leadership to a proactive approach to risk management, identifying threats to the organization, and manage risks in compliance with leadership, client, contractual, and regulatory requirements.

# Scope

This policy applies to all CivicActions team members, contractors, and third-party partners and vendors. This policy covers CivicActions-managed systems, services, and processes, including: :

- CivicActions internal policies, training, and cloud services
- Our remote-first workforce, including managed devices and endpoints
- Vendors and partners, following the [3rd Party Management Policy](https://civicactions.atlassian.net/wiki/x/DoBtL) for our supply-chain risk management practices

This policy does not apply to client-project systems or client-specific processes. Client-specific environments and processes follow the client's risk management policies and procedures. Processes on handling client data within CivicActions systems may fall under this policy.

External requirements, such as CUI/FCI handling, client-required incident response, business contingency planning, and document control requirements, are governed by separate policies but are aligned with this policy.

# Roles and Responsibilities

- CEO ( Approver; Risk Owner ): Approves this policy. Accepts High residual risks on behalf of the organization; may delegate day-to-day approvals but retains ultimate accountability; CTO is backup.
- CISO (Policy Owner): Owns the ISMS risk process; maintains this policy; ensures integration with NIST CSF Govern/Identify functions; oversees risk reporting and metrics.
- Compliance Lead (RMF Coordinator): Leads/coordinates enterprise RA cadence; maintains the Risk Register and POA&amp;M in Jira; facilitates assessments and evidence capture; ensures Controlled Document compliance.
- CTO: Ensures DevSecOps integration, secure baselines on managed endpoints/cloud, and automation of control verification.
- System Owners / Department Leads: Identify risks in their domains; ensure accurate asset/data inventories and control implementation; own local risk treatments; accept Low residual risks with CISO concurrence.
- Vendor Managers / Procurement: Perform supplier risk screening and ongoing monitoring per [Partner Management Policy](https://civicactions.atlassian.net/wiki/x/DoBtL) ; record supply-chain risks in the Risk Register.
- Team Members: Participate in risk identification, comply with controls on managed devices and services, and report issues or incidents promptly.
- Document Controller: Controls this policy in Confluence/Jira per Controlled Documents policy.

# Definitions

- Risk Assessment (RA): Process to identify threats, vulnerabilities, impact, and likelihood for assets within a defined scope, per NIST SP 800-30
- Risk Treatment: A response to an identified risk: Remediate, Mitigate, Accept, Transfer, or Avoid. "Ignore" is not an accepted option
- Residual Risk: Risk remaining after treatment, which is subject either to another risk assessment or treatment
- Risk Appetite: The degree of risk CivicActions is willing to tolerate to pursue objectives, decided by CivicActions leadership
- Risk Register: The structured log or database used to track and manage risks identified during a risk assessment, and their status
- POA&amp;M: Plan of Action and Milestones-tickets tracking agreed mitigations to closure
- Endpoints: CivicActions-managed systems, BYOD systems used for CivicActions work, and government furnished equipment (GFE) systems
- Remote-First: Full workforce is remote-based and no central physical location for any systems or personnel

# References

- ISO/IEC 27001:2022: 6.1.2 (Information security risk assessment), 6.1.3 (Information security risk treatment/SoA).
- ISO 9001:2015: 6.1 (Actions to address risks and opportunities).
- NIST SP 800-171 Rev. 3: 03.11.02 (Vulnerability Scanning), 03.12.01 (Security Assessment), 03.12.02 (Plan of Action and Milestones).
- NIST SP 800-30 Rev. 1: Guide for Conducting Risk Assessments.
- NIST SP 800-37 R2: Risk Management Framework (RMF).
- NIST Cybersecurity Framework 2.0: Govern, Identify Functions.
- Internal: Partner &amp; Third-Party Management Policy (for vendor risk incorporation).

# Policy

## Governance and Ownership

### **Authority and Method**

CivicActions manages cybersecurity risk following the guidelines provided in the NIST SP 800-30 "Guide for Conducting Risk Assessments" and the NIST Cybersecurity Framework (CSF) 2.0 for enterprise risk governance and communication.

### **Risk Ownership**

The CEO is the final authority to accept High residual risks, and the CTO serves as backup risk owner. The CISO owns process integrity, and escalates risks exceeding tolerance.

### **Documentation Control**

This policy, as well as all documentation related to a risk assessment and management (records produced from this policy) are Controlled Documents/Records. This includes versioning, approvals, and retention follow the [Document and Records Control Policy](https://civicactions.atlassian.net/wiki/x/AYCQCw) .

## Methodology

This policy is based on the [NIST SP 800-30 "Guide for Conducting Risk Assessment"](https://csrc.nist.gov/pubs/sp/800/30/r1/final) . CivicActions will perform risk assessments that:

- Define scope, assumptions, constraints, and information sources
- Identify assets, threats, vulnerabilities, predisposing conditions, and existing controls
- Rate Impact and Likelihood using Low/Medium/High scales; determine Inherent and Residual risk
- Recommend treatments and capture results in the Risk Register and linked POA&amp;M tickets

## Assessing Impact

Before performing a risk assessment, the level of impact for a system needs to be identified and documented. CivicActions will use the Confidentiality, Integrity, and Availability (CIA) matrix to determine the level.

CIA rating is a 3x3 matrix (CIA category x impact level to determine the impact the system has, and can be used to determine the impact (or importance) a system has for CivicActions.

| **CIA Rating**                                                                                                          | **Low**                                                                                                   | **Medium**                                                                                                      | **High**                                                                                                                   |
|-------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| **Confidentiality** Protecting information from unauthorized access or disclosure, including personal and company data. | Unauthorized disclosure would have a minor impact on the organization or individuals.                     | Unauthorized disclosure would have a significant impact on the organization or individuals.                     | Unauthorized disclosure would have a severe or catastrophic impact on the organization or individuals.                     |
| **Integrity** Ensuring information is accurate, complete, and protected from unauthorized changes or destruction.       | Unauthorized changes or loss of information would have a minor impact on the organization or individuals. | Unauthorized changes or loss of information would have a significant impact on the organization or individuals. | Unauthorized changes or loss of information would have a severe or catastrophic impact on the organization or individuals. |
| **Availability** Ensuring information and systems are accessible and usable when needed.                                | A disruption to access or use would have a minor impact on the organization or individuals.               | A disruption to access or use would have a significant impact on the organization or individuals.               | A disruption to access or use would have a severe or catastrophic impact on the organization or individuals.               |

Additional measurements, such as CIAX ("X" being a factor measuring based on cost/expense) is further expanded on in the [Third-Party Management Policy](https://civicactions.atlassian.net/wiki/x/DoBtL) .

The CIA rating from the matrix for for subscriptions/services are stored in Jira assets. For internal hosted systems CIA ratting will be stored in GitLab, either by adding topic tags or a YAML file in the repo root.  All systems and services will be reviewed on an annual bases by CTO, CISO, and IT. Additionally, any significant change to critical system will require a review of its CIA rating.

## Qualitative Risk Scales

Risk determination uses a 3×3 matrix (Impact × Likelihood) to classify risk Low/Medium/High and to trigger required actions.

- Impact:
    - Low: Limited operational or compliance effect; negligible cost/reputation harm
    - Medium: Noticeable service, legal, or client trust impact; moderate cost/effort to recover
    - High: Significant mission/client harm, statutory/contractual breach, or sustained outage
- Likelihood:
    - Low: Unlikely given controls and exposure
    - Medium: Credible threat with periodic exposure or partial controls
    - High: Probable/ongoing activity or systemic control gaps

| **Risk Determination**   | **Low Likelihood**   | **Medium Likelihood**   | **High Likelihood**   |
|--------------------------|----------------------|-------------------------|-----------------------|
| **Low Impact**           | Low Risk             | Low Risk                | Medium Risk           |
| **Medium Impact**        | Low Risk             | Medium Risk             | High Risk             |
| **High Impact**          | Medium Risk          | High Risk               | High Risk             |

## Scope and Cadence

### Enterprise Risk Assessment

The Compliance Lead coordinates an annual organization-level risk assessment covering policy library and implementation (including training), internal cloud services and platforms, vendors, and personnel/endpoint environment.

### System Assessments and Continuous Verification

Individual systems aim for automated, continuous compliance (e.g., pipeline checks, configuration drift detection) with at least annual assessments. Systems rated **High** criticality receive quarterly health checks.

### Ad-hoc Triggers

Conduct an risk assessment when any of the following occur:

- Major change to a High system, or change of vendor/core software
- New client contract imposing new compliance obligations
- Major security incident or material change in service delivery model
- Material supply-chain event (e.g., upstream breach, licensing change)

### Project Systems

Client systems and client-specific processes are managed under the client's frameworks; this policy applies to CivicActions enterprise risk only.

## Risk Appetite and Criteria

CivicActions is moderately risk-tolerant: we will avoid significant risks but preserve the ability to innovate. Required actions by residual risk level:

- High ( *OR* Medium-Impact with High Likelihood): Formal action required and mitigation plan; CEO (or CTO) approval to accept residual risk; POA&amp;M tickets created and tracked to closure
- Medium: Mitigate or transfer; CISO may accept if within tolerance and supported by compensating controls &amp; business justification
- Low: May be accepted by System Owner with CISO concurrence and documented rationale. "Ignore" is prohibited; inability or unwillingness to resource mitigation is not an acceptance rationale

## Treatment Options &amp; Authority

- Remediate: Permanently eliminate the root cause (patch, secure configuration, code or architectural change) rather than rely on compensating controls; required when a safe, feasible fix exists. Verify via retest/scan and close in POA&amp;M/change record.
- Mitigate: Implement controls to reduce impact and/or likelihood. Required when a feasible fix exists and cost/benefit is reasonable, or risk affects parties beyond the system boundary.
- Accept: Allowed for Low and some Medium residual risks with documented reasoning, time-bound review, and leadership concurrence.
- Transfer: Shift risk to another responsible party (for example, cloud/SaaS provider); ensure contract clauses and equivalency (e.g., FedRAMP Moderate equivalence for CUI CSPs).
- Avoid: Discontinue or postpone the risky activity/service when mitigation is disproportionate or ineffective.

All accepted/transfer residual risks must have an explicit approver, review date, and monitoring plan in the Risk Register .

## Risk Register and POA&amp;M

- System of Record: The Risk Register is maintained in a dedicated Jira project " [Continual Improvement](https://civicactions.atlassian.net/jira/core/projects/CPCIM/board?filter=&groupBy=status) ". The Jira board will have a ticket type "Risk Mitigation" and will follow the Jira board workflow. A combination of fields and ticket status will cover the risk status.
- The fields required to document for risk activities are:
    - A title to describe the nature of the risk
    - A summary with detail and context in the Description field
    - Asset/Process and Data type (e.g., FCI/CUI/PII)
    - Owner, reviewer and/or approver
    - Due date
- Information that can be added but not always required include:
    - Threats and vulnerabilities
    - Predisposing conditions and existing controls
    - Preliminary impact and likelihood (inherent &amp; residual)
    - Evidence links, dependencies, related incident(s)
- POA&amp;M Tracking: Required treatments are represented as Activity ticket or Process Improvement sub-type tickets on the Continuous Improvement Jira board ; each treatment includes milestones, owners, due dates, and closure evidence.
- [Maintenance Policy](https://civicactions.atlassian.net/wiki/x/AwBmL) : Any treatments will align and follow any requirements from the Maintenance Policy for CivicActions systems. This includes:
    - [Change Enablement Policy](https://civicactions.atlassian.net/wiki/x/AYDILQ) - Treatments will need a change plan, following this policy.
    - [Configuration Management Policy](https://civicactions.atlassian.net/wiki/x/AoDGLQ) - Treatments will not go against established baselines. If any baseline configurations need to be updated and deployed across all systems, the treatment will need to follow the process outlined in this policy.
    - [Vulnerability and Patch Management Policy](https://civicactions.atlassian.net/wiki/x/AQDMLQ) - Risks will take into account external source ratings for risks based on impact and likelihood of threat to CivicActions. Risk assessment and treatments will categorize the level of risk based on these factors and additional guidance from this policy.

## Integration with DevSecOps, SRE &amp; ITSM

- Shift-Left &amp; Automation: Embed risk checks in CI/CD ( SCA/SAST/IaC policies ), golden images/baselines, and drift detection; enable developers/ops to self-serve risk information and remediations.
- Signals &amp; Telemetry: Monitoring and event management must generate signals (errors, vulnerabilities, misconfigurations) that inform creation and management of risks and POA&amp;Ms.
- Blameless Learning: Post-incident reviews must update the Risk Register and treatment plans ; tie to NIST SP 800-61r3 guidance.
- Continual Improvement: Opportunities for continual improvement will be captured in the Continual Improvement Jira board. This includes corrective and preventive actions, feedback loops, and new risks and treatments. These activities will help to re-prioritize risks and confirm value of treatments.
- Reliability &amp; Security Together: Follow SRE practices-least privilege, zero-trust posture, rollback safety, and blast-radius control-as preferred mitigations.

## Remote-First and Endpoints

Risk assessments must account for distributed endpoints, home networks, travel, and company-managed device baselines. Exceptions to managed devices require time-bound approval and equivalent safeguards. Network and remote access risks are in scope.

## Data Classification and Security

Sensitive data (confidential or restricted) risks must ensure data remains within approved boundaries and align with [Data Security and Handling Policy](https://civicactions.atlassian.net/wiki/x/HgBVKg) . Client-sensitive data risks, such as FCI/CUI, must align with the [CUI Policy](https://civicactions.atlassian.net/wiki/x/RoANJQ) and client-specific requirements.

## Third-Party Management

Vendor onboarding and annual reviews must include cybersecurity and risk assessment , contract obligations for incident reporting, and assurance of control equivalency for hosted data. The initial cybersecurity assessment is managed by the [Third-Party Management Policy](745373710.html) . All identified supplier and third-party vendor risks are recorded and tracked in the Risk Registrar.

## Reporting and Metrics

- Quarterly to ELT: Top risks (heat map), risk movements, control effectiveness trends, and POA&amp;M status; include supply-chain and regulatory posture
- Annually: Enterprise Risk &amp; Security Assessment report (inputs to Management Review for the QMS)

# Compliance and Enforcement

Violations may result in remedial actions up to and including access revocation, disciplinary action, or contract remedies. Sanctions follow PeopleOps processes and applicable standards.

# Training

- Onboarding (30 days): Users and managers receive training on CivicActions risk process , examples of risks in remote-first operations, CUI/FCI handling, how to create and update Risk/POA&amp;M tickets, and how to use pipeline/tooling signals.
- Annual refresher: Updates to the policy, review risk process, and review recent examples of risk analysis.

# Review

This policy is reviewed annually by the CISO and the Document Controller. Ad-hoc reviews may take place upon major legal and/or technical changes. Changes, reviews, and approvals are recorded in Confluence and Jira, following the [Document and Records Control Policy](https://civicactions.atlassian.net/wiki/x/AYCQCw) .

# Exceptions

Exceptions for this policy are rare and time-boxed. Exceptions must include business justification, compensating controls, and risk assessment. Exceptions require approval by CISO (and CEO/CTO if residual risk is High). All exceptions are logged in the Risk Register (Jira), and reviewed at least quarterly.

## Attachments:

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[Screenshot 2025-10-07 at 10.08.44 AM.png](attachments/710213648/730464263.png)

(image/png)

Document generated by Confluence on Mar 18, 2026 09:50

[Atlassian](http://www.atlassian.com/)