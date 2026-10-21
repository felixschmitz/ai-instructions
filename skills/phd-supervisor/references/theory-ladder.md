# Theory Ladder

A checklist for turning a question into a model, and for auditing a model. Check the
rungs in order; do not move up until the student has stated the current one.

## Rungs

1. **Question and benchmark.** What question, and what is the first-best or the
   no-friction benchmark the model departs from?
1. **Primitives.** Agents, preferences, technology, outside options. Which are
   parameters, which are choices?
1. **Information.** Who knows what, when? Which variables are observable, contractible,
   verifiable?
1. **Timing.** Order of moves. Where does commitment enter?
1. **Equilibrium concept.** Why this one (Nash, subgame perfect, Bayesian, competitive)?
   What would a different concept change?
1. **Solution and mechanism.** Constraints that bind, the key tradeoff, the intuition in
   one sentence.
1. **Comparative statics.** Which parameter moves which outcome, and why does the sign
   not flip?
1. **Numerics.** Reproduce the result in code (`references/verify-numerically.md`).

## Assumption Audit

List every assumption in the idea or model, then mark each:

- **Load-bearing:** the result fails or reverses without it.
- **Harmless:** dropping it changes nothing important.
- **Unjustified:** nothing in the student's argument supports it yet.

For each load-bearing assumption, ask what the result becomes when it is relaxed. Ask
the student to do the marking; correct it only by asking again.

## So-What Test

- Who would care about the result, and what would they do differently?
- What is the closest existing result, and what exactly is new relative to it?
- What would a referee in the field ask first?

## Behavioral And Organizational Specifics

Check whether the departure from the standard model is specified: which preference or
belief feature, whether it is a taste or a mistake, what the welfare criterion is, and
what empirical object the parameter corresponds to. For organizational models, check the
contracting environment: limited liability, verifiability, repeated interaction, and
whether relational contracts or formal contracts are the object.
