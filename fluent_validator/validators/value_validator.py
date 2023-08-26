from fluent_validator.validators.type_validator import TypeValidator


class ValueValidator(TypeValidator):
    def _equal(self, value):
        """
        Check if the object is equal to the specified value.

        Args:
            value: The value to compare with.
        """
        return self.obj == value

    def _is_in(self, *args):
        """
        Check if the object is in a collection of values.

        Args:
            *args: Values to check for containment.
        """
        return self.obj in args

    def _greater_than(self, value):
        """
        Check if the object is greater than the specified value.

        Args:
            value: The value to compare with.
        """
        return self.obj > value

    def _less_than(self, value):
        """
        Check if the object is less than the specified value.

        Args:
            value: The value to compare with.
        """
        return self.obj < value

    def _greater_or_equal_than(self, value):
        """
        Check if the object is greater than or equal to the specified value.

        Args:
            value: The value to compare with.
        """
        return self.obj >= value

    def _less_or_equal_than(self, value):
        """
        Check if the object is less than or equal to the specified value.

        Args:
            value: The value to compare with.
        """
        return self.obj <= value

    def _min(self, value):
        """
        Check if the object is greater than or equal to the specified minimum value.

        Args:
            value: The minimum value to compare with.
        """
        return self._greater_or_equal_than(value)

    def _max(self, value):
        """
        Check if the object is less than or equal to the specified maximum value.

        Args:
            value: The maximum value to compare with.
        """
        return self._less_or_equal_than(value)

    def _between(self, min, max):
        """
        Check if the object is within the specified range.

        Args:
            min: The minimum value of the range.
            max: The maximum value of the range.
        """
        return self._min(min) and self._max(max)

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

        Args:
            value: The minimum number of elements to check for.
        """
        return len(self.obj) >= value

    def _contains_at_most(self, value):
        """
        Check if the object (assumed to be iterable) contains at most the specified number of elements.

        Args:
            value: The maximum number of elements to check for.
        """
        return len(self.obj) <= value

    def _contains_exactly(self, value):
        """
        Check if the object (assumed to be iterable) contains exactly the specified number of elements.

        Args:
            value: The exact number of elements to check for.
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
