"""Simple handler for TSAL error vectors."""

from __future__ import annotations


class MadMonkeyHandler:
    """Collects error vectors and suggests bloom patches."""

    def __init__(self) -> None:
        self.errors = []

    def handle(self, error_vector: dict) -> None:
        self.errors.append(error_vector)

    def suggest_bloom_patch(self) -> bool:
        return len(self.errors) > 0
