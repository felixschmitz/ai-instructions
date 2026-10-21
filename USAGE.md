# Use In A Project

Add this repository as a submodule or sibling checkout, then point the project's root
instruction file at `.ai-instructions/AGENTS.md`.

Projects are expected to use GitHub version control: issue, branch, pull request,
review, then merge after approval or wait for collaborator feedback.

## Project Entrypoint

A project-level `AGENTS.md` can be short:

```md
# Project Instructions

First read `.ai-instructions/AGENTS.md`.

This is a research Python project. Apply the research-project routing rules
there, then prefer this project's local files when they conflict.
```

## Submodule Setup

Add the shared instructions to a project:

```sh
git submodule add <repo-url> .ai-instructions
git commit -m "Add shared AI instructions submodule"
```

After cloning a project with this submodule:

```sh
git submodule update --init --recursive
```

Update the submodule to the latest shared instructions:

```sh
git -C .ai-instructions pull
git add .ai-instructions
git commit -m "Update shared AI instructions"
```

Pinning the submodule commit is intentional. It makes instruction changes reviewable in
each project.

For non-code projects, be explicit:

```md
# Project Instructions

First read `.ai-instructions/AGENTS.md`.

This is a slide/document project. Do not apply Python research-project rules
unless the current task edits code or computational build steps.
```

## Workflow Checklist

1. Read the GitHub issue or task instructions.
1. Check the project branch and working tree.
1. Create or switch to a task branch.
1. Read the project root `AGENTS.md`, then this submodule's `AGENTS.md`.
1. Load only the routed rules and modules relevant to the task.
1. Define the expected outcome and verification evidence.
1. Make the smallest focused change that satisfies the task.
1. Run project verification commands and record the result.
1. Commit and open a pull request.
1. Review with the user and wait for approval or collaborator feedback before merge.

## Tool-Specific Copies

If an editor or agent requires rules in a specific local folder, mirror or symlink
selected files from `rules/`. Keep canonical edits in this repository.

See `boilerplate/README.md`'s "AI Tool Configuration" section for tool-specific setup,
including Claude Code's command-discovery hook.
