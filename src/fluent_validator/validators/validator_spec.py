from collections.abc import Callable, Iterable
from typing import Any, Literal, Self

from .exceptions import ValidationError
from fluent_validator.validators import functions as F


class ValidatorSpec:
    def __init__(
        self,
        validations: list[tuple[Callable[[Any], bool], str]] | None = None,
        _describe_tree: tuple | None = None,
    ):
        self._validations = validations or []
        self._describe_tree = _describe_tree

    @classmethod
    def from_validations(
        cls,
        validations: list[tuple[Callable[[Any], bool], str]],
        _describe_tree: tuple | None = None,
    ) -> Self:
        return cls(validations=validations, _describe_tree=_describe_tree)

    def validations(self) -> list[tuple[Callable[[Any], bool], str]]:
        return self._validations.copy()

    def add_validation(self, validation_fn: Callable[[Any], bool], *, msg: str) -> Self:
        return self.add_validations([(validation_fn, msg)])

    def _get_describe_tree(self) -> tuple | None:
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
        msg = msg or f"Should not be an instance of {types} (rule: is_not_instance_of)"
        return self.add_validation(
            lambda obj: F.is_not_instance_of(obj, types),
            msg=msg,
        )

    def is_callable(self, *, msg: str | None = None) -> Self:
        msg = msg or "Should be callable (rule: is_callable)"
        return self.add_validation(lambda obj: F.is_callable(obj), msg=msg)

    def is_not_callable(self, *, msg: str | None = None) -> Self:
        msg = msg or "Should not be callable (rule: is_not_callable)"
        return self.add_validation(
            lambda obj: F.is_not_callable(obj),
            msg=msg,
        )

    def is_iterable(self, *, msg: str | None = None) -> Self:
        msg = msg or "Should be iterable (rule: is_iterable)"
        return self.add_validation(lambda obj: F.is_iterable(obj), msg=msg)

    def is_not_iterable(self, *, msg: str | None = None) -> Self:
        msg = msg or "Should not be iterable (rule: is_not_iterable)"
        return self.add_validation(
            lambda obj: F.is_not_iterable(obj),
            msg=msg,
        )

    def is_dataclass(self, *, msg: str | None = None) -> Self:
        msg = msg or "Should be a dataclass (rule: is_dataclass)"
        return self.add_validation(lambda obj: F.is_dataclass(obj), msg=msg)

    def is_not_dataclass(self, *, msg: str | None = None) -> Self:
        msg = msg or "Should not be a dataclass (rule: is_not_dataclass)"
        return self.add_validation(
            lambda obj: F.is_not_dataclass(obj),
            msg=msg,
        )

    def is_string(self, *, msg: str | None = None) -> Self:
        msg = msg or "Should be a string (rule: is_string)"
        return self.add_validation(lambda obj: F.is_string(obj), msg=msg)

    def is_not_string(self, *, msg: str | None = None) -> Self:
        msg = msg or "Should not be a string (rule: is_not_string)"
        return self.add_validation(lambda obj: F.is_not_string(obj), msg=msg)

    def is_number(self, *, msg: str | None = None) -> Self:
        msg = msg or "Should be a number (rule: is_number)"
        return self.add_validation(lambda obj: F.is_number(obj), msg=msg)

    def is_not_number(self, *, msg: str | None = None) -> Self:
        msg = msg or "Should not be a number (rule: is_not_number)"
        return self.add_validation(lambda obj: F.is_not_number(obj), msg=msg)

    def is_bool(self, *, msg: str | None = None) -> Self:
        msg = msg or "Should be a boolean (rule: is_bool)"
        return self.add_validation(lambda obj: F.is_bool(obj), msg=msg)

    def is_not_bool(self, *, msg: str | None = None) -> Self:
        msg = msg or "Should not be a boolean (rule: is_not_bool)"
        return self.add_validation(lambda obj: F.is_not_bool(obj), msg=msg)

    def is_none(self, *, msg: str | None = None) -> Self:
        msg = msg or "Should be None (rule: is_none)"
        return self.add_validation(lambda obj: F.is_none(obj), msg=msg)

    def is_not_none(self, *, msg: str | None = None) -> Self:
        msg = msg or "Should not be None (rule: is_not_none)"
        return self.add_validation(lambda obj: F.is_not_none(obj), msg=msg)

    def is_greater_than(self, value: Any, *, msg: str | None = None) -> Self:
        msg = msg or f"Should be greater than {value} (rule: is_greater_than)"
        return self.add_validation(
            lambda obj: F.is_greater_than(obj, value),
            msg=msg,
        )

    def is_not_greater_than(self, value: Any, *, msg: str | None = None) -> Self:
        msg = msg or f"Should not be greater than {value} (rule: is_not_greater_than)"
        return self.add_validation(lambda obj: F.is_not_greater_than(obj, value), msg=msg)

    def is_gt(self, value: Any, *, msg: str | None = None) -> Self:
        return self.is_greater_than(value, msg=msg)

    def is_not_gt(self, value: Any, *, msg: str | None = None) -> Self:
        return self.is_not_greater_than(value, msg=msg)

    def is_greater_or_equal(self, value: Any, *, msg: str | None = None) -> Self:
        msg = msg or f"Should be greater than or equal to {value} (rule: is_greater_or_equal)"
        return self.add_validation(
            lambda obj: F.is_greater_or_equal(obj, value),
            msg=msg,
        )

    def is_not_greater_or_equal(self, value: Any, *, msg: str | None = None) -> Self:
        msg = msg or f"Should not be greater than or equal to {value} (rule: is_not_greater_or_equal)"
        return self.add_validation(lambda obj: F.is_not_greater_or_equal(obj, value), msg=msg)

    def is_gte(self, value: Any, *, msg: str | None = None) -> Self:
        return self.is_greater_or_equal(value, msg=msg)

    def is_not_gte(self, value: Any, *, msg: str | None = None) -> Self:
        return self.is_not_greater_or_equal(value, msg=msg)

    def is_equal(self, value: Any, *, msg: str | None = None) -> Self:
        msg = msg or f"Should be equal to {value} (rule: is_equal)"
        return self.add_validation(
            lambda obj: F.is_equal(obj, value),
            msg=msg,
        )

    def is_not_equal(self, value: Any, *, msg: str | None = None) -> Self:
        msg = msg or f"Should not be equal to {value} (rule: is_not_equal)"
        return self.add_validation(lambda obj: F.is_not_equal(obj, value), msg=msg)

    def is_eq(self, value: Any, *, msg: str | None = None) -> Self:
        return self.is_equal(value, msg=msg)

    def is_not_eq(self, value: Any, *, msg: str | None = None) -> Self:
        return self.is_not_equal(value, msg=msg)

    def is_less_than(self, value: Any, *, msg: str | None = None) -> Self:
        msg = msg or f"Should be less than {value} (rule: is_less_than)"
        return self.add_validation(
            lambda obj: F.is_less_than(obj, value),
            msg=msg,
        )

    def is_not_less_than(self, value: Any, *, msg: str | None = None) -> Self:
        msg = msg or f"Should not be less than {value} (rule: is_not_less_than)"
        return self.add_validation(lambda obj: F.is_not_less_than(obj, value), msg=msg)

    def is_lt(self, value: Any, *, msg: str | None = None) -> Self:
        return self.is_less_than(value, msg=msg)

    def is_not_lt(self, value: Any, *, msg: str | None = None) -> Self:
        return self.is_not_less_than(value, msg=msg)

    def is_less_or_equal(self, value: Any, *, msg: str | None = None) -> Self:
        msg = msg or f"Should be less than or equal to {value} (rule: is_less_or_equal)"
        return self.add_validation(
            lambda obj: F.is_less_or_equal(obj, value),
            msg=msg,
        )

    def is_not_less_or_equal(self, value: Any, *, msg: str | None = None) -> Self:
        msg = msg or f"Should not be less than or equal to {value} (rule: is_not_less_or_equal)"
        return self.add_validation(lambda obj: F.is_not_less_or_equal(obj, value), msg=msg)

    def is_lte(self, value: Any, *, msg: str | None = None) -> Self:
        return self.is_less_or_equal(value, msg=msg)

    def is_not_lte(self, value: Any, *, msg: str | None = None) -> Self:
        return self.is_not_less_or_equal(value, msg=msg)

    def is_between(
        self,
        lower_bound: Any,
        upper_bound: Any,
        *,
        closed: Literal["both", "left", "right", "none"] = "both",
        msg: str | None = None,
    ) -> Self:
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
        msg = (
            msg
            or f"Should not be between {lower_bound} and {upper_bound} (closed='{closed}') (rule: is_not_between)"
        )
        return self.add_validation(lambda obj: F.is_not_between(obj, lower_bound, upper_bound, closed), msg=msg)

    def _render_pretty(self, node: tuple | None, indent: int = 0, *, is_top_level: bool = True) -> str:
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
        def inverted_factory(validator: Self):
            validator = validator.from_validations(validator.validations())

            def inverted(obj: Any) -> bool:
                return not validator.validate(obj, strategy="return_result")

            msg = f"NOT({validator.describe()})"
            return inverted, msg

        current_tree = self._get_describe_tree()
        new_tree = ("not", current_tree)

        return self.from_validations([inverted_factory(self)], _describe_tree=new_tree)
