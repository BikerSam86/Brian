"""Reconstruct spiral path and summarize changes."""

from pathlib import Path
import json
from tsal.tools.brian.optimizer import SymbolicOptimizer


def reflect(path: str = "src/tsal", as_json: bool = False) -> str:
    opt = SymbolicOptimizer()
    report = {}
    for file in Path(path).rglob("*.py"):
        results = opt.analyze(file.read_text())
        delta = sum(m["delta"] for _, m in results)
        report[str(file)] = delta
    if as_json:
        return json.dumps(report)
    return "\n".join(f"{k}: Δ{v}" for k, v in report.items())


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="reflect on repo")
    parser.add_argument("path", nargs="?", default="src/tsal")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    print(reflect(args.path, as_json=args.json))


if __name__ == "__main__":
    main()
