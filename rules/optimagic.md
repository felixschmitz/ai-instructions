# Optimagic Standards

Optimization library guidance and algorithm-selection rules.

- Use `optimagic` for numerical optimization in this codebase.
- Always specify the optimization algorithm explicitly.
- Choose algorithms to match the problem class:
  - smooth, unconstrained: `scipy_lbfgsb`
  - smooth, constrained: `ipopt`
  - least-squares: `scipy_ls_lm`
  - non-smooth, few parameters: `nlopt_bobyqa`
  - global search: `scipy_brute` plus local refinement
- Compare multiple algorithms with `om.criterion_plot()` when diagnosing or validating
  optimization behavior.
- Check `res.success` before trusting an optimization result.
- Do not use Nelder-Mead as the default optimizer.
