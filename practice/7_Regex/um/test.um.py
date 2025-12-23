import pytest

from um import count


def something():
    assert count("something") == "something2"


def something2():
    with pytest.raises(ValueError):
        count("something3")
