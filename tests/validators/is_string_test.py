from fluent_validator import Validator as vb


def test_is_string():
    validator_positive = vb.is_string()
    validator_negative = vb.is_not_string()

    assert validator_positive.validate("hello", strategy="return_result") is True
    assert validator_positive.validate("", strategy="return_result") is True
    assert validator_negative.validate(123, strategy="return_result") is True
