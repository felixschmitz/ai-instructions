# Polars Standards

Polars-specific practices for data management and tabular transformations.

## Apply When

The code imports `polars` or the task concerns tabular data management in a project that
uses Polars. Projects using pandas follow `pandas.md` instead; do not mix the two
libraries within one pipeline stage.

## Core Practices

- Write expressions, not loops: build transformations from `pl.col(...)` expressions
  inside `select`, `with_columns`, `filter`, and `group_by(...).agg(...)`.
- Never iterate over rows (`iter_rows`, `rows`, `to_dicts`) and never use row-wise
  `map_elements` for logic that expressions can express. Use `map_batches` only to hand
  whole columns to a vectorised NumPy/SciPy function.
- Use window expressions (`.over(...)`, `.rolling_*`, `.shift`, `.cum_*`) for per-group
  and time-window features instead of per-group Python loops.
- Use lazy evaluation for multi-step transformations: `pl.scan_csv` / `pl.scan_parquet`,
  chain expressions, then `.collect()` once at the end of the pure function or at the
  task boundary.
- Frames are immutable. Build new frames with `with_columns`; never mutate a frame in
  place.
- Touch each variable once in cleaning functions: one `with_columns` per logical step,
  explicit dtype casts, explicit column names.

## Joins And Keys

- Always specify `on=` (or `left_on=` / `right_on=`) and `how=` explicitly.
- Pass `validate=` (for example `"m:1"`) so unexpected key duplication fails loudly.
- Prefer normalised intermediate tables and join late in the pipeline.

## Types

- Declare dtypes explicitly when reading data (`schema_overrides=`) and when
  constructing frames; use `pl.Enum` / `pl.Categorical` for categorical columns and
  `pl.Date` / `pl.Datetime` for time columns, never strings that look like dates.
- Parse dates once at the cleaning boundary with `str.to_date(format)` and an explicit
  format.
- Missing values are `null`, not `NaN`. Convert deliberately at library boundaries
  (`fill_nan`, `fill_null`, `drop_nulls`).

## File Formats

- Use `.parquet` for intermediate and shareable files (`write_parquet`, `read_parquet`,
  `scan_parquet`).
- Keep raw downloads in their original format (for example `.csv`) and convert to
  Parquet in the first cleaning task.

## NumPy And Scikit-Learn Boundary

- Convert to NumPy only at the boundary of a library that requires arrays
  (`DataFrame.to_numpy()`, `Series.to_numpy()`), and convert results back with an
  explicit schema.
- Keep the conversion inside the pure helper that calls the library, not in tasks.

## Testing

- Compare frames with `polars.testing.assert_frame_equal`; set `check_exact=False` and
  explicit tolerances for floating-point columns.
- Construct small test frames inline with explicit schemas.

## Agent Behavior

- Do not introduce pandas into a Polars project, including for plotting; pass Polars
  frames directly to Plotly or convert at the plotting boundary only.
- When translating pandas code, replace index-based logic with explicit key columns;
  Polars has no index.
