import pytest
from datetime import date

from seasons import convert_minutes


def test_valid_1_year():
    d1 = date(2025, 12, 26)
    d2 = date(2024, 12, 26)
    assert (
        convert_minutes(d1, d2)
        == "Five hundred twenty-five thousand, six hundred minutes"
    )


def test_valid_2_year():
    d1 = date(2025, 12, 26)
    d2 = date(2023, 12, 26)
    assert (
        convert_minutes(d1, d2)
        == "One million, fifty-two thousand, six hundred forty minutes"
    )


def test_valid_100_years():
    d1 = date(2000, 1, 1)
    d2 = date(1900, 1, 1)
    assert (
        convert_minutes(d1, d2)
        == "Fifty-two million, five hundred ninety-four thousand, five hundred sixty minutes"
    )
