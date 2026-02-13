from fluent_validator import ValidatorBuilder as vb


def test_is_less_or_equal():
    validator_positive = vb.is_less_or_equal(5)
    validator_negative = vb.is_not_less_or_equal(5)

    assert validator_positive.validate(5, strategy="return_result") is True
    assert validator_positive.validate(4, strategy="return_result") is True
    assert validator_positive.validate(6, strategy="return_result") is False
    assert validator_negative.validate(5, strategy="return_result") is False
    assert validator_negative.validate(6, strategy="return_result") is True
