"""Verify spiral alignment of proposed changes."""

from .spiral_vector import SpiralVector, phi_alignment


THRESH_ACCEPT = 0.76
THRESH_DEFER = 0.5


def verify_spiral_integrity(vector: SpiralVector) -> str:
    """Return ACCEPTED/DEFER_TO_MADMONKEY/REJECTED based on φ-score."""
    score = phi_alignment(vector.complexity, vector.coherence)
    if score >= THRESH_ACCEPT:
        return "ACCEPTED"
    if score >= THRESH_DEFER:
        return "DEFER_TO_MADMONKEY"
    return "REJECTED"


__all__ = ["verify_spiral_integrity"]
