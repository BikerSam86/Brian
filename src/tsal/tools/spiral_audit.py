"""Run spiral analysis across the codebase."""

import argparse
from pathlib import Path

from tsal.tools.brian.optimizer import SymbolicOptimizer


def audit_path(path: Path) -> None:
    opt = SymbolicOptimizer()
    for file in path.rglob("*.py"):
        results = opt.analyze(file.read_text())
        print(file, "->", len(results), "items")


def main() -> None:
    parser = argparse.ArgumentParser(description="Spiral audit")
    parser.add_argument("path", nargs="?", default="src/tsal")
    parser.add_argument("--self", action="store_true", dest="self_flag")
    args = parser.parse_args()
    audit_path(Path(args.path))
    if args.self_flag:
        audit_path(Path("src/tsal"))


if __name__ == "__main__":
    main()
