from fluent_validator.validators import ValidatorBuilder as vb


def test_is_callable():
    def func():
        pass

    validator_positive = vb.is_callable()
    validator_negative = vb.is_not_callable()

    assert validator_positive.validate(func, strategy="return_result") is True
    assert validator_negative.validate(func, strategy="return_result") is False
