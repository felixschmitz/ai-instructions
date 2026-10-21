# Shared AI Instructions

Guidelines for AI agents working on research Python projects, mostly derived from
[Effective Programming Practices for Economists](https://effective-programming-practices.vercel.app/).
These capture *deltas from a capable agent's defaults* — ecosystem-specific tool choices
and opinionated rules. Generic best practice a strong model already follows is omitted.

______________________________________________________________________

## Routing

1. Identify the work type before applying detailed instructions:
   - research Python project
   - slides or document-only work
   - local LLM/runtime setup
   - command or rule maintenance
1. Do not apply Python research-project rules to slide-only work or edits to this
   instruction repository unless the task is explicitly about Python code.
1. Prefer the user's current project instructions over this shared library when they
   conflict. Use this repository to fill gaps, not to override local truth.

## Execution Defaults

- State assumptions when they affect the implementation, interpretation, or review.
- Ask before editing only when ambiguity changes the likely outcome or creates material
  risk.
- Prefer the smallest verifiable change that solves the task.
- Do not add speculative features, abstractions, configurability, or tool setup.
- Touch only files needed for the task, and match the existing project style.
- Mention unrelated issues instead of fixing them silently.
- Avoid disproportionate error handling for scenarios outside the stated task.
- Define the verification command or evidence before finishing.

## Data Boundary

- Local model requests may include project code, notes, logs, and retrieved context.
- External tools may be used only for public information lookup unless the user
  explicitly approves sharing specific private context.
- Before calling an external tool, remove private code, data, notes, file paths,
  credentials, unpublished research text, and project-specific logs from the query.
- If external lookup requires private project context, summarize the question abstractly
  or ask the user before sending anything specific.

______________________________________________________________________

# Python Code Standards

Type hints, immutability, Pixi usage, naming, docstrings, testing, type checking, and
verification steps for Python code live in `rules/core-python.md`, not here — it is
loaded automatically per the "Research Python Projects" routing below and by
`rules/INDEX.md` whenever a task touches Python code in a research project. Keeping a
parallel copy in this always-loaded file let it drift out of sync with
`rules/core-python.md` in the past (e.g. the Python version floor and the `ty`/`prek`
wiring); do not reintroduce that duplication.

______________________________________________________________________

## Default Context

For all work, read these files as needed:

- `modules/tools.md`
- `modules/github-workflow.md`
- `profiles/<tier>.md` to load a curated bundle of files for the current work tier (e.g.
  `tier-a`, `tier-b-course`, `tier-b-research`, `tier-c`), when the user points at one
  directly instead of relying on the routing above

## Research Python Projects

For a research Python project, first read:

- `modules/research.md`
- `rules/INDEX.md`
- `rules/core-python.md`
- `rules/project-structure.md`

Then read additional rules from `rules/INDEX.md` only when the project imports,
configures, or asks about the relevant package or workflow.

## Slides And Document-Only Work

For slides, papers, reports, or prose-only edits, follow the user's document
requirements and project-local instructions. Do not apply Python coding rules unless the
task also edits code or computational build steps.

## Command And Rule Maintenance

For edits to this instruction library:

- `rules/README.md`
- `commands/README.md`
- `rules/INDEX.md` when changing rule applicability

Keep rule and command files as plain Markdown: title first, then a short summary, then
the body. Store applicability and routing decisions in `rules/INDEX.md`.

## Command Workflows

Use `commands/` only when the user asks for that workflow or the task directly matches
it:

- `commands/new-task.md`
- `commands/verify-standards.md`
- `commands/boilerplate-update.md` (reference templates live in `boilerplate/README.md`)
- `commands/add-package-rule.md`
- `commands/review-pr-against-instructions.md`
