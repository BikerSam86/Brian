"""Reconstruct spiral path and summarize changes."""

"""Produce a simple reflection summary from a Rev_Eng instance."""

from pathlib import Path
import json
from tsal.core.rev_eng import Rev_Eng
from tsal.tools.brian.optimizer import SymbolicOptimizer


def reflect(path: str = "src/tsal") -> str:
    opt = SymbolicOptimizer()
    rev = Rev_Eng(origin="reflect")
    lines = []
    for file in Path(path).rglob("*.py"):
        results = opt.analyze(file.read_text())
        rev.log_event("AUDIT", payload={"file": str(file), "count": len(results)})
        lines.append(str(file))
    summary = rev.summary()
    summary["files"] = lines
    return json.dumps(summary, indent=2)


def main() -> None:
    print(reflect())


if __name__ == "__main__":
    main()
