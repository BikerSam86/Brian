"""Reconstruct spiral path and summarize changes."""
from pathlib import Path
from tsal.tools.brian.optimizer import SymbolicOptimizer
def reflect(path: str = "src/tsal") -> str:
    opt = SymbolicOptimizer()
    lines = []
    for file in Path(path).rglob("*.py"):
        results = opt.analyze(file.read_text())
        delta = sum(m["delta"] for _, m in results)
        lines.append(f"{file}: Δ{delta}")
    return "\n".join(lines)


def main() -> None:
    print(reflect())


if __name__ == "__main__":
    main()
    print(reflect_summary(rev))

    
if __name__ == "__main__":
    main()
    
=======

"""Reconstruct spiral path and summarize changes."""

def reflect(path: str = "src/tsal") -> str:
    opt = SymbolicOptimizer()
    lines = []
    for file in Path(path).rglob("*.py"):
        results = opt.analyze(file.read_text())
        delta = sum(m["delta"] for _, m in results)
        lines.append(f"{file}: Δ{delta}")
    return "\n".join(lines)
