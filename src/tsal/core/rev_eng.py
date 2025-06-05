import os
import time
import uuid
from collections import defaultdict
from typing import Optional, Dict, List, Any


class Rev_Eng:
    """
    Reverse-Engineer (Rev_Eng): System-wide tracker and cataloguer for lineage, state, IO spin, and mesh context.
    """

    def __init__(self, origin: str = None, session_id: str = None):
        self.origin = origin or "Root"
        self.session_id = session_id or str(uuid.uuid4())
        self.lineage = []  # List of ancestor names/IDs
        self.events = []  # Log of (timestamp, action, details)
        self.state = {}  # Arbitrary live state storage
        self.data_stats = {  # Real-time stats for IO/data
            "total_bytes": 0,
            "chunk_count": 0,
            "last_rate": 0.0,  # bytes/sec
            "last_update": time.time(),
        }
        self.rate_log = []  # (timestamp, bytes, rate) tuples
        self.spin_log = []  # (timestamp, spin_dir, I/O, updown)
        self.mesh_coords = (
            {}
        )  # e.g., {x:..., y:..., z:..., vx:..., vy:..., vz:..., phase:..., mesh:...}
        self.identity = {}  # Who/What/Why/When/Where details

    # === LINEAGE TRACKING ===
    def add_lineage(self, name: str):
        self.lineage.append(name)

    def get_lineage(self) -> List[str]:
        return list(self.lineage)

    # === DATA FLOW TRACKING ===
    def log_data(self, n_bytes: int, direction: str, updown: str = None):
        now = time.time()
        dt = now - self.data_stats["last_update"]
        self.data_stats["total_bytes"] += n_bytes
        self.data_stats["chunk_count"] += 1
        rate = n_bytes / dt if dt > 0 else 0.0
        self.data_stats["last_rate"] = rate
        self.data_stats["last_update"] = now
        self.rate_log.append((now, n_bytes, rate))
        self.log_spin(direction=direction, updown=updown, I_O=direction)

    def log_spin(self, direction: str, updown: str = None, I_O: str = None):
        # direction: 'in', 'out', 'clockwise', 'counter', etc.
        now = time.time()
        self.spin_log.append((now, direction, I_O, updown))

    # === STATE/CONTEXT TRACKING ===
    def set_state(self, **kwargs):
        self.state.update(kwargs)

    def log_event(self, action: str, **details):
        now = time.time()
        self.events.append((now, action, details))

    def update_mesh_coords(self, **coords):
        self.mesh_coords.update(coords)

    def set_identity(
        self,
        who: str,
        what: str,
        where: str,
        when: Optional[str] = None,
        why: str = None,
    ):
        self.identity = {
            "who": who,
            "what": what,
            "where": where,
            "when": when or time.strftime("%Y-%m-%d %H:%M:%S"),
            "why": why,
        }

    # === UNIVERSAL REPORTING / EXPORT ===
    def summary(self) -> Dict[str, Any]:
        return {
            "origin": self.origin,
            "session_id": self.session_id,
            "lineage": self.lineage,
            "data_stats": self.data_stats,
            "recent_rate": self.data_stats["last_rate"],
            "rate_log": self.rate_log[-5:],
            "spin_log": self.spin_log[-5:],
            "state": self.state,
            "mesh_coords": self.mesh_coords,
            "identity": self.identity,
            "event_count": len(self.events),
        }

    def print_summary(self):
        import pprint

        pprint.pprint(self.summary())

    # === EXTENSIBLE: Custom Hooks for TSAL/mesh logging, e.g., phase, spiral, error dignity ===
    def log_tsal_phase(self, phase: str, symbol: str, context: Optional[str] = None):
        self.log_event("TSAL_PHASE", phase=phase, symbol=symbol, context=context)

    def log_error(self, err: str, location: str = None, recoverable: bool = True):
        self.log_event("ERROR", error=err, location=location, recoverable=recoverable)
        # Optional: Spiral/bloom logic could re-inject error into mesh for "mad monkey" learning


# Example Usage:
if __name__ == "__main__":
    rev = Rev_Eng(origin="Genesis_Spiral")
    rev.add_lineage("Proto_Node_0")
    rev.set_identity(
        "RevEngKernel", "Reverse-Engineer", "Mesh_Center", why="System Audit"
    )
    rev.log_data(4096, direction="in", updown="up")
    rev.log_data(2048, direction="out", updown="down")
    rev.update_mesh_coords(
        x=1, y=2, z=3, vx=0.1, vy=0.2, vz=0.3, phase="spiral", mesh="central"
    )
    rev.log_tsal_phase("ALIGN", "6", context="Startup Alignment")
    rev.log_error("Checksum mismatch", location="sector_17")
    rev.print_summary()
