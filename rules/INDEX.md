# Rule Index

Routing table for deciding which shared standards apply to a task.

Use this file to choose rule files. Do not load every rule by default.

## Work-Type Routing

| Work Type                    | Read These Rules                                                            | Do Not Apply                            |
| ---------------------------- | --------------------------------------------------------------------------- | --------------------------------------- |
| Research Python project      | `core-python.md`, `project-structure.md`, then relevant package rules below | None                                    |
| Slides or document-only work | No coding rules by default                                                  | Python, package, plotting, pytask rules |
| This instruction repository  | No coding rules by default unless editing Python scripts                    | Research project layout rules           |
| Local LLM/runtime setup      | No coding rules by default                                                  | Python, package, plotting, pytask rules |

## Research Python Rule Routing

| Rule                   | Apply When                                                                                                                 |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `core-python.md`       | The task edits or reviews Python code in a research project.                                                               |
| `project-structure.md` | The task edits or reviews a research project's repository layout, build outputs, instruction files, or path configuration. |
| `pytask.md`            | The project uses pytask, has `task_*.py` files, or the task concerns data/build pipeline tasks.                            |
| `pandas.md`            | The code imports pandas or the task concerns tabular data management.                                                      |
| `numpy.md`             | The code imports NumPy or the task concerns array programming or simulation.                                               |
| `jax.md`               | The code imports JAX or the task concerns JAX-compatible numerical code.                                                   |
| `dags.md`              | The project uses `dags` or the task concerns function composition through dependency graphs.                               |
| `optimagic.md`         | The project uses optimagic or the task concerns numerical optimization.                                                    |
| `ml-econometrics.md`   | The task concerns prediction, causal inference, estimation, or model evaluation.                                           |
| `pyfixest.md`          | The project uses pyfixest or the task concerns fixed effects, IV, DiD, event studies, or regression tables in PyFixest.    |
| `maketables.md`        | The project uses maketables or the task concerns publication tables (regression, descriptive, balance, custom).            |
| `plotting.md`          | The task edits figure-generation code or asks for project plotting standards.                                              |
| `markitdown.md`        | The task converts documents (PDF, Office, images, audio, HTML, ...) to Markdown/text, or the project imports `markitdown`. |

## Selection Principles

- Load the smallest set of rules that covers the task.
- Apply package rules only when the package, workflow, or files are present.
- If a project-local instruction conflicts with a shared rule, follow the project-local
  instruction and mention the conflict.
- If uncertain whether a rule applies, inspect the project before loading more rules.
