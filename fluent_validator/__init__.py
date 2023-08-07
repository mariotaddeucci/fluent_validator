from functools import wraps
from fluent_validator.validator import Validator

@wraps(Validator.__init__)
def validate(*args, **kwargs):
    return Validator(*args, **kwargs)
