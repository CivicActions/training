# Policies : Physical Security Policy

Created by Owen Barton , last modified by Sammy De La O on Dec 23, 2025

[https://civicactions.atlassian.net/browse/CPDOC-39?atlOrigin=eyJpIjoiNDQyNTNlYjc3ZGY1NGEyYTg1YTY3ZThlMjQ0NDI1MTgiLCJwIjoiaiJ9](https://civicactions.atlassian.net/browse/CPDOC-39?atlOrigin=eyJpIjoiNDQyNTNlYjc3ZGY1NGEyYTg1YTY3ZThlMjQ0NDI1MTgiLCJwIjoiaiJ9)

# Purpose

The purpose of this policy is to provide guidelines for physical and environmental security measures for CivicActions environment. CivicActions is a remote-first workforce, with no physical or centrally-owned location. Therefore, this policy focuses on securing home workspaces and travel environments for team members.

# Scope

This policy applies to all CivicActions Team Members, contractors, and third parties who handle CivicActions or client information, on CivicActions-managed devices and approved services, in:

- Designated home work areas
- Temporary locations while traveling (for example, client sites, coworking, hotels)
- Any future CivicActions-controlled space or co-location facility

CivicActions does not currently operate offices or data centers; this policy focuses on remote/home and travel use. For policies and procedures on changing between a set home location, a location outside of their home, a location outside of one's municipality, or a location outside of the state or country, see the [Work Location Policy](https://civicactions.atlassian.net/wiki/x/AgBkI) .

# Roles and Responsibilities

- CEO and CTO (Approvers): Approve this policy and resource the managed-device baseline
- CISO (Policy Owner): Maintains the policy; aligns controls to NIST CSF/ISO; ensures metrics and audits; owns exceptions
- IT / Service Desk: Operates MDM baselines (for example, full-disk encryption, screen-lock, remote wipe); supports remote media sanitization workflows
- Managers and Project Leads: Reinforce expectations with their teams; ensure travel plans and work locations follow this policy
- Team Members: Follow the rules in this policy, keep devices under control, lock screens when away, minimize printing, and report lost or stolen assets immediately
- Document Controller (Compliance): Controls this Controlled Document in Confluence and tracks approvals, versioning, and change history

# Definitions

- Alternate Work Site: The Team Member's home or any non-CivicActions facility used for work
- Managed Device: A CivicActions-managed endpoint under MDM with enforced baseline
- FCI/CUI: Federal Contract Information / Controlled Unclassified Information
- Sensitive information: Internal, Confidential, or Restricted data, as defined by [Data Security and Handling Policy](https://civicactions.atlassian.net/wiki/x/HgBVKg)

# References

- FAR Clause 52.204-21: b.1.viii (Limit physical access), b.1.ix (Control/monitor physical access).
- NIST SP 800-171 Rev. 3: 03.10 (Physical and Environmental Protection).
- CMMC Assessment Guide L2 v2.13: PE.L2-3.10.3 (Visitor controls), PE.L2-3.10.5 (Alternate work sites).
- ISO/IEC 27002:2022: 6.7 (Remote working), 7.1-7.9 (Physical and environmental controls, including Clear Desk/Screen).
- Internal: Incident Response Policy, Contingency Plan.

# Policy

## Overview and Principles

- Remote-first and minimal: CivicActions relies on managed devices, encryption in transit, and simple habits in place of costly physical controls. Controls are designed to be achievable without Team Member expense or special equipment.
- Baselines by technology: Managed devices enforce full-disk encryption, auto-lock, and remote wipe; Team Members still have duties in the moments when technology cannot act (for example, stepping away from a screen).

## Home Workspace Minimums

CivicActions sets a small set of must-dos for designated home work areas that applies to all team members:

- Control Visibility: Position screens to avoid casual viewing by others, or wait to work on sensitive information until you are in a more private location.
- Secure Printed Material: Do not print sensitive information unless you have confirmed access to a secure printer (where you are present at time of printing) and secure disposal method. If you must print, keep it out of sight when unattended and shred as soon as practical the same day using cross-cut shredder.
- Keep Devices Under Your Control: Do not leave company devices unattended in shared spaces. When you step away at home, lock the screen; if others are present, close the lid or store the laptop out of sight.
- Environmental Care: Protect devices from spills, extreme heat/cold, and smoke/fire risks, and use a surge-protected outlet when practical.

## Networks and Wi-Fi at Home

- Use encrypted Wi-Fi with a password, or wired Ethernet.
- Strongly recommended: WPA2 or WPA3 and a non-default router admin password.
- All connections to CivicActions systems must be end-to-end encrypted; do not bypass TLS warnings.

CivicActions intentionally keeps these to essentials. If you cannot meet them in a location, use a personal hotspot or relocate.

## Visitors and Working Around Others

- Avoid sensitive conversations if unauthorized people are present. Use a headset for calls.
- Avoid working on sensitive information if others can see your screen.
- If anyone you do not live with will be in your work area (for example, a contractor), lock the device and put sensitive papers away.

## Travel and Public Locations

- Keep the device with you or in a physically secure location.
- Manually lock your screen or power down whenever you are not present.
- Work so others cannot read your screen if working on sensitive information. Move, rotate, or choose seating to reduce visibility.
- Use encrypted Wi-Fi or a personal hotspot. Do not use public WiFi.
- Do not print sensitive material while traveling unless required and you have a plan to secure and destroy it promptly.

## Paper, Removable Media, and End-of-Life

- Printing: Avoid by default. If printed, secure and shred the same day.
- Removable media: Avoid using USB storage for sensitive data. If used for client reasons, encrypt and track per project instruction.
- Sanitization and disposal: Media and devices must be sanitized or destroyed before reuse or disposal, consistent with NIST SP 800-88 methods. CivicActions provides remote wipe and ITAD processes with chain-of-custody and certificates; Team Members must follow the provided instructions for any mail-in or return kits.

## Lost, Stolen, or Physically Compromised Assets

- Report immediately using the channels in the Incident Response Plan (for example, the designated security contact or incident intake).
- Include what happened, when and where, which asset, and any suspected exposure of printed materials.
- This applies to both CivicActions Laptops, as well as any personal devices that authenticated to CivicActions systems or contain CivicActions data.
- Securit y will initiate containment (for example, remote lock or wipe) and coordinate any notifications. Reporting is blame-free and expected.

## Future CivicActions Facilities, Co-Locations, and Client Spaces

If CivicActions establishes a facility or uses co-location space, or when operating inside a client facility, the following will apply at that location:

- Physical access authorization and control, visitor logs and escorts, and monitoring of access to secure areas
- Environmental protections for power, fire, and HVAC, and defined security perimeters
- Quarterly access reviews for secure areas and management of keys and badges

## Evidence, Monitoring, and Continual Improvement

- Evidence: MDM posture (encryption, auto-lock), remote wipe records, incident reports, and ITAD certificates serve as evidence for audits.
- Metrics: Time to report lost assets, successful remote wipes, and closure of destruction records are reviewed with the ISMS.
- Improvement: Post-incident reviews are blameless and feed improvements to this policy and supporting procedures, consistent with SRE and ISO PDCA practices.

# Compliance and Enforcement

Violations may result in remedial actions up to and including access revocation, disciplinary action, or contract remedies. Sanctions follow PeopleOps processes and applicable standards.

# Training

- Onboarding (30 days): Users receive training emphasizes remote/home setup, locking screens, minimal printing, handling visitors, and how to report a lost device.
- Annual refresher: Updated expectations, updated to list of risks and threats, and additional security controls. Records are maintained per the Controlled Documents Policy .

# Review

This policy is reviewed annually by the CISO and the Document Controller. Ad-hoc reviews may take place upon major legal and/or technical changes. Changes, reviews, and approvals are recorded in Confluence and Jira, following the [Document and Records Control Policy](https://civicactions.atlassian.net/wiki/x/AYCQCw) .

# Exceptions

Exceptions for this policy are rare and time-boxed. Exceptions must include business justification, compensating controls, and risk assessment. Exceptions require approval by CISO (and CEO/CTO if residual risk is High). All exceptions are logged in the Risk Register (Jira), and reviewed at least quarterly.

Document generated by Confluence on Mar 18, 2026 09:50

[Atlassian](http://www.atlassian.com/)