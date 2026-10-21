---
description: Create or update a routed package-specific rule from authoritative package documentation
---

# Add Package Rule

Create or update a routed package-specific rule from authoritative package
documentation.

## Inputs

Ask for or infer:

- package name
- package import name and common alias
- official documentation URL
- official `llms.txt`, `llms-full.txt`, skills page, or agent-facing guide when
  available
- whether the rule is for research Python projects, general Python utilities, document
  workflows, or another routed work type

## Source Policy

- Prefer official package sources over blogs, examples, or generated summaries.
- Treat an official skills page, agent guide, or LLM-oriented reference as acceptable
  direct source material for the rule.
- Use `llms.txt` as the documentation map: identify relevant Markdown pages, API
  references, tutorials, changelogs, and version-specific caveats.
- Do not copy an entire external reference into the rule. Extract stable, high-value
  conventions that agents need during code writing and review.
- Verify facts that are version-sensitive, surprising, or likely to change against the
  current official docs.
- Follow the global data boundary: send only public package names, public API questions,
  and sanitized examples to external tools.

## Rule Shape

Create or update `rules/<package>.md`.

Use the existing rule format:

```md
# <Package> Standards

<Package>-specific guidance for <main use case>.
```

Keep applicability rules in `rules/INDEX.md`, not in file-level metadata.

Recommended sections:

- `Apply When`
- `Core API`
- package-specific syntax or object model
- configuration and defaults
- performance or memory guidance when relevant
- testing and reproducibility guidance
- common pitfalls and version caveats
- plotting, tables, output, or serialization when relevant
- `Agent Behavior`

Keep the rule concise enough to load during normal coding sessions. If the package has
large APIs, prioritize the parts agents are likely to edit or review in this user's
research projects.

## Routing

Update `rules/INDEX.md` so agents can discover the rule. The routing row should state
when the package rule applies, not just repeat the package name.

Examples:

```md
| `pyfixest.md` | The project uses pyfixest or the task concerns fixed effects, IV, DiD, event studies, or regression tables in PyFixest. |
```

Only add the rule to root `AGENTS.md` if it changes top-level routing. Most package
rules belong only in `rules/INDEX.md`.

## Quality Checks

Before finishing:

1. Confirm the rule does not conflict with existing shared standards.
1. Confirm package rules apply only when routed by `rules/INDEX.md`.
1. Follow `modules/github-workflow.md` for branching, the `CHANGELOG.md` entry, and the
   commit/PR workflow (including the Attribution trailer). Do not re-derive a separate
   checklist here — that file is the source of truth and this one drifts if it repeats
   it.
1. Run this repository's own verification tasks, `pixi run check` and
   `pixi run pre-commit` (defined in `pixi.toml`) — not `rules/core-python.md`'s
   `prek`-based flow, which applies to downstream research projects, not to editing this
   repository.

## Response Template

Report:

- package rule created or updated
- official sources used
- routing added or changed
- checks run
- commit hash, if committed
