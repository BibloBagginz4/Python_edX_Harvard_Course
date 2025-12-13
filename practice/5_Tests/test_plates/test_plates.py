"""
Testing Requirements:
    1) All vanity plates must start with at least two letters.
    2) All vanity plates may contain a maximum of 6 characters (letters
       or numbers) and a minimum of 2 characters.
    3) Numbers cannot be used in the middle of a plate; they must come
       at the end.
        3a) For example, AAA222 would be an acceptable vanity plate;
        3b) AAA22A would not be acceptable.
    4) The first number used cannot be a ‘0’.
    5) No periods, spaces, or punctuation marks are allowed.
"""

import pytest
from plates import is_valid


def test_length():
    assert is_valid("A") == False
    assert is_valid("AB") == True
    assert is_valid("ABC") == True
    assert is_valid("ABCD") == True
    assert is_valid("ABCDE") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("ABCDEFG") == False


def test_num_locations():
    assert is_valid("AB1234") == True
    assert is_valid("1ABCDE") == False
    assert is_valid("A1BCDE") == False
    assert is_valid("AB1CDE") == False
    assert is_valid("ABC1DE") == False
    assert is_valid("ABCD1E") == False
    assert is_valid("ABCDE1") == True


def test_zero_location():
    assert is_valid("ABCDE0") == False
    assert is_valid("ABCD10") == True


def test_no_punctuation():
    assert is_valid("AB.123") == False
    assert is_valid("AB!123") == False
    assert is_valid("AB 123") == False
    assert is_valid(" ABCDE") == False
    assert is_valid(".ABCDE") == False


def test_all_numbers():
    assert is_valid("123456") == False
