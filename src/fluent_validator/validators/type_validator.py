from typing import Iterable, Any

from fluent_validator.validators.base_validator import BaseValidator


class TypeValidator(BaseValidator):
    def _is_instance(self, *args: type) -> bool:
        """
        Check if the object is an instance of one or more specified types.
        """

        return isinstance(self.obj, args)

    def _is_callable(self) -> bool:
        """
        Check if the object is callable (e.g., a function or method).
        """
        return callable(self.obj)

    def _is_iterable(self) -> bool:
        """
        Check if the object is iterable.
        """
        return self._is_instance(Iterable)

    def _is_string(self) -> bool:
        """
        Check if the object is a string.
        """
        return self._is_instance(str)

    def _is_number(self) -> bool:
        """
        Check if the object is a number (int or float).
        """
        return self._is_instance(int, float)

    def _is_bool(self) -> bool:
        """
        Check if the object is a boolean.
        """
        return self._is_instance(bool)

    # Semantic negative methods
    def _is_not_instance(self, *args: type) -> bool:
        """
        Check if the object is not an instance of one or more specified types.
        """
        return not self._is_instance(*args)

    def _is_not_callable(self) -> bool:
        """
        Check if the object is not callable.
        """
        return not self._is_callable()

    def _is_not_iterable(self) -> bool:
        """
        Check if the object is not iterable.
        """
        return not self._is_iterable()

    def _is_not_string(self) -> bool:
        """
        Check if the object is not a string.
        """
        return not self._is_string()

    def _is_not_number(self) -> bool:
        """
        Check if the object is not a number.
        """
        return not self._is_number()

    def _is_not_bool(self) -> bool:
        """
        Check if the object is not a boolean.
        """
        return not self._is_bool()
