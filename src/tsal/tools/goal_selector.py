"""Simple mesh-aware goal prioritizer."""

from typing import Iterable, Dict, Any


def select_goal(goals: Iterable[Dict[str, Any]]) -> Dict[str, Any]:
    """Return the goal with highest alignment/impact minus cost."""
    ranked = sorted(
        goals,
        key=lambda g: (g.get("alignment", 0) * g.get("impact", 0) - g.get("cost", 0)),
        reverse=True,
    )
    return ranked[0] if ranked else {}


__all__ = ["select_goal"]
