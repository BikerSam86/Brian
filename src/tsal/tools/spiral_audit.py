"""Directory auditor using SymbolicOptimizer."""

import argparse
import json
from pathlib import Path

from typing import List, Dict

from tsal.tools.brian.optimizer import SymbolicOptimizer

def audit_path(path: Path) -> Dict[str, int]:
    opt = SymbolicOptimizer()
    files = list(path.rglob("*.py"))
    sigs = 0
    for file in files:
        sigs += len(opt.analyze(file.read_text()))
    return {"files": len(files), "signatures": sigs}


def audit_paths(paths: List[Path]) -> Dict[str, Dict[str, int]]:
    """Audit multiple directories and return a mapping of results."""
    return {str(p): audit_path(p) for p in paths}

def main() -> None:
    parser = argparse.ArgumentParser(description="Spiral audit")
    parser.add_argument("paths", nargs="*", default=["src/tsal"])
    parser.add_argument("--self", action="store_true", dest="self_flag")
    args = parser.parse_args()
    path_objs = [Path(p) for p in args.paths]
    aggregate = audit_paths(path_objs)
    result: Dict[str, int] | Dict[str, Dict[str, int]]
    if len(aggregate) == 1:
        result = next(iter(aggregate.values()))
    else:
        result = aggregate
    if args.self_flag:
        self_report = audit_path(Path("src/tsal"))
        if isinstance(result, dict) and "files" in result:
            result["self_signatures"] = self_report["signatures"]
        else:
            result["self_signatures"] = self_report["signatures"]
    print(json.dumps(result))

if __name__ == "__main__":
    main()
