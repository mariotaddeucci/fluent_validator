from fluent_validator import ValidatorBuilder as vb


def test_is_none():
    validator_positive = vb.is_none()
    validator_negative = vb.is_not_none()

    assert validator_positive.validate(None, strategy="return_result") is True
    assert validator_negative.validate(None, strategy="return_result") is False

    assert validator_positive.validate(0, strategy="return_result") is False
    assert validator_negative.validate(0, strategy="return_result") is True
