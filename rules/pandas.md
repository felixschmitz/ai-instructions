# Pandas Standards

Pandas-specific practices for data management and tabular transformations.

- Assume `pandas >= 3.0`. Do not configure legacy `pd.options` for copy-on-write or
  string inference.
- Use `engine="pyarrow"` when reading CSV files.
- Never use `inplace=True`.
- Prefer `.loc` for label-based selection and `.query()` for readable filters.
- Never iterate over rows with `iterrows()`, `itertuples()`, or row-wise `apply()`.
- Use pure, column-oriented data cleaning functions: build a fresh DataFrame, touch each
  variable once, and keep each transform explicit.
- Prefer normalized intermediate tables and merge only at the end of the pipeline.
- Always specify merge keys and join type explicitly.
- Use `.pkl` for private intermediate files and `.arrow` for shareable files.
