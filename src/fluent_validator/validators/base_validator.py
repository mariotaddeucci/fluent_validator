from typing import Any, Generic, TypeVar, Optional

T = TypeVar('T')


class BaseValidator(Generic[T]):
    def __init__(self, obj: T, identifier: Optional[Any] = None) -> None:
        self.obj = obj
        self.identifier: Any = identifier or obj
