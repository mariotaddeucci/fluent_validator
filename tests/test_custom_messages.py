import pytest

from fluent_validator import validate, validate_all


def test_custom_message_with_single_validation():
    """Test that custom messages work with single validator"""
    custom_msg = "Age must be greater than 18"
    with pytest.raises(ValueError, match=custom_msg):
        validate(15).greater_than(18, message=custom_msg)


def test_custom_message_with_is_none():
    """Test custom message with is_none validation"""
    custom_msg = "Value cannot be None"
    with pytest.raises(ValueError, match=custom_msg):
        validate(None).is_not_none(message=custom_msg)


def test_custom_message_with_equal():
    """Test custom message with equal validation"""
    custom_msg = "Expected value to be 10"
    with pytest.raises(ValueError, match=custom_msg):
        validate(5).equal(10, message=custom_msg)


def test_custom_message_with_is_string():
    """Test custom message with type validation"""
    custom_msg = "Value must be a string"
    with pytest.raises(ValueError, match=custom_msg):
        validate(123).is_string(message=custom_msg)


def test_custom_message_with_chained_validation():
    """Test that custom message only applies to the specific validation in chain"""
    custom_msg = "Value must be greater than 5"
    # This should pass the first two validations
    validate(10).is_not_none().is_number()
    
    # This should fail on greater_than with custom message
    with pytest.raises(ValueError, match=custom_msg):
        validate(3).is_not_none().is_number().greater_than(5, message=custom_msg)


def test_no_custom_message_uses_default():
    """Test that without custom message, default message is used"""
    with pytest.raises(ValueError, match="does not match criteria"):
        validate(5).greater_than(10)


def test_custom_message_with_old_style_negation():
    """Test custom message with old style negation (not_)"""
    custom_msg = "Value should not be None"
    with pytest.raises(ValueError, match=custom_msg):
        validate(None).not_is_none(message=custom_msg)


def test_custom_message_with_multi_validator():
    """Test custom message with validate_all"""
    custom_msg = "All values must be greater than 10"
    with pytest.raises(ValueError, match=custom_msg):
        validate_all(5, 15, 20).greater_than(10, message=custom_msg)


def test_custom_message_with_is_empty():
    """Test custom message with is_empty validation"""
    custom_msg = "List must not be empty"
    with pytest.raises(ValueError, match=custom_msg):
        validate([]).is_not_empty(message=custom_msg)


def test_custom_message_with_between():
    """Test custom message with between validation"""
    custom_msg = "Value must be between 10 and 20"
    with pytest.raises(ValueError, match=custom_msg):
        validate(25).between(10, 20, message=custom_msg)


def test_success_validation_with_message_param():
    """Test that successful validation returns validator even when message is provided"""
    # Should not raise any exception and return the validator
    result = validate(15).greater_than(10, message="Should not see this")
    assert result is not None
