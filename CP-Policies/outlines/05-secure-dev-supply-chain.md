# Training 5 — Secure Development & Supply Chain

| Field | Value |
|-------|-------|
| **Audience** | Developers (engineers, DevOps, anyone writing or deploying code) |
| **Prerequisite** | Training 1 (Security Awareness Essentials) |
| **Target duration** | 10–15 minutes |
| **Delivery** | Written module + quiz |
| **Cadence** | Onboarding (within 30 days) · annual refresher · ad-hoc on toolchain or policy change |
| **Compliance** | CMMC L2 SC.L2-3.13.1–3.13.15, SI.L2-3.14.1–3.14.7, SR.L2-3.17.1–3.17.3 · ISO 27001 A.8.25–A.8.28 |

---

## Purpose

This training covers developer-specific security responsibilities: secure engineering practices, AI-assisted coding rules, DevSecOps data handling gates, and open-source/third-party software supply chain management. It complements Training 3 (IT Operations) which covers the change/config/patch infrastructure developers operate within.

---

## Session outline

### Module A — Secure engineering principles (3–4 min)

**Outcome sources:** ISP, DSHP, AUP

1. **Shift-left security** — integrate security controls into CI/CD from the start; pre-approved libraries for authentication and cryptography; automated baseline enforcement in pipelines
2. **Design principles** — least privilege, zero trust, rapid rollback; design for defense-in-depth
3. **DevSecOps data handling** — never use real PII/Confidential data in test/dev environments; do not export PII from SaaS platforms for testing; use synthetic or anonymized data
4. **Code review obligations** — peer review is mandatory for all production code; for CIA "High" systems, additional review rigor applies
5. **Secure defaults** — remove non-essential services/components; ship with least-functionality baselines

### Module B — AI-assisted development (2–3 min)

**Outcome sources:** AIP

1. **GitHub Copilot only for code** — use GitHub Copilot exclusively for source code creation; other approved AI tools for non-code technical queries only
2. **Review and test** — carefully review all AI-generated code for correctness and security before committing; treat AI suggestions as untrusted input
3. **Describe AI usage** — document AI assistance in peer review requests so reviewers know to scrutinize AI-generated sections
4. **No sensitive data** — never use Confidential, Restricted, or CUI data as prompts or context in any AI tool

### Module C — Open-source and supply chain (3–4 min)

**Outcome sources:** TPM, VPM

1. **FOSS as suppliers** — treat open-source libraries and containers as suppliers: require SBOMs, triage known vulnerabilities, verify license compliance, assess maintainer health
2. **SCA in CI/CD** — SCA/SAST/DAST feed Dependency-Track; remediate Critical and High vulnerabilities before release
3. **Unmaintained components** — components with no updates in >1 year must be assessed, isolated, or replaced
4. **SBOM requirements** — SBOM required at intake for third-party software; CI/CD-enforced SBOM refresh; update on each release
5. **Prohibited technologies** — screen against the prohibited technology list and DFARS restrictions during intake

### Module D — Access and identity for developers (2–3 min)

**Outcome sources:** ACP, IdP, RSAP

1. **SSH keys and API tokens** — follow naming conventions; link to individual identity; rotate per schedule (quarterly minimum); revoke immediately on role change or departure
2. **CI/CD pipeline credentials** — separate service accounts per pipeline; principle of least privilege; never embed secrets in code or config files; use approved secret management tools
3. **Risk context** — understand which systems are CIA "High"; apply proportional controls (peer review, change records, encryption); know how to check the Risk Register for system classifications

---

## Quiz (sample — 3 questions)

1. **You are using GitHub Copilot and it suggests a function that handles authentication. What should you do?**
   - a) Accept it — Copilot is an approved tool
   - b) Review the suggestion carefully for correctness and security, test it, and note AI usage in your PR description ✅
   - c) Replace it with code from Stack Overflow
   - d) Accept it but add a comment "AI generated"

2. **An open-source library used in a project has not received any updates in over a year. What does the Third-Party Management Policy require?**
   - a) Continue using it — open source is always safe
   - b) Treat it as unmaintained: assess maintainer health and isolate or replace the component ✅
   - c) Fork it and maintain it yourself without further review
   - d) No action needed until a vulnerability is discovered

3. **You need test data that mirrors production for a new feature. What is the correct approach?**
   - a) Copy production data into the test environment
   - b) Export PII from the SaaS platform into a local database
   - c) Use synthetic or anonymized data — never use real PII/Confidential data in test/dev environments ✅
   - d) Ask a colleague to share their production access

---

## Outcome coverage

This training covers Developer-specific rows from:

- [ai-usage-outcomes.md](../outcomes/ai-usage-outcomes.md) — 2 developer rows (coding, peer review)
- [third-party-mgmt-outcomes.md](../outcomes/third-party-mgmt-outcomes.md) — 3 rows (FOSS, SBOM/SCA, prohibited tech)
- [info-security-outcomes.md](../outcomes/info-security-outcomes.md) — 1 row (secure engineering)
- [data-security-outcomes.md](../outcomes/data-security-outcomes.md) — 1 row (DevSecOps data handling)
- [acceptable-use-outcomes.md](../outcomes/acceptable-use-outcomes.md) — 1 row (developer-specific)
- [access-control-outcomes.md](../outcomes/access-control-outcomes.md) — 2 rows (CI/CD access, developer pipelines)
- [identification-outcomes.md](../outcomes/identification-outcomes.md) — 2 rows (SSH keys, service identities for devs)
- [risk-security-outcomes.md](../outcomes/risk-security-outcomes.md) — 1 row (developer risk context)
- [vuln-patch-outcomes.md](../outcomes/vuln-patch-outcomes.md) — 1 row (SCA/SAST/DAST in CI/CD)
