from fluent_validator.validators.type_validator import TypeValidator


class ValueValidator(TypeValidator):
    def _equal(self, value):
        """
        Check if the object is equal to the specified value.
        """
        return self.obj == value

    def _is_in(self, *values):
        """
        Check if the object is in a collection of values.
        """
        return self.obj in values

    def _greater_than(self, value):
        """
        Check if the object is greater than the specified value.
        """
        return self.obj > value

    def _less_than(self, value):
        """
        Check if the object is less than the specified value.
        """
        return self.obj < value

    def _greater_or_equal_than(self, value):
        """
        Check if the object is greater than or equal to the specified value.
        """
        return self.obj >= value

    def _less_or_equal_than(self, value):
        """
        Check if the object is less than or equal to the specified value.
        """
        return self.obj <= value

    def _min(self, value):
        """
        Check if the object is greater than or equal to the specified minimum value.
        """
        return self._greater_or_equal_than(value)

    def _max(self, value):
        """
        Check if the object is less than or equal to the specified maximum value.
        """
        return self._less_or_equal_than(value)

    def _between(self, min_vl, max_vl):
        """
        Check if the object is within the specified range.
        """
        return self._min(min_vl) and self._max(max_vl)

    def _is_true(self):
        """
        Check if the object is a boolean and has a value of True.
        """
        return self._is_bool() and self.obj is True

    def _is_false(self):
        """
        Check if the object is a boolean and has a value of False.
        """
        return self._is_bool() and self.obj is False

    def _contains_at_least(self, value):
        """
        Check if the object (assumed to be iterable) contains at least the specified number of elements.
        """
        return len(self.obj) >= value

    def _contains_at_most(self, value):
        """
        Check if the object (assumed to be iterable) contains at most the specified number of elements.
        """
        return len(self.obj) <= value

    def _contains_exactly(self, value):
        """
        Check if the object (assumed to be iterable) contains exactly the specified number of elements.
        """
        return len(self.obj) == value

    def _is_none(self):
        """
        Check if the object is None.
        """
        return self.obj is None

    def _has_unique_values(self):
        """
        Check if the object (assumed to be iterable) contains unique values.

        Note: This function assumes that the object's elements are hashable.
        """
        return len(self.obj) == len(set(self.obj))
