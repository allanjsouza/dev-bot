def get_story_point(issues):
    list_result = 0
    for issue in issues:
        list_result += __story_points(issue)

    return list_result


def issues_count(issues):
    return issues.__len__()


def critical_level(issues):
    minor = 0
    normal = 0
    major = 0
    critical = 0

    for issue in issues:
        result = __critical_level(issue)
        if result == "Normal":
            normal += 1

        elif result == "Major":
            major += 1

        elif result == "Critical":
            critical += 1

        else:
            minor += 1

    return f"Minor: {minor}\nNormal: {normal}\nMajor: {major}\nCritical: {critical}"


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
