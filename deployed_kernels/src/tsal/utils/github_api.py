import requests
from typing import Dict, List, Optional
import yaml


def _get_json(url: str, headers: Dict[str, str]) -> List[Dict]:
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    return resp.json()


def fetch_repo_files(
    repo: str,
    extensions: Optional[List[str]] = None,
    token: Optional[str] = None,
) -> Dict[str, str]:
    """Fetch files from a GitHub repository via the GitHub API."""
    base = f"https://api.github.com/repos/{repo}/contents"
    headers = {}
    if token:
        headers["Authorization"] = f"token {token}"

    def recurse(path: str) -> Dict[str, str]:
        url = base + ("/" + path if path else "")
        items = _get_json(url, headers)
        files: Dict[str, str] = {}
        for item in items:
            if item["type"] == "file":
                if extensions is None or any(
                    item["name"].endswith(ext) for ext in extensions
                ):
                    f = requests.get(item["download_url"], headers=headers)
                    if f.status_code == 200:
                        files[item["path"]] = f.text
            elif item["type"] == "dir":
                files.update(recurse(item["path"]))
        return files

    return recurse("")


def fetch_languages(
    url: str = (
        "https://raw.githubusercontent.com/github/linguist/"
        "master/lib/linguist/languages.yml"
    ),
) -> List[str]:
    """Return programming languages from GitHub's Linguist database."""
    resp = requests.get(url)
    resp.raise_for_status()
    data = yaml.safe_load(resp.text)
    return list(data.keys())
