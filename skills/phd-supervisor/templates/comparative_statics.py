"""Comparative statics: symbolic first-order condition, checked numerically.

Workflow: write the principal's objective, take the first-order condition, get the
comparative static with the implicit function theorem, and check it against a direct
numerical optimizer. Replace the objective in ``build_model`` with your own.

The demo is the linear-contract model with a CARA agent and normal noise. Effort e costs
c * e**2 / 2, the wage is a + b * output, output has variance sigma2, and the agent's
risk aversion is r. The agent's effort choice gives e = b / c, and the principal chooses
the slope b to maximize total surplus.
"""

from __future__ import annotations

import sympy as sp
from scipy.optimize import minimize_scalar


def build_model() -> tuple[sp.Expr, dict[str, sp.Symbol], sp.Symbol]:
    """Return the objective, the parameter symbols, and the choice variable."""
    b = sp.Symbol("b", positive=True)
    c, r, sigma2 = sp.symbols("c r sigma2", positive=True)
    effort = b / c
    surplus = effort - c * effort**2 / 2 - r * b**2 * sigma2 / 2
    return surplus, {"c": c, "r": r, "sigma2": sigma2}, b


def implicit_comparative_static(
    objective: sp.Expr, choice: sp.Symbol, param: sp.Symbol
) -> tuple[sp.Expr, sp.Expr]:
    """Return the closed-form optimum and d(choice*)/d(param) via the implicit function.

    With the first-order condition F(choice, param) = 0, the comparative static is
    -F_param / F_choice.
    """
    foc = sp.diff(objective, choice)
    solution = sp.solve(sp.Eq(foc, 0), choice)[0]
    derivative = -sp.diff(foc, param) / sp.diff(foc, choice)
    return solution, sp.simplify(derivative.subs(choice, solution))


def main() -> None:
    objective, params, b = build_model()
    solution, derivative = implicit_comparative_static(objective, b, params["sigma2"])
    print("Optimal slope b* =", sp.simplify(solution))
    print("db*/dsigma2      =", derivative)

    values = {params["c"]: 1.0, params["r"]: 2.0, params["sigma2"]: 0.5}
    symbolic = float(derivative.subs(values))

    def optimal_b(sigma2_value: float) -> float:
        numeric_objective = sp.lambdify(
            b, objective.subs({**values, params["sigma2"]: sigma2_value}), "numpy"
        )
        result = minimize_scalar(
            lambda x: -numeric_objective(x), bounds=(0, 10), method="bounded"
        )
        return float(result.x)

    step = 1e-4
    sigma2_0 = float(values[params["sigma2"]])
    numeric = (optimal_b(sigma2_0 + step) - optimal_b(sigma2_0 - step)) / (2 * step)
    print(f"Symbolic: {symbolic:.4f}  Numerical: {numeric:.4f}")

    assert abs(symbolic - numeric) < 1e-3, (symbolic, numeric)
    assert symbolic < 0, "More risk should flatten incentives."
    print("Check passed: the symbolic and numerical comparative statics agree.")


if __name__ == "__main__":
    main()
