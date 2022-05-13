import pytest
from app.models.shouldideploy import ShouldideployMessage


@pytest.fixture
def shouldideploy_message():
    return ShouldideployMessage("check message testing purposes")


def test_quote_valid_params(shouldideploy_message: ShouldideployMessage):
    assert shouldideploy_message.text == "check message testing purposes"
    assert len(shouldideploy_message.thumb_url) == 0
    assert len(shouldideploy_message.footer) == 0
    assert len(shouldideploy_message.footer_icon) == 0
    assert shouldideploy_message.color == 0


def test_quote_empty_text():
    with pytest.raises(ValueError):
        ShouldideployMessage("")


def test_quote_empty_author(shouldideploy_message: ShouldideployMessage):
    shouldideploy_message.color = "#32a852"
    assert shouldideploy_message.color == 3319890


def test_quote_empty_author(shouldideploy_message: ShouldideployMessage):
    shouldideploy_message.color = "0x32a852"
    assert shouldideploy_message.color == 3319890


def test_quote_empty_author(shouldideploy_message: ShouldideployMessage):
    shouldideploy_message.color = "32a852"
    assert shouldideploy_message.color == 3319890


def test_quote_empty_author(shouldideploy_message: ShouldideployMessage):
    shouldideploy_message.color = "3319890"
    assert shouldideploy_message.color == 3319890


def test_quote_empty_author(shouldideploy_message: ShouldideployMessage):
    shouldideploy_message.color = 3319890
    assert shouldideploy_message.color == 3319890
