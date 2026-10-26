# PyFixest Standards

PyFixest-specific guidance for econometric estimation, inference, and tables.

This rule applies to research Python projects using `pyfixest` for econometric
estimation, causal inference, fixed effects models, or regression tables.

## Apply When

- The code imports `pyfixest`, commonly as `import pyfixest as pf`.
- The task edits OLS, WLS, IV, Poisson, GLM, quantile regression, DiD, event-study, or
  regression-table code using PyFixest.
- The task asks for fixest-style formula syntax, fixed effects, clustered inference, or
  post-estimation output.

## Core API

- Use `pf.feols()` for OLS, WLS, IV, and fixed-effects linear models.
- Use `pf.fepois()` for Poisson models with fixed effects.
- Use `pf.feglm()` for GLM models with fixed effects.
- Use `pf.quantreg()` for quantile regression.
- Prefer `import pyfixest as pf` so examples, tables, and plotting calls stay compact.

## Formula Syntax

- Use fixest-style formulas with one to three parts separated by `|`.
- Use one-part formulas for models without fixed effects or IV: `"y ~ x1 + x2"`.
- Use two-part formulas for fixed effects: `"y ~ x1 + x2 | firm_id + year"`.
- Use two-part IV formulas without fixed effects: `"y ~ x1 | x_endog ~ z1 + z2"`.
- Use three-part IV formulas with fixed effects:
  `"y ~ x1 | firm_id + year | x_endog ~ z1 + z2"`.
- In IV models, write the IV part as `endogenous ~ instruments`.
- Do not specify multiple endogenous variables unless current PyFixest documentation
  confirms support for the version used by the project.
- Use `i()` for categorical indicators and interactions, and set reference categories
  explicitly when interpretation depends on the omitted category.
- Use `^` for interacted fixed effects, for example `"y ~ x | firm_id ^ year"`.
- Remember that `x1 * x2` expands to main effects plus the interaction, while `x1:x2` is
  the interaction term only.

## Multiple Estimation

- Prefer PyFixest multiple-estimation operators over repeated independent model calls
  when estimating systematic model variants.
- Use `sw()` for separate stepwise alternatives.
- Use `sw0()` when the baseline model without the stepwise terms is also needed.
- Use `csw()` for cumulative additions.
- Use `csw0()` when the baseline model and cumulative additions are both needed.
- Use `mvsw()` only when the full multiverse is substantively intended; it can expand
  quickly.
- Use `split` or `fsplit` for repeated subsample estimates. Use `fsplit` when the full
  sample estimate should be included with the split estimates.

## Inference

- Specify `vcov` deliberately; do not rely on an implicit default when inference
  matters.
- Use `"iid"` only when IID errors are substantively justified.
- Use `"hetero"` or `"HC1"` for heteroskedasticity-robust inference.
- Use `{"CRV1": "cluster_var"}` for cluster-robust inference.
- Use `{"CRV1": "var1 + var2"}` for two-way clustering.
- Use `{"CRV3": "cluster_var"}` when leave-one-cluster-out jackknife inference is
  appropriate and computationally feasible.
- Use `"NW"` or `"DK"` only with the required `vcov_kwargs`, including time identifiers
  and, where needed, panel identifiers and lags.
- Do not use `"HC2"` or `"HC3"` with fixed effects or IV unless the project version's
  documentation confirms support.
- Use `pf.ssc()` when small-sample correction choices need to be explicit and
  reproducible.

## Post-Estimation

- Use `.summary()` for human-readable summaries during exploration.
- Use `.tidy()` for programmatic tables of coefficients, standard errors, test
  statistics, p-values, and confidence intervals.
- Use `.coef()`, `.se()`, `.pvalue()`, `.confint()`, `.tstat()`, and `.vcov()` for
  targeted extraction.
- Use `.predict(newdata)` for predictions and `.resid()` for residual diagnostics.
- For IV models, inspect `.first_stage()` and `.IV_Diag()` when instrument relevance or
  diagnostics matter.
- For IV tables that need both stages, use `pf.etable()` with the first-stage model and
  the second-stage fit.
- Use `.wald_test()` for linear hypothesis tests instead of manual variance-covariance
  calculations.

## Causal Inference And DiD

- Use `pf.did2s()` for two-stage DiD specifications when that estimator matches the
  research design.
- Use `pf.event_study()` or `pf.SaturatedEventStudy()` for event-study designs.
- Use `pf.lpdid()` for local-projections DiD.
- Use `pf.panelview()` to inspect treatment timing and panel structure before estimating
  staggered-adoption designs.
- Use `pf.iplot()` for event-study-style plots from `i()` interactions.
- Do not treat a two-way fixed-effects event study as valid by default; check the
  identifying assumptions and the package's estimator options.

## Tables And Plots

- Use `pf.etable()` for regression tables. If the project uses maketables, follow
  `maketables.md` for tables that are published or saved.
- Use `type="md"` for Markdown output, `type="tex"` for LaTeX, `type="df"` for
  programmatic post-processing, and the project-preferred rich table backend otherwise.
- Use `keep`, `drop`, `labels`, and `felabels` to make tables readable.
- Set captions and model headers explicitly for publication or slides.
- Use `pf.coefplot()` for coefficient plots and `pf.qplot()` for quantile-regression
  coefficient plots.

## Agent Behavior

- Verify package-specific details against current PyFixest documentation when changing
  formulas, inference, IV models, DiD estimators, or table output.
- Prefer documentation Markdown endpoints when available; PyFixest documentation pages
  can be accessed as clean Markdown by appending `.md` to the HTML URL.
- Keep model formulas readable and close to the research specification. Do not hide
  important identification choices in helper strings without tests or comments.
- In reviews, check that clustering, fixed effects, weights, sample restrictions, and
  omitted categories match the stated research design.
