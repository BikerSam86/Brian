from tsal.tools.goal_selector import select_goal


def test_select_goal_picks_highest():
    goals = [
        {"name": "a", "impact": 1, "alignment": 0.9, "cost": 0.1},
        {"name": "b", "impact": 2, "alignment": 0.4, "cost": 0.2},
    ]
    best = select_goal(goals)
    assert best["name"] == "a"
