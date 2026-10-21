# DAG Composition Standards

Guidance for composing functions with dags and for regime-specific DAG simplification.

- Use `dags` to combine interrelated functions into a single composed function when
  dependency order can be inferred from signatures.
- Let parameter names define dependencies between functions.
- Rely on automatic pruning so only functions needed for the selected target(s) are
  included.
- When a function becomes irrelevant for a regime, remove it from the DAG rather than
  zeroing inputs or manually dropping states.
- If a removed function's output should become a constant, fix that external input with
  `functools.partial`.
- Use multi-target composition when the workflow needs several outputs from the same
  dependency graph.
- Use `rename_arguments` to adapt third-party functions to the DAG's naming convention.
- Use `with_signature` when wrapped functions need an explicit programmatic signature.
- If the constituent functions are JAX-compatible, treat the combined function as
  JAX-compatible too and use `jit`, `vmap`, or autodiff as needed.
