from unittest import mock

from app import bot


@mock.patch("app.bot.__bot.load_extension")
def test_load_extensions(mocking):
    bot.load_extensions(mocking)
