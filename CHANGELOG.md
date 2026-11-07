# Changelog

All notable changes to this repository are recorded here, following
[Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

- Add the `polars.md` package rule (expression-based data management with Polars) and
  route it in `rules/INDEX.md`.

- Add the `tier-d-project` profile for small, non-research coding projects: core Python,
  project structure, pytask, NumPy, and the GitHub workflow, with package rules (Polars,
  pandas, plotting, ML) routed through `rules/INDEX.md`.

- Relax the branch naming convention: tool-generated branch names are fine if the PR
  body links the issue; the PR review command checks the issue link instead.

- Add the `merge-commit` and `merge-squash` commands: merge the current PR, delete its
  local and remote branches and worktrees, and pull `main`.

- Add the `maketables.md` package rule (publication tables with `ETable`, `DTable`,
  `BTable`, `MTable`) and route it in `rules/INDEX.md`.

- Initial public release, derived from
  [OpenSourceEconomics/ai-instructions](https://github.com/OpenSourceEconomics/ai-instructions)
  (MIT). See `LICENSE`.
