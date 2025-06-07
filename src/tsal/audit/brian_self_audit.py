from pathlib import Path
from tsal.core.spiral_vector import SpiralVector
from tsal.core.rev_eng import Rev_Eng
from tsal.tools.brian import analyze_and_repair, spiral_optimize

rev = Rev_Eng(origin="self_audit")


def optimize_spiral_order(vectors: list[SpiralVector]) -> list[SpiralVector]:
    """Return ``vectors`` sorted by φ-alignment."""
    return spiral_optimize(vectors)



def brian_repairs_brian() -> list[str]:
    """Run ``analyze_and_repair`` on every Python file in ``src/tsal``."""

    print("🧠 Initiating self-audit and repair sequence…")
    repaired: list[str] = []
    for file in Path("src/tsal").rglob("*.py"):
        repaired.extend(analyze_and_repair(str(file), repair=True))
    rev.log_event("Self-audit complete", state="repair", spin="φ")
    return repaired


def brian_improves_brian() -> list[str]:
    """Run repair cycle and log the event."""

    print("🧠 Evaluating improvements post-repair...")
    suggestions = brian_repairs_brian()
    rev.log_event("Improvement loop triggered", state="optimize", spin="up")
    return suggestions


import sys


def recursive_bestest_beast_loop(cycles: int = 3) -> None:
    """Repeat ``brian_improves_brian`` ``cycles`` times."""

    if len(sys.argv) > 1:
        try:
            cycles = int(sys.argv[1])
        except ValueError:
            pass

    for i in range(cycles):
        print(f"🔁 Brian loop {i+1}/{cycles}")
        brian_improves_brian()
