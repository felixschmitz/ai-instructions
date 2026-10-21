# Project Structure

Research projects use a `src/` + `bld/` layout:

```
src/<project>/
├── config.py           # defines SRC / ROOT / BLD / data-stage paths
└── <domain>/           # one subpackage per pipeline concern — organize by what the
    └── __init__.py     # code does (e.g. data, features, econometrics, models,
                         # evaluation), not by pipeline stage
bld/                     # generated outputs, entirely gitignored
├── data/
│   ├── raw/
│   ├── interim/
│   ├── processed/
│   └── external/
└── figures/
tests/
pyproject.toml
```

`config.py` derives every path from `__file__` and creates the `bld/` subdirectories on
import, so the tree is usable immediately without committing placeholder files inside a
directory that is meant to stay untracked:

```python
from pathlib import Path

SRC = Path(__file__).resolve().parent
ROOT = SRC.parent.parent
BLD = ROOT / "bld"

DATA_RAW = BLD / "data" / "raw"
DATA_INTERIM = BLD / "data" / "interim"
DATA_PROCESSED = BLD / "data" / "processed"
DATA_EXTERNAL = BLD / "data" / "external"
FIGURES = BLD / "figures"

for _path in (DATA_RAW, DATA_INTERIM, DATA_PROCESSED, DATA_EXTERNAL, FIGURES):
    _path.mkdir(parents=True, exist_ok=True)
```

Nothing under `bld/` is version controlled, including raw data — treat raw data as a
regenerable artifact that code fetches or downloads, not a file checked into git. Never
rely on manual execution order; let pytask resolve dependencies once a project adopts
it.

## AI agent instruction files

Each project root has `AGENTS.md` (the content) plus thin `CLAUDE.md` wrapper,
containing only `@AGENTS.md`. When `AGENTS.md` lives in a parent directory or submodule,
adjust the include path accordingly (e.g. `@../AGENTS.md`).
