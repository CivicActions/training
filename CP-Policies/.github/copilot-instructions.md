# Project Guidelines

## Architecture
- This project transforms 17 CivicActions security policies into 6 role-based training courses.
- Pipeline: `policies/` (source markdown from Confluence) → `outcomes/` (learning outcome tables + CSV/mappings) → `outlines/` (course structure) → `drafts/` (LiaScript interactive courses with quizzes).
- `policies-HTML/` is the raw Confluence HTML export (gitignored); `policies/` contains the markdown conversions that are the working source.
- Compliance scope: CMMC L1/L2, ISO 27001:2022, FAR 52.204-21, ITIL.

## Build and Test
- No package manager, build step, or automated test suite.
- `outcomes/generate_csvs.py` regenerates all CSV and mapping files from the outcome markdown tables. Run with `python3 outcomes/generate_csvs.py`.
- Preview LiaScript courses at `https://liascript.github.io/course/?YOUR_RAW_URL` or with the LiaScript VS Code extension.
- Do not invent setup or lint commands unless the user explicitly asks.

## Conventions
- **Policies:** Markdown files named `Policy-Name_<page-id>.md`; some use only the numeric Confluence page ID. Preserve Confluence structure and naming.
- **Outcomes:** Each policy has three files: `<policy>-outcomes.md` (markdown table), `<policy>-outcomes.csv` (CSV with Training Name/Module columns), `<policy>-mappings.md` (summary of training assignments). CSV columns: `Policy,Section,Training Name,Module,Audience,Learning Outcome`.
- **Outlines:** Named `01-security-awareness-essentials.md` through `06-access-governance-risk-supplier.md`. Each contains audience, prerequisites, module breakdown with outcome sources, sample quiz questions, and outcome coverage summary.
- **Drafts:** LiaScript format — header metadata in `<!-- -->` HTML comment (author, email, version, language, narrator), `#`/`##`/`###` sections as slides, `[(X)]`/`[( )]` for single-choice quizzes, `[[X]]`/`[[ ]]` for multiple-choice, `***` delimiters for solution blocks. One `README.md` per training in its own subfolder.
- Module references use letter + title format: `A - Your devices and workspace`.

## Gotchas
- The 193 outcome rows across 17 policies map to 6 trainings via `outcomes/generate_csvs.py`. If outcome tables change, re-run the script to regenerate CSVs and mappings.
- `policies-HTML/` is gitignored. The `policies/` markdown folder is the tracked source of truth.
- Some policies target multiple audiences (e.g., "All Staff; Developers (deeper)"). The mapping assigns each outcome to its primary training; some rows appear in multiple trainings via the outlines' "Outcome sources" cross-references.
- Drafts are at 8th–10th grade reading level. Maintain this when editing course content.