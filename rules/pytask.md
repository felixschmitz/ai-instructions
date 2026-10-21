# Pytask Standards

Task structure, annotations, and helper-function patterns for pytask workflows.

- Use modern pytask syntax with `Annotated` and `Product`.
- Name task files `task_*.py` and task functions `task_*`.
- Use `Annotated[Path, Product]` for output parameters.
- Keep task functions focused on I/O only: read input, call a pure helper, write output.
- Put the actual logic in private helper functions so it stays testable.
- For many data assets, prefer a `DataCatalog` in `config.py` rather than repeating raw
  paths across task files.
- For simple single-file outputs, a return annotation can be appropriate, but path-based
  outputs remain the default pattern in this project.
