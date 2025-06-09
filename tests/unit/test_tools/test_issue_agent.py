from tsal.tools.issue_agent import create_issue, handle_http_error


class DummyResp:
    def __init__(self, json_data=None, status=201):
        self._json = json_data or {}
        self.status_code = status

    def json(self):
        return self._json

    def raise_for_status(self):
        if self.status_code >= 400:
            raise RuntimeError


def test_create_issue(monkeypatch):
    def fake_post(url, json=None, headers=None):
        return DummyResp({"number": 42})

    monkeypatch.setattr("tsal.tools.issue_agent.requests.post", fake_post)
    num = create_issue("me/repo", "t", "b", "tok")
    assert num == 42


def test_handle_http_error(monkeypatch):
    calls = []

    def fake_post(url, json=None, headers=None):
        calls.append(json["title"])
        return DummyResp()

    monkeypatch.setattr("tsal.tools.issue_agent.requests.post", fake_post)
    handle_http_error("me/repo", RuntimeError("status 403"), "log", token="tok")
    assert calls == ["Auth failure detected"]


def test_handle_http_error_no_token(monkeypatch):
    logs = []

    def fake_diag(msg):
        logs.append(msg)

    monkeypatch.setattr("tsal.tools.issue_agent.sandbox_diagnostics", fake_diag)
    handle_http_error("me/repo", RuntimeError("status 403"), "log", token=None)
    assert logs and "log" in logs[0]

