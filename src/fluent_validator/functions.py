"""Predicate functions for fluent_validator.

These are simple, composable boolean predicate helpers used by ValidatorSpec and
ValidatorBuilder. Each function returns True when the predicate matches the
provided value; negative counterparts are also provided.
"""

import dataclasses
from collections.abc import Iterable
from decimal import Decimal
from typing import Any, Literal


def is_instance_of(obj: Any, types: type | tuple[type, ...]) -> bool:
    """Return True if ``obj`` is an instance of the given ``types``.

    Args:
        obj: Value to check.
        types: A type or tuple of types to check against.

    Returns:
        True if ``isinstance(obj, types)``.

    """
    return isinstance(obj, types)


def is_not_instance_of(obj: Any, types: type | tuple[type, ...]) -> bool:
    """Return the negation of :func:`is_instance_of`.

    This returns True when ``obj`` is not an instance of ``types``.

    """
    return not is_instance_of(obj, types)


def is_callable(obj: Any) -> bool:
    """Return True if ``obj`` is callable.

    Args:
        obj: Value to check.

    Returns:
        True if ``callable(obj)``.

    """
    return callable(obj)


def is_not_callable(obj: Any) -> bool:
    """Return True if ``obj`` is not callable."""
    return not is_callable(obj)


def is_iterable(obj: Any) -> bool:
    """Return True if ``obj`` is an iterable.

    Strings are handled by :func:`is_string` if needed by higher-level validators.

    Args:
        obj: Value to check.

    Returns:
        True if ``isinstance(obj, Iterable)``.

    """
    return is_instance_of(obj, Iterable)


def is_not_iterable(obj: Any) -> bool:
    """Return True if ``obj`` is not an iterable."""
    return not is_iterable(obj)


def is_dataclass(obj: Any) -> bool:
    """Return True if ``obj`` is a dataclass instance or dataclass type.

    Uses :mod:`dataclasses.is_dataclass` under the hood.

    """
    return dataclasses.is_dataclass(obj)


def is_not_dataclass(obj: Any) -> bool:
    """Return True if ``obj`` is not a dataclass."""
    return not is_dataclass(obj)


def is_string(obj: Any) -> bool:
    """Return True if ``obj`` is a string.

    Args:
        obj: Value to check.

    Returns:
        True if ``isinstance(obj, str)``.

    """
    return is_instance_of(obj, str)


def is_not_string(obj: Any) -> bool:
    """Return True if ``obj`` is not a string."""
    return not is_string(obj)


def is_number(obj: Any) -> bool:
    """Return True if ``obj`` is a number (int, float or Decimal)."""
    return is_instance_of(obj, (int, float, Decimal))


def is_not_number(obj: Any) -> bool:
    """Return True if ``obj`` is not a number."""
    return not is_number(obj)


def is_bool(obj: Any) -> bool:
    """Return True if ``obj`` is a boolean."""
    return is_instance_of(obj, bool)


def is_not_bool(obj: Any) -> bool:
    """Return True if ``obj`` is not a boolean."""
    return not is_bool(obj)


def is_none(obj: Any) -> bool:
    """Return True if ``obj`` is ``None``."""
    return obj is None


def is_not_none(obj: Any) -> bool:
    """Return True if ``obj`` is not ``None``."""
    return not is_none(obj)


def is_greater_than(obj: Any, value: Any) -> bool:
    """Return True if ``obj`` is greater than ``value``.

    Args:
        obj: Left-hand value for comparison.
        value: Right-hand value for comparison.

    """
    return obj > value


def is_not_greater_than(obj: Any, value: Any) -> bool:
    """Return the negation of :func:`is_greater_than`."""
    return not is_greater_than(obj, value)


def is_equal(obj: Any, value: Any) -> bool:
    """Return True if ``obj`` is equal to ``value``."""
    return obj == value


def is_not_equal(obj: Any, value: Any) -> bool:
    """Return True if ``obj`` is not equal to ``value``."""
    return not is_equal(obj, value)


def is_less_than(obj: Any, value: Any) -> bool:
    """Return True if ``obj`` is less than ``value``."""
    return obj < value


def is_not_less_than(obj: Any, value: Any) -> bool:
    """Return the negation of :func:`is_less_than`."""
    return not is_less_than(obj, value)


def is_greater_or_equal(obj: Any, value: Any) -> bool:
    """Return True if ``obj`` is greater than or equal to ``value``."""
    return obj >= value


def is_not_greater_or_equal(obj: Any, value: Any) -> bool:
    """Return the negation of :func:`is_greater_or_equal`."""
    return not is_greater_or_equal(obj, value)


def is_less_or_equal(obj: Any, value: Any) -> bool:
    """Return True if ``obj`` is less than or equal to ``value``."""
    return obj <= value


def is_not_less_or_equal(obj: Any, value: Any) -> bool:
    """Return the negation of :func:`is_less_or_equal`."""
    return not is_less_or_equal(obj, value)


def is_between(
    obj: Any,
    lower_bound: Any,
    upper_bound: Any,
    closed: Literal["both", "left", "right", "none"] = "both",
) -> bool:
    """Return True if ``obj`` is between ``lower_bound`` and ``upper_bound``.

    The ``closed`` argument controls inclusion of the bounds:
      - "both": include both bounds (>= lower, <= upper)
      - "left": include left bound only (>= lower, < upper)
      - "right": include right bound only (> lower, <= upper)
      - "none": exclude both bounds (> lower, < upper)

    Raises:
        ValueError: If ``closed`` is not one of the expected strings.

    """
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
    """Return True if ``obj`` is not between the provided bounds."""
    return not is_between(obj, lower_bound, upper_bound, closed)
