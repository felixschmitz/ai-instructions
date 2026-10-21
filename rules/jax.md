# JAX Standards

JAX, jaxtyping, and functional-array programming guidance for performance-critical code.

- When a project uses JAX, prefer it over NumPy for performance-critical code.
- Use `jax.numpy as jnp` rather than `numpy` in JAX-native code paths.
- Use `jnp.where()` for array conditionals rather than Python `if` branching on array
  values.
- Treat arrays as immutable. JAX operations return new arrays.
- JIT-compile hot paths with `jit` when the computation benefits from it.
- Use `vmap` instead of Python loops for batched array computations.
- Use `jax.random` with explicit keys. Do not rely on global random state.
- Use `jaxtyping` for shape-aware array annotations when the project already depends on
  it.
- If the project uses `jaxtyping`, include Ruff ignore rule `F722` with the jaxtyping
  FAQ link in the comment.
- If JAX code needs immutable mappings, register `MappingProxyType` as a pytree so it
  remains compatible with JIT and tree utilities.
