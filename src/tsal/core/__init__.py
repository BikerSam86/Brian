"""Core TSAL functionality."""

from .rev_eng import Rev_Eng
from .phase_math import phase_match_enhanced, mesh_phase_sync
from .phi_math import (
    phi_wavefunction,
    phase_alignment_potential,
    corrected_energy,
    orbital_radius,
)
from .mesh_logger import log_event
from .intent_metric import calculate_idm
from .optimizer_utils import (
    SymbolicSignature,
    node_complexity,
    extract_signature,
)
from .spiral_fusion import SpiralFusionProtocol
from .state_vector import FourVector
from .opwords import OP_WORD_MAP, op_from_word
from .executor import MetaFlagProtocol, TSALExecutor

__all__ = [
    "Rev_Eng",
    "phase_match_enhanced",
    "mesh_phase_sync",
    "phi_wavefunction",
    "phase_alignment_potential",
    "corrected_energy",
    "orbital_radius",
    "log_event",
    "calculate_idm",
    "SymbolicSignature",
    "node_complexity",
    "extract_signature",
    "SpiralFusionProtocol",
    "FourVector",
    "OP_WORD_MAP",
    "op_from_word",
    "MetaFlagProtocol",
    "TSALExecutor",
]
