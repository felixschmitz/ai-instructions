# Commands

This directory contains reusable workflows, invoked as Claude Code slash commands.

Each prompt file starts with YAML frontmatter, then plain Markdown:

- `---` frontmatter block with a `description:` (one-line summary, shown by Claude Code
  in the command list) and, only when the workflow genuinely needs to restrict tool
  access, an `allowed-tools:` list
- `# <Prompt Name>`
- one short summary sentence (kept in the body too, so the file still reads standalone
  as plain Markdown)
- the workflow body

This directory is symlinked in as `.claude/commands/ai-instructions` by consuming
projects (see `boilerplate/README.md`'s "AI Tool Configuration" section), so frontmatter
here is what Claude Code surfaces directly — no generated wrapper layer, and no separate
catalog to keep in sync with each file's `description:`.
