from fluent_validator.validators import ValidatorBuilder as vb


def test_is_between_inclusive_and_exclusive():
    validator_both = vb.is_between(1, 3)  # default closed='both'
    validator_none = vb.is_between(1, 3, closed="none")

    assert validator_both.validate(1, strategy="return_result") is True
    assert validator_both.validate(3, strategy="return_result") is True
    assert validator_both.validate(2, strategy="return_result") is True
    assert validator_both.validate(0, strategy="return_result") is False
    assert validator_both.validate(4, strategy="return_result") is False

    assert validator_none.validate(1, strategy="return_result") is False
    assert validator_none.validate(3, strategy="return_result") is False
    assert validator_none.validate(2, strategy="return_result") is True
