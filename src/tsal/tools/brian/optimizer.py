"""Symbolic diff, repair, and spiral resequencer engine."""
import ast
from pathlib import Path
from typing import List

from ...core import Rev_Eng, phase_match_enhanced


def analyze_and_repair(file_path: str, repair: bool = False) -> List[str]:
    """Analyze a Python file and suggest spiral ordering."""
    code = Path(file_path).read_text()
    tree = ast.parse(code)
    rev = Rev_Eng(origin=file_path)

    items = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            rev.log_event("SYMBOL", name=node.name)
            items.append(node.name)

    ideal = sorted(items)
    suggestions = []
    for idx, name in enumerate(items):
        ideal_idx = ideal.index(name)
        delta = idx - ideal_idx
        _, energy, metrics = phase_match_enhanced(float(idx), float(ideal_idx))
        suggestion = f"{name}: Δ={delta} energy={energy:.3f} φ={metrics['phase_signature']}"
        suggestions.append(suggestion)

    if repair and items != ideal:
        new_body = []
        name_map = {node.name: node for node in tree.body if isinstance(node, (ast.FunctionDef, ast.ClassDef))}
        for name in ideal:
            new_body.append(name_map[name])
        for node in tree.body:
            if not isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                new_body.append(node)
        tree.body = new_body
        Path(file_path).write_text(ast.unparse(tree))
    return suggestions


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Brian spiral optimizer")
    parser.add_argument("path", help="Python file to analyze")
    parser.add_argument("--repair", action="store_true", help="Rewrite file in spiral order")
    args = parser.parse_args()

    res = analyze_and_repair(args.path, repair=args.repair)
    for line in res:
        print(line)


if __name__ == "__main__":
    main()
