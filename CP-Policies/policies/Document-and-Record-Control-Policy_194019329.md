# Policies : Document and Record Control Policy

Created by Sammy De La O , last modified on Feb 23, 2026

[https://civicactions.atlassian.net/browse/CPDOC-2?atlOrigin=eyJpIjoiNjA1M2Y5MTljNDAxNDI1NDg2NGRkZTgyMTk0N2JjNzQiLCJwIjoiaiJ9](https://civicactions.atlassian.net/browse/CPDOC-2?atlOrigin=eyJpIjoiNjA1M2Y5MTljNDAxNDI1NDg2NGRkZTgyMTk0N2JjNzQiLCJwIjoiaiJ9)

# Purpose

The purpose of this policy is to establish guidelines for the creation, management, storage, retrieval, and disposal of controlled documents and records within CivicActions.

# Scope

This policy applies to all employees, contractors, and 3rd parties who create, manage, or interact with documents and records on behalf of CivicActions.

# Roles and Responsibilities

- **Management** : Responsible for designating the Document Controller, Responsible Person, and Designated Person. They will also be included for reviewing changes to this policy.
- **Compliance** : Owning department of this policy. The Document Controller will be part of this internal department.
- **Document Controller** : The person designated by Management to prepare, update, and control the distribution of Controlled Documents, in accordance with this policy.
- **Responsible Person** : The person designated by a procedure as being responsible for the review and implementation of this procedure.
- **Designated Person** : The person designated by the responsible person for implementation of the procedure.

# Definitions

- **Document** : Any recorded information, regardless of medium or format, including but not limited to electronic files, paper documents, emails, and reports
- **Record** : A document that provides evidence of business activities, transactions, decisions, or processes
- **Controlled Document** : A written procedure or other document which is necessary to ensure that the quality of the services provided by CivicActions conform to applicable standards and requirements
- **Documented Information** : Documentation required by ISO 9001:2015

# References

- ISO 9001:2015 - Clause 7.5: Documented Information
- ISO 9001:2015 - Clause 4.4.2: Documented Information for the QMS
- ISO 9001:2015 - Clause 9.3.3: Management Review Outputs
- ISO 9001:2015 - Clause 10.2.2: Nonconformity and Corrective Action

# Policy

## Overview

## Document Identification

Management and the Document Controller will identify internal documents that will be identified as a **controlled document** .

The criteria for controlled documents can include, but are not limited to:

- Documented Information for the QMS
- Key policies and procedures identified by Senior Management, or internal department/practice area leads
- Policies and standards that are company-wide

Controlled documents will be tracked in the **Controlled Document Jira board** . Each document will have a card created for it. A collection of documents (such as a manual or playbook) will have its own card and the individual documents will be linked to the document.

Within the **Controlled Document Jira board** , controlled documents will be assigned a unique Document Identification Number, following the  format below:

1. The document identification numbering system consists of a two-character alpha prefix followed by four digits. (Examples: CP1023, EN4117, IT2076)
2. The document identification number assigned is formatted following the following attributes:
    1. Owning department - two-character code used to identify specific top-level and secondary-level practice areas and internal departments at CivicActions.
        1. List of Prefixes: [Group Directory Codes / Prefixes](https://docs.google.com/spreadsheets/d/1xArUHLGu-6v3D6x0LLjdYwbhGwWKGiE5wY73tJrAgNo/edit?usp=sharing)
    2. Document Type - single-digit number corresponding to a specific type of document
        1. 0 - Manual (collection of policies and procedures)
        2. 1 - Policy
        3. 2 - Procedure/SOP
        4. 3 - Form
        5. 4 - Checklist
        6. 5 - Guideline
        7. 6 - Diagram
        8. 7 - Training Material (slide deck, curriculum)
        9. 8 - Template
        10. 9 - Other
    3. Unique Identification - a unique 3-digit series unique to the specific document, which cannot be reused (sequential numbers 000 to 999)
3. The list of owning departments, document type, and unique identification number are managed in the Document Control Change Log. The log can be seen in the List view in the **Controlled Documents Jira board** .
4. The document identification will be assigned and documented in the board. **Individual document identification numbers can be retired but cannot be reused.**

## Document Classification

The Document Controller will work with the Owning Department and Management to determine the data classification of a Controlled Document. The team will use the Data Classification SOP to access, review, and designate a classification to a Controlled Document. This includes any criteria required by customer requirements that dictates the classification of a document.

For this policy, a Controlled Document is assigned a data classification and documented in the Document Control Change log. The data classification options used for CivicActions documents are:

| **Level**        | **Description**                                                     | **Examples**                                                 |
|------------------|---------------------------------------------------------------------|--------------------------------------------------------------|
| **Public**       | Information approved for public access                              | Website, Guidebook                                           |
| **Internal**     | Non-sensitive information shared only within the organization       | Company policies and procedures, AHC                         |
| **Confidential** | Sensitive information intended for those with "need-to-know" access | Client project documentation, CUI, HIPAA, PII                |
| **Restricted**   | Highly sensitive information requiring specific control and access  | Financial, accounting, payroll, personnel/HR info, passwords |

## Controlled Document Format

The formatting of a controlled document will require, at a minimum:

1. **Document Information** - A document will contain specific information about the document (in the header, a document information section in the document, or within the **Controlled Documents Jira Board** ) that includes:
    1. Document Name
    2. Document ID
    3. Version
    4. Effective Date
    5. Data Classification
    6. *Example of a document header:*

| **Example Policy**   | - Document ID: CP1001 - Version: 1.1 - Effective Date: 2024-02-17 - Class: INTERNAL   |
|----------------------|---------------------------------------------------------------------------------------|

2. The document will be formatted with headers for each section. At a minimum, a controlled document requires :
    1. **Purpose** - The reason for preparing the document and its intended use.
    2. **Scope** - The applicability of the document to practice areas, internal departments, personnel, CivicActions as a whole, and any 3rd party entities.
    3. **Roles and Responsibilities** - Team and personnel responsible for implementing and maintaining the document.
    4. **References** - List of all applicable specification documents, including standard and frameworks, regulatory or contract requirements, and/or other Controlled Documents.
    5. [ ***General*** ] - The main section, either a Policy, Procedure or other main section for the document.
    6. **Training** - Training requirements for the document, including who needs training and the required interval of the training.
    7. **Review** - How often will the document be required to be reviewed and by who.
3. Other sections can be added to the document as needed.
4. **Record of Change** (Optional)- The version control of a document is tracked in the **Controlled Documents Jira board** . Optionally, depending on the requirements or needs of the document, a section to document the history of the document creation and changes, including version, author, summary of changes, and effective date. Example:

|   **Version** | **Author(s)**      | **Summary of Changes**                                                                                                               | **Effective Date**   |
|---------------|--------------------|--------------------------------------------------------------------------------------------------------------------------------------|----------------------|
|           1   | J. Smith           | Initial draft of the document                                                                                                        | 2023-10-11           |
|           1.1 | J. Smith, M. Smith | - Added updated content for Training - Removed "Management" from Roles section - Added NIST CSF controls to the "References Section" | 2024-02-17           |

## Document Version Control

Effective Controlled Documents will have version numbers , following the format of major and minor versions. These documents are immutable and can only be changed when a new document is created and set to "DRAFT" status.

- **Major Versions** - Major revisions to Controlled Documents will be noted with the whole number (example: **1** .0, **2** .3, **12** .5) or left side of the decimal point. Criteria for requiring a major revision includes:
    - Changes to requirements that impact the content of the Controlled Document
    - Significant updates to policies, procedures, or processes referenced in the document
    - Substantial changes to the document's structure, format, or organization (including branding)
    - Updates that result in changes to the document's intended purpose, scope, or audience
    - Changes that substantially alter the meaning or interpretation of the document
    - Changes stemming from the document review period.
- **Minor Versions** - Minor revisions to Controlled Documents will be noted with the fractional part (example: 1. **0** , 2. **3** , 12. **5** ) or the right side of the decimal point. Criteria for requiring a minor revision includes:
    - Correction of typographical errors, spelling mistakes, or grammatical errors.
    - Updates to contact information, references, or hyperlinks.
    - Clarifications or enhancements to existing content without altering the document's overall meaning or intent.
    - Addition of minor content such as examples, illustrations, or explanatory notes.
    - Reformatting of the document for consistency or readability purposes.
- **Draft** - A Controlled Document that is set to **DRAFT** will not be an effective document and will not be enforced.
    - The first draft of a document will be numbered at version 0.1 in the Document Control Change Log.

The Document Controller will be responsible for confirming the document number change and documenting it in the Document Control Change Log.

## Document Control Change Log

Each controlled document in the **Controlled Document Jira board** is tagged with the version. The list view in the Controlled Document Jira board will show the list of all documents, the document identification number, current version and/or status, and effective date.

## Document Change Request Process

Management, Responsible Person(s), Document Controller, or other key members of Owning Departments can submit a Document Change Request. The Document Controller will follow the Document Change Request Process to review, approve, and start a document change request.

## Document Change Request

Request for document creations, changes, or retirement will be managed in the **Compliance Jira board** . A card will be created for the document change request (DCR).

The Document Controller will review the DCR and approved the activity. For controlled documents, the card will link to the controlled document card in the **Controlled Documents Jira board** .

### Distribution of Draft Copies

Document change request activities are tracked in the **Compliance Jira board** . The ticket will be linked to the Controlled Documents Jira board ticket linked to the document. The Document Controller and Responsible Person may distribute the link to the document for the purpose of gaining feedback from key team members, stakeholders, or management. This includes getting approval of the document.

### Distribution of Controlled Copies

After reviewing a Controlled Document and receiving feedback from Managers and team members, the Responsible Person(s) determines the Controlled Document is ready for final review, implementation, distribution.

The Responsible Person will send out a communication to the owning department to notify of the updated document. The Document Controller will coordinate with the Responsible Person(s) to update training material, and if necessary plan training sessions for the owning department.

### Access Control and Security

Locations of Controlled Documents will be configured to make it available to all intended parties. Access control and security is managed and enforced by security groups in the CivicActions systems, including Google Workspace, Confluence, and Jira.

### Document Training Requirements

Management and the Responsible Person(s) will be responsible for determining and documenting the training requirements for a Controlled Document. This includes reviewing contractual, regulatory, or legal requirements.

The Document Controller will work with the Responsible Person(s) to create and plan the training program for the document.

### Document Review

By default, all Controlled Documents will be reviewed on an annual basis. Documents with different review schedules will be noted in the Review section of the document.

# Training

- This document will be included in the QMS Training program. This is required for annual training for any personnel working with the QMS.
- This document will also be included in the Document Management System Training program, which is required for new onboarding, role change that makes them a Responsible Person for a Owning Department Controlled Document, and upon major revisions.

# Review

This document will be reviewed annually as part of the internal QMS internal audit. Changes to this document outside of an annual review will need to be approved by Senior Management.

## Attachments:

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~drawio~63e27d2f1b13d42998e4db2a~Untitled Diagram-1732045723575.drawio.tmp](attachments/194019329/387579946.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~drawio~63e27d2f1b13d42998e4db2a~Untitled Diagram-1732045723575.drawio.tmp](attachments/194019329/387514474.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~drawio~63e27d2f1b13d42998e4db2a~Untitled Diagram-1732045723575.drawio.tmp](attachments/194019329/387285086.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~drawio~63e27d2f1b13d42998e4db2a~Untitled Diagram-1732045723575.drawio.tmp](attachments/194019329/387842129.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~drawio~63e27d2f1b13d42998e4db2a~Untitled Diagram-1732045723575.drawio.tmp](attachments/194019329/387186721.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~drawio~63e27d2f1b13d42998e4db2a~Untitled Diagram-1732045723575.drawio.tmp](attachments/194019329/388005982.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~drawio~63e27d2f1b13d42998e4db2a~Untitled Diagram-1732045723575.drawio.tmp](attachments/194019329/387219546.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~drawio~63e27d2f1b13d42998e4db2a~Untitled Diagram-1732045723575.drawio.tmp](attachments/194019329/387219557.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~drawio~63e27d2f1b13d42998e4db2a~Untitled Diagram-1732045723575.drawio.tmp](attachments/194019329/387809396.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~drawio~63e27d2f1b13d42998e4db2a~Untitled Diagram-1732045723575.drawio.tmp](attachments/194019329/387842054.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[Untitled Diagram-1732045723575.drawio](attachments/194019329/389578803.drawio)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[Untitled Diagram-1732045723575.drawio.png](attachments/194019329/390234144.png)

(image/png)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[Untitled Diagram-1732045723575.drawio](attachments/194019329/389644378.drawio)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[Untitled Diagram-1732045723575.drawio.png](attachments/194019329/390037592.png)

(image/png)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~Untitled Diagram-1732045723575.drawio.tmp](attachments/194019329/389775430.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~Untitled Diagram-1732045723575.drawio.tmp](attachments/194019329/389644363.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~Untitled Diagram-1732045723575.drawio.tmp](attachments/194019329/390135853.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~Untitled Diagram-1732045723575.drawio.tmp](attachments/194019329/389742707.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~Untitled Diagram-1732045723575.drawio.tmp](attachments/194019329/390135864.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~Untitled Diagram-1732045723575.drawio.tmp](attachments/194019329/389775445.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~Untitled Diagram-1732045723575.drawio.tmp](attachments/194019329/389742723.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~Untitled Diagram-1732045723575.drawio.tmp](attachments/194019329/390004835.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~Untitled Diagram-1732045723575.drawio.tmp](attachments/194019329/389611627.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~Untitled Diagram-1732045723575.drawio.tmp](attachments/194019329/389742627.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[Untitled Diagram-1732045723575.drawio](attachments/194019329/387940423.drawio)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[Untitled Diagram-1732045723575.drawio.png](attachments/194019329/387416130.png)

(image/png)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~drawio~63e27d2f1b13d42998e4db2a~Untitled Diagram-1733942630054.drawio.tmp](attachments/194019329/407666699.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~drawio~63e27d2f1b13d42998e4db2a~Untitled Diagram-1733942630054.drawio.tmp](attachments/194019329/407437326.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~drawio~63e27d2f1b13d42998e4db2a~Untitled Diagram-1733942699680.drawio.tmp](attachments/194019329/407633938.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~drawio~63e27d2f1b13d42998e4db2a~Untitled Diagram-1733942699680.drawio.tmp](attachments/194019329/407339024.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~drawio~63e27d2f1b13d42998e4db2a~Untitled Diagram-1733942969714.drawio.tmp](attachments/194019329/407830538.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~drawio~63e27d2f1b13d42998e4db2a~Untitled Diagram-1733942969714.drawio.tmp](attachments/194019329/407502868.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~drawio~63e27d2f1b13d42998e4db2a~Untitled Diagram-1733943062071.drawio.tmp](attachments/194019329/407765000.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~drawio~63e27d2f1b13d42998e4db2a~Untitled Diagram-1733943062071.drawio.tmp](attachments/194019329/407830549.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~drawio~63e27d2f1b13d42998e4db2a~Untitled Diagram-1733943062071.drawio.tmp](attachments/194019329/407339030.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~drawio~63e27d2f1b13d42998e4db2a~Untitled Diagram-1733943062071.drawio.tmp](attachments/194019329/407502875.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~drawio~63e27d2f1b13d42998e4db2a~Untitled Diagram-1733943210690.drawio.tmp](attachments/194019329/407601170.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~drawio~63e27d2f1b13d42998e4db2a~Untitled Diagram-1733943210690.drawio.tmp](attachments/194019329/407339041.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~drawio~63e27d2f1b13d42998e4db2a~Untitled Diagram-1733943536887.drawio.tmp](attachments/194019329/407699465.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~drawio~63e27d2f1b13d42998e4db2a~Untitled Diagram-1733943536887.drawio.tmp](attachments/194019329/407797801.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~drawio~63e27d2f1b13d42998e4db2a~Untitled Diagram-1733943536887.drawio.tmp](attachments/194019329/407699476.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~drawio~63e27d2f1b13d42998e4db2a~Untitled Diagram-1733943536887.drawio.tmp](attachments/194019329/407830573.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~drawio~63e27d2f1b13d42998e4db2a~Untitled Diagram-1733943536887.drawio.tmp](attachments/194019329/407765023.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~drawio~63e27d2f1b13d42998e4db2a~Untitled Diagram-1733943536887.drawio.tmp](attachments/194019329/407502892.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~drawio~63e27d2f1b13d42998e4db2a~Untitled Diagram-1733943536887.drawio.tmp](attachments/194019329/407699487.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~drawio~63e27d2f1b13d42998e4db2a~Untitled Diagram-1733943536887.drawio.tmp](attachments/194019329/407633949.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~drawio~63e27d2f1b13d42998e4db2a~Untitled Diagram-1733943536887.drawio.tmp](attachments/194019329/407502903.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~drawio~63e27d2f1b13d42998e4db2a~Untitled Diagram-1733943536887.drawio.tmp](attachments/194019329/407797773.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[Untitled Diagram-1733943536887.drawio](attachments/194019329/407568424.drawio)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[Untitled Diagram-1733943536887.drawio.png](attachments/194019329/407601197.png)

(image/png)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~Untitled Diagram-1733943536887.drawio.tmp](attachments/194019329/407601182.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~Untitled Diagram-1733943536887.drawio.tmp](attachments/194019329/407830592.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~Untitled Diagram-1733943536887.drawio.tmp](attachments/194019329/407666722.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~Untitled Diagram-1733943536887.drawio.tmp](attachments/194019329/407797812.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~Untitled Diagram-1733943536887.drawio.tmp](attachments/194019329/407797823.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~Untitled Diagram-1733943536887.drawio.tmp](attachments/194019329/407470097.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~Untitled Diagram-1733943536887.drawio.tmp](attachments/194019329/407633964.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[~Untitled Diagram-1733943536887.drawio.tmp](attachments/194019329/407502921.tmp)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[Untitled Diagram-1733943536887.drawio](attachments/194019329/407732237.drawio)

(application/vnd.jgraph.mxfile)

<!-- 🖼️❌ Image not available. Please use `PdfPipelineOptions(generate_picture_images=True)` -->

[Untitled Diagram-1733943536887.drawio.png](attachments/194019329/407568403.png)

(image/png)

Document generated by Confluence on Mar 18, 2026 09:50

[Atlassian](http://www.atlassian.com/)