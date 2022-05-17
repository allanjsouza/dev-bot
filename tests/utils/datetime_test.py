import re
from datetime import datetime, timedelta

from app.utils.datetime import pretty_date


def test_pretty_date_now():
    assert pretty_date(datetime.utcnow()) == "just now"


def test_pretty_date_future():
    future_date = datetime.utcnow() + timedelta(minutes=1)
    assert pretty_date(future_date) == ""


def test_pretty_date_few_seconds():
    for seconds in range(10, 15):
        few_seconds_ago = datetime.utcnow() - timedelta(seconds=seconds)
        assert re.match(r"^\d{2} seconds ago$", pretty_date(few_seconds_ago))


def test_pretty_date_many_seconds():
    for seconds in range(50, 55):
        many_seconds_ago = datetime.utcnow() - timedelta(seconds=seconds)
        assert re.match(r"^\d{2} seconds ago$", pretty_date(many_seconds_ago))


def test_pretty_date_minute():
    minute_ago = datetime.utcnow() - timedelta(minutes=1)
    assert pretty_date(minute_ago) == "a minute ago"


def test_pretty_date_few_minutes():
    for minutes in range(10, 15):
        few_minutes_ago = datetime.utcnow() - timedelta(minutes=minutes)
        assert re.match(r"^\d{2} minutes ago$", pretty_date(few_minutes_ago))


def test_pretty_date_many_minutes():
    for minutes in range(50, 55):
        many_minutes_ago = datetime.utcnow() - timedelta(minutes=minutes)
        assert re.match(r"^\d{2} minutes ago$", pretty_date(many_minutes_ago))


def test_pretty_date_hour():
    hour_ago = datetime.utcnow() - timedelta(hours=1)
    assert pretty_date(hour_ago) == "an hour ago"


def test_pretty_date_few_hours():
    for hours in range(2, 6):
        few_hours_ago = datetime.utcnow() - timedelta(hours=hours)
        assert re.match(r"^\d hours ago$", pretty_date(few_hours_ago))


def test_pretty_date_many_hours():
    for hours in range(19, 23):
        many_hours_ago = datetime.utcnow() - timedelta(hours=hours)
        print(many_hours_ago)
        assert re.match(r"^\d{2} hours ago$", pretty_date(many_hours_ago))


def test_pretty_date_yesterday():
    yesterday = datetime.utcnow() - timedelta(days=1)
    assert pretty_date(yesterday) == "Yesterday"


def test_pretty_date_days_ago():
    for days in range(2, 6):
        past_time = datetime.utcnow() - timedelta(days=days)
        assert pretty_date(past_time) == f"{days} days ago"


def test_pretty_date_week_ago():
    past_time = datetime.utcnow() - timedelta(weeks=1)
    assert pretty_date(past_time) == "1 week ago"


def test_pretty_date_weeks_ago():
    for weeks in range(2, 4):
        past_time = datetime.utcnow() - timedelta(weeks=weeks)
        assert pretty_date(past_time) == f"{weeks} weeks ago"


def test_pretty_date_month_ago():
    past_time = datetime.utcnow() - timedelta(days=30)
    assert pretty_date(past_time) == "1 month ago"


def test_pretty_date_months_ago():
    for months in range(2, 12):
        past_time = datetime.utcnow() - timedelta(days=months*30)
        assert pretty_date(past_time) == f"{months} months ago"


def test_pretty_date_year_ago():
    past_time = datetime.utcnow() - timedelta(days=365)
    assert pretty_date(past_time) == "1 year ago"


def test_pretty_date_years_ago():
    for years in range(2, 3):
        past_time = datetime.utcnow() - timedelta(days=years*365)
        assert pretty_date(past_time) == f"{years} years ago"
