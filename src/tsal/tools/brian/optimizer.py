"""Symbolic diff, repair, and spiral resequencer engine."""
import ast
from pathlib import Path
from typing import List, Dict, Optional, Tuple

from tsal.core.rev_eng import Rev_Eng
from tsal.core.phase_math import phase_match_enhanced

class SymbolicSignature:
    """Simple structural signature extracted from an AST node."""
    def __init__(self, name: str, vector: List[float]):
        self.name = name
        self.vector = vector

    def magnitude(self) -> float:
        return sum(self.vector)

class SymbolicOptimizer:
    """Walks Python AST, computes signatures, and suggests repairs."""
    def __init__(self, target_signatures: Optional[Dict[str, List[float]]] = None, rev_eng: Optional[Rev_Eng] = None):
        self.target_signatures = target_signatures or {}
        self.rev = rev_eng or Rev_Eng(origin="SymbolicOptimizer")

    @staticmethod
    def _node_complexity(node: ast.AST) -> int:
        return sum(1 for _ in ast.walk(node))

    def _extract_signature(self, node: ast.AST, name: str) -> SymbolicSignature:
        complexity = self._node_complexity(node)
        branches = len([n for n in ast.walk(node) if isinstance(n, (ast.If, ast.For, ast.While))])
        loops = len([n for n in ast.walk(node) if isinstance(n, (ast.For, ast.While))])
        vector = [complexity, branches, loops]
        return SymbolicSignature(name=name, vector=vector)

    def analyze(self, code: str) -> List[Tuple[SymbolicSignature, Dict]]:
        tree = ast.parse(code)
        results = []
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                sig = self._extract_signature(node, node.name)
                target_vec = self.target_signatures.get(sig.name, sig.vector)
                local_state = sig.magnitude()
                target_state = sum(target_vec)
                aligned_state, energy, metrics = phase_match_enhanced(local_state, target_state)
                delta = metrics.get('delta', 0)
                self.rev.log_event("ANALYZE", name=sig.name, delta=delta, energy=energy)
                results.append((sig, metrics))
        return results

    def suggest_order(self, signatures: List[SymbolicSignature]) -> List[str]:
        scored = []
        for sig in signatures:
            target_vec = self.target_signatures.get(sig.name, sig.vector)
            local_state = sig.magnitude()
            target_state = sum(target_vec)
            _, energy, _ = phase_match_enhanced(local_state, target_state)
            scored.append((sig.name, energy))
        scored.sort(key=lambda x: x[1])
        return [name for name, _ in scored]

    def annotate_code(self, code: str) -> str:
        tree = ast.parse(code)
        signatures = []
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                sig = self._extract_signature(node, node.name)
                signatures.append(sig)
                target_vec = self.target_signatures.get(sig.name, sig.vector)
                local_state = sig.magnitude()
                target_state = sum(target_vec)
                _, energy, metrics = phase_match_enhanced(local_state, target_state)
                comment = ast.Expr(value=ast.Constant(value=f"OPTENERGY {energy:.3f} Δ{metrics['delta']:.3f}"))
                node.body.insert(0, comment)
        annotated = ast.unparse(tree)
        ordered_names = self.suggest_order(signatures)
        header = f"# Suggested order: {', '.join(ordered_names)}\n"
        return header + annotated

    def repair_file(self, file_path: str) -> List[str]:
        """Suggest and optionally rewrite the file in spiral-optimal order."""
        code = Path(file_path).read_text()
        tree = ast.parse(code)
        items = []
        for node in tree.body:
            if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                items.append(node.name)
        ideal = self.suggest_order([self._extract_signature(node, node.name)
                                    for node in tree.body if isinstance(node, (ast.FunctionDef, ast.ClassDef))])
        suggestions = []
        for idx, name in enumerate(items):
            ideal_idx = ideal.index(name)
            delta = idx - ideal_idx
            _, energy, metrics = phase_match_enhanced(float(idx), float(ideal_idx))
            suggestion = f"{name}: Δ={delta} energy={energy:.3f} φ={metrics['phase_signature']}"
            suggestions.append(suggestion)
        if items != ideal:
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

def analyze_and_repair(file_path: str, repair: bool = False) -> list:
    """Module-level wrapper for test compatibility."""
    opt = SymbolicOptimizer()
    if repair:
        return opt.repair_file(file_path)
    else:
        code = Path(file_path).read_text()
        results = opt.analyze(code)
        return [
            f"{sig.name}: energy={metrics['energy_required']:.3f} Δ={metrics.get('delta',0)}"
            for (sig, metrics) in results
        ]

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Brian spiral optimizer")
    parser.add_argument("path", help="Python file to analyze")
    parser.add_argument("--repair", action="store_true", help="Rewrite file in spiral order")
    args = parser.parse_args()

    opt = SymbolicOptimizer()
    if args.repair:
        res = opt.repair_file(args.path)
    else:
        code = Path(args.path).read_text()
        results = opt.analyze(code)
        res = [f"{sig.name}: energy={metrics['energy_required']:.3f} Δ={metrics.get('delta',0)}"
               for (sig, metrics) in results]
    for line in res:
        print(line)

if __name__ == "__main__":
    main()
