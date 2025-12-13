""" """

import pytest
from fuel import convert, gauge


def test_convert_positive_ints():
    assert convert("1/2") == 50
    assert convert("250/1000") == 25
    assert convert("30/50") == 60


def test_convert_strings():
    with pytest.raises(ValueError):
        convert("a/b")
        convert("cat/dog")
        convert("cats and dogs")


def test_convert_y_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
        convert("0/0")


def test_convert_xbigger():
    with pytest.raises(ValueError):
        convert("5/4")
        convert("900/50")


def test_gauge():
    assert gauge(0.5) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(99.5) == "F"
    assert gauge(50) == "50%"
    assert gauge(2) == "2%"
    assert gauge(98) == "98%"
