<!--
author:   CivicActions Security Team
email:    security@civicactions.com
version:  0.1.0
language: en
narrator: US English Female

comment:  Secure Development & Supply Chain — training for developers
          on secure engineering, AI-assisted coding rules, DevSecOps
          data handling, and open-source supply chain management.

-->

# Secure Development & Supply Chain

Welcome to **Secure Development & Supply Chain** — the security training built for CivicActions developers.

You already know the security basics from Training 1, and your IT Ops colleagues covered the change/config/patch infrastructure in Training 3. This course focuses on what's specific to *your* work: writing secure code, using AI coding tools responsibly, managing open-source dependencies, and handling credentials properly.

**Who takes this?** Developers — engineers, DevOps, and anyone writing or deploying code.

**Prerequisite:** Training 1 — Security Awareness Essentials.

**How long?** About 10–15 minutes.

**When?** Within 30 days of onboarding, then annually, and whenever there's a toolchain or policy change.

**Compliance:** CMMC L2 (SC, SI, SR controls), ISO 27001 A.8.25–A.8.28.

---

Let's get started!

## Module A — Secure Engineering Principles

Security isn't something you bolt on at the end. It's something you build in from the start. This module covers the core principles that should guide every design decision and code change you make.

### Shift-Left Security

"Shift left" means moving security controls **earlier in the development process** — into your CI/CD pipeline, not just into a final review:

- Use **pre-approved libraries** for authentication and cryptography (don't roll your own)
- Set up **automated baseline enforcement** in your pipelines — security checks run on every commit
- Catch problems in CI, not in production

> **Example:** Your project uses a pre-approved authentication library that integrates with Google Workspace SAML. Your CI pipeline runs SAST and SCA checks on every pull request. A developer opens a PR that accidentally downgrades the library to a version with a known vulnerability — the pipeline catches it before the PR is even reviewed. That's shift-left in action.

> **Think of it this way:** Fixing a security bug in a pull request costs minutes. Fixing one in production costs days — plus the incident response overhead.

### Design Principles

When designing systems, keep these principles in mind:

- **Least privilege** — every component gets only the access it needs, nothing more
- **Zero trust** — don't assume any system or user is trusted by default, even inside the network
- **Rapid rollback** — design so you can undo changes quickly if something goes wrong
- **Defense in depth** — layer your security controls so that no single failure is catastrophic

### DevSecOps Data Handling

This one is simple but critical:

- **Never use real PII, Confidential, or CUI data** in test or development environments
- **Do not export PII from SaaS platforms** for testing purposes
- **Use synthetic or masked datasets** instead — and submit masking scripts for review and approval before use
- **Store test data only in approved environments** — never on personal devices or unapproved platforms

Production data in a test environment is a breach waiting to happen. Synthetic data gives you what you need without the risk.

> **Example:** You're building a feature that displays user profiles. Instead of exporting real user data from Rippling or Google Workspace, you generate synthetic records with fake names, emails, and roles using an approved masking script. The script gets peer-reviewed to make sure it actually strips sensitive fields. The feature works the same way, but if the test environment gets compromised, no real PII is exposed.

### Code Review Obligations

Peer review isn't optional:

- **All production code requires peer review** — no exceptions
- For **CIA "High" systems**, additional review rigor applies (more reviewers, more scrutiny)
- Code review is a security control, not just a quality check

> **Example:** You're working on a CIA "High" system for a federal client. Your PR gets the usual peer review, but because of the system's classification, it also requires a second reviewer with security expertise. The extra rigor isn't bureaucracy — it's proportional to the risk.

### Secure Defaults

Ship your systems with security built in:

- **Remove non-essential services and components** — if it's not needed, it shouldn't be there
- Start with **least-functionality baselines** — users and systems get the minimum by default
- Make the secure option the *easy* option

### Module A Quiz

You need test data that mirrors production for a new feature. What is the correct approach?

- [( )] Copy production data into the test environment
- [( )] Export PII from the SaaS platform into a local database
- [(X)] Use synthetic or anonymized data — never use real PII or Confidential data in test/dev environments
- [( )] Ask a colleague to share their production access
***

**Correct!** Real PII or Confidential data must never be used in test or development environments. Use synthetic or anonymized data instead. Copying production data into test environments creates unnecessary risk — if the test environment is less secure (and it usually is), that data is now exposed.

***

## Module B — AI-Assisted Development

AI coding tools can make you faster, but they come with real responsibilities. This module covers the rules for using AI in your development workflow.

### GitHub Copilot — The Only Approved Coding AI

For writing source code, **GitHub Copilot is the only approved AI tool**:

- Use it exclusively for **source code creation**
- Other approved AI tools (like ChatGPT for Teams or Gemini) can be used for **non-code technical queries** — architecture questions, documentation help, etc.
- Don't use non-approved AI tools for any development work

> **Example:** You need help designing a database schema. GitHub Copilot is approved for writing the actual SQL or migration code. For a higher-level architecture question — "What's the best indexing strategy for this query pattern?" — you can use ChatGPT for Teams or Gemini. But a random AI tool you found online? Not approved, even if it looks helpful.

### Review and Test Everything

AI-generated code is **untrusted input** until you've verified it:

- **Carefully review** all AI suggestions for correctness and security before committing
- **Test** AI-generated code just like you'd test any code — unit tests, integration tests, security scans
- Never assume AI output is correct just because it looks reasonable

> **AI tools are autocomplete on steroids — not a senior engineer.** They can produce code that compiles, passes basic tests, and still contains security vulnerabilities, logic errors, or license violations.

> **Example:** Copilot suggests an authentication function that hard-codes a JWT secret as a string constant. It compiles and works in tests. But in a code review, you'd immediately flag it — secrets belong in an approved secret manager, not in source code. This is exactly the kind of thing AI tools get wrong.

### Document AI Usage

Transparency matters in code review:

- **Describe AI assistance in your pull request description** so reviewers know which sections were AI-generated
- This lets reviewers apply **extra scrutiny** to those sections
- It's not about judgment — it's about making review more effective

### No Sensitive Data in AI Tools

This rule applies to all AI tools, including Copilot:

- **Never use Confidential, Restricted, or CUI data** as prompts or context
- Don't paste production secrets, API keys, or customer data into any AI interface
- If you need to ask an AI tool about a pattern, use **generic or synthetic examples**

> **Example:** You want to ask Copilot how to handle a specific API authentication flow for a federal client. Don't paste the real API endpoint, client credentials, or CUI data into the prompt. Instead, describe the pattern generically: "How do I implement OAuth2 client credentials flow with token rotation?" You get the same useful answer without exposing anything sensitive.

### Module B Quiz

You are using GitHub Copilot and it suggests a function that handles authentication. What should you do?

- [( )] Accept it — Copilot is an approved tool
- [(X)] Review the suggestion carefully for correctness and security, test it, and note AI usage in your PR description
- [( )] Replace it with code from Stack Overflow
- [( )] Accept it but add a comment "AI generated"
***

**Correct!** Being an approved tool doesn't mean the output is automatically safe. Review AI-generated code carefully — especially security-sensitive functions like authentication. Test it thoroughly and document AI usage in your PR so reviewers know to give those sections extra attention.

***

## Module C — Open-Source and Supply Chain

Every open-source library you add to a project is a dependency — and a potential attack surface. This module covers how to treat third-party software with the care it deserves.

### FOSS as Suppliers

CivicActions treats open-source libraries and containers the same way we treat commercial vendors — as **suppliers**:

- Require **SBOMs** (Software Bills of Materials) for third-party components
- **Triage known vulnerabilities** before adding a dependency
- **Verify license compliance** — some licenses have restrictions that may conflict with client contracts
- **Assess maintainer health** — is the project actively maintained? How many contributors does it have?

> **Example:** Before adding a new npm package to your project, you check: Does it have an SBOM? Are there any known CVEs? What's its license — is it compatible with the client's contract? When was the last commit? If the package has 1 contributor, no releases in 8 months, and 30 open security issues, that's a red flag — even if the API is exactly what you need.

### SCA in CI/CD

Your CI/CD pipeline should include automated security scanning:

- **SCA** (Software Composition Analysis) checks third-party dependencies for known vulnerabilities
- **SAST** (Static Application Security Testing) scans your code for common flaws
- **DAST** (Dynamic Application Security Testing) tests running applications
- Results feed into **Dependency-Track** for centralized visibility
- **Remediate Critical and High vulnerabilities before release** — these are blockers, not nice-to-haves

> **Example:** Your CI pipeline runs Dependabot for dependency scanning and feeds results into Dependency-Track. On a Friday afternoon, a PR triggers a Critical vulnerability alert in a transitive dependency. It's tempting to merge and fix it Monday — but Critical and High findings are release blockers. You update the dependency, re-run the pipeline, and the alert clears before the PR is merged.

### Unmaintained Components

An open-source library that nobody is maintaining is a ticking time bomb:

- Components with **no updates in over one year** must be assessed
- Options: **isolate** the component (limit its access and exposure), or **replace** it with an actively maintained alternative
- Don't wait for a vulnerability to be discovered — proactive assessment is required

> **Example:** Your project uses a Node.js logging library that hasn't had a release in 14 months. No CVEs have been filed against it — yet. But per policy, it needs to be assessed. You check the repo: the sole maintainer hasn't responded to issues in months. The team decides to replace it with a well-maintained alternative rather than waiting for a vulnerability to surface.

### SBOM Requirements

SBOMs are central to supply chain security:

- **SBOM required at intake** for all third-party software
- CI/CD pipelines enforce **SBOM refresh** — the SBOM is updated on each release
- This gives CivicActions (and clients) a clear picture of what's in the software

### Prohibited Technologies

Before adding any new dependency or tool:

- **Screen it against the prohibited technology list**
- Check for **DFARS restrictions** — some technologies are not permitted on DoD-related projects
- Do this at intake, not after you've already integrated it

> **Example:** A developer on a DoD project wants to add a container image from a public registry. Before integrating it, they check: Is this image on the prohibited technology list? Are there DFARS restrictions that apply? Does the image come with an SBOM? These checks happen *before* writing the Dockerfile, not after the feature is built.

### Module C Quiz

An open-source library used in a project has not received any updates in over a year. What does the Third-Party Management Policy require?

- [( )] Continue using it — open source is always safe
- [(X)] Treat it as unmaintained: assess maintainer health and isolate or replace the component
- [( )] Fork it and maintain it yourself without further review
- [( )] No action needed until a vulnerability is discovered
***

**Correct!** Open-source libraries without updates for over a year must be assessed. The options are to isolate the component (limit its access and blast radius) or replace it with an actively maintained alternative. Waiting for a vulnerability to appear is reactive — CivicActions requires proactive assessment.

***

## Module D — Access and Identity for Developers

Developers often have elevated access — to production systems, CI/CD pipelines, and infrastructure. This module covers how to manage that access responsibly.

### SSH Keys and API Tokens

Your SSH keys and API tokens are as sensitive as passwords:

- Follow the **CivicActions naming conventions** so keys are identifiable
- Every key must be **linked to your individual identity** — no shared keys
- **Rotate** keys and tokens on schedule — **quarterly minimum**
- **Revoke immediately** on role change or departure

> **A leaked API token is an open door.** Treat your keys with the same care as your password — and rotate them on schedule even if you don't think they've been exposed.

> **Example:** Your SSH key for GitLab follows the naming convention `firstname.lastname-gitlab-projectx` so it's immediately identifiable. It's linked to your `firstname.lastname@civicactions.com` identity, and you have a quarterly Jira reminder to rotate it. When you move to a different project, you revoke the old key as part of the transition — don't leave stale keys lying around.

### CI/CD Pipeline Credentials

Pipelines need credentials too, and they have their own rules:

- Use **separate service accounts per pipeline** — don't share service accounts across pipelines
- Apply **least privilege** — each pipeline gets only the access it needs
- **Never embed secrets in code or config files** — not in source code, not in environment files checked into Git
- Use **approved secret management tools** (like vault services) to manage pipeline secrets

> **Example:** Your GitHub Actions workflow needs a deploy token for the production environment. Instead of putting it in a `.env` file committed to the repo, you store it in the repository's encrypted secrets (or an external vault). The pipeline pulls it at runtime, and it never appears in logs, code, or config files. If someone forks the repo, the secret doesn't come with it.

### Risk Context

Not all systems are equal, and you should know the difference:

- Understand which systems are classified as **CIA "High"** — these require extra controls
- Apply **proportional controls**: more peer review, formal change records, stronger encryption
- Know how to check the **Risk Register** for system classifications

If you're unsure whether a system requires elevated controls, check the Risk Register or ask your project lead.

> **Example:** You're assigned to a new project and aren't sure about its CIA classification. You check the Jira Continual Improvement project where the Risk Register lives and see the system is rated CIA "High" for confidentiality. That means: additional code review rigor, formal change records for significant changes, FIPS-validated encryption for data at rest and in transit, and quarterly access reviews. Knowing this upfront shapes how you work from day one.

### Module D Quiz

Where should CI/CD pipeline secrets (like API keys and service account credentials) be stored?

- [( )] In environment variables within the Git repository
- [( )] In a shared document accessible to the dev team
- [(X)] In approved secret management tools — never embedded in code or config files
- [( )] In comments within the pipeline configuration file
***

**Correct!** Secrets must never be stored in code, config files, or Git repositories — even in environment variable files that are committed. Use approved secret management tools (vault services) that provide encryption, access control, and audit logging. Shared documents are also not acceptable — they lack the security controls that proper secret management provides.

***

## Bonus Quiz

You've completed all four modules — excellent work! Here's a final question on a key development security concept.

You're starting a new project and need to implement user authentication. What's the best approach?

- [( )] Write a custom authentication library from scratch to meet the project's exact needs
- [( )] Copy authentication code from a previous project without reviewing it
- [(X)] Use a pre-approved authentication library and integrate it with automated security checks in the CI/CD pipeline
- [( )] Let the AI coding tool generate the entire authentication system and deploy it directly
***

**Correct!** "Shift-left" means using **pre-approved libraries** for security-critical functions like authentication — not building from scratch. Custom authentication code is one of the most common sources of security vulnerabilities. Pre-approved libraries have been vetted, and integrating them with automated CI/CD security checks means problems are caught early, not in production.

***

## Course Complete

Congratulations — you've finished **Secure Development & Supply Chain**!

Here's what you covered:

1. **Secure engineering principles** — shift-left security, design principles (least privilege, zero trust, defense in depth), no real data in test environments, mandatory code review
2. **AI-assisted development** — Copilot only for code, review and test all AI output, document AI usage in PRs, no sensitive data in prompts
3. **Open-source and supply chain** — treat FOSS as suppliers, SCA/SAST/DAST in CI/CD, assess unmaintained components, SBOM at intake, screen against prohibited tech lists
4. **Access and identity** — rotate SSH keys and tokens quarterly, separate pipeline service accounts, use secret management tools, know your CIA "High" systems

**Remember the essentials:**

- Use pre-approved libraries for security-critical functions — don't roll your own
- Treat AI-generated code as untrusted input — review, test, and document it
- Every open-source dependency is a supply chain link — assess it before you add it
- Never put secrets in code or config files — use proper secret management
- Know which systems are CIA "High" and apply proportional controls

Questions? Reach out to **security@civicactions.com** or your engineering lead.
