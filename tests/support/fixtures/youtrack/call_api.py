def valid_response_data():
    return {
        "issues": [
            {
                "project": {"name": "Test1", "$type": "Project"},
                "idReadable": "T1-25",
                "summary": "ASd12",
                "resolved": 1653444862821,
                "customFields": [
                    {
                        "value": {"name": "Minor", "$type": "EnumBundleElement"},
                        "name": "Priority",
                        "$type": "SingleEnumIssueCustomField",
                    },
                    {
                        "value": {"name": "Bug", "$type": "EnumBundleElement"},
                        "name": "Type",
                        "$type": "SingleEnumIssueCustomField",
                    },
                    {
                        "value": {"name": "Fixed", "$type": "StateBundleElement"},
                        "name": "State",
                        "$type": "StateIssueCustomField",
                    },
                    {
                        "value": None,
                        "name": "Assignee",
                        "$type": "SingleUserIssueCustomField",
                    },
                    {
                        "value": None,
                        "name": "Subsystem",
                        "$type": "SingleOwnedIssueCustomField",
                    },
                    {
                        "value": [],
                        "name": "Sprints",
                        "$type": "MultiVersionIssueCustomField",
                    },
                    {
                        "value": 5,
                        "name": "Story points",
                        "$type": "SimpleIssueCustomField",
                    },
                    {
                        "value": None,
                        "name": "Estimation",
                        "$type": "PeriodIssueCustomField",
                    },
                    {
                        "value": None,
                        "name": "Spent time",
                        "$type": "PeriodIssueCustomField",
                    },
                    {
                        "value": None,
                        "name": "Due Date",
                        "$type": "DateIssueCustomField",
                    },
                ],
                "created": 1653340971452,
                "id": "2-73",
                "$type": "Issue",
            },
            {
                "project": {"name": "Test1", "$type": "Project"},
                "idReadable": "T1-25",
                "summary": "ASd12",
                "resolved": 1653444862821,
                "customFields": [
                    {
                        "value": {"name": "Minor", "$type": "EnumBundleElement"},
                        "name": "Priority",
                        "$type": "SingleEnumIssueCustomField",
                    },
                    {
                        "value": {"name": "Bug", "$type": "EnumBundleElement"},
                        "name": "Type",
                        "$type": "SingleEnumIssueCustomField",
                    },
                    {
                        "value": {"name": "Fixed", "$type": "StateBundleElement"},
                        "name": "State",
                        "$type": "StateIssueCustomField",
                    },
                    {
                        "value": None,
                        "name": "Assignee",
                        "$type": "SingleUserIssueCustomField",
                    },
                    {
                        "value": None,
                        "name": "Subsystem",
                        "$type": "SingleOwnedIssueCustomField",
                    },
                    {
                        "value": [],
                        "name": "Sprints",
                        "$type": "MultiVersionIssueCustomField",
                    },
                    {
                        "value": 2,
                        "name": "Story points",
                        "$type": "SimpleIssueCustomField",
                    },
                    {
                        "value": None,
                        "name": "Estimation",
                        "$type": "PeriodIssueCustomField",
                    },
                    {
                        "value": None,
                        "name": "Spent time",
                        "$type": "PeriodIssueCustomField",
                    },
                    {
                        "value": None,
                        "name": "Due Date",
                        "$type": "DateIssueCustomField",
                    },
                ],
                "created": 1653340971452,
                "id": "2-73",
                "$type": "Issue",
            },
            {
                "project": {"name": "Test1", "$type": "Project"},
                "idReadable": "T1-25",
                "summary": "ASd12",
                "resolved": 1653444862821,
                "customFields": [
                    {
                        "value": {"name": "Minor", "$type": "EnumBundleElement"},
                        "name": "Priority",
                        "$type": "SingleEnumIssueCustomField",
                    },
                    {
                        "value": {"name": "Bug", "$type": "EnumBundleElement"},
                        "name": "Type",
                        "$type": "SingleEnumIssueCustomField",
                    },
                    {
                        "value": {"name": "Fixed", "$type": "StateBundleElement"},
                        "name": "State",
                        "$type": "StateIssueCustomField",
                    },
                    {
                        "value": None,
                        "name": "Assignee",
                        "$type": "SingleUserIssueCustomField",
                    },
                    {
                        "value": None,
                        "name": "Subsystem",
                        "$type": "SingleOwnedIssueCustomField",
                    },
                    {
                        "value": [],
                        "name": "Sprints",
                        "$type": "MultiVersionIssueCustomField",
                    },
                    {
                        "value": 3,
                        "name": "Story points",
                        "$type": "SimpleIssueCustomField",
                    },
                    {
                        "value": None,
                        "name": "Estimation",
                        "$type": "PeriodIssueCustomField",
                    },
                    {
                        "value": None,
                        "name": "Spent time",
                        "$type": "PeriodIssueCustomField",
                    },
                    {
                        "value": None,
                        "name": "Due Date",
                        "$type": "DateIssueCustomField",
                    },
                ],
                "created": 1653340971452,
                "id": "2-73",
                "$type": "Issue",
            },
        ]
    }


def error_response_json():
    return {"error": "Internal server error"}
