# NumPy Standards

NumPy array programming and random-number generation practices.

- Vectorize computations. Prefer array operations over Python loops.
- Use `axis=` explicitly for reductions.
- Use `*` for elementwise multiplication and `@` for matrix multiplication.
- Prefer broadcasting instead of `np.repeat` or `np.tile`.
- Use the modern random API only: `rng = np.random.default_rng(seed=...)`.
- Always provide a seed when constructing a random generator for reproducible work.
- Do not use `np.random.seed()`, `np.random.rand()`, `np.random.randn()`, or
  `np.random.random()`.
