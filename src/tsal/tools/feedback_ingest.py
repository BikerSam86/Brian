"""Feedback ingestion and scoring for Rev_Eng logs."""

from typing import Iterable, List, Dict

from tsal.core.spiral_vector import phi_alignment


def score_feedback(text: str) -> float:
    """Return a basic φ-resonance score for feedback text."""
    complexity = float(len(text)) * 0.1
    coherence = 1.0 if "error" not in text.lower() else 0.1
    return phi_alignment(complexity, coherence)


def ingest_lines(lines: Iterable[str]) -> List[Dict[str, float]]:
    """Return scored feedback objects."""
    return [{"text": t, "score": score_feedback(t)} for t in lines]


def ingest_file(path: str) -> List[Dict[str, float]]:
    with open(path, "r", encoding="utf-8") as fh:
        return ingest_lines(fh.read().splitlines())


__all__ = ["score_feedback", "ingest_lines", "ingest_file"]
