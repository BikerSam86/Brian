from tsal.utils.github_api import fetch_repo_files


def test_fetch_repo_files_public():
    files = fetch_repo_files("octocat/Hello-World")
    assert any(name.endswith("README") for name in files)

