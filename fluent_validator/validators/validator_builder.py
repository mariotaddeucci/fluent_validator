from typing import Type, Any, Callable
from functools import wraps
from .validator_spec import ValidatorSpec


class ValidatorBuilder:
    @classmethod
    def prepare(cls) -> ValidatorSpec:
        return ValidatorSpec()

    @classmethod
    def is_instance_of(cls, types: Type | tuple[Type, ...], *, msg: str | None = None) -> ValidatorSpec:
        return cls.prepare().is_instance_of(types, msg=msg)

    @wraps(ValidatorSpec.is_callable)
    @classmethod
    def is_callable(cls, *, msg: str | None = None) -> ValidatorSpec:
        return cls.prepare().is_callable(msg=msg)

    @classmethod
    def is_iterable(cls, *, msg: str | None = None) -> ValidatorSpec:
        return cls.prepare().is_iterable(msg=msg)

    @classmethod
    def is_dataclass(cls, *, msg: str | None = None) -> ValidatorSpec:
        return cls.prepare().is_dataclass(msg=msg)

    @classmethod
    def is_string(cls, *, msg: str | None = None) -> ValidatorSpec:
        return cls.prepare().is_string(msg=msg)

    @classmethod
    def is_number(cls, *, msg: str | None = None) -> ValidatorSpec:
        return cls.prepare().is_number(msg=msg)

    @classmethod
    def is_bool(cls, *, msg: str | None = None) -> ValidatorSpec:
        return cls.prepare().is_bool(msg=msg)

    @classmethod
    def is_none(cls, *, msg: str | None = None) -> ValidatorSpec:
        return cls.prepare().is_none(msg=msg)

    @classmethod
    def is_greater_than(cls, value: Any, *, msg: str | None = None) -> ValidatorSpec:
        return cls.prepare().is_greater_than(value, msg=msg)

    @classmethod
    def is_gt(cls, value: Any, *, msg: str | None = None) -> ValidatorSpec:
        return cls.prepare().is_gt(value, msg=msg)

    @classmethod
    def is_greater_than_or_equal(cls, value: Any, *, msg: str | None = None) -> ValidatorSpec:
        return cls.prepare().is_greater_than_or_equal(value, msg=msg)

    @classmethod
    def is_gte(cls, value: Any, *, msg: str | None = None) -> ValidatorSpec:
        return cls.prepare().is_gte(value, msg=msg)

    @classmethod
    def is_equal(cls, value: Any, *, msg: str | None = None) -> ValidatorSpec:
        return cls.prepare().is_equal(value, msg=msg)

    @classmethod
    def is_eq(cls, value: Any, *, msg: str | None = None) -> ValidatorSpec:
        return cls.prepare().is_eq(value, msg=msg)

    @classmethod
    def is_less_than(cls, value: Any, *, msg: str | None = None) -> ValidatorSpec:
        return cls.prepare().is_less_than(value, msg=msg)

    @classmethod
    def is_lt(cls, value: Any, *, msg: str | None = None) -> ValidatorSpec:
        return cls.prepare().is_lt(value, msg=msg)

    @classmethod
    def is_less_than_or_equal(cls, value: Any, *, msg: str | None = None) -> ValidatorSpec:
        return cls.prepare().is_less_than_or_equal(value, msg=msg)

    @classmethod
    def is_lte(cls, value: Any, *, msg: str | None = None) -> ValidatorSpec:
        return cls.prepare().is_lte(value, msg=msg)

    @classmethod
    def add_validation(cls, validation_fn: Callable[[Any], bool], *, msg: str) -> ValidatorSpec:
        return cls.prepare().add_validation(validation_fn, msg=msg)

    @classmethod
    def add_validations(cls, validations: list[tuple[Callable[[Any], bool], str]]) -> ValidatorSpec:
        return cls.prepare().add_validations(validations)
