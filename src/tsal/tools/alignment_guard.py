"""Check proposed changes for spiral alignment."""  # [!INTERNAL STUB]

from dataclasses import dataclass


@dataclass
class Change:
    description: str
    spiral_score: float


def is_aligned(change: Change, threshold: float = 0.76) -> bool:
    """Return True if change respects mesh axioms and score threshold."""
    if change.spiral_score < threshold:
        return False
    banned = {"coerce", "exploit"}
    lowered = change.description.lower()
    return not any(word in lowered for word in banned)
