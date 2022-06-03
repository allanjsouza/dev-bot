from typing import List
from github import Github, UnknownObjectException

from app.config import Config
from app.helpers import github as help_github
from app.services.scm.errors import RepoNotFoundError
from app.services.scm.providers.provider import ScmProvider
from app.models.pull_request import PullRequest, User

GITHUB_BASE_URL = Config.GITHUB_BASE_URL
GITHUB_PAT = Config.GITHUB_PAT
GITHUB_ORG = Config.GITHUB_ORG
PULL_STATE_OPEN = "open"
PULL_STATE_ALL = "all"


class GithubProvider(ScmProvider):
    def __init__(self):
        self._github = Github(GITHUB_PAT)

    def get_open_pull_requests(self, repo_name):
        repo = self.get_repo(repo_name)
        open_pulls = repo.get_pulls(PULL_STATE_OPEN)

        return self.build_pull_requests(repo_name, open_pulls)

    def get_repo(self, repo_name):
        repo_full_name = self.repo_full_name(repo_name)
        try:
            return self._github.get_repo(repo_full_name)
        except UnknownObjectException:
            raise RepoNotFoundError(f"Could not find repo {repo_full_name}")

    def build_pull_requests(self, repo_name, pulls) -> List[PullRequest]:
        result = []
        for pull in pulls:
            result.append(self.build_pull_request(repo_name, pull))

        return result

    def build_pull_request(self, repo_name, pull) -> PullRequest:
        result = (
            PullRequest(repo_name, pull.number, pull.title)
            .add_author(self.build_user(pull.user))
            .add_state(pull.state)
            .add_merging_state(pull.mergeable_state)
            .add_body(pull.body)
            .add_draft(pull.draft)
            .add_merged(pull.merged)
            .add_url(pull.html_url)
            .add_created_at(pull.created_at)
            .add_updated_at(pull.updated_at)
        )

        for assignee in pull.assignees:
            result.add_assignee(self.build_user(assignee))

        reviewers, _teams = pull.get_review_requests()
        for reviewer in reviewers:
            result.add_reviewer(self.build_user(reviewer))

        return result

    def build_user(self, user) -> User:
        return User(
            name=user.login,
            url=f"{GITHUB_BASE_URL}/{user.login}",
            icon_url=f"{GITHUB_BASE_URL}/{user.login}.png",
        )

    def repo_full_name(self, repo_name):
        return "/".join([GITHUB_ORG, repo_name])

    def get_all_pull_requests(self, repo_name):
        repo = self.get_repo(repo_name)
        all_pulls = repo.get_pulls(state=PULL_STATE_ALL)

        return help_github.time_median_return(all_pulls)

    def get_open_pr_this_week(self, repo_name):
        repo = self.get_repo(repo_name)
        open_pulls = repo.get_pulls(PULL_STATE_OPEN)

        return help_github.count_pulls(open_pulls)
