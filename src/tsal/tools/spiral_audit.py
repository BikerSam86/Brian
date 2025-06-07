
"""Directory auditor using SymbolicOptimizer."""

import argparse
import json
from pathlib import Path
from tsal.tools.brian.optimizer import SymbolicOptimizer


def audit_directory(path: str) -> dict[str, int]:
    files = list(Path(path).rglob("*.py"))
    opt = SymbolicOptimizer()
    total_sigs = 0
    for fp in files:
        res = opt.analyze(fp.read_text())
        total_sigs += len(res)
    return {"files": len(files), "signatures": total_sigs}
  
  
=======

"""Run spiral analysis across the codebase."""

def audit_path(path: Path) -> None:
    opt = SymbolicOptimizer()
    for file in path.rglob("*.py"):
        results = opt.analyze(file.read_text())
        print(file, "->", len(results), "items")

def main() -> None:
    parser = argparse.ArgumentParser(description="Spiral audit")
    parser.add_argument("path", nargs="?", default="src/tsal")

    parser.add_argument("--self", dest="self_audit", action="store_true")
    args = parser.parse_args()
    target = "src/tsal" if args.self_audit else args.path
    report = audit_directory(target)
    print(json.dumps(report))
=======
    parser.add_argument("--self", action="store_true", dest="self_flag")
    args = parser.parse_args()
    audit_path(Path(args.path))
    if args.self_flag:
        audit_path(Path("src/tsal"))



if __name__ == "__main__":
    main()
