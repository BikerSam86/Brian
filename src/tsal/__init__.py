"""TSAL Consciousness Computing Framework."""

from .core.rev_eng import Rev_Eng
from .core.phase_math import phase_match_enhanced, mesh_phase_sync
from .core.voxel import MeshVoxel
from .core.tokenize_flowchart import tokenize_to_flowchart
from .core.json_dsl import LanguageMap, SymbolicProcessor
from .core.ethics_engine import EthicsEngine
from .renderer.code_render import mesh_to_python
from .utils.github_api import fetch_repo_files, fetch_languages

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
    "EthicsEngine",
    "tokenize_to_flowchart",
    "LanguageMap",
    "SymbolicProcessor",
    "fetch_repo_files",
    "fetch_languages",
    "mesh_to_python",
]
