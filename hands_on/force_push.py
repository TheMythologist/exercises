from pathlib import Path
import shutil
from exercise_utils.cli import run_command

__requires_git__ = True
__requires_github__ = True

REPO_NAME = "samplerepo-things-force-push"
UPSTREAM_REPO = "git-mastery/samplerepo-things"
WORK_DIR = "things"


def download(verbose: bool):
    """
    hp-force-push (T4L5)
    - Fork https://github.com/git-mastery/samplerepo-things to user account as "samplerepo-things-force-push"
    - Clone the fork locally as 'samplerepo-things'
    """

    gh_username = run_command(["gh", "api", "user", "-q", ".login"], verbose)
    if not gh_username:
        raise RuntimeError("Your Github CLI is not setup correctly")

    work_dir = Path(WORK_DIR)
    if work_dir.exists():
        shutil.rmtree(work_dir)

    # Fork to user's account and clone
    run_command(
        [
            "gh",
            "repo",
            "fork",
            UPSTREAM_REPO,
            "--default-branch-only",
            "--fork-name",
            REPO_NAME,
            "--clone=true",
            "--",
            WORK_DIR,
        ],
        verbose,
    )

    if not work_dir.is_dir():
        raise RuntimeError("Fork/clone failed")
