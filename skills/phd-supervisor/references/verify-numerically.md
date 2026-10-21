# Verify Numerically

Use code to test understanding, not to replace it. The student predicts, then runs.

## Protocol

1. The student states a prediction in words: what the solution looks like, or the sign
   of a comparative static.
1. The student (not the supervisor) writes or adapts the code. Offer a template only if
   they are stuck.
1. Run it. Compare to the prediction. When they disagree, ask where the reasoning or the
   code went wrong before giving any hint.
1. Vary one primitive and ask the student to predict the change first.

## Where Code Lives

Scratch code goes in the project's `sandbox/` (or equivalent), run in the project's Pixi
environment. Templates live in this skill's `templates/` and need only `numpy`, `scipy`,
and `sympy`. Copy a template into the sandbox rather than editing it in place.

## Templates

- `templates/moral_hazard_lp.py`: finite-outcome moral-hazard problem under limited
  liability, solved as a linear program. Use it to see which incentive constraints bind
  and what shape the optimal contract takes.
- `templates/comparative_statics.py`: symbolic first-order condition, implicit-function
  comparative statics, and a numerical check against a direct optimizer. Demo is the
  linear-contract CARA-normal model.

Both run as scripts and print a self-check. They are starting points, not libraries.
