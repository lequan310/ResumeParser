import pytest
from freezegun import freeze_time

from core.workflows.parser.utils.tools import get_position_duration


# --- Test Cases for Valid Dates ---
@pytest.mark.parametrize(
    "start_str, end_str, expected_duration",
    [
        # Simple cases
        ("2022-01-15", "2023-01-15", {"year": 1, "month": 0}),  # Exactly 1 year
        ("2022-01-15", "2022-03-15", {"year": 0, "month": 2}),  # Exactly 2 months
        ("Jan 5, 2020", "Mar 10, 2023", {"year": 3, "month": 2}),  # Different formats
        ("2021/05/10", "2024/08/20", {"year": 3, "month": 3}),
        # Edge cases - Month boundaries
        ("2023-01-01", "2023-01-01", {"year": 0, "month": 0}),  # Same date
        (
            "2022-12-30",
            "2023-01-02",
            {"year": 0, "month": 0},
        ),  # Crossing year, < 1 month
        (
            "2023-01-31",
            "2023-02-28",
            {"year": 0, "month": 1},
        ),  # Jan 31 to Feb 28 (non-leap) -> 0 months, 28 days
        (
            "2024-01-31",
            "2024-02-29",
            {"year": 0, "month": 1},
        ),  # Jan 31 to Feb 29 (leap) -> 0 months, 29 days
        (
            "2024-01-31",
            "2024-03-01",
            {"year": 0, "month": 1},
        ),  # Jan 31 to Mar 1 -> 1 month, 1 day
        (
            "2024-01-31",
            "2024-03-30",
            {"year": 0, "month": 1},
        ),  # Jan 31 to Mar 30 -> 1 month, 30 days
        (
            "2024-01-31",
            "2024-03-31",
            {"year": 0, "month": 2},
        ),  # Jan 31 to Mar 31 -> Exactly 2 months
        # Start date after end date (relativedelta handles this)
        ("2024-01-01", "2023-01-01", {"year": -1, "month": 0}),
        (
            "2023-05-10",
            "2023-02-05",
            {"year": 0, "month": -3},
        ),  # relativedelta(months=-4, days=+25) -> months = -4
    ],
)
def test_get_position_duration_valid_dates(start_str, end_str, expected_duration):
    """Test get_position_duration with various valid date strings."""
    assert get_position_duration(start_str, end_str) == expected_duration


# --- Test Cases for Invalid Dates ---


# Use freezegun to control datetime.now() for predictable results
@freeze_time("2024-04-27 10:00:00")
def test_get_position_duration_invalid_start_date():
    """Test when the start date string is invalid."""
    # end_date = 2023-01-01, start_date = now() = 2024-04-27
    expected = {
        "year": -1,
        "month": -3,
    }  # relativedelta(2023-01-01, 2024-04-27) -> months=-16 -> year=-2, month=-4
    assert get_position_duration("invalid-date", "2023-01-01") == expected


@freeze_time("2024-04-27 10:00:00")
def test_get_position_duration_invalid_end_date():
    """Test when the end date string is invalid."""
    # start_date = 2023-01-01, end_date = now() = 2024-04-27
    expected = {
        "year": 1,
        "month": 3,
    }  # relativedelta(2024-04-27, 2023-01-01) -> months=15 -> year=1, month=3
    assert get_position_duration("2023-01-01", "not-a-date") == expected


@freeze_time("2024-04-27 10:00:00")
def test_get_position_duration_both_invalid_dates():
    """Test when both date strings are invalid."""
    # start_date = now(), end_date = now()
    expected = {"year": 0, "month": 0}  # relativedelta(now, now)
    assert get_position_duration("invalid-start", "invalid-end") == expected
