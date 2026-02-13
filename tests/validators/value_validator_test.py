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


@pytest.mark.parametrize(
    "value,expected",
    [
        (1, True),
        (2, False),
        (0, False),
    ],
)
def test_equal(value, expected):
    validator = ValueValidator(value)
    assert validator._equal(1) is expected


@pytest.mark.parametrize(
    "value,args,expected",
    [
        (1, [1, 2, 3], True),
        (2, [1, 2, 3], True),
        (4, [1, 2, 3], False),
    ],
)
def test_is_in(value, args, expected):
    validator = ValueValidator(value)
    assert validator._is_in(*args) is expected


@pytest.mark.parametrize(
    "value,expected",
    [
        (1, True),
        (0, False),
        (-1, False),
    ],
)
def test_greater_than(value, expected):
    validator = ValueValidator(value)
    assert validator._greater_than(0) is expected


@pytest.mark.parametrize(
    "value,expected",
    [
        (1, True),
        (2, False),
        (3, False),
    ],
)
def test_less_than(value, expected):
    validator = ValueValidator(value)
    assert validator._less_than(2) is expected


@pytest.mark.parametrize(
    "value,expected",
    [
        (1, True),
        (2, True),
        (0, False),
    ],
)
def test_greater_or_equal_than(value, expected):
    validator = ValueValidator(value)
    assert validator._greater_or_equal_than(1) is expected


@pytest.mark.parametrize(
    "value,expected",
    [
        (1, True),
        (2, True),
        (3, False),
    ],
)
def test_less_or_equal_than(value, expected):
    validator = ValueValidator(value)
    assert validator._less_or_equal_than(2) is expected


@pytest.mark.parametrize(
    "value,expected",
    [
        (1, True),
        (2, True),
        (0, False),
    ],
)
def test_min(value, expected):
    validator = ValueValidator(value)
    assert validator._min(1) is expected


@pytest.mark.parametrize(
    "value,expected",
    [
        (1, True),
        (2, True),
        (3, False),
    ],
)
def test_max(value, expected):
    validator = ValueValidator(value)
    assert validator._max(2) is expected


@pytest.mark.parametrize(
    "value,min,max,expected",
    [
        (1, 0, 2, True),
        (2, 0, 2, True),
        (0, 0, 2, True),
        (3, 0, 2, False),
    ],
)
def test_between(value, min, max, expected):
    validator = ValueValidator(value)
    assert validator._between(min, max) is expected


@pytest.mark.parametrize(
    "value,min_length,expected",
    [
        ([1, 2, 3], 2, True),
        ([1, 2, 3], 3, True),
        ([1, 2, 3], 4, False),
    ],
)
def test_contains_at_least(value, min_length, expected):
    validator = ValueValidator(value)
    assert validator._contains_at_least(min_length) is expected


@pytest.mark.parametrize(
    "value,max_length,expected",
    [
        ([1, 2, 3], 2, False),
        ([1, 2, 3], 3, True),
        ([1, 2, 3], 4, True),
    ],
)
def test_contains_at_most(value, max_length, expected):
    validator = ValueValidator(value)
    assert validator._contains_at_most(max_length) is expected


@pytest.mark.parametrize(
    "value,length,expected",
    [
        ([1, 2, 3], 3, True),
        ([1, 2, 3], 2, False),
        ([1, 2, 3], 4, False),
    ],
)
def test_contains_exactly(value, length, expected):
    validator = ValueValidator(value)
    assert validator._contains_exactly(length) is expected


@pytest.mark.parametrize(
    "value,expected",
    [
        (True, False),
        (None, True),
        (1, False),
        ("", False),
    ],
)
def test_is_none(value, expected):
    validator = ValueValidator(value)
    assert validator._is_none() is expected


@pytest.mark.parametrize(
    "value,expected",
    [
        ((1, 2), True),
        ({1, 2}, True),
        ([4, 5, 6], True),
        ([1, 1, 1], False),
        ("abc", True),
        ("AA", False),
    ],
)
def test_has_unique_values(value, expected):
    validator = ValueValidator(value)
    assert validator._has_unique_values() is expected
