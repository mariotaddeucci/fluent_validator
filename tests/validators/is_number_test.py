from decimal import Decimal

from fluent_validator import Validator as vb


def test_is_number():
    validator_positive = vb.is_number()
    validator_negative = vb.is_not_number()

    assert validator_positive.validate(42, strategy="return_result") is True
    assert validator_positive.validate(3.14, strategy="return_result") is True
    assert validator_positive.validate(Decimal("1.2"), strategy="return_result") is True
    # note: bool is a subclass of int in Python
    assert validator_positive.validate(True, strategy="return_result") is True

    assert validator_negative.validate("not a number", strategy="return_result") is True
