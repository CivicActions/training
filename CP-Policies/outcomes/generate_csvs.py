#!/usr/bin/env python3
"""Generate CSV and mapping MD files for all policy outcome tables."""
import csv
import os
import re
from collections import OrderedDict

BASE = os.path.dirname(os.path.abspath(__file__))

# Training names
T1 = "Training 1 \u2014 Security Awareness Essentials"
T2 = "Training 2 \u2014 CUI Awareness & Handling"
T3 = "Training 3 \u2014 IT Operations: Change, Configuration & Patch Management"
T4 = "Training 4 \u2014 Incident Response for Responders"
T5 = "Training 5 \u2014 Secure Development & Supply Chain"
T6 = "Training 6 \u2014 Access Governance, Risk & Supplier Oversight"

# Modules
T1A = "A - Your devices and workspace"
T1B = "B - Your identity and access"
T1C = "C - Data handling and classification"
T1D = "D - Acceptable use and AI"
T1E = "E - Recognizing and reporting incidents"
T1F = "F - Governance, risk, and compliance awareness"

T2A = "A - What is CUI and why it matters"
T2B = "B - The CUI Security Boundary"
T2C = "C - CUI handling rules"
T2D = "D - CUI document markings"

T3A = "A - Configuration management"
T3B = "B - Change enablement"
T3C = "C - Vulnerability and patch management"
T3D = "D - Endpoint posture and privileged access"
T3E = "E - Disaster recovery operations"

T4A = "A - IRP structure and phases"
T4B = "B - Evidence and forensics"
T4C = "C - Communications and escalation"
T4D = "D - Recovery and emergency changes"
T4E = "E - Post-incident learning"

T5A = "A - Secure engineering principles"
T5B = "B - AI-assisted development"
T5C = "C - Open-source and supply chain"
T5D = "D - Access and identity for developers"

T6A = "A - Access governance"
T6B = "B - Risk management responsibilities"
T6C = "C - Supplier and third-party oversight"
T6D = "D - Document and record control"
T6E = "E - AI governance for managers"

# (Policy, Section) -> (Training, Module)
MAPPING = {
    # Acceptable Use Policy (AUP)
    ("AUP", "Principles for Acceptable Use"): (T1, T1D),
    ("AUP", "Ownership, Privacy, and Monitoring"): (T1, T1D),
    ("AUP", "Authorized and Personal Use"): (T1, T1D),
    ("AUP", "Prohibited Activities"): (T1, T1D),
    ("AUP", "Devices \u2014 Company-Managed"): (T1, T1A),
    ("AUP", "Devices \u2014 BYOD"): (T1, T1A),
    ("AUP", "Home and Travel Workspaces"): (T1, T1A),
    ("AUP", "Data Handling and Sharing"): (T1, T1C),
    ("AUP", "Cloud, Social Media, and External Communications"): (T1, T1D),
    ("AUP", "Software Installation and Open-Source Use"): (T1, T1A),
    ("AUP", "Development, Automation, and Infrastructure"): (T5, T5A),
    ("AUP", "Generative AI and Code Assistants"): (T1, T1D),
    ("AUP", "Session Management and Authentication"): (T1, T1B),
    ("AUP", "Malware Protection and Downloads"): (T1, T1A),
    ("AUP", "Reporting Obligations"): (T1, T1E),
    ("AUP", "Consequences for Violations"): (T1, T1D),
    ("AUP", "Acknowledgment"): (T1, T1D),

    # Access Control Policy (ACP)
    ("ACP", "Intent and Principles"): (T1, T1B),
    ("ACP", "Identity and SSO"): (T1, T1B),
    ("ACP", "RBAC as Baseline"): (T1, T1B),
    ("ACP", "Segregation by Client/Project"): (T1, T1B),
    ("ACP", "Privileged Access Management"): (T3, T3D),
    ("ACP", "Non-Person Identities (NPIs)"): (T3, T3D),
    ("ACP", "Remote Access"): (T1, T1B),
    ("ACP", "Cloud and SaaS Governance"): (T6, T6A),
    ("ACP", "Endpoint Prerequisite"): (T1, T1B),
    ("ACP", "Physical Safeguards Linkage"): (T1, T1B),
    ("ACP", "Access Lifecycle \u2014 Request"): (T1, T1B),
    ("ACP", "Access Lifecycle \u2014 Approve"): (T6, T6A),
    ("ACP", "Access Lifecycle \u2014 Grant"): (T3, T3D),
    ("ACP", "Access Lifecycle \u2014 Review/Change"): (T6, T6A),
    ("ACP", "Access Lifecycle \u2014 Revoke"): (T6, T6A),
    ("ACP", "Periodic Access Reviews"): (T6, T6A),
    ("ACP", "Project Boundary and CUI Segregation"): (T2, T2B),
    ("ACP", "Data and Secrets Access"): (T1, T1C),
    ("ACP", "Logging, Monitoring, and Evidence"): (T3, T3D),
    ("ACP", "Emergency Access (Break-Glass)"): (T3, T3D),
    ("ACP", "Third-Party and Supplier Access"): (T6, T6C),
    ("ACP", "Critical Systems and Enforcement Mechanisms"): (T3, T3D),
    ("ACP", "Change Control and Configuration Alignment"): (T3, T3D),
    ("ACP", "Compliance and Enforcement"): (T1, T1F),

    # AI Usage Policy (AIP)
    ("AIP", "General Requirements"): (T1, T1D),
    ("AIP", "Usage in Software Development"): (T5, T5B),
    ("AIP", "Usage on Client Projects"): (T1, T1D),
    ("AIP", "Usage in Sales"): (T6, T6E),
    ("AIP", "Approved Generative AI Tools"): (T1, T1D),
    ("AIP", "AI Usage Approval"): (T6, T6E),
    ("AIP", "Usage in Professional Development"): (T1, T1D),

    # Change Enablement Policy (CEP)
    ("CEP", "Change Classes and Criteria"): (T3, T3B),
    ("CEP", "Required Content for Change Records"): (T3, T3B),
    ("CEP", "Approvals and Guardrails"): (T3, T3B),
    ("CEP", "Scheduling and Communication"): (T3, T3B),
    ("CEP", "Post-Implementation Review"): (T3, T3B),
    ("CEP", "Change Freezes"): (T3, T3B),

    # Configuration Management Policy (CMP)
    ("CMP", "Configurable Item Scope and Granularity"): (T3, T3A),
    ("CMP", "CMDB Architecture and Tooling"): (T3, T3A),
    ("CMP", "Baselines and Secure Defaults"): (T3, T3A),
    ("CMP", "Change Governance and Traceability"): (T3, T3A),
    ("CMP", "Continuous Verification and Drift Management"): (T3, T3A),
    ("CMP", "Evidence and Audit"): (T3, T3A),

    # CUI Policy
    ("CUI", "Overview"): (T2, T2A),
    ("CUI", "Safeguarding CUI"): (T2, T2B),
    ("CUI", "CUI Handling Guidelines"): (T2, T2C),
    ("CUI", "CUI Security Boundary"): (T2, T2B),
    ("CUI", "CUI Document Markings"): (T2, T2D),

    # Data Security and Handling Policy (DSHP)
    ("DSHP", "Data Classification and Labeling"): (T1, T1C),
    ("DSHP", "Data Classification \u2014 Labeling Requirements"): (T1, T1C),
    ("DSHP", "Data Classification \u2014 Data Minimization"): (T1, T1C),
    ("DSHP", "Data Classification \u2014 CUI"): (T2, T2C),
    ("DSHP", "Approved Locations and Boundaries"): (T1, T1C),
    ("DSHP", "Encryption Requirements \u2014 In Transit"): (T1, T1C),
    ("DSHP", "Encryption Requirements \u2014 At Rest"): (T1, T1C),
    ("DSHP", "Encryption Requirements \u2014 CUI Cryptography"): (T3, T3D),
    ("DSHP", "Encryption Requirements \u2014 Key Management"): (T3, T3D),
    ("DSHP", "Endpoints and Remote-First"): (T1, T1A),
    ("DSHP", "Software Development and Testing (DevSecOps)"): (T5, T5A),
    ("DSHP", "Sharing and Communication Channels"): (T1, T1C),
    ("DSHP", "Sharing \u2014 CUI Channels"): (T2, T2C),
    ("DSHP", "Data Loss Prevention (DLP) and Monitoring"): (T1, T1C),
    ("DSHP", "Removable Media and Printing"): (T1, T1C),
    ("DSHP", "Backup and Recovery"): (T1, T1C),
    ("DSHP", "Retention and Legal Holds"): (T1, T1C),
    ("DSHP", "Open Data and Public Release Controls"): (T1, T1C),
    ("DSHP", "Media Sanitization and Destruction"): (T6, T6A),
    ("DSHP", "Third-Party Management"): (T6, T6C),
    ("DSHP", "Incident Response and Contingency"): (T1, T1E),
    ("DSHP", "Governance, Evidence and Continuous Improvement"): (T3, T3D),
    ("DSHP", "Compliance and Enforcement"): (T1, T1C),

    # Disaster Recovery Plan (DRP)
    ("DRP", "Policy Awareness"): (T1, T1E),
    ("DRP", "Communication Plan"): (T1, T1E),
    ("DRP", "System-Specific Recovery"): (T3, T3E),
    ("DRP", "Backup and Data Protection"): (T3, T3E),
    ("DRP", "Testing and Maintenance"): (T3, T3E),
    ("DRP", "Post-Incident Review"): (T3, T3E),

    # Document and Record Control Policy (DRCP)
    ("DRCP", "Document Identification"): (T6, T6D),
    ("DRCP", "Document Classification"): (T6, T6D),
    ("DRCP", "Controlled Document Format"): (T6, T6D),
    ("DRCP", "Document Version Control"): (T6, T6D),
    ("DRCP", "Document Change Request Process"): (T1, T1F),
    ("DRCP", "Access Control and Security"): (T1, T1F),
    ("DRCP", "Document Training Requirements"): (T6, T6D),
    ("DRCP", "Document Review"): (T1, T1F),

    # Identification Policy (IdP)
    ("IdP", "Identity Foundations & Account Naming"): (T1, T1B),
    ("IdP", "SSO and Federation"): (T1, T1B),
    ("IdP", "Authentication Requirements (MFA)"): (T1, T1B),
    ("IdP", "Authentication Requirements \u2014 Passwordless Trajectory"): (T1, T1B),
    ("IdP", "Authenticator Issuance, Protection and Lifecycle"): (T1, T1B),
    ("IdP", "Authenticator Issuance \u2014 Admin Requirements"): (T3, T3D),
    ("IdP", "Session Management and Re-authentication"): (T1, T1B),
    ("IdP", "Managed Endpoints and Remote-First Alignment"): (T1, T1B),
    ("IdP", "Credentials and Secrets Hygiene"): (T1, T1B),
    ("IdP", "Non-Person Identities (NPIs)"): (T3, T3D),
    ("IdP", "Logging, Monitoring and Auditability"): (T3, T3D),
    ("IdP", "Identity Proofing \u2014 Onboarding"): (T1, T1B),
    ("IdP", "Identity Proofing \u2014 Role Changes"): (T1, T1B),
    ("IdP", "Identity Proofing \u2014 Offboarding"): (T6, T6A),
    ("IdP", "Incident Reporting & Response"): (T1, T1E),
    ("IdP", "Compliance and Enforcement"): (T1, T1F),

    # Incident Response Policy (IRP)
    ("IRP", "Policy Awareness"): (T1, T1E),
    ("IRP", "Report Quickly, Report Safely"): (T1, T1E),
    ("IRP", "Confidentiality and Post-Incident"): (T1, T1E),
    ("IRP", "Communications and Stakeholder Updates"): (T4, T4C),
    ("IRP", "Third-Party and Client Notifications"): (T4, T4C),
    ("IRP", "Evidence, Logging, and Forensics"): (T4, T4B),
    ("IRP", "Recovery Objectives and Emergency Change"): (T4, T4D),
    ("IRP", "Execution Model and IRP Phases"): (T4, T4A),
    ("IRP", "Post-Incident Learning and Risk Integration"): (T4, T4E),
    ("IRP", "Compliance and Enforcement"): (T4, T4E),

    # Information Security Policy (ISP)
    ("ISP", "Governance and Leadership Commitment"): (T1, T1F),
    ("ISP", "Security Objectives"): (T1, T1F),
    ("ISP", "Core Security Principles"): (T1, T1F),
    ("ISP", "Compliance Commitments"): (T1, T1F),
    ("ISP", "Delegation to Subordinate Policies"): (T1, T1F),
    ("ISP", "Risk Management"): (T1, T1F),
    ("ISP", "Assets, Endpoints, and Remote-First Security"): (T1, T1A),
    ("ISP", "Secure Engineering, DevOps, and SRE"): (T5, T5A),
    ("ISP", "Monitoring, Detection, and Incident Response"): (T1, T1E),
    ("ISP", "Data Governance, Openness, and Classification"): (T1, T1C),
    ("ISP", "Supplier and Third-Party Management"): (T1, T1F),

    # Maintenance Policy (MP)
    ("MP", "Policy Awareness"): (T1, T1F),
    ("MP", "Configuration Management"): (T3, T3A),
    ("MP", "Change Enablement"): (T3, T3B),
    ("MP", "Vulnerability and Patch Management"): (T3, T3C),
    ("MP", "Endpoints and Mobile Devices"): (T1, T1A),
    ("MP", "Software Management and Prohibited Technology"): (T1, T1A),
    ("MP", "Scheduling, Communication, and Freezes"): (T3, T3B),
    ("MP", "Evidence, Monitoring, and Metrics"): (T3, T3A),

    # Physical Security Policy (PSP)
    ("PSP", "Overview and Principles"): (T1, T1A),
    ("PSP", "Home Workspace Minimums"): (T1, T1A),
    ("PSP", "Networks and Wi-Fi at Home"): (T1, T1A),
    ("PSP", "Visitors and Working Around Others"): (T1, T1A),
    ("PSP", "Travel and Public Locations"): (T1, T1A),
    ("PSP", "Paper, Removable Media, and End-of-Life"): (T1, T1A),
    ("PSP", "Lost, Stolen, or Physically Compromised Assets"): (T1, T1E),
    ("PSP", "Future Facilities and Client Spaces"): (T1, T1A),
    ("PSP", "Evidence, Monitoring, and Continual Improvement"): (T3, T3D),

    # Risk and Security Assessment Policy (RSAP)
    ("RSAP", "Governance \u2014 Authority and Method"): (T1, T1F),
    ("RSAP", "Governance \u2014 Risk Ownership"): (T6, T6B),
    ("RSAP", "Governance \u2014 Documentation Control"): (T1, T1F),
    ("RSAP", "Methodology"): (T6, T6B),
    ("RSAP", "Assessing Impact (CIA Matrix)"): (T6, T6B),
    ("RSAP", "Qualitative Risk Scales"): (T1, T1F),
    ("RSAP", "Scope and Cadence \u2014 Enterprise RA"): (T1, T1F),
    ("RSAP", "Scope and Cadence \u2014 System Assessments"): (T6, T6B),
    ("RSAP", "Scope and Cadence \u2014 Ad-hoc Triggers"): (T6, T6B),
    ("RSAP", "Risk Appetite and Criteria"): (T6, T6B),
    ("RSAP", "Treatment Options and Authority"): (T6, T6B),
    ("RSAP", "Risk Register and POA&M"): (T6, T6B),
    ("RSAP", "Integration with DevSecOps, SRE & ITSM"): (T5, T5D),
    ("RSAP", "Remote-First and Endpoints"): (T1, T1F),
    ("RSAP", "Data Classification and Security"): (T2, T2C),
    ("RSAP", "Third-Party Management"): (T6, T6C),
    ("RSAP", "Reporting and Metrics"): (T6, T6B),
    ("RSAP", "Compliance and Enforcement"): (T1, T1F),

    # Third-Party Management Policy (TPM)
    ("TPM", "Governance and Program Structure"): (T6, T6C),
    ("TPM", "Risk Tiering and Categorization"): (T6, T6C),
    ("TPM", "Mandatory Due Diligence \u2014 All Suppliers"): (T1, T1F),
    ("TPM", "Mandatory Due Diligence \u2014 Digital Services"): (T6, T6C),
    ("TPM", "Mandatory Due Diligence \u2014 Software"): (T5, T5C),
    ("TPM", "Mandatory Due Diligence \u2014 Professional Services"): (T6, T6C),
    ("TPM", "Contracting and Required Security Clauses"): (T6, T6C),
    ("TPM", "Monitoring, Reviews, and Continuous Improvement"): (T6, T6C),
    ("TPM", "Open-Source Software (FOSS)"): (T5, T5C),
    ("TPM", "Prohibited and Restricted Technologies"): (T6, T6C),
    ("TPM", "Access and Identity Alignment"): (T6, T6C),
    ("TPM", "Integration with Incident Response"): (T4, T4C),
    ("TPM", "Records and Evidence"): (T6, T6C),

    # Vulnerability and Patch Management Policy (VPM)
    ("VPM", "Discovery and Cadence"): (T3, T3C),
    ("VPM", "Prioritization"): (T3, T3C),
    ("VPM", "Remediation Targets"): (T3, T3C),
    ("VPM", "Policy Awareness"): (T1, T1F),
    ("VPM", "Testing and Deployment Integration"): (T3, T3C),
    ("VPM", "Verification and Evidence"): (T3, T3C),
}

POLICY_NAMES = {
    "AUP": "Acceptable Use Policy",
    "ACP": "Access Control Policy",
    "AIP": "AI Usage Policy",
    "CEP": "Change Enablement Policy",
    "CMP": "Configuration Management Policy",
    "CUI": "CUI Policy",
    "DSHP": "Data Security and Handling Policy",
    "DRP": "Disaster Recovery Plan",
    "DRCP": "Document and Record Control Policy",
    "IdP": "Identification Policy",
    "IRP": "Incident Response Policy",
    "ISP": "Information Security Policy",
    "MP": "Maintenance Policy",
    "PSP": "Physical Security Policy",
    "RSAP": "Risk and Security Assessment Policy",
    "TPM": "Third-Party Management Policy",
    "VPM": "Vulnerability and Patch Management Policy",
}


def brief(section):
    """Create a short keyword from a section name."""
    for prefix in [
        "Data Classification \u2014 ",
        "Encryption Requirements \u2014 ",
        "Access Lifecycle \u2014 ",
        "Mandatory Due Diligence \u2014 ",
        "Scope and Cadence \u2014 ",
        "Governance \u2014 ",
        "Identity Proofing \u2014 ",
        "Authenticator Issuance \u2014 ",
        "Authentication Requirements \u2014 ",
        "Sharing \u2014 ",
    ]:
        if section.startswith(prefix):
            return section[len(prefix):].lower()
    s = section.lower()
    s = re.sub(r'\s*\(.*?\)', '', s)
    words = s.split()
    if len(words) <= 3:
        return ' '.join(words)
    return ' '.join(words[:3])


def parse_md_table(filepath):
    """Parse a markdown table and return list of row dicts."""
    rows = []
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    headers = None
    past_separator = False
    for line in lines:
        line = line.strip()
        if not line.startswith('|'):
            if past_separator:
                break
            continue

        cells = [c.strip() for c in line.split('|')[1:-1]]

        if headers is None:
            headers = cells
            continue

        if all(re.match(r'^[-:]+$', c) for c in cells):
            past_separator = True
            continue

        if not past_separator:
            continue

        row = dict(zip(headers, cells))
        rows.append(row)

    return rows


def generate_files():
    created = []

    for filename in sorted(os.listdir(BASE)):
        if not filename.endswith('-outcomes.md') and filename != 'cui-outcomes.md':
            continue
        if filename == 'README.md':
            continue
        if not filename.endswith('.md'):
            continue

        filepath = os.path.join(BASE, filename)
        rows = parse_md_table(filepath)
        if not rows:
            print(f"WARNING: No rows parsed from {filename}")
            continue

        policy = rows[0].get('Policy', '').strip()

        # --- CSV ---
        csv_filename = filename.replace('.md', '.csv')
        csv_path = os.path.join(BASE, csv_filename)
        unmapped = []

        with open(csv_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                'Policy', 'Section', 'Training Name', 'Module',
                'Audience', 'Learning Outcome'
            ])
            for row in rows:
                p = row.get('Policy', '').strip()
                section = row.get('Section', '').strip()
                outcome = row.get('Learning Outcome', '').strip()
                audience = row.get('Audience', '').strip()

                key = (p, section)
                if key in MAPPING:
                    training, module = MAPPING[key]
                else:
                    unmapped.append(key)
                    training = "UNMAPPED"
                    module = "UNMAPPED"

                writer.writerow([p, section, training, module, audience, outcome])

        if unmapped:
            print(f"WARNING: {filename} has unmapped rows: {unmapped}")

        # --- Mapping MD ---
        base_name = filename.replace('-outcomes.md', '')
        if filename == 'cui-outcomes.md':
            base_name = 'cui'
        mapping_filename = f"{base_name}-mappings.md"
        mapping_path = os.path.join(BASE, mapping_filename)

        groups = OrderedDict()
        for row in rows:
            p = row.get('Policy', '').strip()
            section = row.get('Section', '').strip()
            key = (p, section)
            if key in MAPPING:
                training, module = MAPPING[key]
            else:
                training, module = "UNMAPPED", "UNMAPPED"
            gkey = (training, module)
            if gkey not in groups:
                groups[gkey] = []
            groups[gkey].append(section)

        policy_display = POLICY_NAMES.get(policy, policy)

        with open(mapping_path, 'w', encoding='utf-8') as f:
            f.write(f"# {policy_display} \u2014 Training Mappings\n\n")
            f.write("| Module | Training | Rows |\n")
            f.write("|--------|----------|------|\n")

            for (training, module), sections in sorted(groups.items()):
                briefs = [brief(s) for s in sections]
                desc = ', '.join(briefs)
                f.write(f"| {module} | {training} | {len(sections)} ({desc}) |\n")

        created.append(csv_filename)
        created.append(mapping_filename)
        print(f"Created {csv_filename} + {mapping_filename} ({len(rows)} rows, policy={policy})")

    print(f"\nDone. Created {len(created)} files.")


if __name__ == '__main__':
    generate_files()
