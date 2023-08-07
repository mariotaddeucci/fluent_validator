from fluent_validator import validate

import pytest


def test_chained_validation():
    validate(True).is_true().not_is_false().not_is_none()

    with pytest.raises(ValueError):
        validate(True).is_false()

    with pytest.raises(ValueError):
        validate(True).is_string()
    

def test_unimplemented_validation():
    with pytest.raises(NotImplementedError):
        validate(True).validation_not_implemented()