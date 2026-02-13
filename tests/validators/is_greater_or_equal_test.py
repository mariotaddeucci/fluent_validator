from fluent_validator.validators import ValidatorBuilder as vb


def test_is_greater_or_equal():
    validator_positive = vb.is_greater_or_equal(5)
    validator_negative = vb.is_not_greater_or_equal(5)

    assert validator_positive.validate(5, strategy="return_result") is True
    assert validator_positive.validate(6, strategy="return_result") is True
    assert validator_positive.validate(4, strategy="return_result") is False
    assert validator_negative.validate(5, strategy="return_result") is False
    assert validator_negative.validate(4, strategy="return_result") is True
