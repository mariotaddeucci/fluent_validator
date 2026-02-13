from dataclasses import dataclass

from fluent_validator import ValidatorBuilder as vb


@dataclass
class D:
    x: int


class C:
    def __init__(self, x):
        self.x = x


def test_is_dataclass():
    validator_positive = vb.is_dataclass()
    validator_negative = vb.is_not_dataclass()

    assert validator_positive.validate(D(1), strategy="return_result") is True
    assert validator_negative.validate(D(1), strategy="return_result") is False

    assert validator_positive.validate(C(1), strategy="return_result") is False
    assert validator_negative.validate(C(1), strategy="return_result") is True
