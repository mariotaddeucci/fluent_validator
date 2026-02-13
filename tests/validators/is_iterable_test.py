from fluent_validator import ValidatorBuilder as vb


def test_is_iterable():
    validator_positive = vb.is_iterable()
    validator_negative = vb.is_not_iterable()

    assert validator_positive.validate([1, 2, 3], strategy="return_result") is True
    assert validator_positive.validate("abc", strategy="return_result") is True
    assert validator_negative.validate(123, strategy="return_result") is True
