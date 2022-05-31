from unittest import TestCase, main, mock

import pytest
from support.fixtures.youtrack.call_api import valid_response_data

from app.services.youtrack import handle_data


def valid_arguments():
    arguments = valid_response_data()
    return arguments["issues"]


def invalid_arguments():
    return {"invalid": {"test": "invalid"}}


def assert_error(error):
    assert error == "RuntimeError: Invalid Arguments: {'invalid': {'test': 'invalid'}}"


class HandleDataTest(TestCase):
    def test_issues_count_valide_list(self):
        assert handle_data.issues_count(valid_arguments()) == "**Total:**  3"

    def test_issues_count_invalide(self):
        result = handle_data.issues_count(invalid_arguments())
        assert result == None

    def test_issues_count_empty_list(self):
        result = handle_data.issues_count([])
        assert result == 0

    def test_get_story_point_valid_arguments(self):
        result = handle_data.get_story_point(valid_arguments())
        assert result == 10

    def test_get_story_point_invalid_arguments_value(self):
        args = [
            {"customFields": [{"value": None, "name": "Story Point"}]},
            {"customFields": [{"value": None, "name": "Story Point"}]},
        ]
        result = handle_data.get_story_point(args)
        assert result == 0

    def test_get_story_point_invalid_arguments(self):
        with pytest.raises(RuntimeError) as error:
            handle_data.get_story_point(invalid_arguments())
        error_msg = error.exconly(True)
        assert_error(error_msg)

    def test_critical_level_valid_arguments(self):
        result = handle_data.critical_level(valid_arguments())
        assert result == "Minor: 3\nNormal: 0\nMajor: 0\nCritical: 0\n**Total:** 3"

    def test_critical_level_empty_list(self):
        result = handle_data.critical_level([])
        assert result == 0

    def test_critical_level_valid_arguments_one_value(self):
        args = [
            {"customFields": [{"value": {"name": "3 - Normal"}, "name": "Priority"}]},
            {"customFields": [{"value": {"name": "2 - Major"}, "name": "Priority"}]},
            {"customFields": [{"value": {"name": "1 - Critical"}, "name": "Priority"}]},
            {
                "customFields": [
                    {"value": {"name": "0 - Show-stopper"}, "name": "Priority"}
                ]
            },
            {"customFields": [{"value": {"name": "4 - Minor"}, "name": "Priority"}]},
        ]

        result = handle_data.critical_level(args)
        assert (
            result
            == "Minor: 1\nNormal: 1\nMajor: 1\nCritical: 1\nStopper: 1\n**Total:** 5"
        )

    def test_critical_level_invalid_value_name(self):
        args = [
            {"customFields": [{"value": {"name": None}, "name": "Priority"}]},
            {"customFields": [{"value": {"name": None}, "name": "Priority"}]},
            {"customFields": [{"value": {"name": None}, "name": "Priority"}]},
            {"customFields": [{"value": {"name": None}, "name": "Priority"}]},
            {"customFields": [{"value": {"name": None}, "name": "Priority"}]},
        ]

        result = handle_data.critical_level(args)
        assert result == 0

    def test_critical_level_invalid_arguments(self):
        with pytest.raises(RuntimeError) as error:
            handle_data.critical_level(invalid_arguments())
        error_msg = error.exconly(True)
        assert_error(error_msg)

    def test_solve_time_bugs_valid_arguments_and_invalids(self):
        args = [
            {"resolved": 1633444862821, "created": 1653310971452},
            {"resolved": 1653443862821, "created": 1653340971452},
            {"resolved": None, "created": 1653640971452},
        ]

        result = handle_data.solve_time_bugs(args)
        assert result == "Days: -115\nHours: 15\nMinutes: 7\n**Total: 2**"

    def test_solve_time_bugs_valid_arguments(self):
        result = handle_data.solve_time_bugs([])
        assert result == 0

    def test_solve_time_bugs_invalid_arguments(self):
        with pytest.raises(RuntimeError) as error:
            handle_data.solve_time_bugs(invalid_arguments())
        error_msg = error.exconly(True)
        assert_error(error_msg)


if __name__ == "__main__":
    main()
