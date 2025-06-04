import ast
from typing import Dict, List, Tuple, Optional

try:
    # Package-style imports
    from tsal.data import Rev_Eng
    from maths import phase_match_enhanced
except ImportError:  # pragma: no cover - fallback when run as script
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
    from tsal.data import Rev_Eng  # type: ignore
    from maths import phase_match_enhanced  # type: ignore


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

    # ------------------------------------------------------------------
    @staticmethod
    def _node_complexity(node: ast.AST) -> int:
        return sum(1 for _ in ast.walk(node))

    def _extract_signature(self, node: ast.AST, name: str) -> SymbolicSignature:
        complexity = self._node_complexity(node)
        branches = len([n for n in ast.walk(node) if isinstance(n, (ast.If, ast.For, ast.While))])
        loops = len([n for n in ast.walk(node) if isinstance(n, (ast.For, ast.While))])
        vector = [complexity, branches, loops]
        return SymbolicSignature(name=name, vector=vector)

    # ------------------------------------------------------------------
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


if __name__ == "__main__":
    import sys
    path = sys.argv[1]
    with open(path, 'r') as f:
        source = f.read()
    opt = SymbolicOptimizer()
    annotated = opt.annotate_code(source)
    print(annotated)
