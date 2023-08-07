from fluent_validator.validators.value_validator import ValueValidator
from functools import wraps

class Validator(ValueValidator):

    def __getattr__(self, fn_name):
        is_negative = fn_name.startswith("not_")
        validation_name = fn_name[3:] if is_negative else f"_{fn_name}"

        if validation_name not in dir(self):
            raise NotImplementedError(f"{validation_name} is not implemented")

        def wrapper(*args, **kwargs):
            result = getattr(self, validation_name)(*args, **kwargs)
            result = not result if is_negative else result
            if result:
                return self
            
            raise ValueError(f"{self.identifier} does not match criteria for {fn_name}")
        
        return wrapper

@wraps(Validator.__init__)
def validate(*args, **kwargs):
    return Validator(*args, **kwargs)
