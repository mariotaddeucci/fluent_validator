import pytest

from fluent_validator.validators.value_validator import ValueValidator


@pytest.mark.parametrize(
    "value,expected",
    [
        (1, False),
        ("True", False),
        (True, True),
        (False, False),
    ],
)
def test_is_true(value, expected):
    validator = ValueValidator(value)
    assert validator._is_true() is expected


@pytest.mark.parametrize(
    "value,expected",
    [
        (True, False),
        (0, False),
        (None, False),
        (False, True),
    ],
)
def test_is_false(value, expected):
    validator = ValueValidator(value)
    assert validator._is_false() is expected
