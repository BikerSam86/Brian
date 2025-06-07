from tsal.tools.goal_selector import Goal, score_goals


def test_score_goals():
    goals = [
        Goal("a", mesh_benefit=1, alignment=1, cost=1, novelty=0),
        Goal("b", mesh_benefit=2, alignment=0.5, cost=1, novelty=0),
    ]
    ordered = score_goals(goals)
    assert ordered[0].name == "b"
