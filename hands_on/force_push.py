from pathlib import Path
import shutil
from exercise_utils.cli import run_command

__requires_git__ = True
__requires_github__ = True

REPO_NAME = "samplerepo-things-force-push"
UPSTREAM_REPO = "git-mastery/samplerepo-things"
WORK_DIR = "things"


def download(verbose: bool):
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
