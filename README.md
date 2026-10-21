# AI Instructions

Shared local-agent instructions for research Python projects.

## Layout

- `AGENTS.md`: Main instruction entry point.
- `USAGE.md`: How to adopt this repository as a submodule in a project.
- `CHANGELOG.md`: High-level changes to this instruction repository.
- `rules/INDEX.md`: Routing table for deciding which rules apply.
- `rules/`: Canonical coding and project standards.
- `commands/`: Reusable workflows, invoked as Claude Code slash commands.
- `modules/`: Reusable instruction modules.
- `profiles/`: Machine-specific runtime profiles.
- `boilerplate/README.md`: Reference `pyproject.toml`/`.pre-commit-config.yaml`/CI
  workflow/`.gitignore` templates per project tier, used by
  `commands/boilerplate-update.md`.
- `skills/`: Personal Claude Code skills (for example `phd-supervisor`), installed
  globally by symlink, not per project. See `skills/README.md`.

## Workflow

Projects are assumed to use GitHub workflow: issue, branch, pull request, review, then
merge after approval or wait for collaborator feedback. See
`modules/github-workflow.md`.

## Use As A Submodule

From a research project:

```sh
git submodule add <repo-url> .ai-instructions
```

Then point your editor extension or agent startup command at
`.ai-instructions/AGENTS.md`. See `USAGE.md` for project-level entrypoint examples.

## Rules And Commands

Keep coding standards in `rules/` and reusable command workflows in `commands/`. These
are the canonical files. If a tool expects another layout, mirror or symlink these files
into that tool-specific location and keep edits here.

`AGENTS.md` is a router, not a request to load every file. In normal project work, read
`rules/INDEX.md` and then load only the rules that match the current project and task.

## Python Utilities

This repository includes a minimal Pixi environment for its own maintenance tasks. There
is no Python source in this repository — these tasks lint/format its config and Markdown
files.

| Task                  | Purpose                                                                 |
| --------------------- | ----------------------------------------------------------------------- |
| `pixi run check`      | Run yamllint.                                                           |
| `pixi run lint`       | Same as `check`.                                                        |
| `pixi run format`     | Format `pyproject.toml` with `pyproject-fmt`.                           |
| `pixi run pre-commit` | Run the full pre-commit hook suite. This may need network on first use. |

## License And Attribution

Released under the MIT License, see [`LICENSE`](LICENSE).

The repository layout (profiles, commands, boilerplate) and parts of
`boilerplate/README.md` are derived from
[OpenSourceEconomics/ai-instructions](https://github.com/OpenSourceEconomics/ai-instructions)
(MIT, Copyright (c) 2026 Hans-Martin von Gaudecker and the Open Source Economics team).
That copyright notice is kept in `LICENSE`.
