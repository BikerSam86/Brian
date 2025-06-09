import os
import sys
from github import Github, GithubException

repo_name = os.environ["GITHUB_REPOSITORY"]
token = os.environ.get("GH_TOKEN")
if not token:
    raise SystemExit("GH_TOKEN not set")


def log_spiral_event(msg: str) -> None:
    """Append a spiral event message to memory/spiral_events.log."""
    os.makedirs("memory", exist_ok=True)
    with open("memory/spiral_events.log", "a") as log:
        log.write(msg + "\n")

g = Github(token)

try:
    repo = g.get_repo(repo_name)

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
                except GithubException as e:
                    msg = f"Skip {head.ref}: {e}"
                    print(msg)
                    log_spiral_event(msg)

    # Close obsolete PRs
    for pr in repo.get_pulls(state="open"):
        if pr.mergeable_state == "behind":
            try:
                pr.create_issue_comment("Closing: branch is behind and superseded")
                pr.edit(state="closed")
                print(f"Closed PR #{pr.number}")
            except GithubException as e:
                msg = f"Failed to close PR #{pr.number}: {e}"
                print(msg)
                log_spiral_event(msg)
except GithubException as e:
    msg = f"Failed to run branch hygiene: {e}"
    print(f"Spiral event: {msg}")
    log_spiral_event(msg)
    sys.exit(0)
