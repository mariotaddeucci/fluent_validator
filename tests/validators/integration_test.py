"""
Tests for semantic negative methods integration with Validator class
Testing both old style (not_is_X) and new semantic style (is_not_X)
"""
import pytest

from fluent_validator import validate, validate_all


# Test semantic negative methods (is_not_X)
def test_is_not_none_semantic():
    validate(10).is_not_none()
    validate("hello").is_not_none()
    
    with pytest.raises(ValueError):
        validate(None).is_not_none()


def test_is_empty_semantic():
    validate([]).is_empty()
    validate("").is_empty()
    validate({}).is_empty()
    validate(None).is_empty()
    
    with pytest.raises(ValueError):
        validate([1, 2, 3]).is_empty()
    
    with pytest.raises(ValueError):
        validate("hello").is_empty()


def test_is_not_empty_semantic():
    validate([1, 2, 3]).is_not_empty()
    validate("hello").is_not_empty()
    validate({"a": 1}).is_not_empty()
    
    with pytest.raises(ValueError):
        validate([]).is_not_empty()
    
    with pytest.raises(ValueError):
        validate("").is_not_empty()
    
    with pytest.raises(ValueError):
        validate(None).is_not_empty()


def test_is_not_equal_semantic():
    validate(10).is_not_equal(5)
    validate("hello").is_not_equal("world")
    
    with pytest.raises(ValueError):
        validate(10).is_not_equal(10)


def test_is_not_in_semantic():
    validate(4).is_not_in(1, 2, 3)
    validate("d").is_not_in("a", "b", "c")
    
    with pytest.raises(ValueError):
        validate(2).is_not_in(1, 2, 3)


def test_is_not_true_semantic():
    validate(False).is_not_true()
    validate(0).is_not_true()
    validate(None).is_not_true()
    
    with pytest.raises(ValueError):
        validate(True).is_not_true()


def test_is_not_false_semantic():
    validate(True).is_not_false()
    validate(1).is_not_false()
    validate(None).is_not_false()
    
    with pytest.raises(ValueError):
        validate(False).is_not_false()


def test_is_not_instance_semantic():
    validate(10).is_not_instance(str)
    validate("hello").is_not_instance(int)
    
    with pytest.raises(ValueError):
        validate(10).is_not_instance(int)


def test_is_not_callable_semantic():
    validate(10).is_not_callable()
    validate("hello").is_not_callable()
    
    with pytest.raises(ValueError):
        validate(lambda x: x).is_not_callable()


def test_is_not_iterable_semantic():
    validate(10).is_not_iterable()
    validate(5.5).is_not_iterable()
    
    with pytest.raises(ValueError):
        validate([1, 2, 3]).is_not_iterable()
    
    with pytest.raises(ValueError):
        validate("hello").is_not_iterable()


def test_is_not_string_semantic():
    validate(10).is_not_string()
    validate(True).is_not_string()
    
    with pytest.raises(ValueError):
        validate("hello").is_not_string()


def test_is_not_number_semantic():
    validate("hello").is_not_number()
    # Note: bool is a subclass of int in Python, so True/False are considered numbers
    
    with pytest.raises(ValueError):
        validate(10).is_not_number()
    
    with pytest.raises(ValueError):
        validate(5.5).is_not_number()


def test_is_not_bool_semantic():
    validate(10).is_not_bool()
    validate("hello").is_not_bool()
    
    with pytest.raises(ValueError):
        validate(True).is_not_bool()
    
    with pytest.raises(ValueError):
        validate(False).is_not_bool()


# Test backward compatibility with old style (not_is_X)
def test_old_style_not_is_none():
    validate(10).not_is_none()
    
    with pytest.raises(ValueError):
        validate(None).not_is_none()


def test_old_style_not_is_true():
    validate(False).not_is_true()
    
    with pytest.raises(ValueError):
        validate(True).not_is_true()


def test_old_style_not_equal():
    validate(10).not_equal(5)
    
    with pytest.raises(ValueError):
        validate(10).not_equal(10)


# Test chaining with semantic negative methods
def test_chained_validation_semantic():
    validate(10).is_not_none().is_not_equal(5).greater_than(5)
    validate([1, 2, 3]).is_not_empty().contains_at_least(2)
    validate("hello").is_string().is_not_empty()


# Test multi-validation with semantic methods
def test_multi_validation_semantic():
    validate_all(10, 20, 30).is_not_none()
    validate_all(10, 20, 30).is_not_equal(5)
    validate_all([1], [2], [3]).is_not_empty()
    
    with pytest.raises(ValueError):
        validate_all(10, None, 30).is_not_none()
    
    with pytest.raises(ValueError):
        validate_all([1], [], [3]).is_not_empty()


# Test mixing old and new styles
def test_mixed_styles():
    validate(10).not_is_none().is_not_equal(5).greater_than(5)
    validate("hello").is_not_empty().not_equal("world")


# Test generic type support
def test_generic_type_inference():
    """Test that generic types work correctly"""
    # These should work without type errors
    v1 = validate(10)
    v2 = validate("hello")
    v3 = validate([1, 2, 3])
    
    # Validate correct types
    v1.is_number()
    v2.is_string()
    v3.is_iterable()
