from fluent_validator.validators import ValidatorBuilder as vb


def test_is_less_than():
    validator_positive = vb.is_less_than(5)
    validator_negative = vb.is_not_less_than(5)

    assert validator_positive.validate(3, strategy="return_result") is True
    assert validator_positive.validate(5, strategy="return_result") is False
    assert validator_negative.validate(3, strategy="return_result") is False
    assert validator_negative.validate(5, strategy="return_result") is True
