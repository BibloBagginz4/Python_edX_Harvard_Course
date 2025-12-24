import pytest

from validators import ValidationError
from response import validate


def test_valid():
    assert validate("malan@harvard.edu") == True
    assert validate("sdsutruesdell@yahoo.com") == True
    assert validate("sdsuguard-2018@yahoo.com") == True


# Since the validators returns an object, not an error, we must check
# for an object(Instance)
def test_invalid():
    result = validate("fred@@yahoo.edu")
    assert isinstance(result, ValidationError)
    result = validate("malan@@harvard.edu")
    assert isinstance(result, ValidationError)
    result = validate("sdsutruesdell@yahoo..com")
    assert isinstance(result, ValidationError)
    result = validate("malan")
    assert isinstance(result, ValidationError)
    result = validate("malan at harvard dot edu")
    assert isinstance(result, ValidationError)


# Since validators returns an error code if an interger is entered, we
# must check for an Error Code being raised.
def test_invalid_type():
    with pytest.raises(AttributeError):
        validate(1)
