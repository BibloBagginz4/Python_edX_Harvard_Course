"""
(Written by: Jeff Truesdell 12-19-2025)
"""

import pytest

from numb3rs import validate


def test_valid_addresses():
    assert validate("0.0.0.0") == True
    assert validate("0.1.1.1") == True
    assert validate("1.0.1.1") == True
    assert validate("1.1.0.1") == True
    assert validate("1.1.1.0") == True
    assert validate("255.255.255.255") == True
    assert validate("255.255.255.0") == True
    assert validate("127.0.0.1") == True
    assert validate("1.2.3.4") == True


def test_invalid_address():
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("275.3.6.28") == False
    assert validate("3.275.6.28") == False
    assert validate("3.6.275.28") == False
    assert validate("3.6.28.275") == False
    assert validate("256.0.0.0") == False
    assert validate("0.256.0.0") == False
    assert validate("0.0.256.0") == False
    assert validate("0.0.0.256") == False


def test_invalid_format():
    assert validate("255.255.255") == False
    assert validate("255.255") == False
    assert validate("255") == False
    assert validate("cat") == False
    assert validate("1a.1.1.1") == False
    assert validate("1.1a.1.1") == False
    assert validate("1.1.1a.1") == False
    assert validate("1.1.1.1a") == False
    assert validate("") == False
    assert validate(" ") == False
    assert validate("1 1 1 1") == False
    assert validate("1.2.3.4.5") == False
    assert validate("1..2.3") == False
    assert validate("1. .2.3") == False
    assert validate("...") == False


def test_invalid_leading_zeros():
    assert validate("01.0.0.0") == False
    assert validate("0.01.0.0") == False
    assert validate("0.0.01.0") == False
    assert validate("0.0.0.01") == False
    assert validate("001,192.168.1") == False
    assert validate("192.001.168.1") == False
    assert validate("192.168.001.1") == False
    assert validate("192.168.1.001") == False
