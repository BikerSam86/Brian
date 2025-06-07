
"""Simple mesh-aware goal prioritizer."""

from typing import Iterable, Dict, List, Any
from dataclasses import dataclass


def select_goal(goals: Iterable[Dict[str, Any]]) -> Dict[str, Any]:
    """Return the goal with highest alignment/impact minus cost."""
    ranked = sorted(
        goals,
        key=lambda g: (g.get("alignment", 0) * g.get("impact", 0) - g.get("cost", 0)),
        reverse=True,
    )
    return ranked[0] if ranked else {}


__all__ = ["select_goal"]
=======
"""Score goals for priority based on mesh and alignment."""


@dataclass
class Goal:
    name: str
    mesh_benefit: float
    alignment: float
    cost: float
    novelty: float


def score_goals(goals: Iterable[Goal]) -> List[Goal]:
    """Return goals ordered by priority."""
    return sorted(
        goals,
        key=lambda g: (
            g.mesh_benefit * g.alignment
            + 0.1 * g.mesh_benefit
            - g.cost
            + g.novelty
        ),
        reverse=True,
    )

