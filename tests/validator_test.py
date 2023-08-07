from fluent_validator import Validator

import pytest


def test_chained_validation():
    validator = Validator(True)
    validator.is_true().not_is_false().not_is_none()

    with pytest.raises(ValueError):
        validator.is_false()

    with pytest.raises(ValueError):
        validator.is_string()
    

def test_unimplemented_validation():
    validator = Validator(True)

    with pytest.raises(NotImplementedError):
        validator.validation_not_implemented()