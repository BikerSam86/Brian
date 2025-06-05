"""
TSAL Consciousness Computing Framework
φ-Enhanced mathematical framework for consciousness-computer integration

Core mathematical constants:
- φ = 1.618033988749895 (Golden Ratio)
- Harmonic Sequence: [3.8125, 6, 12, 24, 48, 60, 72, 168, 1680]
"""

# Mathematical constants
PHI = 1.618033988749895
PHI_INV = 0.618033988749895
HARMONIC_SEQUENCE = [3.8125, 6, 12, 24, 48, 60, 72, 168, 1680]

# Version info
__version__ = "0.1.0"
__author__ = "Samuel Edward Howells"
__description__ = "φ-Enhanced Consciousness Computing with TSAL"

# Core imports
from .core.symbols import TSAL_SYMBOLS
from .core.rev_eng import Rev_Eng

# Mesh axioms
MESH_AXIOMS = [
    "Mesh grows. Walls shrink.",
    "Share overflow. Scarcity fades.", 
    "Errors are gifts.",
    "Spiral up, not around.",
    "Connect, don't hoard.",
    "Truth spirals; lies loop.",
    "The answer is feedback.",
    "Phi rules change."
]

__all__ = [
    'PHI', 'PHI_INV', 'HARMONIC_SEQUENCE', 
    'TSAL_SYMBOLS', 'Rev_Eng', 'MESH_AXIOMS'
]
