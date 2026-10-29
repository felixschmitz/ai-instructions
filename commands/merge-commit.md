---
description: Merge the current PR with a merge commit, clean up branches and worktrees, and pull main
argument-hint: [pr-number]
allowed-tools: Bash, Read
---

# Merge Commit

Merge the pull request under discussion with a merge commit, delete its local and remote
branches and worktrees, and update local `main`.

Invoking this command is the user's approval to merge (see "Agent Behavior" in
`modules/github-workflow.md`). Use `merge-squash.md` instead for a single squashed
commit.

## Inputs

- `$ARGUMENTS`: PR number. If empty, use the PR under discussion in this conversation;
  otherwise the PR of the current branch (`gh pr view --json number`). If none can be
  determined, ask.

## Workflow

1. **Inspect the PR.** `gh pr view <number> --json
   state,isDraft,mergeable,mergeStateStatus,headRefName,baseRefName,statusCheckRollup`.
   Stop and report instead of merging if the PR is not `OPEN`, is a draft, is not
   mergeable, or has failing required checks. Do not bypass with `--admin`.
1. **Find the checkouts.** The main checkout is the first entry of
   `git worktree list --porcelain`. Run the remaining steps from there (`git -C <main>`),
   not from a worktree that is about to be removed. List every worktree whose branch is
   the PR's head branch.
1. **Merge.** `gh pr merge <number> --merge`. Do not pass `--delete-branch`: it cannot
   delete a branch that is checked out in a worktree. If the merge is refused, report
   why and stop; leave all branches and worktrees untouched.
1. **Clean up** (see "Cleanup" below).

## Cleanup

Run only after the merge succeeded.

1. Remove each worktree of the head branch: `git worktree remove <path>`. Without
   `--force`: if it refuses because of uncommitted changes, report the path and leave it
   (and its branch) in place.
1. Switch the main checkout to the base branch and update it:
   `git -C <main> switch <base> && git -C <main> pull --ff-only`.
1. Delete the local branch: `git branch -d <head>`. `-d` is safe after a merge commit;
   if it refuses, the branch has unmerged commits, so report instead of forcing.
1. Delete the remote branch if it still exists (GitHub may have auto-deleted it):
   `git push origin --delete <head>`, ignoring "remote ref does not exist".
1. `git fetch --prune`, then `git worktree prune`.
1. Report: the merge commit SHA, which branches and worktrees were removed, anything left
   behind and why, and the new `main` HEAD.

Never delete the base branch, never use `git branch -D` or `--force` without asking, and
never touch branches or worktrees of other PRs.
