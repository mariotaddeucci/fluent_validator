from typing import Iterable
from fluent_validator.validators.base_validator import BaseValidator

class TypeValidator(BaseValidator):
    
    def _is_instance(self, *args) -> bool:
        return isinstance(self.obj, args)

    def _is_callable(self) -> bool:
        return callable(self.obj)
    
    def _is_iterable(self) -> bool:
        return self._is_instance(Iterable)

    def _is_string(self) -> bool:
        return self._is_instance(str)

    def _is_number(self) -> bool:
        return self._is_instance(int, float)
    
    def _is_bool(self) -> bool:
        return self._is_instance(bool)
    