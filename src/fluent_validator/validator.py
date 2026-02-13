import typing
from functools import wraps

from fluent_validator.validators.value_validator import ValueValidator


class Validator(ValueValidator):
    def __getattr__(self, fn_name):
        # Check for old style negation: not_is_X -> negate _is_X
        is_old_style_negative = fn_name.startswith("not_")

        # Check for new semantic style: is_not_X -> use _is_not_X directly
        is_semantic_negative = fn_name.startswith("is_not_")

        if is_semantic_negative:
            # For semantic style (is_not_X), map directly to _is_not_X
            validation_name = f"_{fn_name}"
        elif is_old_style_negative:
            # For old style (not_is_X), map to the base method and negate
            validation_name = fn_name[3:]  # Remove "not_"
        else:
            # For positive methods, map to _method_name
            validation_name = f"_{fn_name}"

        if validation_name not in dir(self):
            raise NotImplementedError(f"{validation_name} is not implemented")

        def wrapper(*args, **kwargs):
            result = getattr(self, validation_name)(*args, **kwargs)
            # Only negate for old style (not_is_X), semantic methods already handle negation
            result = not result if is_old_style_negative else result
            if result:
                return self

            raise ValueError(f"{self.identifier} does not match criteria for {fn_name}")

        return wrapper


class MultiValidator:
    def __init__(self, validators: typing.List[Validator]):
        self._validators = validators

    def __getattr__(self, fn_name):
        def wrapper(*args, **kwargs):
            result = all(
                getattr(validator, fn_name)(*args, **kwargs)
                for validator in self._validators
            )

            if result:
                return self

            raise ValueError(
                f"{self._validators} does not match criteria for {fn_name}"
            )

        return wrapper


@wraps(Validator.__init__)
def validate(*args, **kwargs):
    return Validator(*args, **kwargs)


def validate_all(*args):
    return MultiValidator([validate(arg) for arg in args])
