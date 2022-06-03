from app.utils import datetime as date


def time_median_return(pulls: list):
    count_issue = 0
    seconds = 0
    pull_all_total = 0

    for item in pulls:
        if item.merged_at is not None and date.week_calcule(item.created_at):
            pull_all_total += 1
            count_issue += 1
            time_result = item.created_at - item.merged_at
            seconds += time_result.days * 24 * 3600 + time_result.seconds

    seconds = seconds / count_issue
    minutes, seconds_ = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)

    return (days, hours, minutes, pull_all_total)


def count_pulls(pulls: list):
    pull_open_total = 0

    for item in pulls:
        if item.created_at is not None:
            if date.week_calcule(item.created_at):
                pull_open_total += 1

    return pull_open_total
