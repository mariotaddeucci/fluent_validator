from typing import Callable, Any, Self, Iterable, Literal, Type
from .validator_fns import ValidatorFns
from .exceptions import ValidationError


class ValidatorSpec:
    def __init__(self, validations: list[tuple[Callable[[Any], bool], str]] | None = None):
        self._validations = validations or []

    @classmethod
    def from_validations(cls, validations: list[tuple[Callable[[Any], bool], str]])  -> Self:
        return cls(validations=validations)

    @property
    def validations(self) -> list[tuple[Callable[[Any], bool], str]]:
        return self._validations.copy()

    def add_validation(self, validation_fn: Callable[[Any], bool], *, msg: str)  -> Self:
        return self.add_validations([(validation_fn, msg)])

    def add_validations(self, validations: list[tuple[Callable[[Any], bool], str]])  -> Self:
        return self.from_validations(self.validations + validations)

    def is_instance_of(self, types: Type | tuple[Type, ...], *, msg: str | None = None)  -> Self:
        msg = msg or f"object is not an instance of {types}"
        return self.add_validation(lambda obj: ValidatorFns.is_instance_of(obj, types), msg=msg)

    def is_callable(self, *, msg: str | None = None)  -> Self:
        msg = msg or "object is not callable"
        return self.add_validation(lambda obj: ValidatorFns.is_callable(obj), msg=msg)

    def is_iterable(self, *, msg: str | None = None)  -> Self:
        msg = msg or "object is not iterable"
        return self.add_validation(lambda obj: ValidatorFns.is_iterable(obj), msg=msg)

    def is_dataclass(self, *, msg: str | None = None)  -> Self:
        msg = msg or "object is not a dataclass"
        return self.add_validation(lambda obj: ValidatorFns.is_dataclass(obj), msg=msg)

    def is_string(self, *, msg: str | None = None)  -> Self:
        msg = msg or "object is not a string"
        return self.add_validation(lambda obj: ValidatorFns.is_string(obj), msg=msg)

    def is_number(self, *, msg: str | None = None)  -> Self:
        msg = msg or "object is not a number"
        return self.add_validation(lambda obj: ValidatorFns.is_number(obj), msg=msg)

    def is_bool(self, *, msg: str | None = None)  -> Self:
        msg = msg or "object is not a boolean"
        return self.add_validation(lambda obj: ValidatorFns.is_bool(obj), msg=msg)

    def is_none(self, *, msg: str | None = None)  -> Self:
        msg = msg or "object is not None"
        return self.add_validation(lambda obj: ValidatorFns.is_none(obj), msg=msg)

    def is_greater_than(self, value: Any, *, msg: str | None = None)  -> Self:
        msg = msg or f"object is not greater than {value}"
        return self.add_validation(lambda obj: ValidatorFns.is_greater_than(obj, value), msg=msg)

    def is_gt(self, value: Any, *, msg: str | None = None)  -> Self:
        return self.is_greater_than(value, msg=msg)

    def is_greater_than_or_equal(self, value: Any, *, msg: str | None = None)  -> Self:
        msg = msg or f"object is not greater than or equal to {value}"
        return self.add_validation(lambda obj: ValidatorFns.is_greater_than_or_equal(obj, value), msg=msg)

    def is_gte(self, value: Any, *, msg: str | None = None)  -> Self:
        return self.is_greater_than_or_equal(value, msg=msg)

    def is_equal(self, value: Any, *, msg: str | None = None)  -> Self:
        msg = msg or f"object is not equal to {value}"
        return self.add_validation(lambda obj: ValidatorFns.is_equal(obj, value), msg=msg)

    def is_eq(self, value: Any, *, msg: str | None = None)  -> Self:
        return self.is_equal(value, msg=msg)

    def is_less_than(self, value: Any, *, msg: str | None = None)  -> Self:
        msg = msg or f"object is not less than {value}"
        return self.add_validation(lambda obj: ValidatorFns.is_less_than(obj, value), msg=msg)

    def is_lt(self, value: Any, *, msg: str | None = None)  -> Self:
        return self.is_less_than(value, msg=msg)

    def is_less_than_or_equal(self, value: Any, *, msg: str | None = None)  -> Self:
        msg = msg or f"object is not less than or equal to {value}"
        return self.add_validation(lambda obj: ValidatorFns.is_less_than_or_equal(obj, value), msg=msg)

    def is_lte(self, value: Any, *, msg: str | None = None)  -> Self:
        return self.is_less_than_or_equal(value, msg=msg)

    def is_between(self, lower_bound: Any, upper_bound: Any, *, closed: Literal["both", "left", "right", "none"] = "both", msg: str | None = None)  -> Self:
        msg = msg or f"object is not between {lower_bound} and {upper_bound} (closed='{closed}')"
        return self.add_validation(lambda obj: ValidatorFns.is_between(obj, lower_bound, upper_bound, closed), msg=msg)


    def __and__(self, other: "ValidatorSpec")  -> Self:
        if not isinstance(other, ValidatorSpec):
            return NotImplemented

        return self.add_validations(other.validations)

    def __or__(self, other: "ValidatorSpec")  -> Self:
        if not isinstance(other, ValidatorSpec):
            return NotImplemented
        def combined_validation_factory(validations1: list[tuple[Callable[[Any], bool], str]], validations2: list[tuple[Callable[[Any], bool], str]]) -> Callable[[Any], bool]:
            def combined_validation(obj: Any) -> bool:
                return all(validation_fn(obj) for validation_fn, _ in validations1) or all(validation_fn(obj) for validation_fn, _ in validations2)
            return combined_validation

        combined_validation_fn = combined_validation_factory(self.validations, other.validations)
        combined_msg = f"object does not satisfy either: ({' and '.join(msg for _, msg in self.validations)}) or ({' and '.join(msg for _, msg in other.validations)})"
        return self.from_validations([(combined_validation_fn, combined_msg)])


    def __neg__(self)  -> Self:
        def negate(validation_fn: Callable[[Any], bool]) -> Callable[[Any], bool]:
            return lambda obj: not validation_fn(obj)

        validations= [
            (negate(validation_fn), f"object does not satisfy: {msg}")
            for validation_fn, msg in self._validations
        ]
        return self.from_validations(validations)

    def validate(self, obj: Any, *, strategy: Literal["raise_after_first_error", "raise_after_all_errors", "return_result"] = "raise_after_first_error") -> bool:
        errors = []
        for validation_fn, msg in self._validations:
            if not validation_fn(obj):
                if strategy == "raise_after_first_error":
                    raise ValidationError(msg)
                errors.append(msg)

            if strategy == "return_result" and errors:
                return False

        if strategy == "raise_after_all_errors" and errors:
            raise ValidationError("; ".join(errors))

        return not errors

    def validate_each(self, iterable: Iterable[Any], *, strategy: Literal["raise_after_first_error", "raise_after_all_errors", "return_result"] = "raise_after_first_error") -> bool:
        errors = []
        for index, item in enumerate(iterable):
            try:
                self.validate(item, strategy=strategy)
            except ValidationError as e:
                error_msg = f"Item at index {index} failed validation: {str(e)}"
                if strategy == "raise_after_first_error":
                    raise ValidationError(error_msg)
                errors.append(error_msg)

        if strategy == "raise_after_all_errors" and errors:
            raise ValidationError("; ".join(errors))

        return not errors
