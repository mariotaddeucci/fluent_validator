from typing import Generic, TypeVar

T = TypeVar('T')


class BaseValidator(Generic[T]):
    def __init__(self, obj: T, identifier=None):
        self.obj = obj
        self.identifier = identifier or obj
