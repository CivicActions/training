---
description: "Add CivicActions-specific examples to a training course module. USE WHEN: enriching a draft course with realistic workplace scenarios, tool references, and day-to-day examples."
argument-hint: "Which course or module? e.g. 'Training 1 Module C' or 'all of Training 2'"
agent: "agent"
---

Add concrete, CivicActions-specific examples to the specified training module(s).

## Context

- Read the draft course at [drafts/](../drafts/) to understand the current content
- Read the corresponding outline at [outlines/](../outlines/) for outcome sources and coverage
- Read the relevant policy source(s) at [policies/](../policies/) for authoritative details

## CivicActions environment

Use these real tools and practices when crafting examples:

| Category | Tools / Services |
|----------|-----------------|
| **Identity & SSO** | Google Workspace (SAML/OIDC), YubiKey hardware keys, Rippling |
| **Communication** | Slack (#general, #loving-security), Zoom, Google Chat (DR fallback) |
| **Code & CI/CD** | GitHub, GitLab, GitHub Copilot, Dependabot / Dependency-Track |
| **Project mgmt** | Jira, Confluence |
| **Endpoints** | Kandji (macOS MDM), FileVault, CIS benchmarks |
| **Cloud** | Google Workspace Shared Drives, FedRAMP-equivalent CSPs for CUI |
| **HR / Onboarding** | Rippling, Culture Amp |
| **Incident** | security@civicactions.com, Slack #general, SIRT, Incident Commander role |
| **Work style** | Remote-first (no offices), macOS laptops, WPA2/WPA3 home Wi-Fi |

## Requirements

1. **Realistic scenarios** — frame examples as things a CivicActions team member would actually encounter (sharing a Google Doc, getting a Slack DM about a phishing email, onboarding a new SaaS tool, rotating a GitLab deploy token)
2. **Inline placement** — insert examples directly into the existing module text where they strengthen a point; do not create a separate "examples" section
3. **Tone** — conversational, 8th–10th grade reading level, matching the existing draft style
4. **Format** — use blockquotes (`>`) for short scenarios, or a brief narrative paragraph; keep each example to 2–4 sentences
5. **No invented policies** — only reference tools, channels, and processes documented in the policies/ folder
6. **Preserve structure** — do not change headings, quiz questions, or LiaScript metadata; only add example text within existing sections
