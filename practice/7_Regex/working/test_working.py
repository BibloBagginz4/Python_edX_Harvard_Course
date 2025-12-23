import pytest

from working import convert


def test_valid_times():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("9 AM to 5:30 PM") == "09:00 to 17:30"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"


def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

    with pytest.raises(ValueError):
        convert("9:00 AM - 17:00 PM")

    with pytest.raises(ValueError):
        convert("09:00 to 17:00)")

    with pytest.raises(ValueError):
        convert("09 AM to 5:001 PM")

    with pytest.raises(ValueError):
        convert("10:7 AM - 5:1 PM")


def test_invalid_range():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")


def test_invalid_case():
    with pytest.raises(ValueError):
        convert("8 PM to 8 am")

    with pytest.raises(ValueError):
        assert convert("8:00 PM to 8:00 am")
