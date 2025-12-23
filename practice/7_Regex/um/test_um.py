import pytest

from um import count


def test_single_counts():
    assert count("hello, um, world") == 1
    assert count("um...") == 1
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("The umbrella is um red") == 1
    assert count("123 um, umbrellas") == 1


def test_multiple_count():
    assert count("Um, thanks um...") == 2
    assert count("um, hello, um, world") == 2


def test_zero_counts():
    assert count("This is a zero count scenario.") == 0
    assert count("yum") == 0
    assert count("tumble or fumble") == 0
    assert count("tantrum") == 0
    assert count("yummy") == 0
    assert count("Umbrella, umami and umpires") == 0
    assert count("123") == 0


def test_errors():
    with pytest.raises(TypeError):
        count(1)
