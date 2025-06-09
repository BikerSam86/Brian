from tsal.utils.octopus_api import get_products, get_electricity_tariffs


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
    if url.endswith("products/"):
        return DummyResponse({"results": ["p1"]})
    if url.endswith("products/P123/electricity-tariffs/"):
        return DummyResponse({"tariffs": ["t1"]})
    return DummyResponse(status=404)


def test_get_products(monkeypatch):
    monkeypatch.setattr("tsal.utils.octopus_api.requests.get", fake_get)
    res = get_products()
    assert res == {"results": ["p1"]}


def test_get_electricity_tariffs(monkeypatch):
    monkeypatch.setattr("tsal.utils.octopus_api.requests.get", fake_get)
    res = get_electricity_tariffs("P123")
    assert res == {"tariffs": ["t1"]}
