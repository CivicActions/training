# Configuration Management Policy — Training Outcomes

Source: [Configuration Management Policy](../policies/Configuration-Management-Policy_767983618.md)

| Policy | Section | Learning Outcome | Audience |
|--------|---------|-----------------|----------|
| CMP | Configurable Item Scope and Granularity | Identify the five CI classes under formal configuration control (CIA "High" systems, managed endpoints, cloud resources, production SaaS configs, critical documentation); determine whether a given component falls under configuration management | IT / Service Desk; Developers; System/Data Owners |
| CMP | CMDB Architecture and Tooling | Explain that configuration-as-code in Git is the authoritative baseline; Git history is the change history; Jira/Confluence links service asset records to repos and pipelines; know that when config cannot be managed as code, change tickets capture before/after state | IT / Service Desk; Developers |
| CMP | Baselines and Secure Defaults | Apply least functionality in baselines (remove non-essential services/components); include hardening guidance, identity/access parameters, logging, and monitoring hooks; know that baselines are reviewed at least annually | IT / Service Desk; Developers; System/Data Owners |
| CMP | Change Governance and Traceability | Ensure peer review on pull/merge requests is mandatory for CIA "High" systems; run automated policy checks, tests, and scans in pipelines; trace every deployed change to an approved change record and CI record | IT / Service Desk; Developers |
| CMP | Continuous Verification and Drift Management | Understand that automated drift detection generates tickets triaged within two business days; resolve drift by reconciling to baseline or raising a change request | IT / Service Desk; Developers; System/Data Owners |
| CMP | Evidence and Audit | Retain CI inventories, baseline definitions, change histories, drift reports, and approvals as Controlled Records subject to the Document and Record Control Policy | IT / Service Desk; System/Data Owners |
