
"""Produce a simple reflection summary from a Rev_Eng instance."""

import argparse
import json
from pathlib import Path
from tsal.core.rev_eng import Rev_Eng
from tsal.tools.brian.optimizer import SymbolicOptimizer

def reflect_summary(rev: Rev_Eng) -> str:
    return json.dumps(rev.summary(), indent=2)


def main() -> None:
    parser = argparse.ArgumentParser(description="Reflect on current state")
    parser.add_argument("--origin", default="reflect")
    args = parser.parse_args()
    rev = Rev_Eng(origin=args.origin)
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
