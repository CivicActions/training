# Welcome
?[datawelcome.webm](https://github.com/user-attachments/assets/2c18653b-4d9b-43f6-977f-f41c88cb68bf)

Welcome to the Data Handling training. In this training, you’ll learn how to classify, store, and share data securely. Get ready to move beyond general awareness and master the specific technical and commercial requirements that help safeguard CivicActions and maintain compliance. This training is key for the awareness of everyone across the company and provides the context for us to understand and embrace this initiative.

## Agenda
?[agenda.webm](https://github.com/user-attachments/assets/d2abc5f2-d8e5-40c1-b60e-fd066ffa4ab6)

- Data Classification
- Data handling fundamentals
- Secure storage
- Sharing data safely
- Device integrity
- Role-specific responsibilities

## Data Classification
?[classification.webm](https://github.com/user-attachments/assets/a09660ea-de2d-4985-9654-68ab5ee6f891)

Understanding how to properly classify and handle data is essential for compliance and operational excellence. Whether you’re an engineer, designer, manager, or part of the sales team, knowing the fundamentals of data security ensures you protect sensitive information and support CivicActions' compliance goals. Let's start by looking at the four tiers of data classification.

### Four Tiers of Data Classification
<img width="729" height="388" alt="four binders representing the four tiers of data classification" src="https://github.com/user-attachments/assets/4b0446dd-41c0-45bc-a7a3-d8691589ad55" />

?[4tiers.webm](https://github.com/user-attachments/assets/de855409-ef11-424d-bb3c-02da69af8896)

| Data type | Definition | 
| :---------- | :----------------------------------------------------------------- |
| Public | Approved for release, such as website content or open-source code. Can be accessed by anyone with the link. |
| Internal | Used for non-sensitive internal procedures. Not for public release, but not highly sensitive. |
| Confidential | Includes high-stakes data like Federal Contract Information (FCI) and Controlled Unclassified Information (CUI). Disclosure could impact contract eligibility. |
| Restricted | The most sensitive data, such as payroll, credentials, or Social Security Numbers. Unauthorized disclosure could cause severe harm. |

### Data Visualization

<img width="681" height="625" alt="a rock pyramid that has a larger rock on the bottom and gets smaller in rock size until the top rock, which is very small and likely to fall off if the rock moves" src="https://github.com/user-attachments/assets/a6295a9b-dff6-4f3c-8eca-2c0dfcf94e09" />

?[pyramid.webm](https://github.com/user-attachments/assets/441e7838-5f87-4638-a8ea-c1414ac7b6f0)

This pyramid shows how data is classified by sensitivity and risk. Public data forms the broad base, while restricted data sits at the top and represents the highest risk if mishandled. As you move up the tiers, the potential consequences of improper handling increase, making strict controls essential for confidential and restricted data.

### Classification in Practice
?[practice.webm](https://github.com/user-attachments/assets/337da55e-550c-457b-8a05-504831b7365b)

Let's look at each data type to see which types of data belong in each tier, who typically handles them, and what can happen if they’re mishandled.

| Data type | Definition | Consequences |
| :---------- | :---------------------------------------- | :---------------------------------------------- |
| Public | Public data includes information such as website content, published marketing materials, and open-source code. Anyone in the organization can access and share this data. | If mishandled, there are minimal risks. |
| Internal | Internal data covers non-sensitive internal procedures, such as meeting notes or internal process documents. Typically, employees across departments use this data, but it should not be shared outside the organization. | If mishandled, there may be minor operational disruptions, but no severe compliance consequences. |
| Confidential | Confidential data includes FCI and CUI, such as client technical drawings or sensitive contract details. Engineers and sales/contract teams often interact with this data. | If mishandled, it could jeopardize contract eligibility or lead to regulatory penalties. |
| Restricted | Restricted data includes highly sensitive items such as payroll records, login credentials, or Social Security Numbers. Typically, only managers or HR personnel should access this data. | If mishandled, it can result in severe harm, including legal action or significant financial loss. |

### Data Minimization
?[minimization.webm](https://github.com/user-attachments/assets/797b21cc-5edf-4854-b469-fda4e23d550f)

Data minimization means collecting and storing only the information you truly need. By limiting the amount of data you handle and favoring secure, cloud-native sharing, you reduce the risk of breaches and make compliance easier for everyone.

> Only collect the information that is necessary. Do not create local copies; instead, use cloud-native sharing methods within approved boundaries.

## Checkpoint quiz
?[quizstart.webm](https://github.com/user-attachments/assets/d7c1e995-c489-4c3d-bbd7-6bf5e6d39466)

Let's take a moment to review what we've covered so far. Select the correct answer or answers for the next few questions.

### Which of the following is an example of violating the data minimization principle?
- [( )] Storing only essential client information in a secure cloud drive
- [(X)] Downloading confidential files to your personal laptop for convenience
- [( )] Sharing documents through approved company platforms
- [( )] Limiting access to sensitive data based on job roles

### What are the four tiers of data classification? (select all that apply)
- [[ ]] Governmental
- [[X]] Public
- [[X]] Internal
- [[ ]] FOSS
- [[ ]] Personal
- [[X]] Confidential
- [[X]] Restricted

## Mandatory Marking and Labeling
?[marking.webm](https://github.com/user-attachments/assets/1827e477-5bfa-4135-9a48-1e274497f9bf)

For confidential and restricted data, it's essential to use electronic labels, banners, or filename tags to clearly identify sensitive information. If you receive unmarked data that may be Controlled Unclassified Information (CUI), you have a duty to report it and ensure it's properly labeled before storing and sharing it.

### Recognizing Proper Labeling
?[properlabel.webm](https://github.com/user-attachments/assets/b9bbc68d-de9b-479a-8717-d09c82ff4c0e)

Properly labeled files in Google Workspace are easy to spot: look for banners, filename tags, or workspace labels indicating _Confidential_ or _Restricted_. If a file lacks these labels but contains sensitive information, it needs to be reported and labeled before further handling.

### Handling Unmarked CUI
?[handling.webm](https://github.com/user-attachments/assets/e3a40852-31f0-49b7-8792-726218e69caa)

Sometimes, you may come across files or documents that contain sensitive information but do not have the required CUI markings. It's important to know how to handle such situations to ensure compliance and protect sensitive data. Follow these steps when you encounter CUI that isn't properly marked.

1. Identify potential CUI.
   - Notice if a file, such as a technical drawing from a client, lacks proper labeling but appears sensitive.
2. Report to the appropriate authority.
   - Notify your manager or compliance officer about the unmarked data immediately.
3. Ensure correct marking.
   - Work with the responsible party to apply the correct electronic labels or tags before any further storage or sharing.
4. Store and share securely.
   - Once labeled, store and share the data only within approved boundaries, such as designated shared drives.

## Secure Storage
?[storage.webm](https://github.com/user-attachments/assets/ea445e26-d380-4d1c-8cc0-c4d8787ef075)

Protecting sensitive data isn’t just about knowing what information you have; it’s about how you store, share, and access it every day. Approved storage boundaries are the digital spaces where sensitive data may reside. These include company-approved cloud platforms, such as Google Workspace Shared Drives. Storing data outside these boundaries, like on personal cloud accounts or local downloads, creates significant security risks, including unauthorized access, data loss, and compliance violations. Understanding and respecting these boundaries is the first step in protecting your organization’s information.

### Storing Data
?[storing.webm](https://github.com/user-attachments/assets/978ca801-9607-4cda-b696-e15e12eeea6e)

Let's take a look at where different types of data can be stored, who can access them, and what you should avoid when storing them.

- **Public data**:
    - Public data is approved for release and may be shared broadly, including on public websites. However, always confirm that data is truly public before sharing outside the organization. No special storage restrictions apply, but caution is still advised.
- **Internal data**:
    - Internal data can be stored within company-managed drives, but should not be shared externally. While less sensitive, it still must not be placed on personal or public platforms. Access is typically limited to employees within the organization.
- **Confidential data**:
    - Confidential data must be stored only in company-approved shared drives or authorized SaaS platforms. Access is limited to individuals with a legitimate business need. Never download confidential files to personal devices or store them on unapproved cloud services.
- **Restricted data**:
    - Restricted data, such as payroll or credentials, requires the highest level of protection. Store only in designated, secure folders on approved platforms. Access is strictly controlled and monitored. Storing restricted data on local devices or personal storage is strictly forbidden.

## Checkpoint quiz
?[quizstart.webm](https://github.com/user-attachments/assets/d7c1e995-c489-4c3d-bbd7-6bf5e6d39466)

Let's take a moment to review what we've covered so far. Select the correct answer or answers for the next few questions.

### Match the data examples to the correct classification tier:

- [[Public] (Internal) [Confidential] (Restricted)]
- [  ( )        ( )         ( )          (X)     ] Employee login credentials
- [  ( )        ( )         ( )          (X)     ] Payroll spreadsheet
- [  ( )        (X)         ( )          ( )     ] Meeting notes about project timelines
- [  ( )        ( )         (X)          ( )     ] Technical drawing from the client
- [  (X)        ( )         ( )          ( )     ] Published product brochure

### Which of the following is an approved storage practice for confidential data?
- [( )] Saving to a personal Dropbox account
- [( )] Uploading to an unapproved SaaS platform
- [( )] Downloading to your local "Downloads" folder
- [(X)] Storing in a company-approved Google Workspace Shared Drive

## The "No Email" Rule
?[email.webm](https://github.com/user-attachments/assets/8a72c7b2-9177-48ff-b110-1c879771bf98)

Sharing sensitive data requires strict adherence to secure protocols. The default approach is to use named accounts for sharing, never public links, and to avoid email for transmitting confidential or restricted information. When email is absolutely necessary, encryption protocols must be followed to ensure data remains protected.

### Safe Sharing Protocols
?[sharing.webm](https://github.com/user-attachments/assets/55d5544d-481a-4c6a-b0e9-4805a48cfc17)

Sharing confidential or restricted data requires careful attention to security protocols. Follow these steps to safely share confidential or restricted data and protect sensitive information from unauthorized access.

1. Confirm recipient identity.
   - Always share files using specific, named accounts. Double-check that only authorized individuals are included in the sharing permissions.
2. Avoid public links.
   - Never use the "Anyone with the link" option for sharing sensitive data. This setting is only appropriate for public information.
3. Use encryption for email exceptions.
   - If email is the only option, place the data in an AES-256 password-protected archive. The passphrase must be at least 20 characters and sent via a separate channel, such as a secure messaging app.
4. Verify secure delivery.
   - Ensure the recipient has received both the encrypted file and the passphrase through separate, secure channels before confirming completion.
  
Never send confidential or restricted data via standard email or attachments; use only approved secure channels.

## Device Integrity
?[integrity.webm](https://github.com/user-attachments/assets/95e60e56-6041-43e9-a379-8fb7485df19a)

Securing your devices is just as important as securing your data. Only company-managed hardware should be used for handling sensitive information, and all endpoints must have full-disk encryption enabled. For Controlled Unclassified Information (CUI), additional FIPS compliance is required to meet federal standards.

**Engineers**
- Engineers working on federal contracts must use only company-managed laptops. Personal devices are strictly prohibited. All endpoints must have full-disk encryption, and FIPS 140-2/3 validated cryptographic modules are required for handling CUI.

**Sales and managers**
- Sales, managers, project leads, directors, and executive leadership must use company-managed devices for all work involving sensitive data. Encryption and endpoint security controls must be active at all times. Never store or access sensitive information on personal laptop or mobile devices.

**All CivicActions employees and contractors**
- No one should ever store sensitive data on unapproved devices. Always ensure that your device meets company security standards before accessing or handling confidential or restricted information.

## Data Handling by Roles
?[rolehandling.webm](https://github.com/user-attachments/assets/ec5e3465-6c33-4911-ad17-fb136116b36f)

Each role in the organization has unique responsibilities for handling sensitive data. Let's take a look at some roles and examples:

**Engineers**: _Secure development and secrets management_:
?[engineers.webm](https://github.com/user-attachments/assets/62bed6e3-f461-442d-8a90-4ed9a1c1605c)

Engineers must never use real production confidential data or CUI data in development or test environments. Instead, synthetic or masked datasets should be created and used, with masking scripts reviewed and approved. Secrets like API keys and passwords must never be stored in source code; always use the approved secrets vault.
- Practical Example: Using a company-approved tool to generate fake customer data for testing a new feature.
- Common Mistake: Copying production data for testing or leaving credentials in code repositories.

**Sales and contract teams**: _Handling proposals and slack restrictions_:
?[sales.webm](https://github.com/user-attachments/assets/3b5900a4-06c6-480a-a15c-7f6ae6b599f4)

Sales and contract teams must treat all client RFPs and technical diagrams as confidential by default. These documents should only be stored in authorized CUI enclaves and never shared via Slack or email without proper safeguards. Slack is for coordination only, not for sharing technical data.
- Practical Example: Uploading a proposal to a secure document management system instead of sending it via Slack.
- Common Mistake: Discussing sensitive details in open channels or sending unprotected files to clients or partners.

**Managers**: _Data minimization and flow-down requirements_:
?[managers.webm](https://github.com/user-attachments/assets/c4ce9136-1fcf-4381-a648-e64140b2ce2d)

Managers are responsible for ensuring that only necessary data is collected and that access is granted strictly on a need-to-know basis. Before sharing project data with subcontractors or partners, managers must ensure that they understand and agree to all data-handling protocols.
- Practical Example: Briefing a new subcontractor on data handling requirements before granting access to project files.
- Common Mistake: Failing to brief partners, leading to accidental exposure of sensitive information.

### Best Practices
<img width="676" height="591" alt="2 locked file cabinets and a padlock to represent securing data correctly" src="https://github.com/user-attachments/assets/5637cf5d-15bc-42cb-b910-4169136eec86" />

?[bestpractices.webm](https://github.com/user-attachments/assets/8b59bc00-330c-4111-ba0d-4399953b09a3)

Protecting sensitive data in development and test environments is critical for compliance and risk reduction. Follow these steps to ensure no real confidential or CUI data is exposed during testing.

1. Never use real production data.
   - Always avoid using actual production confidential data or CUI data in any development or test environment.
2. Create synthetic or masked datasets.
   - Develop and use synthetic or masked datasets that mimic real data without exposing sensitive information.
3. Submit masking scripts for review.
   - All masking scripts must be submitted for review and approval to ensure effectiveness and compliance.
4. Store test data in approved environments.
   - Only store datasets in company-approved, secure environments—never on personal devices or unauthorized platforms.
5. Manage secrets in an approved vault.
   - All secrets, such as API keys and passwords, must be managed exclusively in the organization’s approved secrets vault.

## Checkpoint quiz
?[quizstart.webm](https://github.com/user-attachments/assets/d7c1e995-c489-4c3d-bbd7-6bf5e6d39466)

Let's take a moment to review what we've covered so far. Select the correct answer or answers for the next few questions.

### You need to access confidential data remotely. Which device and security measures are required?
- [( )] Personal laptop with no encryption
- [( )] Tablet with a basic password
- [(X)] Company-managed laptop with full-disk encryption
- [( )] Any device with antivirus software

### Which of the following practices are compliant in a development or test environment? (select all that apply)
- [[X]] Using synthetic datasets for testing
- [[X]] Storing secrets in the approved vault
- [[ ]] Using real production CUI data for testing
- [[X]] Submitting masking scripts for review

## Commercial Data Handling and Flow-Down
?[commercialhandling.webm](https://github.com/user-attachments/assets/e16e5259-24d9-43ab-9529-ba0fe5f2dd26)

Everyone, from project teams to us at CivicActions, plays a critical role in protecting sensitive commercial information. Proposals, RFPs, and technical diagrams must always be treated as confidential and stored in authorized locations. Before sharing any project data with subcontractors or partners, it’s essential to provide clear instructions on data handling requirements to prevent accidental exposure or mishandling.

**Proposal security**:
- All client proposals, RFPs, and technical diagrams must be classified as confidential by default. These documents should be stored only in the designated CUI enclave or authorized shared drives, never on personal devices or unapproved platforms. When sharing proposals, use secure, named account invitations and avoid sending files via email or Slack. This ensures only authorized recipients have access and maintains a clear audit trail.

**Communications restrictions**:
- Slack should only be used for coordination and not for sharing technical CUI or confidential data. Never paste technical diagrams or sensitive details into Slack messages or channels. If technical data must be discussed, use the authorized CUI enclave or approved secure channels. This reduces the risk of accidental leaks or unauthorized access.

**Flow-down requirements**:
- Before sharing any project data with subcontractors or partners, managers must ensure they are briefed on all data handling protocols. This includes providing written instructions and confirming understanding. Never send technical or confidential data to a subcontractor before confirming they are trained and agree to follow all compliance requirements. This step is critical for maintaining contractual and regulatory obligations.

## Media Handling and Device Sanitization
<img width="726" height="299" alt="a person using a removable drive next to a person shredding a document" src="https://github.com/user-attachments/assets/3e6a2241-c455-4982-acf4-6b06eb8d918c" />

?[media.webm](https://github.com/user-attachments/assets/2f23870a-ba25-461a-b288-19f3b045b3c9)

Physical data security is just as important as digital safeguards. Let's take a look at handling removable media, printing sensitive data, and device sanitization. 

**Removable media**:
- Only use removable media, such as USB drives, if absolutely necessary, and with explicit company approval. All such media must be encrypted to protect sensitive data. Generally speaking, removable media is disallowed.

**Printing sensitive data**:
- Print sensitive documents only when required, and always store them in a locked container. When no longer needed, shred documents to prevent unauthorized access.

**Device Sanitization**:
- When decommissioning laptops or storage devices, use cryptographic erasure (destroying encryption keys) to render data unrecoverable. Simply deleting files or reformatting drives is not sufficient. Skipping this step can result in data exposure if devices are reused or discarded.

## Checkpoint quiz
?[quizstart.webm](https://github.com/user-attachments/assets/d7c1e995-c489-4c3d-bbd7-6bf5e6d39466)

Let's take a moment to review what we've covered so far. Select the correct answer or answers for the next few questions.

### Mark the actions as compliant or non-compliant:

-[[Compliant] (Non-compliant)]
- [  (X)        ( )         ] Storing the proposal in the CUI enclave
- [  (X)        ( )         ] Using a named account to share the proposal
- [  (X)        ( )         ] Briefing a subcontractor before sharing the proposal
- [  ( )        (X)         ] Sharing an RFP via Slack
- [  ( )        (X)         ] Sending technical diagrams to the subcontractor before briefing them

### Which action is required when decommissioning a laptop that stored confidential data??
- [(X)] Cryptographic erasure
- [( )] Simple file deletion
- [( )] Physical destruction only
- [( )] Doing nothing

## Summary
?[summary.webm](https://github.com/user-attachments/assets/a6665e85-f169-41fc-8d5b-0320cca90bdf)

As we close out this training, please remember that we all have a role in ensuring the safe storage and transfer of data. Take an inventory of your data storage practices and ensure they align with our data policy. Thank you for playing your part in helping CivicActions deliver on our commitment to using secure data practices.

