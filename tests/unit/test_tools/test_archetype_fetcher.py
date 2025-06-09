from tsal.tools.archetype_fetcher import fetch_online_mesh, merge_mesh
import json
from pathlib import Path

class DummyResp:
    def __init__(self, text: str) -> None:
        self.text = text
        self.status_code = 200
    def raise_for_status(self):
        pass


def test_merge_mesh(tmp_path):
    mesh = tmp_path / "mesh.json"
    mesh.write_text(json.dumps([{"name": "A"}]))
    merge_mesh(mesh, [{"name": "B"}])
    data = json.loads(mesh.read_text())
    assert any(e["name"] == "B" for e in data)


def test_fetch_online_mesh(monkeypatch):
    def fake_get(url):
        return DummyResp('[{"name": "X"}]')
    monkeypatch.setattr('tsal.tools.archetype_fetcher.requests.get', fake_get)
    entries = fetch_online_mesh('http://example.com')
    assert entries and entries[0]['name'] == 'X'
