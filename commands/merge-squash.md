---
description: Squash-merge the current PR, clean up branches and worktrees, and pull main
argument-hint: [pr-number]
allowed-tools: Bash, Read
---

# Merge Squash

Squash-merge the pull request under discussion, delete its local and remote branches and
worktrees, and update local `main`.

Invoking this command is the user's approval to merge (see "Agent Behavior" in
`modules/github-workflow.md`). Use `merge-commit.md` instead to keep the branch's
commits behind a merge commit.

## Inputs

- `$ARGUMENTS`: PR number. If empty, use the PR under discussion in this conversation;
  otherwise the PR of the current branch (`gh pr view --json number`). If none can be
  determined, ask.

## Workflow

Follow `merge-commit.md`, with these differences:

1. Steps "Inspect the PR" and "Find the checkouts" are identical.
1. **Merge** with a squash commit instead of a merge commit:
   `gh pr merge <number> --squash --subject "<PR title> (#<number>)" --body-file <file>`.
   - Subject: the PR title plus ` (#<number>)`.
   - Body: the PR description with the closing `Fixes #<issue>` line kept, not the list
     of squashed commit messages. Write it to a temporary file in `$CLAUDE_JOB_DIR/tmp`
     when set, else a `mktemp` file, and delete it afterwards.
   - End the body with the attribution trailer from `modules/github-workflow.md`
     (`Co-Authored-By: Claude <model name> <noreply@anthropic.com>`) when an agent
     authored the change.
   - Still no `--delete-branch`.
1. **Cleanup** is identical, with one change: a squash merge leaves the head branch's
   commits unreachable from `main`, so `git branch -d` refuses. After confirming
   `gh pr view <number> --json state` reports `MERGED`, delete the local branch with
   `git branch -D <head>`. That is the only place `-D` is allowed.
