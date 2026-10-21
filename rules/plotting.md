# Plotting Standards

Plotly-only plotting guidance for figures and visual outputs.

- Use Plotly exclusively. Do not introduce matplotlib, seaborn, or other plotting
  libraries unless the project explicitly changes that rule.
- Favor charts that show the data directly and avoid decorative clutter.
- Prefer facets over spaghetti plots when comparing many groups or series.
- Use gray as the default color and reserve accent colors for emphasis.
- Label directly on the chart when it improves readability.
- Keep figure code reproducible and scriptable so the same task can regenerate plots
  without manual edits.
