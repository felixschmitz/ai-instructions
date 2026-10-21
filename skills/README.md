# Skills

Personal Claude Code skills. Unlike `rules/`, they are not project standards: install
them once per machine, not per project.

## Install

From a local clone of this repository (not a project's submodule copy, so the skill
tracks `main`):

```sh
mkdir -p ~/.claude/skills
ln -sfn "$(pwd)/skills/phd-supervisor" ~/.claude/skills/phd-supervisor
```

## Available Skills

- `phd-supervisor`: invoke as
  `/phd-supervisor [survey|model|defend|paper|status] [topic]`. Reads private state from
  `~/.claude/phd/` (profile, concept notes) and per-project state from `.supervisor/`
  (gitignored). Neither is part of this repository; keep `~/.claude/phd/` in its own
  private repository.

## Skill Layout

Each skill is a folder with a lean `SKILL.md` that routes to files under `references/`
(read only when needed) and, where useful, runnable `templates/`. Keep `SKILL.md` short:
everything behind a file read costs no context until it is opened.
