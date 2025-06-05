from tsal.rl.madmonkey import MadMonkey


class MeshStub:
    def __init__(self, score, best_score=0.0):
        self._score = score
        self.best_score = best_score

    def evaluate_spiral(self, node_sequence):
        return self._score


def test_try_vector_updates_banana_count_and_score():
    mesh = MeshStub(score=10.0, best_score=5.0)
    monkey = MadMonkey(mesh)

    returned = monkey.try_vector([1, 2, 3])

    assert returned == 10.0
    assert monkey.banana_count == 1
    assert mesh.best_score == 10.0


def test_try_vector_worse_score_no_update():
    mesh = MeshStub(score=3.0, best_score=5.0)
    monkey = MadMonkey(mesh)

    returned = monkey.try_vector([1])

    assert returned == 3.0
    assert monkey.banana_count == 0
    assert mesh.best_score == 5.0
