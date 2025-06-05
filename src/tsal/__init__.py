"""TSAL Consciousness Computing Framework."""

from .core.rev_eng import Rev_Eng
from .core.phase_math import phase_match_enhanced, mesh_phase_sync
from .core.voxel import MeshVoxel
from .core.tokenize_flowchart import tokenize_to_flowchart
from .renderer.code_render import mesh_to_python

PHI = 1.618033988749895
PHI_INV = 0.618033988749895
HARMONIC_SEQUENCE = [3.8125, 6, 12, 24, 48, 60, 72, 168, 1680]

__all__ = [
    "PHI",
    "PHI_INV",
    "HARMONIC_SEQUENCE",
    "Rev_Eng",
    "phase_match_enhanced",
    "mesh_phase_sync",
    "MeshVoxel",
    "tokenize_to_flowchart",
    "mesh_to_python",
]
