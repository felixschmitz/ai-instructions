---
description: Generate a pytask task file from a description
argument-hint: <description of what the task should do>
allowed-tools: Read, Grep, Glob, Write, Edit
---

# New Task

Generate a pytask task file based on the user's description: **$ARGUMENTS**

## Steps

1. **Understand the project layout.** Read the project's `config.py` to find:

   - `SRC`, `ROOT`, `BLD`, and the `bld/data/{raw,interim,processed,external}` /
     `bld/figures` constants (see `rules/project-structure.md`)
   - Whether a `DataCatalog` is used (and its variable name)
   - Existing task files and domain subpackages under `src/<project>/` for
     naming/numbering conventions

1. **Determine inputs and outputs** from the user's description.

1. **Generate the task file** following these patterns:

### Task file template

```python
from pathlib import Path
from typing import Annotated

import pandas as pd
from pytask import Product

from <package>.config import DATA_RAW, DATA_PROCESSED


def task_<name>(
    input_file: Path = DATA_RAW / "<input>.arrow",
    output_file: Annotated[Path, Product] = DATA_PROCESSED / "<output>.pkl",
) -> None:
    """<Brief description>."""
    raw = pd.read_feather(input_file)
    result = _<helper_name>(raw)
    result.to_pickle(output_file)


def _<helper_name>(data: pd.DataFrame) -> pd.DataFrame:
    """<Pure function that does the actual work>."""
    ...
```

### With DataCatalog

If the project uses a `DataCatalog`, use catalog references instead of raw paths:

```python
from <package>.config import DATA_CATALOG


def task_<name>(
    input_file: Path = DATA_CATALOG["<input>"],
    output_file: Annotated[Path, Product] = DATA_CATALOG["<output>"],
) -> None: ...
```

## Rules

- **File naming**: `task_<descriptive_name>.py`
- **Function naming**: `task_<descriptive_name>` matching the file
- **Separation of concerns**: Task function handles I/O only (read input, call helper,
  write output). Helper function contains all logic and is pure.
- **Type hints**: All function signatures must have full type annotations
- **Annotated[Path, Product]**: Always use this for output parameters
- **Helper functions**: Prefix with `_`, make them pure (no I/O), make them testable
- **One task per file** unless tasks are closely related
- **Imports**: Use project's config module for paths, not hardcoded strings

## After generating

- Place the file in the project's relevant domain subpackage under `src/<project>/`
  (organized by what the code does — data, features, econometrics, models, evaluation —
  not by pipeline stage; see `rules/project-structure.md`), never in a
  `data_management/`/`analysis/`/`final/`-style stage directory
- If using DataCatalog, add new entries to `config.py`
- Remind the user to run `pixi run pytask --collect-only` to verify the task is
  discovered
