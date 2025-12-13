"""
(Written by Jeff Truesdell 12-10-2025)
    Unit Test will test the function shorten() in a file named twttr.py
        1)  It will test to ensure that vowels are removed regardless of
            whether the letter is capital or lower case.
        2)  Numbers are ignored.
        3)  Integers and floats will raise a TypeError.
"""

import pytest

from twttr import shorten


def test_lower_case():
    assert shorten("twitter") == "twttr"
    assert shorten("orange") == "rng"


def test_all_caps():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("ORANGE") == "RNG"


def test_mix():
    assert shorten("Hello") == "Hll"
    assert shorten("SomEThiNg") == "SmThNg"


def test_no_vowels():
    assert shorten("bcdfg") == "bcdfg"


def test_spaces():
    assert shorten("Hello World") == "Hll Wrld"


def test_numbers():
    assert shorten("A1b2C3d4E5") == "1b2C3d45"
    assert shorten("12345") == "12345"


def test_integers():
    with pytest.raises(TypeError):
        shorten(1)
        shorten(1.1)


def test_punctuation():
    assert shorten("Won't") == "Wn't"
    assert shorten("I can't believe it works!") == " cn't blv t wrks!"
