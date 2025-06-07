from pathlib import Path
from tsal.core.spiral_vector import SpiralVector
import argparse
import sys
from tsal.core.rev_eng import Rev_Eng
from tsal.tools.brian import analyze_and_repair, spiral_optimize

rev = Rev_Eng(origin="self_audit")


def optimize_spiral_order(vectors: list[SpiralVector]) -> list[SpiralVector]:
    """Return ``vectors`` sorted by φ-alignment."""
    return spiral_optimize(vectors)



def brian_repairs_brian(safe: bool = False) -> list[str]:
    """Run ``analyze_and_repair`` on every Python file in ``src/tsal``."""

    print("🧠 Initiating self-audit and repair sequence…")
    repaired: list[str] = []
    for file in Path("src/tsal").rglob("*.py"):
        repaired.extend(analyze_and_repair(file, repair=not safe))
    rev.log_event("Self-audit complete", state="repair", spin="φ")
    return repaired


def brian_improves_brian(safe: bool = False) -> list[str]:
    """Run repair cycle and log the event."""

    print("🧠 Evaluating improvements post-repair...")
    suggestions = brian_repairs_brian(safe=safe)
    rev.log_event("Improvement loop triggered", state="optimize", spin="up")
    return suggestions


    parser.add_argument("--safe", "--safe-mode", dest="safe", action="store_true")

def recursive_bestest_beast_loop(cycles: int = 3, safe_mode: bool = False) -> None:

    """Repeat ``brian_improves_brian`` ``cycles`` times."""

    if len(sys.argv) > 1 and not safe_mode:
        try:
            cycles = int(sys.argv[1])
        except ValueError:
            pass

    for i in range(cycles):
        print(f"🔁 Brian loop {i+1}/{cycles}")

        brian_improves_brian(safe_mode=safe_mode)


def cli_main() -> None:
    parser = argparse.ArgumentParser(description="Run bestest beast loop")
    parser.add_argument("cycles", nargs="?", type=int, default=1)
    parser.add_argument("--safe", action="store_true")
    args = parser.parse_args()
    recursive_bestest_beast_loop(args.cycles, safe_mode=args.safe_mode)

        if safe_mode:
            print("🛡 SAFE MODE ENABLED — Analysis only, no writes.")
            for file in Path("src/tsal").rglob("*.py"):
                analyze_and_repair(str(file), repair=False)
            rev.log_event("Safe audit pass", state="analyze", spin="φ")
        else:
            brian_improves_brian()

