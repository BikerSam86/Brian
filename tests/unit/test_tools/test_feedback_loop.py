from tsal.tools.feedback_ingest import categorize, Feedback
from tsal.tools.alignment_guard import is_aligned, Change
from tsal.tools.goal_selector import Goal, score_goals
from tsal.tools.reflect import reflect


def test_categorize():
    lines = ["Good job", "bad idea"]
    fb = categorize(lines)
    assert fb[0].score > fb[1].score


def test_alignment_guard():
    c = Change("Add feature", 1.0, 1.0)
    assert is_aligned(c)
    c2 = Change("coerce user", 1.0, 1.0)
    assert not is_aligned(c2)


def test_goal_selector():
    goals = [
        Goal("a", mesh_benefit=1, alignment=1, cost=1, novelty=0),
        Goal("b", mesh_benefit=2, alignment=0.5, cost=1, novelty=0),
    ]
    ordered = score_goals(goals)
    assert ordered[0].name == "b"


def test_reflect(tmp_path):
    sample = tmp_path / "m.py"
    sample.write_text("def x():\n    pass\n")
    res = reflect(str(tmp_path))
    assert "m.py" in res
