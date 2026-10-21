# State And Persistence

Where the supervisor keeps state and how to keep it small. All files are plain Markdown
the student can read and edit.

## Layout

| Scope                           | Path                                | Contents                              |
| ------------------------------- | ----------------------------------- | ------------------------------------- |
| Student (all projects, private) | `~/.claude/phd/profile.md`          | Field, background, tone, known gaps   |
| Student (all projects, private) | `~/.claude/phd/index.md`            | One line per concept note             |
| Student (all projects, private) | `~/.claude/phd/concepts/<topic>.md` | One note per concept or paper cluster |
| Project (gitignored)            | `.supervisor/status.md`             | Rewritten snapshot of the project     |
| Project (gitignored)            | `.supervisor/log.md`                | Append-only session log               |

`~/.claude/phd/` is private data: it is not part of this repository and should be its
own private repo. `.supervisor/` must be gitignored in the project.

## Context Budget

- Session start reads `profile.md`, `status.md`, `index.md`: aim for about 100 lines in
  total.
- Concept notes are opened only when the topic comes up.
- `log.md` is never read in full. Use `tail -n 40` or grep.
- `status.md` is rewritten each session, never appended to.

## File Formats

`profile.md`:

```markdown
# Profile

- Field: <fields>
- Dissertation: <title>
- Background: <methods and coursework>
- Gaps: <topics not yet known>
- Tone: firm
```

`index.md`: `- [topic](concepts/topic.md): one-line summary`.

`concepts/<topic>.md`:

```markdown
# <Topic>

Status: <not started | partially understood | understood | can teach>

## Student's understanding
## Errors made (and the fix)
## Open questions
## Sources
```

Record the student's own formulation, including mistakes. Do not paste textbook
summaries; the value of a note is what a model cannot supply.

`.supervisor/status.md`:

```markdown
# Status

- Question: <current research question>
- Model: <where the model stands, in a few lines>
- Assumptions: <list with load-bearing / harmless / unjustified>
- Open problems:
- Next steps:
- Updated: <date>
```

`.supervisor/log.md`: newest entry last, one entry per session:

```markdown
## <date> <mode>: <topic>
Covered: ... | Student got wrong: ... | Next: ...
```

## Consolidation

At session end: rewrite `status.md`, append one log entry, and update the concept notes
and `index.md`. If `log.md` exceeds about 200 lines, fold what still matters into
`status.md` and the concept notes and truncate the log.
