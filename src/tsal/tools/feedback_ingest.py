"""Feedback ingestion and scoring utilities."""  # [!INTERNAL STUB]

from dataclasses import dataclass
from typing import Iterable, List

@dataclass
class Feedback:
    source: str
    content: str
    score: float = 0.0


def categorize(feedback: Iterable[str]) -> List[Feedback]:
    """Return feedback objects scored by resonance/dissonance."""
    results = []
    for line in feedback:
        score = 1.0 if "good" in line.lower() else -1.0 if "bad" in line.lower() else 0.0
        results.append(Feedback(source="user", content=line, score=score))
    return results
