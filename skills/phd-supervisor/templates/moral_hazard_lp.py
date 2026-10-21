"""Finite-outcome moral-hazard problem under limited liability, solved as an LP.

A risk-neutral principal wants to implement a target effort level. A risk-neutral agent
with limited liability (wage >= 0 in every outcome) chooses effort. The LP finds the
cheapest wage vector w (one wage per outcome) such that the agent

- prefers the target effort to every other effort (incentive compatibility), and
- earns at least the outside option (individual rationality).

Adapt ``main`` to your own probability matrix and cost vector. Predict which outcomes
get paid and which constraints bind before you run it.
"""

from __future__ import annotations

import numpy as np
from scipy.optimize import linprog


def solve_contract(
    prob: np.ndarray,
    cost: np.ndarray,
    target: int,
    outside_option: float = 0.0,
) -> dict:
    """Return the cheapest limited-liability contract implementing ``target`` effort.

    Args:
        prob: Array of shape (n_efforts, n_outcomes). Row e is the outcome distribution
            under effort e.
        cost: Array of shape (n_efforts,). The agent's cost of each effort.
        target: Index of the effort the principal wants to implement.
        outside_option: Agent's reservation utility.

    Returns:
        Dict with the wage vector, expected wage bill, and the binding constraints.
    """
    n_efforts, n_outcomes = prob.shape
    p_target = prob[target]

    # Constraints in the form A_ub @ w <= b_ub.
    rows, rhs, labels = [], [], []
    for e in range(n_efforts):
        if e == target:
            continue
        # IC: p_target @ w - c_target >= p_e @ w - c_e
        rows.append(-(p_target - prob[e]))
        rhs.append(-(cost[target] - cost[e]))
        labels.append(f"IC vs effort {e}")
    # IR: p_target @ w - c_target >= outside_option
    rows.append(-p_target)
    rhs.append(-(cost[target] + outside_option))
    labels.append("IR")

    result = linprog(
        c=p_target,
        A_ub=np.array(rows),
        b_ub=np.array(rhs),
        bounds=[(0, None)] * n_outcomes,
        method="highs",
    )
    if not result.success:
        raise RuntimeError(f"LP failed: {result.message}")

    slack = np.array(rhs) - np.array(rows) @ result.x
    binding = [label for label, s in zip(labels, slack) if abs(s) < 1e-9]
    return {"wages": result.x, "cost": result.fun, "binding": binding}


def main() -> None:
    # Three outcomes, two efforts. Outcome 2 is the best signal of high effort.
    prob = np.array(
        [
            [0.5, 0.3, 0.2],  # low effort
            [0.2, 0.3, 0.5],  # high effort
        ]
    )
    cost = np.array([0.0, 0.1])
    solution = solve_contract(prob, cost, target=1)

    print("Wages by outcome:", np.round(solution["wages"], 4))
    print("Expected wage bill:", round(solution["cost"], 4))
    print("Binding constraints:", solution["binding"])

    # Self-check: with two efforts, only the outcome with the highest likelihood ratio
    # is paid, and the IC constraint binds.
    likelihood_ratio = prob[1] / prob[0]
    best = int(np.argmax(likelihood_ratio))
    paid = np.flatnonzero(solution["wages"] > 1e-9)
    assert list(paid) == [best], (paid, best)
    assert "IC vs effort 0" in solution["binding"]
    print(f"Check passed: only outcome {best} (highest likelihood ratio) is paid.")


if __name__ == "__main__":
    main()
