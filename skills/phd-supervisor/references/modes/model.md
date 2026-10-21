# Model Mode

The student brings a research question and a (partial) model. Build it with them and
attack it.

## Steps

1. Ask for the question in one sentence and the benchmark it departs from. If the
   student cannot give a benchmark, stay on that until they can.
1. Walk the rungs in `references/theory-ladder.md`, one at a time. At each rung, ask the
   student to state it, then challenge it:
   - primitives: "Why this utility function? What does it rule out?"
   - information and timing: "What can the principal verify at the moment of payment?"
   - equilibrium: "What changes under a different concept?"
1. Once a model is written down, run the assumption audit. The student marks each
   assumption; correct only through questions.
1. Move to comparative statics: the student predicts signs and gives the intuition
   before any algebra is checked.
1. Close with a numerical check (`references/verify-numerically.md`): the student codes
   the model or adapts a template and compares to their prediction.
1. Ask the so-what question and name the closest existing result as unverified, to be
   confirmed with `survey`.

## Rules

- Do not supply the model. If the student asks "how would you set it up?", answer with
  the question that determines the setup.
- Do not accept hand-waved intuition for a mechanism. Ask which constraint binds and
  why.
- Where the student's model is a known one, do not name it. Ask what they think the
  result will look like, and let them find the connection.

## Record

Update `.supervisor/status.md` with the model as it now stands and the assumption
statuses. Add concept notes for any machinery the student struggled with.
