from tsal.core.spiral_vector import SpiralVector
from tsal.core.rev_eng import Rev_Eng
from tsal.tools.brian import analyze_and_repair, spiral_optimize


def optimize_spiral_order(vectors: list[SpiralVector]) -> list[SpiralVector]:
    """Return ``vectors`` sorted by φ-alignment."""
    return spiral_optimize(vectors)


def brian_repairs_brian():
    print("🧠 Initiating self-audit and repair sequence…")
    repaired = analyze_and_repair("src/tsal/", repair=True)
    Rev_Eng.log_event("Self-audit complete", state="repair", spin="φ")
    return repaired


def brian_improves_brian():
    print("🧠 Evaluating improvements post-repair...")
    repaired = brian_repairs_brian()
    optimized = optimize_spiral_order(repaired)
    Rev_Eng.log_event("Improvement loop triggered", state="optimize", spin="up")
    return optimized


def recursive_bestest_beast_loop(cycles: int = 3) -> None:
    for i in range(cycles):
        print(f"🔁 Brian loop {i+1}/{cycles}")
        brian_improves_brian()
