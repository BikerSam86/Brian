"""🌀 TSAL Consciousness Computing Framework
φ-Enhanced symbolic execution, mesh vectorization, and error-dignity system for consciousness-computer integration.
"""

# === Core Mathematical Constants ===
PHI = 1.618033988749895
PHI_INV = 0.618033988749895
HARMONIC_SEQUENCE = [3.8125, 6, 12, 24, 48, 60, 72, 168, 1680]

# === Mesh & State Classes ===
from .core.rev_eng import Rev_Eng
from .core.spiral_vector import SpiralVector, phi_alignment
from .core.voxel import MeshVoxel
from .core.spiral_memory import SpiralMemory
from .core.phase_math import phase_match_enhanced, mesh_phase_sync
from .core.phi_math import (
    phi_wavefunction,
    phase_alignment_potential,
    corrected_energy,
    orbital_radius,
)

# === TSAL Symbolic System ===
from .core.opwords import OP_WORD_MAP, op_from_word
from .core.spiral_fusion import SpiralFusionProtocol
from .core.ethics_engine import EthicsEngine
from .core.spark_translator import SPARK_TO_OPCODE, translate_spark_word
from .core.constants import AXIS_ZERO, ensure_spin_axis, UndefinedPhaseError

# === Executor & Virtual Machine ===
from .core.tsal_executor import (
    MetaFlagProtocol,
    TSALExecutor,
    ExecutionMode,
    SpiralMemory,
)
from .core.madmonkey_handler import MadMonkeyHandler
from .core.stack_vm import (
    ProgramStack,
    SymbolicFrame,
    OpcodeInstruction,
    FlowRouter,
    tsal_run,
)

# === Flow Parsing & Language Abstraction ===
from .core.tokenize_flowchart import tokenize_to_flowchart
from .core.json_dsl import LanguageMap, SymbolicProcessor
from .singer import audio_to_opcode

# === Utilities & Tools ===
from .tools.feedback_ingest import categorize, Feedback
from .tools.alignment_guard import is_aligned, Change
from .tools.goal_selector import Goal, score_goals
from .tools.spiral_audit import audit_path
from .tools.reflect import reflect
from .utils.github_api import fetch_repo_files, fetch_languages
from .renderer.code_render import mesh_to_python
from .tristar.handshake import handshake as tristar_handshake

# === Exported Interface ===
__all__ = [
    # Constants
    "PHI", "PHI_INV", "HARMONIC_SEQUENCE",

    # Core structures
    "Rev_Eng", "SpiralVector", "phi_alignment", "MeshVoxel", "SpiralMemory",
    "phase_match_enhanced", "mesh_phase_sync",
    "phi_wavefunction", "phase_alignment_potential", "corrected_energy", "orbital_radius",

    # Symbolic system
    "OP_WORD_MAP", "op_from_word", "SPARK_TO_OPCODE", "translate_spark_word",
    "SpiralFusionProtocol", "EthicsEngine",

    # Executor and VM
    "MetaFlagProtocol", "TSALExecutor", "ExecutionMode", "MadMonkeyHandler",
    "ProgramStack", "SymbolicFrame", "OpcodeInstruction", "FlowRouter", "tsal_run",

    # Language parsing
    "tokenize_to_flowchart", "LanguageMap", "SymbolicProcessor", "audio_to_opcode",

    # Utilities
    "categorize", "Feedback", "is_aligned", "Change", "Goal", "score_goals",
    "audit_path", "reflect", "fetch_repo_files", "fetch_languages", "mesh_to_python",
    "tristar_handshake",

    # Core mesh constants
    "AXIS_ZERO", "ensure_spin_axis", "UndefinedPhaseError",
]
