from fluent_validator import ValidatorBuilder as vb


def test_is_equal():
    validator_positive = vb.is_equal(3)
    validator_negative = vb.is_not_equal(3)

    assert validator_positive.validate(3, strategy="return_result") is True
    assert validator_positive.validate(4, strategy="return_result") is False
    assert validator_negative.validate(3, strategy="return_result") is False
    assert validator_negative.validate(4, strategy="return_result") is True
