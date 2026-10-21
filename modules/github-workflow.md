# GitHub Workflow

Assume projects use GitHub version control unless the user explicitly says otherwise.

## Branch Naming

Use `issue-<number>-<short-description>` (e.g. `issue-12-clean-umsatz`,
`issue-34-fix-outer-join`). If no issue exists for the work, create one first for
anything beyond a trivial fix.

## Standard Workflow

1. Start from a GitHub issue or task description whenever one exists.
1. Check out a new branch named `issue-<number>-<short-description>`.
1. Make focused changes that address the issue.
1. Run the relevant verification commands.
1. Open a pull request with a clear summary, verification notes, and links to the issue.
1. Spawn an independent review agent against the diff (see "Independent Review Before
   Merge" below) before asking the user to merge.
1. Review the pull request with the user.
1. Merge only after the user approves, or leave the PR open for feedback from others.

## Independent Review Before Merge

Before asking the user to merge, spawn a second agent session to review the PR diff
against this project's instructions. The agent that wrote the change is a poor judge of
its own compliance — it already believes its reasoning was correct.

- The reviewer must not have participated in writing the change. In Claude Code, use the
  `Agent` tool (a fresh subagent has no memory of the implementation); in other tools,
  start a new session or conversation.
- Give the reviewer only the PR diff (`gh pr diff <number>`) and the instruction files
  it needs — not the implementation rationale or prior conversation.
- Follow `commands/review-pr-against-instructions.md` for the reviewer's task definition
  and report format.
- Post the findings as a PR comment (`gh pr comment <number> --body-file <file>`), so
  they are visible without requiring CI infrastructure.
- The review is advisory: it surfaces instruction violations for the user to weigh, it
  does not block merge, and a clean report is one input to the merge decision, not
  approval.

This is a manually-invoked stand-in for CI-based review. Once a project has GitHub
Actions and an `ANTHROPIC_API_KEY` secret available, replace this manual step with a
`pull_request`-triggered workflow using Anthropic's official
[`claude-code-action`](https://github.com/anthropics/claude-code-action) running the
same prompt, instead of building a custom API-calling script.

## Changelog

Every pull request that changes behavior, dependencies, or repository structure adds an
entry under `[Unreleased]` in `CHANGELOG.md`, using the
[Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format. Do not bump the version
number as part of a feature/fix PR — that is a separate release step. If the project has
no `CHANGELOG.md` yet, create one the first time this applies.

## Attribution

When an agent authors a commit or a pull request, add a trailer identifying the
assisting model as the final line of the commit message, and again at the end of the PR
description body:

```
Co-Authored-By: Claude <model name> <noreply@anthropic.com>
```

Use the exact model name/version reported by the current session (e.g.
`Claude Opus 4.8`, `Claude Sonnet 5`) — never a placeholder or a hardcoded version,
since it goes stale as models change. Skip the trailer only when the user is committing
directly and the agent did not author the change.

## Local Safeguards Before Branch Protection

Until a project has GitHub branch protection configured on `main`, enforce the same
discipline locally with `prek` (or `pre-commit` in older projects) so agents cannot
bypass it by committing directly:

```yaml
- repo: https://github.com/pre-commit/pre-commit-hooks
  rev: v6.0.0
  hooks:
    - id: no-commit-to-branch
      args: [--branch, main]
- repo: local
  hooks:
    - id: require-issue-reference
      name: Require issue reference in commit message
      language: system
      entry: >-
        bash -c 'grep -qE "^(Merge|Revert)" "$1" || grep -qE "#[0-9]+" "$1" ||
        { echo "Commit message must reference an issue, e.g. \"Fixes #12\"." >&2; exit 1; }'
        --
      stages: [commit-msg]
```

Install both hook types after cloning: `prek install -t pre-commit -t commit-msg`. A
fast-forward merge (`git merge --ff-only`) does not create a commit and so does not
trigger `no-commit-to-branch`; use it to land a feature branch into `main` locally
before a project has a GitHub remote or branch protection.

## Agent Behavior

- Before editing, inspect the current branch and working tree.
- Do not commit unrelated local changes.
- Do not merge, close, or delete branches unless the user asks.
- Keep PR descriptions factual: what changed, why, and how it was verified.
- If the issue contains task instructions, treat it as the primary task source unless
  the user gives newer instructions in chat.
- If the user asks for review, use a code-review stance and focus on risks, regressions,
  missing tests, and unclear behavior.
