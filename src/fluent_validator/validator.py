"""Convenience fluent builder exposing ValidatorSpec factory methods.

This module exposes Validator, which provides classmethods that
create configured :class:`~fluent_validator.validator_spec.ValidatorSpec`
instances for common validations.
"""

from collections.abc import Callable, Iterable
from typing import Any, Literal

from .validator_spec import ValidatorSpec


class Validator:
    """Fluent factory for creating :class:`ValidatorSpec` validators.

    Each classmethod returns a fresh ValidatorSpec pre-configured with the
    requested validation so callers can use the builder as a concise API.
    """

    @classmethod
    def prepare(cls) -> ValidatorSpec:
        """Return a new :class:`ValidatorSpec` for building validations."""
        return ValidatorSpec()

    @classmethod
    def is_instance_of(
        cls,
        types: type | tuple[type, ...],
        *,
        msg: str | None = None,
    ) -> ValidatorSpec:
        """Create a ValidatorSpec that checks instances against ``types``.

        Args:
            types: A type or tuple of types to check against.
            msg: Optional custom error message.

        """
        return cls.prepare().is_instance_of(types, msg=msg)

    @classmethod
    def is_callable(cls, *, msg: str | None = None) -> ValidatorSpec:
        """Create a ValidatorSpec that checks if a value is callable.

        Args:
            msg: Optional custom error message.

        """
        return cls.prepare().is_callable(msg=msg)

    @classmethod
    def is_iterable(cls, *, msg: str | None = None) -> ValidatorSpec:
        """Create a ValidatorSpec that checks if a value is iterable.

        Args:
            msg: Optional custom error message.

        """
        return cls.prepare().is_iterable(msg=msg)

    @classmethod
    def is_dataclass(cls, *, msg: str | None = None) -> ValidatorSpec:
        """Create a ValidatorSpec that checks if a value is a dataclass.

        Args:
            msg: Optional custom error message.

        """
        return cls.prepare().is_dataclass(msg=msg)

    @classmethod
    def is_string(cls, *, msg: str | None = None) -> ValidatorSpec:
        """Create a ValidatorSpec that checks if a value is a string.

        Args:
            msg: Optional custom error message.

        """
        return cls.prepare().is_string(msg=msg)

    @classmethod
    def is_number(cls, *, msg: str | None = None) -> ValidatorSpec:
        """Create a ValidatorSpec that checks if a value is a number.

        Args:
            msg: Optional custom error message.

        """
        return cls.prepare().is_number(msg=msg)

    @classmethod
    def is_bool(cls, *, msg: str | None = None) -> ValidatorSpec:
        """Create a ValidatorSpec that checks if a value is a boolean.

        Args:
            msg: Optional custom error message.

        """
        return cls.prepare().is_bool(msg=msg)

    @classmethod
    def is_none(cls, *, msg: str | None = None) -> ValidatorSpec:
        """Create a ValidatorSpec that checks if a value is None.

        Args:
            msg: Optional custom error message.

        """
        return cls.prepare().is_none(msg=msg)

    @classmethod
    def is_greater_than(cls, value: Any, *, msg: str | None = None) -> ValidatorSpec:
        """Create a ValidatorSpec that checks a value is greater than ``value``.

        Args:
            value: The threshold to compare against.
            msg: Optional custom error message.

        """
        return cls.prepare().is_greater_than(value, msg=msg)

    @classmethod
    def is_gt(cls, value: Any, *, msg: str | None = None) -> ValidatorSpec:
        """Alias for :meth:`is_greater_than`.

        Args:
            value: The threshold to compare against.
            msg: Optional custom error message.

        """
        return cls.prepare().is_gt(value, msg=msg)

    @classmethod
    def is_greater_or_equal(
        cls,
        value: Any,
        *,
        msg: str | None = None,
    ) -> ValidatorSpec:
        """Create a ValidatorSpec that checks a value is >= ``value``.

        Args:
            value: The threshold to compare against.
            msg: Optional custom error message.

        """
        return cls.prepare().is_greater_or_equal(value, msg=msg)

    @classmethod
    def is_gte(cls, value: Any, *, msg: str | None = None) -> ValidatorSpec:
        """Alias for :meth:`is_greater_or_equal`.

        Args:
            value: The threshold to compare against.
            msg: Optional custom error message.

        """
        return cls.prepare().is_gte(value, msg=msg)

    @classmethod
    def is_equal(cls, value: Any, *, msg: str | None = None) -> ValidatorSpec:
        """Create a ValidatorSpec that checks equality to ``value``.

        Args:
            value: Value to compare against.
            msg: Optional custom error message.

        """
        return cls.prepare().is_equal(value, msg=msg)

    @classmethod
    def is_eq(cls, value: Any, *, msg: str | None = None) -> ValidatorSpec:
        """Alias for :meth:`is_equal`.

        Args:
            value: Value to compare against.
            msg: Optional custom error message.

        """
        return cls.prepare().is_eq(value, msg=msg)

    @classmethod
    def is_less_than(cls, value: Any, *, msg: str | None = None) -> ValidatorSpec:
        """Create a ValidatorSpec that checks a value is less than ``value``.

        Args:
            value: The threshold to compare against.
            msg: Optional custom error message.

        """
        return cls.prepare().is_less_than(value, msg=msg)

    @classmethod
    def is_lt(cls, value: Any, *, msg: str | None = None) -> ValidatorSpec:
        """Alias for :meth:`is_less_than`.

        Args:
            value: The threshold to compare against.
            msg: Optional custom error message.

        """
        return cls.prepare().is_lt(value, msg=msg)

    @classmethod
    def is_less_or_equal(cls, value: Any, *, msg: str | None = None) -> ValidatorSpec:
        """Create a ValidatorSpec that checks a value is <= ``value``.

        Args:
            value: The threshold to compare against.
            msg: Optional custom error message.

        """
        return cls.prepare().is_less_or_equal(value, msg=msg)

    @classmethod
    def is_lte(cls, value: Any, *, msg: str | None = None) -> ValidatorSpec:
        """Alias for :meth:`is_less_or_equal`.

        Args:
            value: The threshold to compare against.
            msg: Optional custom error message.

        """
        return cls.prepare().is_lte(value, msg=msg)

    @classmethod
    def add_validation(
        cls,
        validation_fn: Callable[[Any], bool],
        *,
        msg: str,
    ) -> ValidatorSpec:
        """Create a ValidatorSpec that uses a custom validation function.

        Args:
            validation_fn: Callable that receives a value and returns bool.
            msg: Error message used when validation fails.

        """
        return cls.prepare().add_validation(validation_fn, msg=msg)

    @classmethod
    def add_validations(
        cls,
        validations: list[tuple[Callable[[Any], bool], str]],
    ) -> ValidatorSpec:
        """Create a ValidatorSpec and add multiple (fn, msg) validations.

        Args:
            validations: List of (fn, msg) tuples to add.

        """
        return cls.prepare().add_validations(validations)

    @classmethod
    def is_between(
        cls,
        lower_bound: Any,
        upper_bound: Any,
        *,
        closed: Literal["both", "left", "right", "none"] = "both",
        msg: str | None = None,
    ) -> ValidatorSpec:
        """Create a ValidatorSpec that checks a value is between two bounds.

        Args:
            lower_bound: Lower bound for the interval.
            upper_bound: Upper bound for the interval.
            closed: Which bounds are inclusive: 'both', 'left', 'right', or 'none'.
            msg: Optional custom error message.

        """
        return cls.prepare().is_between(
            lower_bound,
            upper_bound,
            closed=closed,
            msg=msg,
        )

    @classmethod
    def is_not_instance_of(
        cls,
        types: type | tuple[type, ...],
        *,
        msg: str | None = None,
    ) -> ValidatorSpec:
        """Create a ValidatorSpec that checks a value is not an instance of ``types``.

        Args:
            types: A type or tuple of types to check against.
            msg: Optional custom error message.

        """
        return cls.prepare().is_not_instance_of(types, msg=msg)

    @classmethod
    def is_not_callable(cls, *, msg: str | None = None) -> ValidatorSpec:
        """Create a ValidatorSpec that checks a value is not callable.

        Args:
            msg: Optional custom error message.

        """
        return cls.prepare().is_not_callable(msg=msg)

    @classmethod
    def is_not_iterable(cls, *, msg: str | None = None) -> ValidatorSpec:
        """Create a ValidatorSpec that checks a value is not iterable.

        Args:
            msg: Optional custom error message.

        """
        return cls.prepare().is_not_iterable(msg=msg)

    @classmethod
    def is_not_dataclass(cls, *, msg: str | None = None) -> ValidatorSpec:
        """Create a ValidatorSpec that checks a value is not a dataclass.

        Args:
            msg: Optional custom error message.

        """
        return cls.prepare().is_not_dataclass(msg=msg)

    @classmethod
    def is_not_string(cls, *, msg: str | None = None) -> ValidatorSpec:
        """Create a ValidatorSpec that checks a value is not a string.

        Args:
            msg: Optional custom error message.

        """
        return cls.prepare().is_not_string(msg=msg)

    @classmethod
    def is_not_number(cls, *, msg: str | None = None) -> ValidatorSpec:
        """Create a ValidatorSpec that checks a value is not a number.

        Args:
            msg: Optional custom error message.

        """
        return cls.prepare().is_not_number(msg=msg)

    @classmethod
    def is_not_bool(cls, *, msg: str | None = None) -> ValidatorSpec:
        """Create a ValidatorSpec that checks a value is not a boolean.

        Args:
            msg: Optional custom error message.

        """
        return cls.prepare().is_not_bool(msg=msg)

    @classmethod
    def is_not_none(cls, *, msg: str | None = None) -> ValidatorSpec:
        """Create a ValidatorSpec that checks a value is not None.

        Args:
            msg: Optional custom error message.

        """
        return cls.prepare().is_not_none(msg=msg)

    @classmethod
    def is_not_greater_than(
        cls,
        value: Any,
        *,
        msg: str | None = None,
    ) -> ValidatorSpec:
        """Create a ValidatorSpec that checks a value is not greater than ``value``.

        Args:
            value: The threshold to compare against.
            msg: Optional custom error message.

        """
        return cls.prepare().is_not_greater_than(value, msg=msg)

    @classmethod
    def is_not_gt(cls, value: Any, *, msg: str | None = None) -> ValidatorSpec:
        """Alias for :meth:`is_not_greater_than`.

        Args:
            value: The threshold to compare against.
            msg: Optional custom error message.

        """
        return cls.prepare().is_not_gt(value, msg=msg)

    @classmethod
    def is_not_greater_or_equal(
        cls,
        value: Any,
        *,
        msg: str | None = None,
    ) -> ValidatorSpec:
        """Create a ValidatorSpec that checks a value is not >= ``value``.

        Args:
            value: The threshold to compare against.
            msg: Optional custom error message.

        """
        return cls.prepare().is_not_greater_or_equal(value, msg=msg)

    @classmethod
    def is_not_gte(cls, value: Any, *, msg: str | None = None) -> ValidatorSpec:
        """Alias for :meth:`is_not_greater_or_equal`.

        Args:
            value: The threshold to compare against.
            msg: Optional custom error message.

        """
        return cls.prepare().is_not_gte(value, msg=msg)

    @classmethod
    def is_not_equal(cls, value: Any, *, msg: str | None = None) -> ValidatorSpec:
        """Create a ValidatorSpec that checks a value is not equal to ``value``.

        Args:
            value: The threshold to compare against.
            msg: Optional custom error message.

        """
        return cls.prepare().is_not_equal(value, msg=msg)

    @classmethod
    def is_not_eq(cls, value: Any, *, msg: str | None = None) -> ValidatorSpec:
        """Alias for :meth:`is_not_equal`.

        Args:
            value: The threshold to compare against.
            msg: Optional custom error message.

        """
        return cls.prepare().is_not_eq(value, msg=msg)

    @classmethod
    def is_not_less_than(cls, value: Any, *, msg: str | None = None) -> ValidatorSpec:
        """Create a ValidatorSpec that checks a value is not less than ``value``.

        Args:
            value: The threshold to compare against.
            msg: Optional custom error message.

        """
        return cls.prepare().is_not_less_than(value, msg=msg)

    @classmethod
    def is_not_lt(cls, value: Any, *, msg: str | None = None) -> ValidatorSpec:
        """Alias for :meth:`is_not_less_than`.

        Args:
            value: The threshold to compare against.
            msg: Optional custom error message.

        """
        return cls.prepare().is_not_lt(value, msg=msg)

    @classmethod
    def is_not_less_or_equal(
        cls,
        value: Any,
        *,
        msg: str | None = None,
    ) -> ValidatorSpec:
        """Create a ValidatorSpec that checks a value is not <= ``value``.

        Args:
            value: The threshold to compare against.
            msg: Optional custom error message.

        """
        return cls.prepare().is_not_less_or_equal(value, msg=msg)

    @classmethod
    def is_not_lte(cls, value: Any, *, msg: str | None = None) -> ValidatorSpec:
        """Alias for :meth:`is_not_less_or_equal`.

        Args:
            value: The threshold to compare against.
            msg: Optional custom error message.

        """
        return cls.prepare().is_not_lte(value, msg=msg)

    @classmethod
    def is_not_between(
        cls,
        lower_bound: Any,
        upper_bound: Any,
        *,
        closed: Literal["both", "left", "right", "none"] = "both",
        msg: str | None = None,
    ) -> ValidatorSpec:
        """Create a ValidatorSpec that checks a value is not between two bounds.

        Args:
            lower_bound: Lower bound for the interval.
            upper_bound: Upper bound for the interval.
            closed: Which bounds are inclusive: 'both', 'left', 'right', or 'none'.
            msg: Optional custom error message.

        """
        return cls.prepare().is_not_between(
            lower_bound,
            upper_bound,
            closed=closed,
            msg=msg,
        )

    @classmethod
    def contains_at_least(cls, value: int, *, msg: str | None = None) -> ValidatorSpec:
        """Create a ValidatorSpec that checks iterable contains at least ``value`` elements."""
        return cls.prepare().contains_at_least(value, msg=msg)

    @classmethod
    def contains_at_most(cls, value: int, *, msg: str | None = None) -> ValidatorSpec:
        """Create a ValidatorSpec that checks iterable contains at most ``value`` elements."""
        return cls.prepare().contains_at_most(value, msg=msg)

    @classmethod
    def contains_exactly(cls, value: int, *, msg: str | None = None) -> ValidatorSpec:
        """Create a ValidatorSpec that checks iterable contains exactly ``value`` elements."""
        return cls.prepare().contains_exactly(value, msg=msg)

    @classmethod
    def has_unique_values(cls, *, msg: str | None = None) -> ValidatorSpec:
        """Create a ValidatorSpec that checks iterable has unique values."""
        return cls.prepare().has_unique_values(msg=msg)

    @classmethod
    def is_empty(cls, *, msg: str | None = None) -> ValidatorSpec:
        """Create a ValidatorSpec that checks a value is empty (or None)."""
        return cls.prepare().is_empty(msg=msg)

    @classmethod
    def is_not_empty(cls, *, msg: str | None = None) -> ValidatorSpec:
        """Create a ValidatorSpec that checks a value is not empty."""
        return cls.prepare().is_not_empty(msg=msg)

    @classmethod
    def is_false(cls, *, msg: str | None = None) -> ValidatorSpec:
        """Create a ValidatorSpec that checks a value is the boolean False."""
        return cls.prepare().is_false(msg=msg)

    @classmethod
    def is_not_false(cls, *, msg: str | None = None) -> ValidatorSpec:
        """Create a ValidatorSpec that checks a value is not the boolean False."""
        return cls.prepare().is_not_false(msg=msg)

    @classmethod
    def is_true(cls, *, msg: str | None = None) -> ValidatorSpec:
        """Create a ValidatorSpec that checks a value is the boolean True."""
        return cls.prepare().is_true(msg=msg)

    @classmethod
    def is_not_true(cls, *, msg: str | None = None) -> ValidatorSpec:
        """Create a ValidatorSpec that checks a value is not the boolean True."""
        return cls.prepare().is_not_true(msg=msg)

    @classmethod
    def is_in(cls, collection: Iterable, *, msg: str | None = None) -> ValidatorSpec:
        """Create a ValidatorSpec that checks a value is in the provided collection."""
        return cls.prepare().is_in(collection, msg=msg)

    @classmethod
    def is_not_in(cls, collection: Iterable, *, msg: str | None = None) -> ValidatorSpec:
        """Create a ValidatorSpec that checks a value is not in the provided collection."""
        return cls.prepare().is_not_in(collection, msg=msg)

