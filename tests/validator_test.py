import pytest

from fluent_validator import validate, validate_all


def test_chained_validation():
    validate(10).not_is_none().greater_than(5).not_equal(40)

    with pytest.raises(ValueError):
        validate(True).is_false()

    with pytest.raises(ValueError):
        validate(True).is_string()


def test_unimplemented_validation():
    with pytest.raises(NotImplementedError):
        validate(True).validation_not_implemented()


def test_multi_validation():
    validate_all(True, True).is_true()
    validate_all(True, True).not_is_false()
    validate_all(10, 100).greater_than(5).not_equal(40)

    with pytest.raises(ValueError):
        validate_all(True, False).is_true()

    with pytest.raises(ValueError):
        validate_all(True, False).is_false()
