from __future__ import annotations

import json
from dataclasses import dataclass, field
from enum import Enum, IntEnum, auto
from typing import Any, Dict, List, Optional, Tuple

from .spiral_memory import SpiralMemory
from .madmonkey_handler import MadMonkeyHandler
from .executor import MetaFlagProtocol
from .symbols import PHI, PHI_INV, HARMONIC_SEQUENCE


class ExecutionMode(Enum):
    SIMULATE = auto()
    TRACE = auto()
    EXECUTE = auto()
    ARM = auto()
    FORK = auto()


class TSALOp(IntEnum):
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
    pace: float = 0.0
    rate: float = 0.0
    state: float = 0.0
    spin: float = 0.0

    def magnitude(self) -> float:
        return (self.pace**2 + self.rate**2 + self.state**2 + self.spin**2) ** 0.5


@dataclass
class MeshNode:
    id: str
    vector: SpiralVector
    memory: Dict[str, Any] = field(default_factory=dict)
    connections: List[str] = field(default_factory=list)
    resonance: float = 1.0


class TSALExecutor:
    def __init__(self, meta: MetaFlagProtocol | None = None) -> None:
        self.mesh: Dict[str, MeshNode] = {}
        self.stack: List[Any] = []
        self.registers: Dict[str, SpiralVector] = {
            "A": SpiralVector(),
            "B": SpiralVector(),
            "C": SpiralVector(),
        }
        self.ip = 0
        self.program: List[Tuple[TSALOp, Any]] = []
        self.mode = ExecutionMode.SIMULATE
        self.error_mansion: List[Dict[str, Any]] = []
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

        self.save_crystal("TVM.crystal.json")

    def _execute_op(self, op: TSALOp, args: Any) -> None:
        pre = self._calculate_mesh_resonance()
        # Dispatch to external handler (not included here)
        # Example: tsal_ops.dispatch(op, args, context=self)
        post = self._calculate_mesh_resonance()
        self.resonance_log.append({"op": op.name, "pre": pre, "post": post, "delta": post - pre})
        self.memory.log_vector({"op": op.name, "resonance": post})

    def save_crystal(self, path: str = "TVM.crystal.json") -> None:
        state = {
            "mesh": {
                nid: {
                    "vector": [n.vector.pace, n.vector.rate, n.vector.state, n.vector.spin],
                    "memory": n.memory,
                    "connections": n.connections,
                    "resonance": n.resonance,
                }
                for nid, n in self.mesh.items()
            },
            "registers": {reg: [v.pace, v.rate, v.state, v.spin] for reg, v in self.registers.items()},
            "spiral_depth": getattr(self, "spiral_depth", 0),
            "resonance_log": self.resonance_log,
        }
        with open(path, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=2)

    def load_from_crystal(self, path: str) -> None:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.__init__()
        for nid, info in data.get("mesh", {}).items():
            vec = SpiralVector(*info["vector"])
            node = MeshNode(id=nid, vector=vec)
            node.memory = info.get("memory", {})
            node.connections = info.get("connections", [])
            node.resonance = info.get("resonance", 1.0)
            self.mesh[nid] = node
        for reg, vec in data.get("registers", {}).items():
            self.registers[reg] = SpiralVector(*vec)
        self.resonance_log = data.get("resonance_log", [])

    def _calculate_resonance(self, a: SpiralVector, b: SpiralVector) -> float:
        dot = a.pace * b.pace + a.rate * b.rate + a.state * b.state + a.spin * b.spin
        mag1 = a.magnitude()
        mag2 = b.magnitude()
        if mag1 == 0 or mag2 == 0:
            return 0.0
        res = dot / (mag1 * mag2)
        if abs(res - PHI) < 0.1:
            res *= PHI
        elif abs(res - PHI_INV) < 0.1:
            res *= PHI_INV
        return max(0.0, min(res, PHI))

    def _calculate_mesh_resonance(self) -> float:
        if not self.mesh:
            return 1.0
        total = 0.0
        count = 0
        for a in self.mesh.values():
            for cid in a.connections:
                if cid in self.mesh:
                    total += self._calculate_resonance(a.vector, self.mesh[cid].vector)
                    count += 1
        return total / count if count else 1.0

    def _spiral_audit(self) -> None:
        mesh_res = self._calculate_mesh_resonance()
        if mesh_res < PHI_INV:
            self.error_mansion.append({
                "type": "resonance_collapse",
                "vector": self.registers["A"],
                "resonance": mesh_res,
                "lesson": "Resonance below φ⁻¹ threshold",
            })
            if len(self.error_mansion) > 10:
                # Self-repair trigger (future: call tsal_ops._op_bloom)
                pass
