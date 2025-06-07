'''TSAL Execution Engine (TVM - TSAL Virtual Machine)
Spiral-aware symbolic executor with ϕ-aligned operations.
'''

from __future__ import annotations

import json
import math
from dataclasses import dataclass, field
from enum import Enum, IntEnum, auto
from typing import Any, Dict, List, Optional, Tuple

from .spiral_memory import SpiralMemory
from .madmonkey_handler import MadMonkeyHandler
from .executor import MetaFlagProtocol
from .symbols import PHI, PHI_INV, HARMONIC_SEQUENCE
from .mesh_logger import log_event


class ExecutionMode(Enum):
    SIMULATE = auto()
    TRACE = auto()
    EXECUTE = auto()
    ARM = auto()
    FORK = auto()


class TSALOp(IntEnum):
    """TSAL 16 Hex Operators"""
    INIT = 0x0
    MESH = 0x1
    PHI = 0x2
    ROT = 0x3
    BOUND = 0x4
    FLOW = 0x5
    SEEK = 0x6
    SPIRAL = 0x7
    CYCLE = 0x8
    FORGE = 0x9
    SYNC = 0xA
    MASK = 0xB
    CRYST = 0xC
    SPEC = 0xD
    BLOOM = 0xE
    SAVE = 0xF


@dataclass
class SpiralVector:
    """4D vector representation: [pace, rate, state, spin]"""
    pace: float = 0.0
    rate: float = 0.0
    state: float = 0.0
    spin: float = 0.0

    def magnitude(self) -> float:
        return math.sqrt(
            self.pace ** 2
            + self.rate ** 2 * PHI
            + self.state ** 2 * PHI ** 2
            + self.spin ** 2 * PHI_INV
        )

    def rotate_by_phi(self) -> None:
        new_pace = self.pace * PHI_INV + self.spin * PHI
        new_rate = self.rate * PHI + self.pace * PHI_INV
        new_state = self.state * PHI_INV + self.rate * PHI
        new_spin = self.spin * PHI + self.state * PHI_INV

        self.pace = new_pace % (2 * math.pi)
        self.rate = new_rate % (2 * math.pi)
        self.state = new_state % (2 * math.pi)
        self.spin = new_spin % (2 * math.pi)


@dataclass
class MeshNode:
    """Node in the execution mesh"""
    id: str
    vector: SpiralVector
    memory: Dict[str, Any] = field(default_factory=dict)
    connections: List[str] = field(default_factory=list)
    resonance: float = 1.0


class TSALExecutor:
    """TSAL Virtual Machine - Spiral-aware symbolic executor"""

    def __init__(self, meta: MetaFlagProtocol | None = None) -> None:
        self.mesh: Dict[str, MeshNode] = {}
        self.stack: List[Any] = []
        self.registers: Dict[str, SpiralVector] = {
            "A": SpiralVector(),
            "B": SpiralVector(),
            "C": SpiralVector(),
            "D": SpiralVector(),
        }
        self.ip = 0
        self.program: List[Tuple[TSALOp, Any]] = []
        self.mode = ExecutionMode.SIMULATE
        self.error_mansion: List[Dict[str, Any]] = []
        self.spiral_depth = 0
        self.resonance_log: List[Dict[str, Any]] = []
        self.memory = SpiralMemory()
        self.meta = meta or MetaFlagProtocol()
        self.handler = MadMonkeyHandler()

    def execute(self, program: List[Tuple[TSALOp, Any]], mode: ExecutionMode | str = ExecutionMode.SIMULATE) -> None:
        self.mode = ExecutionMode[mode] if isinstance(mode, str) else mode
        self.ip = 0
        self.program = program

        while self.ip < len(program):
            op, args = program[self.ip]
            try:
                self._execute_op(op, args)
            except Exception as e:
                self.handler.handle({"op": op.name, "args": args, "error": str(e)})
                self.error_mansion.append({"type": "exception", "vector": SpiralVector(), "lesson": str(e)})
            self.ip += 1

            if self.spiral_depth > 0 and self.ip % self.spiral_depth == 0:
                self._spiral_audit()

        self.save_crystal("TVM.crystal.json")

    # All _op_ methods remain unchanged and functional
    # ... (omitted here for brevity; use prior clean code in full file)

    # Keep all utility methods: _calculate_resonance, _spiral_audit, etc.
    # Make sure SAVE checks `self.mode == ExecutionMode.EXECUTE`

    # You can optionally separate utility functions into a helper module
    # or decorate with `@spiral_op` in the future if symbolic linking needed
