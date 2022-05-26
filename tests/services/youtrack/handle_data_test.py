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
        assert handle_data.issues_count(valid_arguments()) == 3

    def test_issues_count_invalide(self):
        with pytest.raises(RuntimeError) as error:
            handle_data.issues_count(invalid_arguments())
        error_msg = error.exconly(True)
        assert_error(error_msg)

    def test_get_story_point_valid_arguments(self):
        result = handle_data.get_story_point(valid_arguments())
        assert result == 10

    def test_get_story_point_invalid_arguments(self):
        with pytest.raises(RuntimeError) as error:
            handle_data.get_story_point(invalid_arguments())
        error_msg = error.exconly(True)
        assert_error(error_msg)

    def test_critical_level_valid_arguments(self):
        result = handle_data.critical_level(valid_arguments())
        assert result == "Minor: 3\nNormal: 0\nMajor: 0\nCritical: 0\n **Total: 3**"

    def test_critical_level_invalid_arguments(self):
        with pytest.raises(RuntimeError) as error:
            handle_data.critical_level(invalid_arguments())
        error_msg = error.exconly(True)
        assert_error(error_msg)

    def test_solve_time_bugs_valid_arguments(self):
        result = handle_data.solve_time_bugs(valid_arguments())
        assert result == "Days: 1\nHours: 4\nMinutes: 52\n**Total: 3**"

    def test_solve_time_bugs_invalid_arguments(self):
        with pytest.raises(RuntimeError) as error:
            handle_data.solve_time_bugs(invalid_arguments())
        error_msg = error.exconly(True)
        assert_error(error_msg)


if __name__ == "__main__":
    main()
