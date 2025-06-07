"""Directory auditor using SymbolicOptimizer."""

import argparse
from pathlib import Path

from tsal.tools.brian.optimizer import SymbolicOptimizer


def audit_path(path: Path) -> dict[str, int]:
    opt = SymbolicOptimizer()
    files = list(path.rglob("*.py"))
    sigs = 0
    for file in files:
        sigs += len(opt.analyze(file.read_text()))
    return {"files": len(files), "signatures": sigs}


def main() -> None:
    parser = argparse.ArgumentParser(description="Spiral audit")
    parser.add_argument("path", nargs="?", default="src/tsal")
    parser.add_argument("--self", action="store_true", dest="self_flag")
    args = parser.parse_args()
    result = audit_path(Path(args.path))
    if args.self_flag:
        self_report = audit_path(Path("src/tsal"))
        result["self_signatures"] = self_report["signatures"]
    print(json.dumps(result))


if __name__ == "__main__":
    main()
