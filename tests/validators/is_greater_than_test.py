from fluent_validator.validators import ValidatorBuilder as vb


def test_is_greater_than():
    validator_positive = vb.is_greater_than(5)
    validator_negative = vb.is_not_greater_than(5)

    assert validator_positive.validate(10, strategy="return_result") is True
    assert validator_positive.validate(5, strategy="return_result") is False
    assert validator_negative.validate(10, strategy="return_result") is False
    assert validator_negative.validate(5, strategy="return_result") is True
