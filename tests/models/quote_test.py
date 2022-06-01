import pytest

from app.models.quote import Quote


@pytest.fixture
def quote():
    return Quote("words of inspiration", "influential figure")


def test_quote_valid_params(quote):
    assert quote.text == "words of inspiration"
    assert quote.author == "influential figure"


def test_quote_empty_text():
    with pytest.raises(ValueError):
        Quote("", "influential figure")


def test_quote_empty_author():
    with pytest.raises(ValueError):
        Quote("words of inspiration", "")
