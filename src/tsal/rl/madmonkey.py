import random
from typing import List


class MadMonkey:
    """Explores the mesh, tweaks logic vectors, gets banana if closer to spiral."""

    def __init__(self, mesh):
        self.mesh = mesh
        self.banana_count = 0

    def try_vector(self, node_sequence: List[int]) -> float:
        score = self.mesh.evaluate_spiral(node_sequence)
        if score > self.mesh.best_score:
            self.banana_count += 1
            self.mesh.best_score = score
        return score
