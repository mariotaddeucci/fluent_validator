from fluent_validator.validators import ValidatorBuilder as VB


def test_is_instance_of():
    value = "hello"

    validator_positive = VB.is_instance_of(str)
    validator_negative = VB.is_not_instance_of(str)

    assert validator_positive.validate(value, strategy="return_result") is True
    assert validator_negative.validate(value, strategy="return_result") is False


def test_is_instance_of_with_tuple():
    value = 42

    validator_positive = VB.is_instance_of((str, int))
    validator_negative = VB.is_not_instance_of((str, int))

    assert validator_positive.validate(value, strategy="return_result") is True
    assert validator_negative.validate(value, strategy="return_result") is False
