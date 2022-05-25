from datetime import datetime, timedelta


def get_story_point(issues):
    list_result = 0
    for issue in issues:
        list_result += __story_points(issue)

    return list_result


def issues_count(issues):
    return issues.__len__()


def critical_level(issues):
    total_issues = 0
    minor = 0
    normal = 0
    major = 0
    critical = 0

    for issue in issues:
        total_issues += 1
        result = __critical_level(issue)

        if result == "Normal":
            normal += 1

        elif result == "Major":
            major += 1

        elif result == "Critical":
            critical += 1

        else:
            minor += 1

    return f"Minor: {minor}\nNormal: {normal}\nMajor: {major}\nCritical: {critical}\n **Total: {total_issues}**"


def solve_time_bugs(issues):
    days, hours, minutes, seconds, total_issues = __solve_time_bugs(issues)

    return f"Days: {int(days)}\nHours: {int(hours)}\nMinutes: {int(minutes)}\nSeconds: {int(seconds)}\n**Total: {total_issues}**"


def __story_points(issue):
    for item in issue["customFields"]:
        if item["name"] == "Story points":
            if item["value"] is None:
                return 0
            else:
                return int(item["value"])


def __critical_level(issue):
    for item in issue["customFields"]:
        if item["name"] == "Priority":
            return item["value"]["name"]


def __solve_time_bugs(issues):
    seconds = 0
    count_issue = 0

    for issue in issues:
        created_at = datetime.strptime(__unix_to_utc(issue["created"]), "%Y-%m-%d %H:%M")
        resolved_at = datetime.strptime(__unix_to_utc(issue["resolved"]), "%Y-%m-%d %H:%M")

        count_issue += 1

        time_result =  resolved_at - created_at

        seconds += time_result.days * 24 * 3600 + time_result.seconds

    seconds = seconds/count_issue

    minutes, seconds_ = divmod(seconds, 60)

    hours, minutes = divmod(minutes, 60)

    days, hours = divmod(hours, 24)

    return (days, hours, minutes, seconds_, count_issue)


def __unix_to_utc(unix):
    return (datetime.fromtimestamp(unix / 1000.0) - timedelta(hours=-3)).isoformat(" ", "minutes")
