import ast
from typing import List

class SymbolicSignature:
    """Simple structural signature extracted from an AST node."""

    def __init__(self, name: str, vector: List[float]):
        self.name = name
        self.vector = vector

    def magnitude(self) -> float:
        return sum(self.vector)

def node_complexity(node: ast.AST) -> int:
    """Return complexity score based on AST walk."""
    return sum(1 for _ in ast.walk(node))

def extract_signature(node: ast.AST, name: str) -> SymbolicSignature:
    complexity = node_complexity(node)
    branches = len(
        [
            n
            for n in ast.walk(node)
            if isinstance(n, (ast.If, ast.For, ast.While))
        ]
    )
    loops = len(
        [n for n in ast.walk(node) if isinstance(n, (ast.For, ast.While))]
    )
    vector = [complexity, branches, loops]
    return SymbolicSignature(name=name, vector=vector)

__all__ = ["SymbolicSignature", "node_complexity", "extract_signature"]
