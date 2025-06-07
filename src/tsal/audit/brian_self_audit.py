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


def recursive_bestest_beast_loop(cycles: int = 3, safe_mode: bool = False) -> None:
    """Repeat ``brian_improves_brian`` ``cycles`` times."""

    if len(sys.argv) > 1 and not safe_mode:
        try:
            cycles = int(sys.argv[1])
        except ValueError:
            pass

    for i in range(cycles):
        print(f"🔁 Brian loop {i+1}/{cycles}")
        if safe_mode:
            print("🛡 SAFE MODE ENABLED — Analysis only, no writes.")
            for file in Path("src/tsal").rglob("*.py"):
                analyze_and_repair(str(file), repair=False)
            rev.log_event("Safe audit pass", state="analyze", spin="φ")
        else:
            brian_improves_brian()


def cli_main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("cycles", type=int, nargs="?", default=3)
    parser.add_argument("--safe", action="store_true", help="Run in safe mode (analyze-only)")
    args = parser.parse_args()
    recursive_bestest_beast_loop(cycles=args.cycles, safe_mode=args.safe)
