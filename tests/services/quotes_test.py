import pytest
from unittest import mock
from app.services import quotes

from support.fixtures.quotes import valid_response_data, error_response_raw


@pytest.fixture
def valid_response():
    return mock.Mock(
        **{"ok": True, "json.return_value": [valid_response_data()]})


@pytest.fixture
def error_response():
    return mock.Mock(**{"ok": False, "status_code": 500,
                     "raw": error_response_raw()})


def test_get_service_name():
    assert quotes.get_service_name() == "zenquotes.io"


@mock.patch("app.services.quotes.requests.get")
def test_get_random_quote(mocking, valid_response):
    mocking.return_value = valid_response

    random_quote = quotes.get_random_quote()

    assert random_quote.text == "words of inspiration"
    assert random_quote.author == "influential figure"


@mock.patch("app.services.quotes.requests.get")
def test_get_random_quote_request_failure(mocking, error_response):
    mocking.return_value = error_response

    with pytest.raises(RuntimeError) as error:
        quotes.get_random_quote()
    error_msg = error.exconly(True)

    assert error_msg == "RuntimeError: HTTP Status 500 - Internal server error"
