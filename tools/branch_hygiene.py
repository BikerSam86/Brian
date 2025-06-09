import os
from github import Github, GithubException

repo_name = os.environ["GITHUB_REPOSITORY"]
token = os.environ.get("GH_PAT") or os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
if not token:
    raise SystemExit("No GitHub token provided")

g = Github(token)
try:
    repo = g.get_repo(repo_name)
except GithubException as e:
    raise SystemExit(f"GitHub access failed: {e.data.get('message', str(e))}")

# Remove merged branches
for pr in repo.get_pulls(state="closed", sort="updated", direction="desc"):
    if not pr.merged:
        continue
    head = pr.head
    if head.repo and head.repo.full_name == repo.full_name:
        if head.ref != repo.default_branch:
            try:
                repo.get_git_ref(f"heads/{head.ref}").delete()
                print(f"Deleted {head.ref}")
            except Exception as e:
                print(f"Skip {head.ref}: {e}")

# Close obsolete PRs
for pr in repo.get_pulls(state="open"):
    if pr.mergeable_state == "behind":
        pr.create_issue_comment("Closing: branch is behind and superseded")
        pr.edit(state="closed")
        print(f"Closed PR #{pr.number}")
