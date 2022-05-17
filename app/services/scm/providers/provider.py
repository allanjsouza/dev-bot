from typing import List

from app.models.pull_request import PullRequest


class ScmProvider:
    def __init__(self):
        pass

    def get_open_pull_requests(self, repo_name) -> List[PullRequest]:
        pass
