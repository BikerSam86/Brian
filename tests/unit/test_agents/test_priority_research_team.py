from tsal.agents.priority_research_team import PriorityResearchTeamAgent
from tsal.core.tsal_executor import TSALExecutor


def test_scan_creates_issue(monkeypatch):
    calls = []

    def fake_create_issue(repo, title, body, token):
        calls.append((repo, title, body, token))
        return 1

    monkeypatch.setattr(
        "tsal.agents.priority_research_team.create_issue", fake_create_issue
    )

    executor = TSALExecutor()
    executor.meta_agent.entropy = 70
    executor.meta_agent.health = 40

    agent = PriorityResearchTeamAgent(repo="me/repo", token="tok")
    report = agent.scan(executor)

    assert "high_entropy" in report.anomalies
    assert calls and calls[0][1] == "Threat detected"
