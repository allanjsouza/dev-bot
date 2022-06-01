from datetime import datetime


def pretty_date(past_time: datetime):
    """
    Get a datetime object and return a pretty string like:
    'an hour ago', 'Yesterday', '3 months ago', 'just now', etc
    """
    now = datetime.utcnow()
    diff = now - past_time
    diff_days = diff.days

    if diff_days < 0:
        return ""

    if diff_days == 0:
        return __intraday_date(diff.seconds)
    if diff_days == 1:
        return "Yesterday"
    if diff_days < 7:
        return __pluralize(diff_days, "day")
    if diff_days < 30:
        return __pluralize(diff_days // 7, "week")
    if diff_days < 365:
        return __pluralize(diff_days // 30, "month")
    return __pluralize(diff_days // 365, "year")


def __intraday_date(diff_seconds):
    if diff_seconds < 10:
        return "just now"
    if diff_seconds < 60:
        return __pluralize(diff_seconds, "second")
    if diff_seconds < 120:
        return "a minute ago"
    if diff_seconds < 3600:
        return __pluralize(diff_seconds // 60, "minute")
    if diff_seconds < 7200:
        return "an hour ago"
    if diff_seconds < 86400:
        return __pluralize(diff_seconds // 3600, "hour")


def __pluralize(value, term, plural_suffix="s"):
    result_term = term if value <= 1 else term + plural_suffix
    return f"{value} {result_term} ago"
