from unittest import TestCase, main, mock

import pytest
from support.fixtures.youtrack.call_api import error_response_json, valid_response_data

from app.services.youtrack import call_api


def url():
    return call_api.url("21-2")


def success_request():
    return mock.Mock(**{"status_code": 200, "json.return_value": valid_response_data()})


def failure_request():
    return mock.Mock(**{"status_code": 500, "json.return_value": error_response_json()})


class Call_ApiTest(TestCase):
    def test_get_url(self):
        expectation_response = (
            "/savedQueries/21-2?fields=issues(idReadable,id,created,resolved,summary,"
            "customFields(name,value(name)),project(name))"
        )
        assert url() == expectation_response

    @mock.patch("app.services.youtrack.call_api.requests.get")
    def test_youtrack_get_success(self, mock_get):
        mock_get.return_value = success_request()

        response_api = call_api.get(url())

        assert response_api[0]["project"]["name"] == "Test1"
        assert response_api[0]["idReadable"] == "T1-25"

    @mock.patch("app.services.youtrack.call_api.requests.get")
    def test_youtrack_get_request_failure(self, mock_get):
        mock_get.return_value = failure_request()

        with pytest.raises(RuntimeError) as error:
            call_api.get(url())
        error_msg = error.exconly(True)

        assert error_msg == "RuntimeError: HTTP Status 500 - Internal server error"


if __name__ == "__main__":
    main()
