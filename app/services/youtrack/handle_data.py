from datetime import datetime, timedelta
from tracemalloc import stop


def get_story_point(issues: list):
    list_result = 0
    try:
        if issues[0]["customFields"] != KeyError:
            for issue in issues:
                list_result += __story_points(issue)
            return int(list_result)
    except BaseException:
        __error_message(issues)


def issues_count(issues: list):
    try:
        if isinstance(issues, list):
            result = issues.__len__()
            if result == None or result == 0:
                return 0
            return f"**Total:**  {result}"
    except:
        __error_message(issues)


def critical_level(issues: list):
    stopper_message = ""
    total_issues = 0

    minor = 0
    normal = 0
    major = 0
    critical = 0
    stopper = 0

    try:
        if issues == []:
            return 0

        for issue in issues:
            total_issues += 1
            result = __critical_level(issue)

            if result == "3 - Normal":
                normal += 1
            elif result == "2 - Major":
                major += 1
            elif result == "1 - Critical":
                critical += 1
            elif result == "0 - Show-stopper":
                stopper += 1
            else:
                minor += 1

            if stopper != 0:
                stopper_message = f"Stopper: {stopper}\n"

        return f"Minor: {minor}\nNormal: {normal}\nMajor: {major}\nCritical: {critical}\n{stopper_message}**Total:** {total_issues}"
    except BaseException:
        __error_message(issues)


def solve_time_bugs(issues: list):
    try:
        if issues == []:
            return 0

        days, hours, minutes, total_issues = __solve_time_bugs(issues)
        return f"Days: {int(days)}\nHours: {int(hours)}\nMinutes: {int(minutes)}\n**Total: {total_issues}**"

    except BaseException:
        __error_message(issues)


def __error_message(arg):
    raise RuntimeError(f"Invalid Arguments: {arg}")


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
            if item["value"]["name"] is None:
                return
            return item["value"]["name"]


def __solve_time_bugs(issues):
    seconds = 0
    count_issue = 0

    for issue in issues:
        created_at = datetime.strptime(
            __unix_to_utc(issue["created"]), "%Y-%m-%d %H:%M"
        )
        resolved_at = datetime.strptime(
            __unix_to_utc(issue["resolved"]), "%Y-%m-%d %H:%M"
        )

        count_issue += 1
        time_result = resolved_at - created_at
        seconds += time_result.days * 24 * 3600 + time_result.seconds

    seconds = seconds / count_issue
    minutes, seconds_ = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)

    return (days, hours, minutes, count_issue)


def __unix_to_utc(unix):
    return (datetime.fromtimestamp(unix / 1000.0) - timedelta(hours=-3)).isoformat(
        " ", "minutes"
    )
