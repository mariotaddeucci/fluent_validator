from fluent_validator.validators.type_validator import TypeValidator


class ValueValidator(TypeValidator):
    def _equal(self, value) -> bool:
        return self.obj == value

    def _is_in(self, *args) -> bool:
        return self.obj in args

    def _greater_than(self, value) -> bool:
        return self.obj > value

    def _less_than(self, value) -> bool:
        return self.obj < value

    def _greater_or_equal_than(self, value) -> bool:
        return self.obj >= value

    def _less_or_equal_than(self, value) -> bool:
        return self.obj <= value

    def _min(self, value) -> bool:
        return self._greater_or_equal_than(value)

    def _max(self, value) -> bool:
        return self._less_or_equal_than(value)

    def _between(self, min, max) -> bool:
        return self._min(min) and self._max(max)

    def _is_true(self) -> bool:
        return self._is_bool() and self.obj is True

    def _is_false(self) -> bool:
        return self._is_bool() and self.obj is False

    def _is_empty(self) -> bool:
        return not self.obj

    def _contains_at_least(self, value) -> bool:
        return len(self.obj) >= value

    def _contains_at_most(self, value) -> bool:
        return len(self.obj) <= value

    def _contains_exactly(self, value) -> bool:
        return len(self.obj) == value

    def _is_none(self) -> bool:
        return self.obj is None
