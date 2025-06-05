from tsal.utils.github_api import fetch_repo_files, fetch_languages
import requests


class DummyResponse:
    def __init__(self, *, json_data=None, text_data="", status=200):
        self._json = json_data
        self.text = text_data
        self.status_code = status

    def json(self):
        return self._json

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(f"status {self.status_code}")


def fake_get(url, headers=None):
    if url.startswith("https://api.github.com/repos/octocat/Hello-World/contents"):
        return DummyResponse(
            json_data=[
                {
                    "type": "file",
                    "name": "README",
                    "path": "README",
                    "download_url": "https://download/README",
                }
            ]
        )
    if url == "https://download/README":
        return DummyResponse(text_data="Hello World")
    if (
        url
        == "https://raw.githubusercontent.com/github/linguist/master/lib/linguist/languages.yml"
    ):
        return DummyResponse(text_data="Python: {}\nRust: {}")
    return DummyResponse(status=404)


def test_fetch_repo_files_public(monkeypatch):
    monkeypatch.setattr("tsal.utils.github_api.requests.get", fake_get)
    files = fetch_repo_files("octocat/Hello-World")
    assert files == {"README": "Hello World"}


def test_fetch_languages_live(monkeypatch):
    monkeypatch.setattr("tsal.utils.github_api.requests.get", fake_get)
    languages = fetch_languages()
    assert set(languages) == {"Python", "Rust"}

