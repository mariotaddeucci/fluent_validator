from typing import Any, Iterable, Type, Literal
from dataclasses import is_dataclass
from decimal import Decimal


class ValidatorFns:
    @classmethod
    def is_instance_of(cls, obj: Any, types: Type | tuple[Type, ...]) -> bool:
        return isinstance(obj, types)

    @classmethod
    def is_callable(cls, obj: Any) -> bool:
        return callable(obj)

    @classmethod
    def is_iterable(cls, obj: Any) -> bool:
        return cls.is_instance_of(obj, Iterable)

    @classmethod
    def is_dataclass(cls, obj: Any) -> bool:
        return is_dataclass(obj)

    @classmethod
    def is_string(cls, obj: Any) -> bool:
        return cls.is_instance_of(obj, str)

    @classmethod
    def is_number(cls, obj: Any) -> bool:
        return cls.is_instance_of(obj, (int, float, Decimal))

    @classmethod
    def is_bool(cls, obj: Any) -> bool:
        return cls.is_instance_of(obj, bool)

    @classmethod
    def is_none(cls, obj: Any) -> bool:
        return obj is None

    @classmethod
    def is_greater_than(cls, obj: Any, value: Any) -> bool:
        return obj > value

    @classmethod
    def is_greater_or_equal(cls, obj: Any, value: Any) -> bool:
        return obj >= value

    @classmethod
    def is_equal(cls, obj: Any, value: Any) -> bool:
        return obj == value

    @classmethod
    def is_less_than(cls, obj: Any, value: Any) -> bool:
        return obj < value

    @classmethod
    def is_less_or_equal(cls, obj: Any, value: Any) -> bool:
        return obj <= value

    @classmethod
    def is_greater_than_or_equal(cls, obj: Any, value: Any) -> bool:
        return obj >= value

    @classmethod
    def is_less_than_or_equal(cls, obj: Any, value: Any) -> bool:
        return obj <= value

    @classmethod
    def is_between(
        cls,
        obj: Any,
        lower_bound: Any,
        upper_bound: Any,
        closed: Literal["both", "left", "right", "none"] = "both",
    ) -> bool:
        if closed == "both":
            return cls.is_greater_or_equal(obj, lower_bound) and cls.is_less_or_equal(
                obj, upper_bound
            )

        if closed == "left":
            return cls.is_greater_or_equal(obj, lower_bound) and cls.is_less_than(
                obj, upper_bound
            )

        if closed == "right":
            return cls.is_greater_than(obj, lower_bound) and cls.is_less_or_equal(
                obj, upper_bound
            )

        if closed == "none":
            return cls.is_greater_than(obj, lower_bound) and cls.is_less_than(
                obj, upper_bound
            )

        raise ValueError(
            f"Invalid value for 'closed': {closed}. Expected one of 'both', 'left', 'right', 'none'."
        )
