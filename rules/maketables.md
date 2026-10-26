# Maketables Standards

Maketables-specific guidance for publication-ready regression, descriptive, balance, and
custom tables.

This rule applies to research Python projects that use `maketables`
(`import maketables as mt`) to produce tables for papers, slides, or reports.

## Apply When

- The code imports `maketables`, commonly as `import maketables as mt`.
- The task creates or edits regression tables, descriptive statistics, balance tables,
  or custom tables that end up in a paper, slides, or report.
- The task adds table support to a model class from another package.

## Core API

- `mt.ETable` builds regression tables from one or more fitted models. It supports
  pyfixest, statsmodels, linearmodels, lifelines, and Stata models. Other model classes
  work through the plug-in format below.
- `mt.DTable` builds descriptive statistics, optionally by groups (`bycol`).
- `mt.BTable` builds balance tables.
- `mt.MTable` builds a table from any pandas DataFrame.
- Typical use: `mt.ETable([est1, est2], labels={...}, caption="...")`, then `.make(...)`
  or `.save(...)`.
- Prefer `ETable` for tables that are published or saved. `pf.etable()` stays fine for
  exploration (see `pyfixest.md`).

## Output Formats

- `.make(type=...)` accepts `"gt"`, `"html"`, `"tex"`, `"typst"`, `"docx"`, and
  `"quarto"`. There is no Markdown type. With `type=None` it shows HTML, LaTeX, and
  Typst at once for notebooks and Quarto documents.
- `.save(type=..., file_name=...)` writes `"tex"`, `"typst"`, `"docx"`, or `"html"`.
  - Pass `show=False` in pipeline code, so no display object is returned.
  - Pass `replace=True` when a task regenerates the file. Without it an existing file
    raises.
  - Always pass `file_name` explicitly. The default path comes from class-level defaults
    and the table label.
- Style options go in `tex_style`, `typst_style`, `docx_style`, or `gt_style`. With
  `tab_width` in `tex_style`, the LaTeX document must load `tabularx` and `array`.
- Quarto papers render the same table as HTML in notebooks and as LaTeX or Typst in the
  PDF; do not hand-convert tables per format.

## ETable Conventions

- `labels` maps variable names (including the dependent variable) to readable names. Use
  `felabels` for fixed-effect rows, and `keep`, `drop`, `order`, and `feorder` to select
  and arrange rows. `exact_match=True` makes `keep` and `drop` match names exactly
  instead of by regular expression.
- Set `caption`, `tab_label`, `notes`, and `model_heads` explicitly for publication. Put
  the clustering and sample choices in `notes`.
- `model_stats` selects the bottom statistics (default: `N`, `r2`). Add
  `model_stats_labels` for readable names. Use `custom_stats` or `custom_model_stats`
  for values the model does not provide.
- `coef_fmt`, `signif_code`, and `digits` control coefficient display. Set them once per
  project so tables look alike.
- Treat the formats above as the installed version's API (maketables 0.2); check the
  current documentation before relying on options not listed here.

## Plug-In Format

To make a result class work with `ETable` without registering an extractor:

- Add a `__maketables_coef_table__` property returning a DataFrame with columns `b`,
  `se`, `p`, and optionally `t`, `ci95l`, `ci95u`.
- Optionally add `__maketables_stat__(key)`, `__maketables_depvar__`, and further
  `__maketables_*__` attributes.
- The package does not need to import `maketables`.
- For anything else, register a custom `ModelExtractor`. The plug-in specification is
  `PLUGIN_EXTRACTOR_FORMAT.md` in the maketables repository.

## Testing And Reproducibility

- Keep table construction in a pure function that returns the `ETable` object, and keep
  file writing in the task, so the construction is testable without files.
- Test the content, not only that a table exists: check that a known coefficient, the
  observation count, or a label appears in the rendered output (for example
  `table.make("tex")`).
- Write tables into the build directory, never the source tree, and regenerate them
  through the pipeline.

## Common Pitfalls

- Expecting Markdown output: use `"html"`, `"tex"`, `"typst"`, or `"docx"`.
- Forgetting `replace=True`, which makes the second pipeline run fail.
- Relying on the default save path instead of an explicit `file_name`.
- Passing models fitted with different samples without saying so; the table shows `N`
  per column, so state sample restrictions in `notes`.
- Using `pf.etable()` and `mt.ETable` in the same paper, which gives inconsistent
  formatting.

## Agent Behavior

- Verify option names against the current maketables documentation when changing table
  options; the package is young and options change between minor versions.
- Prefer the documentation's Markdown pages and `llms.txt` over memory.
- In reviews, check that labels, notes (clustering, sample), captions, and the set of
  reported statistics match the stated research design.
