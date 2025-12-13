"""
(Written by Jeff Truesdell 12-10-2025)
This Unit test implements three or more functions that collectively test
the function value() from a file called bank.py
Function Returns:
    1) 0 as an integer if input begins with "hello"
    2) 20 as an integer if input begins with "h" but not "hello"
    3) 100 otherwise
* Results are upper/lower case insensitive.
* Assume that the string passed to value() will not contain any leading
spaces.
"""

import pytest

from bank import value


def test_zero():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("HELLO") == 0


def test_twenty():
    assert value("hi") == 20
    assert value("Harold") == 20
    assert value("ha ha HA HA") == 20


def test_hundred():
    assert value("Wasup") == 100
    assert value("dude") == 100


def test_integers():
    with pytest.raises(TypeError):
        value(1)
        value(1.1)
        value(0)
