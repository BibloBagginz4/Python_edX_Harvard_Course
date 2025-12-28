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

    jar.deposit(11)
    assert str(jar) == "🍪" * 12


def test_deposit():
    jar = Jar()

    jar.deposit(1)
    assert jar.size == 1

    jar.deposit(2)
    assert jar.size == 3

    jar.deposit(9)
    assert jar.size == 12

    with pytest.raises(ValueError):
        jar.deposit(1)


def test_withdraw():
    jar = Jar()
    jar.deposit(12)

    jar.withdraw(1)
    assert jar.size == 11

    jar.withdraw(10)
    assert jar.size == 1

    jar.withdraw(1)
    assert jar.size == 0

    with pytest.raises(ValueError):
        jar.withdraw(1)


def test_invalid_capacity():
    with pytest.raises(ValueError):
        Jar(-1)

    with pytest.raises(ValueError):
        Jar("fish")

    with pytest.raises(ValueError):
        Jar(3.5)
