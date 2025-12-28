import pytest

from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0


def test_str():
    jar = Jar()

    assert str(jar) == ""

    jar.deposit(1)
    assert str(jar) == "🍪"

    jar.deposit(1)
    assert str(jar) == "🍪🍪"

    jar.deposit(10)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()

    jar.deposit(1)
    assert jar.size == 1

    jar.deposit(2)
    assert jar.size == 3

    jar.deposit(3)
    assert jar.size == 6

    jar.deposit(6)
    assert jar.size == 12


#   jar.deposit(1) == ValueError


def test_withdraw():
    jar = Jar()
    jar.deposit(12)

    jar.withdraw(1)
    assert jar.size == 11

    jar.withdraw(2)
    assert jar.size == 9

    jar.withdraw(3)
    assert jar.size == 6

    jar.withdraw(4)
    assert jar.size == 2

    jar.withdraw(2)
    assert jar.size == 0


def test_invalid_capacity_type():
    with pytest.raises(ValueError):
        Jar("fish")
    with pytest.raises(ValueError):
        Jar(3.5)


def test_invalid_capacity_value():
    with pytest.raises(ValueError):
        Jar(-1)


def test_invalid_deposit():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(13)


def test_invalid_withdraw():
    jar = Jar()
    jar.deposit(12)
    with pytest.raises(ValueError):
        jar.withdraw(13)
