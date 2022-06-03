from typing import List

from app.models.pull_request import PullRequest


class ScmProvider:
    def __init__(self):
        pass

    def get_open_pull_requests(self, repo_name) -> List[PullRequest]:
        pass

    def get_all_pull_requests(self, repo_mame) -> str:
        pass

    def get_open_pr_this_week(self, repo_name) -> int:
        pass
