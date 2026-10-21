# MarkItDown Standards

Guidance for converting documents (PDF, Office, images, audio, HTML, and more) to
Markdown with [markitdown](https://github.com/microsoft/markitdown) for LLM-facing text
pipelines.

- Use markitdown to turn source documents into Markdown for downstream LLM/text-analysis
  work, not as a high-fidelity converter for human-facing documents.
- Prefer the Python API over shelling out to the CLI in scripts:
  `from markitdown import MarkItDown; md = MarkItDown(); result = md.convert(path)`,
  then read `result.text_content` (or `result.markdown`).
- Call the narrowest `convert_*` method for the input: `convert_local()` for local
  files, `convert_stream()` for in-memory byte streams, `convert_response()` for an
  already-fetched `requests.Response`. Reserve the permissive `convert()` for trusted,
  known-local paths; never pass it untrusted or user-supplied paths/URIs.
- Install only the optional extras a project actually converts (e.g. `markitdown[pdf]`),
  never `markitdown[all]`, to keep the environment minimal and avoid pulling in unused
  Azure/audio/video dependencies.
- Leave `enable_plugins=False` (the default) unless a specific 3rd-party plugin is
  required and vetted — plugins run arbitrary code discovered via entry points.
- MarkItDown performs I/O with the privileges of the calling process, same as `open()`
  or `requests.get()`. Sanitize any input path or URI that could be influenced by an
  untrusted source before conversion.
- Reach for `docintel_endpoint` (Azure Document Intelligence) or `cu_endpoint` (Azure
  Content Understanding) only when local conversion quality is insufficient — scanned
  PDFs, complex tables, or structured field extraction — since both are billable cloud
  calls, not a default.
- Treat markitdown's output as an intermediate artifact to feed into further processing,
  not a final document — do not hand-polish its Markdown formatting.

## Always verify the conversion against the source

markitdown's text extraction is layout-driven and silently mangles content it cannot
linearize — most notably diagrams, game trees, and other figures, which come out as an
unordered dump of labels rather than an error. A conversion that runs without error is
not evidence that it is correct.

- After converting a document, open the original file directly (e.g. read the PDF/image
  itself) and compare it against the generated Markdown, page by page or section by
  section.
- Pay special attention to figures, diagrams, tables, and multi-column layouts — these
  are the content types most likely to be flattened or reordered incorrectly, even when
  surrounding body text extracts cleanly.
- If a figure or structure did not survive extraction, manually reconstruct it (e.g. as
  an ASCII diagram or a Markdown table) from the source rather than leaving the mangled
  output in place.
- Record what was verified and what was corrected in a short note in the output file (or
  the commit/PR description), so readers know which parts are a faithful extraction and
  which were manually reconstructed.

## Render math as LaTeX, not Unicode symbols or spelled-out words

markitdown frequently corrupts math glyphs it cannot map to Unicode (primes, integrals,
radicals) into raw `(cid:NN)` codes, and layout-driven extraction often drops
subscripts/superscripts onto separate lines. When reconstructing any mathematical
content by hand, render it as standard LaTeX wrapped in `$...$` (inline) or `$$...$$`
(display/standalone equations) — not as literal Unicode math symbols (θ, Σ, ∫, ≥) and
not as spelled-out words (`theta`, `sum_i`, `in`, `->`).

- Use real LaTeX commands: `\theta`, `\Gamma`, `\sum`, `\int`, `\sqrt{}`, `\geq`,
  `\leq`, `\neq`, `\in`, `\to`, `\times`, `\mathbb{R}`, `\tilde{}`, `\hat{}`,
  `\frac{}{}`. Subscripts/superscripts are plain `_i` / `^2` inside math mode.
- Verify each reconstructed formula against the source document's rendered page, the
  same as any other reconstructed content — don't guess which symbol a mangled glyph
  stood in for.
- Diagrams (game trees, indifference-curve sketches, and similar figures) are not math
  notation — keep those as ASCII art or a Markdown table, not LaTeX.
