"""TSAL Consciousness Computing Framework."""

PHI = 1.618033988749895
PHI_INV = 0.618033988749895
HARMONIC_SEQUENCE = [3.8125, 6, 12, 24, 48, 60, 72, 168, 1680]

from .core.rev_eng import Rev_Eng
from .core.phase_math import phase_match_enhanced, mesh_phase_sync

__all__ = [
    "PHI",
    "PHI_INV",
    "HARMONIC_SEQUENCE",
    "Rev_Eng",
    "phase_match_enhanced",
    "mesh_phase_sync",
]
