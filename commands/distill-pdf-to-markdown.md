---
description: Convert a source PDF into a distilled, verified Markdown summary
---

# Distill PDF to Markdown

Convert a source PDF (lecture slides, notes, exams, and similar documents) into a
distilled Markdown summary, verified against the original.

The committed output is a summary, not a transcript: the full markitdown conversion is a
working intermediate, never the deliverable.

## Inputs

- One or more source PDF paths (e.g. a `Slides/` directory of numbered decks).
- The target output path/naming convention, if the calling project specifies one.
  Default: mirror the source file name with a `.md` extension (`01_Topic.pdf` ->
  `01_Topic.md`).

## Per-Document Independence

Treat each PDF as its own unit of work — run the full workflow below for one document at
a time, e.g. in a dedicated agent session or subagent where the environment supports it,
so verification and distillation for one document never bleeds context from another.
Documents may be processed in parallel if the environment allows it.

## Workflow

1. **Convert.** Run markitdown on the PDF per `rules/markitdown.md` to produce a
   working, uncommitted intermediate Markdown file. This intermediate is scratch —
   delete it (or leave it untracked) once distillation is done; do not commit it
   alongside the summary.
1. **Verify against the source.** Open the original PDF and compare it page by page or
   section by section against the intermediate conversion, per `rules/markitdown.md`'s
   verification rule. Pay particular attention to figures, diagrams, tables, and
   multi-column layouts, which are the content most likely to be flattened or reordered
   incorrectly.
1. **Reconstruct math and figures.**
   - Render every mathematical expression as LaTeX (`$...$` inline, `$$...$$` display),
     per `rules/markitdown.md`'s LaTeX rule — never as literal Unicode math symbols or
     spelled-out notation.
   - Reconstruct diagrams (game trees, indifference-curve sketches, and similar figures)
     that did not survive extraction as ASCII art or a Markdown table, not as LaTeX.
1. **Strip page furniture.** Remove content that is a formatting artifact of the source
   medium, not substance: running headers/footers, slide or page numbers ("Slide 4",
   "Page 3 of 20"), watermarks, and repeated branding/boilerplate. Do this before
   distilling, so it cannot leak into the summary.
1. **Distill.** Condense the verified, cleaned content into a summary: retain
   definitions, key results/claims, arguments and derivations (with their LaTeX), and
   illustrative examples; drop transitional/verbal filler, restated section dividers,
   and redundant repetition across slides. The result should read as a compact study
   artifact, not a lightly-trimmed full conversion.
1. **Record provenance.** Add a short note in the output file (e.g. a trailing line or
   small "Source" note) stating it was distilled from the source PDF and verified
   against it, so readers know the summary is a checked distillation rather than a raw
   dump.

## Quality Checks

Before finishing, confirm:

- No footers, slide/page numbers, or other page furniture remain in the output.
- Every mathematical expression is LaTeX (`$...$`/`$$...$$`); none are left as Unicode
  symbols or spelled-out words.
- Every diagram that carries substantive content survived, either natively or as a
  manually reconstructed ASCII/table version.
- The output is a genuine distillation (condensed, restructured around the ideas) rather
  than the full conversion with a few lines trimmed.
- The intermediate full conversion was not committed.

## Response Template

Per source PDF, report:

- source path and output path
- what was verified against the source, and any figures/math manually reconstructed
- content dropped during distillation that a reader might expect to still find (so it's
  a deliberate choice, not a silent loss)
- anything left unverified or uncertain
