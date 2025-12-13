import pytest

from convert import convert


def test_conversion():
    assert convert(1) == 149597870700
    assert convert(50) == 7479893535000
    assert convert(0) == 0
    assert convert(-1) == -149597870700
    assert convert(0.1) == 14959787070


def test_error():
    with pytest.raises(TypeError):
        convert("1")
        convert("cat")


def test_float_conversion():
    assert convert(0.001) == pytest.approx(149597870.691, abs=0.001)


# if __name__ == "__main__":
#     main()
