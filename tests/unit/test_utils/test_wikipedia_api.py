from tsal.utils.wikipedia_api import search, summary


class DummyResponse:
    def __init__(self, json_data=None, status=200):
        self._json = json_data
        self.status_code = status

    def json(self):
        return self._json

    def raise_for_status(self):
        if self.status_code >= 400:
            raise RuntimeError


def fake_get(url):
    if "list=search" in url:
        return DummyResponse({"query": {"search": ["x"]}})
    if url.startswith("https://en.wikipedia.org/api/rest_v1/page/summary/"):
        return DummyResponse({"title": "x", "extract": "y"})
    return DummyResponse(status=404)


def test_search(monkeypatch):
    monkeypatch.setattr("tsal.utils.wikipedia_api.requests.get", fake_get)
    res = search("tsal")
    assert res == {"query": {"search": ["x"]}}


def test_summary(monkeypatch):
    monkeypatch.setattr("tsal.utils.wikipedia_api.requests.get", fake_get)
    res = summary("tsal")
    assert res == {"title": "x", "extract": "y"}
