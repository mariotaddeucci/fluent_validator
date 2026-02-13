"""Validators for fluent_validator module.

Provides ValidatorSpec, a composable builder for validation rules.
"""

from collections.abc import Callable, Iterable
from typing import Any, Literal, Self

from fluent_validator import functions as F

from .exceptions import ValidationError


class ValidatorSpec:
    """Builder for validation specifications composed of callable checks and messages.

    Provides methods to compose validators and to validate objects.
    """

    def __init__(
        self,
        validations: list[tuple[Callable[[Any], bool], str]] | None = None,
        _describe_tree: tuple | None = None,
    ):
        """Initialize the ValidatorSpec with optional validations and describe tree."""
        self._validations = validations or []
        self._describe_tree = _describe_tree

    @classmethod
    def from_validations(
        cls,
        validations: list[tuple[Callable[[Any], bool], str]],
        _describe_tree: tuple | None = None,
    ) -> Self:
        """Create a ValidatorSpec from a list of (validation_fn, msg) pairs and optional describe tree."""
        return cls(validations=validations, _describe_tree=_describe_tree)

    def validations(self) -> list[tuple[Callable[[Any], bool], str]]:
        """Return a shallow copy of the validations list."""
        return self._validations.copy()

    def add_validation(self, validation_fn: Callable[[Any], bool], *, msg: str) -> Self:
        """Add a single validation and return a new ValidatorSpec."""
        return self.add_validations([(validation_fn, msg)])

    def _get_describe_tree(self) -> tuple | None:
        """Return the internal describe tree, constructing it from validations if necessary."""
        if self._describe_tree is not None:
            return self._describe_tree
        if not self._validations:
            return None
        leaves = [("leaf", msg) for _, msg in self._validations]
        if len(leaves) == 1:
            return leaves[0]
        return ("and", leaves)

    def add_validations(
        self,
        validations: list[tuple[Callable[[Any], bool], str]],
    ) -> Self:
        """Add multiple validations and return a new ValidatorSpec."""
        new_validations = self.validations() + validations
        current_tree = self._get_describe_tree()
        new_leaves = [("leaf", msg) for _, msg in validations]

        if not new_leaves:
            new_tree = current_tree
        elif current_tree is None:
            new_tree = new_leaves[0] if len(new_leaves) == 1 else ("and", new_leaves)
        elif current_tree[0] == "and":
            new_tree = ("and", list(current_tree[1]) + new_leaves)
        else:
            new_tree = ("and", [current_tree, *new_leaves])

        return self.from_validations(new_validations, _describe_tree=new_tree)

    def is_instance_of(
        self,
        types: type | tuple[type, ...],
        *,
        msg: str | None = None,
    ) -> Self:
        """Add a validation that asserts the object is instance of."""
        msg = msg or f"Should be an instance of {types} (rule: is_instance_of)"
        return self.add_validation(
            lambda obj: F.is_instance_of(obj, types),
            msg=msg,
        )

    def is_not_instance_of(
        self,
        types: type | tuple[type, ...],
        *,
        msg: str | None = None,
    ) -> Self:
        """Add a validation that asserts the object is not instance of."""
        msg = msg or f"Should not be an instance of {types} (rule: is_not_instance_of)"
        return self.add_validation(
            lambda obj: F.is_not_instance_of(obj, types),
            msg=msg,
        )

    def is_callable(self, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the object is callable."""
        msg = msg or "Should be callable (rule: is_callable)"
        return self.add_validation(lambda obj: F.is_callable(obj), msg=msg)

    def is_not_callable(self, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the object is not callable."""
        msg = msg or "Should not be callable (rule: is_not_callable)"
        return self.add_validation(
            lambda obj: F.is_not_callable(obj),
            msg=msg,
        )

    def is_iterable(self, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the object is iterable."""
        msg = msg or "Should be iterable (rule: is_iterable)"
        return self.add_validation(lambda obj: F.is_iterable(obj), msg=msg)

    def is_not_iterable(self, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the object is not iterable."""
        msg = msg or "Should not be iterable (rule: is_not_iterable)"
        return self.add_validation(
            lambda obj: F.is_not_iterable(obj),
            msg=msg,
        )

    def is_dataclass(self, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the object is dataclass."""
        msg = msg or "Should be a dataclass (rule: is_dataclass)"
        return self.add_validation(lambda obj: F.is_dataclass(obj), msg=msg)

    def is_not_dataclass(self, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the object is not dataclass."""
        msg = msg or "Should not be a dataclass (rule: is_not_dataclass)"
        return self.add_validation(
            lambda obj: F.is_not_dataclass(obj),
            msg=msg,
        )

    def is_string(self, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the object is string."""
        msg = msg or "Should be a string (rule: is_string)"
        return self.add_validation(lambda obj: F.is_string(obj), msg=msg)

    def is_not_string(self, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the object is not string."""
        msg = msg or "Should not be a string (rule: is_not_string)"
        return self.add_validation(lambda obj: F.is_not_string(obj), msg=msg)

    def is_number(self, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the object is number."""
        msg = msg or "Should be a number (rule: is_number)"
        return self.add_validation(lambda obj: F.is_number(obj), msg=msg)

    def is_not_number(self, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the object is not number."""
        msg = msg or "Should not be a number (rule: is_not_number)"
        return self.add_validation(lambda obj: F.is_not_number(obj), msg=msg)

    def is_bool(self, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the object is bool."""
        msg = msg or "Should be a boolean (rule: is_bool)"
        return self.add_validation(lambda obj: F.is_bool(obj), msg=msg)

    def is_not_bool(self, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the object is not bool."""
        msg = msg or "Should not be a boolean (rule: is_not_bool)"
        return self.add_validation(lambda obj: F.is_not_bool(obj), msg=msg)

    def is_none(self, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the object is none."""
        msg = msg or "Should be None (rule: is_none)"
        return self.add_validation(lambda obj: F.is_none(obj), msg=msg)

    def is_not_none(self, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the object is not none."""
        msg = msg or "Should not be None (rule: is_not_none)"
        return self.add_validation(lambda obj: F.is_not_none(obj), msg=msg)

    def is_greater_than(self, value: Any, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the object is greater than."""
        msg = msg or f"Should be greater than {value} (rule: is_greater_than)"
        return self.add_validation(
            lambda obj: F.is_greater_than(obj, value),
            msg=msg,
        )

    def is_not_greater_than(self, value: Any, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the object is not greater than."""
        msg = msg or f"Should not be greater than {value} (rule: is_not_greater_than)"
        return self.add_validation(lambda obj: F.is_not_greater_than(obj, value), msg=msg)

    def is_gt(self, value: Any, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the object is gt."""
        return self.is_greater_than(value, msg=msg)

    def is_not_gt(self, value: Any, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the object is not gt."""
        return self.is_not_greater_than(value, msg=msg)

    def is_greater_or_equal(self, value: Any, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the object is greater or equal."""
        msg = msg or f"Should be greater than or equal to {value} (rule: is_greater_or_equal)"
        return self.add_validation(
            lambda obj: F.is_greater_or_equal(obj, value),
            msg=msg,
        )

    def is_not_greater_or_equal(self, value: Any, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the object is not greater or equal."""
        msg = msg or f"Should not be greater than or equal to {value} (rule: is_not_greater_or_equal)"
        return self.add_validation(lambda obj: F.is_not_greater_or_equal(obj, value), msg=msg)

    def is_gte(self, value: Any, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the object is gte."""
        return self.is_greater_or_equal(value, msg=msg)

    def is_not_gte(self, value: Any, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the object is not gte."""
        return self.is_not_greater_or_equal(value, msg=msg)

    def is_equal(self, value: Any, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the object is equal."""
        msg = msg or f"Should be equal to {value} (rule: is_equal)"
        return self.add_validation(
            lambda obj: F.is_equal(obj, value),
            msg=msg,
        )

    def is_not_equal(self, value: Any, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the object is not equal."""
        msg = msg or f"Should not be equal to {value} (rule: is_not_equal)"
        return self.add_validation(lambda obj: F.is_not_equal(obj, value), msg=msg)

    def is_eq(self, value: Any, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the object is eq."""
        return self.is_equal(value, msg=msg)

    def is_not_eq(self, value: Any, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the object is not eq."""
        return self.is_not_equal(value, msg=msg)

    def is_less_than(self, value: Any, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the object is less than."""
        msg = msg or f"Should be less than {value} (rule: is_less_than)"
        return self.add_validation(
            lambda obj: F.is_less_than(obj, value),
            msg=msg,
        )

    def is_not_less_than(self, value: Any, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the object is not less than."""
        msg = msg or f"Should not be less than {value} (rule: is_not_less_than)"
        return self.add_validation(lambda obj: F.is_not_less_than(obj, value), msg=msg)

    def is_lt(self, value: Any, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the object is lt."""
        return self.is_less_than(value, msg=msg)

    def is_not_lt(self, value: Any, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the object is not lt."""
        return self.is_not_less_than(value, msg=msg)

    def is_less_or_equal(self, value: Any, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the object is less or equal."""
        msg = msg or f"Should be less than or equal to {value} (rule: is_less_or_equal)"
        return self.add_validation(
            lambda obj: F.is_less_or_equal(obj, value),
            msg=msg,
        )

    def is_not_less_or_equal(self, value: Any, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the object is not less or equal."""
        msg = msg or f"Should not be less than or equal to {value} (rule: is_not_less_or_equal)"
        return self.add_validation(lambda obj: F.is_not_less_or_equal(obj, value), msg=msg)

    def is_lte(self, value: Any, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the object is lte."""
        return self.is_less_or_equal(value, msg=msg)

    def is_not_lte(self, value: Any, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the object is not lte."""
        return self.is_not_less_or_equal(value, msg=msg)

    def is_between(
        self,
        lower_bound: Any,
        upper_bound: Any,
        *,
        closed: Literal["both", "left", "right", "none"] = "both",
        msg: str | None = None,
    ) -> Self:
        """Add a validation that asserts the object is between."""
        msg = msg or f"Should be between {lower_bound} and {upper_bound} (closed='{closed}') (rule: is_between)"
        return self.add_validation(
            lambda obj: F.is_between(obj, lower_bound, upper_bound, closed),
            msg=msg,
        )

    def is_not_between(
        self,
        lower_bound: Any,
        upper_bound: Any,
        *,
        closed: Literal["both", "left", "right", "none"] = "both",
        msg: str | None = None,
    ) -> Self:
        """Add a validation that asserts the object is not between."""
        msg = msg or f"Should not be between {lower_bound} and {upper_bound} (closed='{closed}') (rule: is_not_between)"
        return self.add_validation(lambda obj: F.is_not_between(obj, lower_bound, upper_bound, closed), msg=msg)

    def contains_at_least(self, value: int, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the iterable contains at least ``value`` elements."""
        msg = msg or f"Should contain at least {value} elements (rule: contains_at_least)"
        return self.add_validation(lambda obj: F.contains_at_least(obj, value), msg=msg)

    def contains_at_most(self, value: int, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the iterable contains at most ``value`` elements."""
        msg = msg or f"Should contain at most {value} elements (rule: contains_at_most)"
        return self.add_validation(lambda obj: F.contains_at_most(obj, value), msg=msg)

    def contains_exactly(self, value: int, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the iterable contains exactly ``value`` elements."""
        msg = msg or f"Should contain exactly {value} elements (rule: contains_exactly)"
        return self.add_validation(lambda obj: F.contains_exactly(obj, value), msg=msg)

    def has_unique_values(self, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the iterable has unique values."""
        msg = msg or "Should have unique values (rule: has_unique_values)"
        return self.add_validation(lambda obj: F.has_unique_values(obj), msg=msg)

    def is_empty(self, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the object is empty (or None)."""
        msg = msg or "Should be empty (rule: is_empty)"
        return self.add_validation(lambda obj: F.is_empty(obj), msg=msg)

    def is_not_empty(self, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the object is not empty."""
        msg = msg or "Should not be empty (rule: is_not_empty)"
        return self.add_validation(lambda obj: F.is_not_empty(obj), msg=msg)

    def is_false(self, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the object is the boolean False."""
        msg = msg or "Should be False (rule: is_false)"
        return self.add_validation(lambda obj: F.is_false(obj), msg=msg)

    def is_not_false(self, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the object is not the boolean False."""
        msg = msg or "Should not be False (rule: is_not_false)"
        return self.add_validation(lambda obj: F.is_not_false(obj), msg=msg)

    def is_true(self, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the object is the boolean True."""
        msg = msg or "Should be True (rule: is_true)"
        return self.add_validation(lambda obj: F.is_true(obj), msg=msg)

    def is_not_true(self, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the object is not the boolean True."""
        msg = msg or "Should not be True (rule: is_not_true)"
        return self.add_validation(lambda obj: F.is_not_true(obj), msg=msg)

    def is_in(self, collection: Iterable, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the object is in the provided collection."""
        msg = msg or f"Should be in {collection} (rule: is_in)"
        return self.add_validation(lambda obj: F.is_in(obj, collection), msg=msg)

    def is_not_in(self, collection: Iterable, *, msg: str | None = None) -> Self:
        """Add a validation that asserts the object is not in the provided collection."""
        msg = msg or f"Should not be in {collection} (rule: is_not_in)"
        return self.add_validation(lambda obj: F.is_not_in(obj, collection), msg=msg)

    def _render_pretty(self, node: tuple | None, indent: int = 0, *, is_top_level: bool = True) -> str:
        """Render the describe tree into a human-friendly string with indentation."""
        if node is None:
            return "No validations"

        pad = "    " * indent
        inner_pad = "    " * (indent + 1)
        node_type = node[0]

        if node_type == "leaf":
            return f"{pad}'{node[1]}'"

        if node_type == "and":
            children = node[1]
            if len(children) == 1:
                return self._render_pretty(children[0], indent, is_top_level=is_top_level)

            if is_top_level:
                parts = []
                for i, child in enumerate(children):
                    child_str = self._render_pretty(child, indent, is_top_level=False)
                    if i > 0:
                        parts.append(f"{pad}AND {child_str.lstrip()}")
                    else:
                        parts.append(child_str)
                return "\n".join(parts)

            parts = [f"{pad}("]
            for i, child in enumerate(children):
                child_str = self._render_pretty(child, indent + 1, is_top_level=False)
                if i < len(children) - 1:
                    parts.append(f"{child_str} AND")
                else:
                    parts.append(child_str)
            parts.append(f"{pad})")
            return "\n".join(parts)

        if node_type == "or":
            left, right = node[1]
            parts = [f"{pad}("]
            parts.append(self._render_pretty(left, indent + 1, is_top_level=False))
            parts.append(f"{inner_pad}OR")
            parts.append(self._render_pretty(right, indent + 1, is_top_level=False))
            parts.append(f"{pad})")
            return "\n".join(parts)

        if node_type == "not":
            child_str = self._render_pretty(node[1], indent, is_top_level=False)
            child_lines = child_str.split("\n")
            child_lines[0] = f"{pad}not {child_lines[0].lstrip()}"
            return "\n".join(child_lines)

        return ""

    def describe(self, pretty: bool = False) -> str:
        """Return a textual description of the validations; pretty formatting if requested."""
        if pretty:
            return self._render_pretty(self._get_describe_tree())
        if not self._validations:
            return "No validations"
        return " AND ".join(msg for _, msg in self._validations)

    def validate(
        self,
        obj: Any,
        *,
        strategy: Literal[
            "raise_after_first_error",
            "raise_after_all_errors",
            "return_result",
        ] = "raise_after_first_error",
    ) -> bool:
        """Validate the given object using the configured validations and provided strategy; may raise ValidationError."""
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

    def validate_each(
        self,
        iterable: Iterable[Any],
        *,
        strategy: Literal[
            "raise_after_first_error",
            "raise_after_all_errors",
            "return_result",
        ] = "raise_after_first_error",
    ) -> bool:
        """Validate each item in an iterable using the configured validations; may raise ValidationError with index info."""
        errors = []
        for index, item in enumerate(iterable):
            try:
                self.validate(item, strategy=strategy)
            except ValidationError as e:
                error_msg = f"Item at index {index} failed validation: {e!s}"
                if strategy == "raise_after_first_error":
                    raise ValidationError(error_msg) from e
                errors.append(error_msg)

        if strategy == "raise_after_all_errors" and errors:
            raise ValidationError("; ".join(errors))

        return not errors

    def __and__(self, other: "ValidatorSpec") -> Self:
        """Combine this ValidatorSpec with another using logical AND and return a new ValidatorSpec."""
        if not isinstance(other, ValidatorSpec):
            return NotImplemented

        new_validations = self.validations() + other.validations()

        self_tree = self._get_describe_tree()
        other_tree = other._get_describe_tree()

        if self_tree is None:
            new_tree = other_tree
        elif other_tree is None:
            new_tree = self_tree
        else:
            self_children = list(self_tree[1]) if self_tree[0] == "and" else [self_tree]
            other_children = list(other_tree[1]) if other_tree[0] == "and" else [other_tree]
            new_tree = ("and", self_children + other_children)

        return self.from_validations(new_validations, _describe_tree=new_tree)

    def __or__(self, other: "ValidatorSpec") -> Self:
        """Combine this ValidatorSpec with another using logical OR and return a new ValidatorSpec."""
        if not isinstance(other, ValidatorSpec):
            return NotImplemented

        def combined_validation_factory(
            validations1: list[tuple[Callable[[Any], bool], str]],
            validations2: list[tuple[Callable[[Any], bool], str]],
        ) -> Callable[[Any], bool]:
            def combined_validation(obj: Any) -> bool:
                return all(validation_fn(obj) for validation_fn, _ in validations1) or all(
                    validation_fn(obj) for validation_fn, _ in validations2
                )

            return combined_validation

        combined_validation_fn = combined_validation_factory(
            self.validations(),
            other.validations(),
        )
        combined_msg = f"({' and '.join(msg for _, msg in self.validations())}) OR ({' and '.join(msg for _, msg in other.validations())})"

        self_tree = self._get_describe_tree()
        other_tree = other._get_describe_tree()
        new_tree = ("or", [self_tree, other_tree])

        return self.from_validations([(combined_validation_fn, combined_msg)], _describe_tree=new_tree)

    def __neg__(self) -> Self:
        """Return a ValidatorSpec representing the logical negation of this spec."""

        def inverted_factory(validator: Self):
            validator = validator.from_validations(validator.validations())

            def inverted(obj: Any) -> bool:
                return not validator.validate(obj, strategy="return_result")

            msg = f"NOT({validator.describe()})"
            return inverted, msg

        current_tree = self._get_describe_tree()
        new_tree = ("not", current_tree)

        return self.from_validations([inverted_factory(self)], _describe_tree=new_tree)
