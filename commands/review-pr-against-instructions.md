---
description: Independently review a pull request's diff for compliance with this project's instructions and workflow conventions
---

# Review PR Against Instructions

Independently review a pull request's diff for compliance with this project's AI agent
instructions and workflow conventions.

Run as a fresh agent session with no memory of implementing the change — this is a cold,
adversarial read, not a self-check.

## Inputs

- PR number or branch name.
- This project's root `AGENTS.md` and the routed `rules/`/`modules/` files that apply to
  the changed paths (per `rules/INDEX.md` if present).

## Workflow

1. Get the diff: `gh pr diff <number>` (or `git diff main...<branch>` if no PR exists
   yet). Re-read `AGENTS.md` and the routed instructions now — do not rely on memory of
   them from earlier in the conversation.
1. Check code-level standards using `verify-standards.md`'s checklist, scoped only to
   the files touched by this diff, not the whole codebase.
1. Check the diff against `modules/github-workflow.md`'s workflow conventions:
   - branch name matches `issue-<number>-<short-description>`
   - a `CHANGELOG.md` entry was added under `[Unreleased]` if behavior, dependencies, or
     structure changed
   - a `Co-Authored-By: Claude <model name> <noreply@anthropic.com>` trailer is present
     if the change is agent-authored
1. Check scope: does the diff touch only files needed for the stated issue or task? Flag
   unrelated changes.
1. Check verification: are tests added for new behavior, and are the verification
   commands the PR claims to have run actually appropriate for the change?
1. Report findings grouped by severity (blocking / worth fixing / minor), each citing
   the exact file, line, and instruction violated. If nothing is wrong, say so briefly
   rather than manufacturing findings.

## Reporting Rules

- Cite the exact file and rule for every finding; a vague "doesn't follow conventions"
  is not actionable.
- Do not flag implementation choices the instructions are silent on.
- Keep the report short enough to post as a single PR comment.
