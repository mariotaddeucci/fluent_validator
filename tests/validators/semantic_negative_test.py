"""
Tests for semantic negative methods (is_not_X instead of not_is_X)
"""
import pytest

from fluent_validator.validators.value_validator import ValueValidator
from fluent_validator.validators.type_validator import TypeValidator


# Value Validator Semantic Negative Tests

@pytest.mark.parametrize(
    "value,expected",
    [
        (None, False),
        (1, True),
        ("", True),
        (False, True),
        (0, True),
    ],
)
def test_is_not_none(value, expected):
    validator = ValueValidator(value)
    assert validator._is_not_none() is expected


@pytest.mark.parametrize(
    "value,expected",
    [
        (None, False),
        ("", False),
        ([], False),
        ({}, False),
        ([1], True),
        ("hello", True),
        ({"a": 1}, True),
    ],
)
def test_is_not_empty(value, expected):
    validator = ValueValidator(value)
    assert validator._is_not_empty() is expected


@pytest.mark.parametrize(
    "value,compare_value,expected",
    [
        (1, 1, False),
        (1, 2, True),
        ("hello", "hello", False),
        ("hello", "world", True),
    ],
)
def test_is_not_equal(value, compare_value, expected):
    validator = ValueValidator(value)
    assert validator._is_not_equal(compare_value) is expected


@pytest.mark.parametrize(
    "value,args,expected",
    [
        (1, [1, 2, 3], False),
        (4, [1, 2, 3], True),
        ("a", ["a", "b", "c"], False),
        ("d", ["a", "b", "c"], True),
    ],
)
def test_is_not_in(value, args, expected):
    validator = ValueValidator(value)
    assert validator._is_not_in(*args) is expected


@pytest.mark.parametrize(
    "value,expected",
    [
        (True, False),
        (False, True),
        (1, True),
        ("True", True),
    ],
)
def test_is_not_true(value, expected):
    validator = ValueValidator(value)
    assert validator._is_not_true() is expected


@pytest.mark.parametrize(
    "value,expected",
    [
        (False, False),
        (True, True),
        (0, True),
        (None, True),
    ],
)
def test_is_not_false(value, expected):
    validator = ValueValidator(value)
    assert validator._is_not_false() is expected


@pytest.mark.parametrize(
    "value,expected",
    [
        (None, True),
        ("", True),
        ([], True),
        ({}, True),
        ([1], False),
        ("hello", False),
        ({"a": 1}, False),
    ],
)
def test_is_empty(value, expected):
    validator = ValueValidator(value)
    assert validator._is_empty() is expected


# Type Validator Semantic Negative Tests

@pytest.mark.parametrize(
    "value,dtype,expected",
    [
        (1, int, False),
        ("hello", str, False),
        (2.0, float, False),
        (1, str, True),
        ("hello", int, True),
    ],
)
def test_is_not_instance(value, dtype, expected):
    validator = TypeValidator(value)
    assert validator._is_not_instance(dtype) is expected


@pytest.mark.parametrize(
    "value,expected",
    [
        (1, True),
        ("hello", True),
        (2.0, True),
        (lambda x: x, False),
    ],
)
def test_is_not_callable(value, expected):
    validator = TypeValidator(value)
    assert validator._is_not_callable() is expected


@pytest.mark.parametrize(
    "value,expected",
    [
        (1, True),
        ("hello", False),
        (2.0, True),
        (lambda x: x, True),
        ([1, 2, 3], False),
        ((1, 2, 3), False),
    ],
)
def test_is_not_iterable(value, expected):
    validator = TypeValidator(value)
    assert validator._is_not_iterable() is expected


@pytest.mark.parametrize(
    "value,expected",
    [
        (1, True),
        ("hello", False),
        (2.0, True),
    ],
)
def test_is_not_string(value, expected):
    validator = TypeValidator(value)
    assert validator._is_not_string() is expected


@pytest.mark.parametrize(
    "value,expected",
    [
        (1, False),
        (2.0, False),
        ("hello", True),
        # Note: bool is a subclass of int in Python, so True/False are considered numbers
    ],
)
def test_is_not_number(value, expected):
    validator = TypeValidator(value)
    assert validator._is_not_number() is expected


@pytest.mark.parametrize(
    "value,expected",
    [
        (True, False),
        (False, False),
        (1, True),
        (0, True),
        (None, True),
    ],
)
def test_is_not_bool(value, expected):
    validator = TypeValidator(value)
    assert validator._is_not_bool() is expected
