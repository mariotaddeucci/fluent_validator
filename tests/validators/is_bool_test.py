from fluent_validator import Validator as vb


def test_is_bool():
    validator_positive = vb.is_bool()
    validator_negative = vb.is_not_bool()

    assert validator_positive.validate(True, strategy="return_result") is True
    assert validator_positive.validate(False, strategy="return_result") is True
    assert validator_negative.validate(1, strategy="return_result") is True
