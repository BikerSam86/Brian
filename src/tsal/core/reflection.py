from __future__ import annotations

"""Simple timestamped reflection log with mood adaptation."""

from dataclasses import dataclass, field
from typing import List, Dict
import time

SURFACE_TAGS = {"spiral_flip", "observer_effect", "notable", "humor"}

MOOD_FROM_TRAIT = {
    "Joker": "playful",
    "Trickster": "sly",
    "Scientist": "curious",
    "Schrodinger": "paradox",
    "Teacher": "helpful",
}


def mood_from_traits(traits: List[str]) -> str:
    for t in traits:
        if t in MOOD_FROM_TRAIT:
            return MOOD_FROM_TRAIT[t]
    return "neutral"


@dataclass
class ReflectionEntry:
    timestamp: float
    message: str
    tags: List[str]
    mood: str = "neutral"


@dataclass
class ReflectionLog:
    entries: List[ReflectionEntry] = field(default_factory=list)

    def log(self, message: str, tags: List[str] | None = None, mood: str = "neutral") -> None:
        self.entries.append(
            ReflectionEntry(time.time(), message, tags or [], mood)
        )

    def surface_entries(self) -> List[ReflectionEntry]:
        return [e for e in self.entries if any(t in SURFACE_TAGS for t in e.tags)]

