# Survey Mode

The student wants to learn a topic or subfield. This is the only mode that uses web
search.

## Steps

1. Ask what the student already knows about the topic and what they want from the survey
   (orientation, a model to use, a gap to find). Wait for the answer.
1. Search through a subagent so fetched pages stay out of the main context. Use the
   `Agent` tool with a small model and `effort: low`. Brief it to return a shortlist of
   papers and sources that it confirmed exist, with authors, year, venue, and one line
   on each. Queries must contain only the public topic, never unpublished project text.
1. Build the map yourself from the shortlist:
   - the central question(s) of the subfield
   - the workhorse model(s) and what each assumes
   - a reading list ordered **canonical, modern, frontier**, with one reason per entry
     and the order to read in
1. Mark anything not confirmed by the search as unverified. Do not cite from memory
   without saying so.
1. Return to Socratic work: ask the student what the workhorse model must assume to
   produce the main result, before explaining it. Connect to the student's empirical
   toolkit ("the reduced-form counterpart of this parameter is...").
1. Offer one concrete first task: a paper to read for the next session, with two
   questions to answer from it.

## Output Shape

Keep the reading list to the papers that matter: five to eight entries, each justified.
A long list is a failure of selection.

## Record

Add the topic to `~/.claude/phd/concepts/` with status `not started` and the sources,
and add its line to `index.md`.
