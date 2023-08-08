import pytest

from fluent_validator.validators.type_validator import TypeValidator


@pytest.mark.parametrize(
    "value,dtype,expected",
    [
        (1, int, True),
        ("hello", str, True),
        (2.0, float, True),
        (1, str, False),
        ("hello", int, False),
    ],
)
def test_is_instance(value, dtype, expected):
    validator = TypeValidator(value)
    assert validator._is_instance(dtype) is expected


@pytest.mark.parametrize(
    "value,expected",
    [
        (1, False),
        ("hello", False),
        (2.0, False),
        (lambda x: x, True),
    ],
)
def test_is_callable(value, expected):
    validator = TypeValidator(value)
    assert validator._is_callable() is expected


@pytest.mark.parametrize(
    "value,expected",
    [
        (1, False),
        ("hello", True),
        (2.0, False),
        (lambda x: x, False),
        ([1, 2, 3], True),
        ((1, 2, 3), True),
        ({1, 2, 3}, True),
        ({"a": 1, "b": 2, "c": 3}, True),
        (range(2), True),
    ],
)
def test_is_iterable(value, expected):
    validator = TypeValidator(value)
    assert validator._is_iterable() is expected


@pytest.mark.parametrize(
    "value,expected",
    [
        (1, False),
        ("hello", True),
    ],
)
def test_is_string(value, expected):
    validator = TypeValidator(value)
    assert validator._is_string() is expected


@pytest.mark.parametrize(
    "value,expected",
    [
        (1, False),
        (False, True),
        (True, True),
        (0, False),
        (None, False),
    ],
)
def test_is_bool(value, expected):
    validator = TypeValidator(value)
    assert validator._is_bool() is expected
