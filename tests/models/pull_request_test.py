from datetime import datetime

import pytest

from app.models.pull_request import PullRequest, User


@pytest.fixture
def user():
    return User("username_tester")


@pytest.fixture
def pull_request():
    return PullRequest("scm_repo_name", "731", "test: a pull request on scm system")


def test_pull_request_valid_params(pull_request: PullRequest):
    assert pull_request.repo == "scm_repo_name"
    assert pull_request.number == 731
    assert pull_request.title == "test: a pull request on scm system"
    assert len(pull_request.assignees) == 0
    assert len(pull_request.reviewers) == 0
    assert pull_request.draft == False
    assert pull_request.merged == False


def test_pull_request_add_author(pull_request: PullRequest, user: User):
    pull_request.add_author(user)
    assert pull_request.author == user


def test_pull_request_add_assignee(pull_request: PullRequest, user: User):
    pull_request.add_assignee(user)
    assert user in pull_request.assignees


def test_pull_request_add_reviewer(pull_request: PullRequest, user: User):
    pull_request.add_reviewer(user)
    assert user in pull_request.reviewers


def test_pull_request_add_state(pull_request: PullRequest):
    for state in "open closed".split(" "):
        pull_request = pull_request.add_state(state)
        assert pull_request.state == state


def test_pull_request_add_state_fail(pull_request: PullRequest):
    with pytest.raises(ValueError):
        pull_request.add_state("wrong_value")


def test_pull_request_add_merging_state(pull_request: PullRequest):
    for merging_state in "clean unstable blocked dirty unknown".split(" "):
        pull_request = pull_request.add_merging_state(merging_state)
        assert pull_request.merging_state == merging_state


def test_pull_request_add_merging_state_fail(pull_request: PullRequest):
    with pytest.raises(ValueError):
        pull_request.add_merging_state("wrong_value")


def test_pull_request_add_body(pull_request: PullRequest):
    pull_request = pull_request.add_body("Lorem ipsum dolor sit amet")
    assert pull_request.body == "Lorem ipsum dolor sit amet"


def test_pull_request_add_draft(pull_request: PullRequest):
    pull_request = pull_request.add_draft(True)
    assert pull_request.draft


def test_pull_request_add_draft_fail(pull_request: PullRequest):
    with pytest.raises(TypeError):
        pull_request.add_draft("Lorem ipsum dolor sit amet")


def test_pull_request_add_merged(pull_request: PullRequest):
    pull_request = pull_request.add_merged(True)
    assert pull_request.merged


def test_pull_request_add_merged_fail(pull_request: PullRequest):
    with pytest.raises(TypeError):
        pull_request.add_merged("Lorem ipsum dolor sit amet")


def test_pull_request_add_url(pull_request: PullRequest):
    pull_request = pull_request.add_url("https://scm-system.io/repo_name")
    assert pull_request.url == "https://scm-system.io/repo_name"


def test_pull_request_add_created_at(pull_request: PullRequest):
    now = datetime.now()
    pull_request = pull_request.add_created_at(now)
    assert pull_request.created_at == now


def test_pull_request_add_created_at_fail(pull_request: PullRequest):
    with pytest.raises(TypeError):
        pull_request.add_created_at("Lorem ipsum dolor sit amet")


def test_pull_request_add_updated_at(pull_request: PullRequest):
    now = datetime.now()
    pull_request = pull_request.add_updated_at(now)
    assert pull_request.updated_at == now


def test_pull_request_add_updated_at_fail(pull_request: PullRequest):
    with pytest.raises(TypeError):
        pull_request.add_updated_at("Lorem ipsum dolor sit amet")


def test_user_valid_params(user: User):
    assert user.name == "username_tester"
    assert user.url == ""
    assert user.icon_url == ""
