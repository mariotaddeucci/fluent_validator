class BaseValidator:
    def __init__(self, obj, identifier=None):
        self.obj = obj
        self.identifier = identifier or obj
