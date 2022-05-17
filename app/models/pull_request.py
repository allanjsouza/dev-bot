from datetime import datetime

STATES = ["open", "closed"]
MERGING_STATES = ["clean", "unstable", "blocked", "dirty", "unknown"]


class User:
    def __init__(self, name, url="", icon_url=""):
        self.name = name
        self.url = url
        self.icon_url = icon_url


class PullRequest:
    def __init__(self, repo: str, number: int, title: str):
        self.repo = str(repo)
        self.number = int(number)
        self.title = str(title)
        self.assignees = []
        self.reviewers = []
        self.draft = False
        self.merged = False

    def add_author(self, author: User):
        self.author = author
        return self

    def add_assignee(self, assignee: User):
        self.assignees.append(assignee)
        return self

    def add_reviewer(self, reviewer: User):
        self.reviewers.append(reviewer)
        return self

    def add_state(self, state):
        if state not in STATES:
            raise ValueError(f"'{state}' not in {STATES}")
        self.state = state
        return self

    def add_merging_state(self, merging_state):
        if merging_state not in MERGING_STATES:
            raise ValueError(f"'{merging_state}' not in {MERGING_STATES}")
        self.merging_state = merging_state
        return self

    def add_body(self, body: str):
        self.body = str(body)
        return self

    def add_draft(self, draft: bool):
        if not type(draft) == bool:
            raise TypeError("it must be of type 'bool'")
        self.draft = draft
        return self

    def add_merged(self, merged: bool):
        if not type(merged) == bool:
            raise TypeError("it must be of type 'bool'")
        self.merged = merged
        return self

    def add_url(self, url: str):
        self.url = str(url)
        return self

    def add_created_at(self, created_at: datetime):
        if not type(created_at) == datetime:
            raise TypeError("it must be of type 'datetime'")
        self.created_at = created_at
        return self

    def add_updated_at(self, updated_at: datetime):
        if not type(updated_at) == datetime:
            raise TypeError("it must be of type 'datetime'")
        self.updated_at = updated_at
        return self
