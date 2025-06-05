from tsal.utils.github_api import fetch_repo_files, fetch_languages


def test_fetch_repo_files_public():
    files = fetch_repo_files("octocat/Hello-World")
    assert any(name.endswith("README") for name in files)


def test_fetch_languages_live():
    languages = fetch_languages()
    assert "Python" in languages

