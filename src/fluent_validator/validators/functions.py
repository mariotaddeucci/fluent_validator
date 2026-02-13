import dataclasses
from collections.abc import Iterable
from decimal import Decimal
from typing import Any, Literal


def is_instance_of(obj: Any, types: type | tuple[type, ...]) -> bool:
    return isinstance(obj, types)


def is_not_instance_of(obj: Any, types: type | tuple[type, ...]) -> bool:
    return not is_instance_of(obj, types)


def is_callable(obj: Any) -> bool:
    return callable(obj)


def is_not_callable(obj: Any) -> bool:
    return not is_callable(obj)


def is_iterable(obj: Any) -> bool:
    return is_instance_of(obj, Iterable)


def is_not_iterable(obj: Any) -> bool:
    return not is_iterable(obj)


def is_dataclass(obj: Any) -> bool:
    return dataclasses.is_dataclass(obj)


def is_not_dataclass(obj: Any) -> bool:
    return not is_dataclass(obj)


def is_string(obj: Any) -> bool:
    return is_instance_of(obj, str)


def is_not_string(obj: Any) -> bool:
    return not is_string(obj)


def is_number(obj: Any) -> bool:
    return is_instance_of(obj, (int, float, Decimal))


def is_not_number(obj: Any) -> bool:
    return not is_number(obj)


def is_bool(obj: Any) -> bool:
    return is_instance_of(obj, bool)


def is_not_bool(obj: Any) -> bool:
    return not is_bool(obj)


def is_none(obj: Any) -> bool:
    return obj is None


def is_not_none(obj: Any) -> bool:
    return not is_none(obj)


def is_greater_than(obj: Any, value: Any) -> bool:
    return obj > value


def is_not_greater_than(obj: Any, value: Any) -> bool:
    return not is_greater_than(obj, value)


def is_equal(obj: Any, value: Any) -> bool:
    return obj == value


def is_not_equal(obj: Any, value: Any) -> bool:
    return not is_equal(obj, value)


def is_less_than(obj: Any, value: Any) -> bool:
    return obj < value


def is_not_less_than(obj: Any, value: Any) -> bool:
    return not is_less_than(obj, value)


def is_greater_or_equal(obj: Any, value: Any) -> bool:
    return obj >= value


def is_not_greater_or_equal(obj: Any, value: Any) -> bool:
    return not is_greater_or_equal(obj, value)


def is_less_or_equal(obj: Any, value: Any) -> bool:
    return obj <= value


def is_not_less_or_equal(obj: Any, value: Any) -> bool:
    return not is_less_or_equal(obj, value)


def is_between(
    obj: Any,
    lower_bound: Any,
    upper_bound: Any,
    closed: Literal["both", "left", "right", "none"] = "both",
) -> bool:
    if closed == "both":
        return is_greater_or_equal(obj, lower_bound) and is_less_or_equal(
            obj,
            upper_bound,
        )

    if closed == "left":
        return is_greater_or_equal(obj, lower_bound) and is_less_than(
            obj,
            upper_bound,
        )

    if closed == "right":
        return is_greater_than(obj, lower_bound) and is_less_or_equal(
            obj,
            upper_bound,
        )

    if closed == "none":
        return is_greater_than(obj, lower_bound) and is_less_than(
            obj,
            upper_bound,
        )

    raise ValueError(
        f"Invalid value for 'closed': {closed}. Expected one of 'both', 'left', 'right', 'none'.",
    )


def is_not_between(
    obj: Any,
    lower_bound: Any,
    upper_bound: Any,
    closed: Literal["both", "left", "right", "none"] = "both",
) -> bool:
    return not is_between(obj, lower_bound, upper_bound, closed)
