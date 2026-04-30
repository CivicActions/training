# Vulnerability and Patch Management Policy — Training Outcomes

Source: [Vulnerability and Patch Management Policy](../policies/Vulnerability-and-Patch-Management-Policy_768344065.md)

| Policy | Section | Learning Outcome | Audience |
|--------|---------|-----------------|----------|
| VPM | Discovery and Cadence | Describe the discovery methods for each asset type: MDM/EDR for endpoints, SBOMs + SCA/SAST/DAST for custom software, vendor security advisories for SaaS dependencies, and approved lists for browser/IDE/SaaS extensions | IT / Service Desk; Developers; System/Data Owners |
| VPM | Prioritization | Prioritize vulnerabilities using severity and exploitability signals, then incorporate service criticality and data sensitivity; confirm applicability before assigning remediation targets | IT / Service Desk; Developers; System/Data Owners |
| VPM | Remediation Targets | State the remediation timelines: Critical (15 days), High (30 days), Medium (60 days), Low (best effort); explain that timelines may tighten during active exploitation and that exceptions require CISO approval | IT / Service Desk; Developers; System/Data Owners |
| VPM | Policy Awareness | Know that the Vulnerability and Patch Management Policy exists and is managed by IT; anti-malware and patching are enforced automatically via MDM; if you notice unusual system behavior or a suspected vulnerability, raise a flag in Slack #general, DM an IT team member or your manager, or email security@civicactions.com | All Staff |
| VPM | Testing and Deployment Integration | Use staged deployment groups in MDM (alpha, beta, company-wide) for endpoint patches; treat patch waves as Standard changes within maintenance windows; validate SaaS configuration changes in test/staging tenants where available | IT / Service Desk; Developers |
| VPM | Verification and Evidence | Verify fixes through re-scan or functional validation; attach evidence to the ticket; maintain reports and tickets as Controlled Records | IT / Service Desk; Developers; System/Data Owners |
