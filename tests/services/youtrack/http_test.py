import pytest
from unittest import mock
from app.services.youtrack import http

from support.fixtures.youtrack.http import valid_response_data, error_response_raw

id_url = "21-2"


@pytest.fixture
def valid_response():
    return mock.Mock(
        **{"ok": True, "json.return_value": [valid_response_data()]})


@pytest.fixture
def error_response():
    return mock.Mock(**{"ok": False, "status_code": 500,
                     "raw": error_response_raw()})

def test_get_url():
    assert http.url(id_url) == "/savedQueries/21-2?fields=issues(idReadable,id,created,resolved,summary,customFields(name,value(name)),project(name))"


@mock.patch("app.services.youtrack.http.get")
def test_youtrack_get(mocking, valid_response):
    mocking.json.return_value = valid_response

    youtrack_response = http.get(http.url(id_url))

    assert youtrack_response["project"]["name"]
    assert youtrack_response["idReadable"]
