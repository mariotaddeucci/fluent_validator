from fluent_validator.validators.validator_fns import ValidatorFns
from fluent_validator.validators.validator_spec import ValidatorSpec

def test_all_validator_methods_available_in_spec():
    validators = {m_name for m_name in dir(ValidatorFns) if not m_name.startswith("_")}
    missing_methods = validators - set(dir(ValidatorSpec))
    assert not missing_methods, f"ValidatorSpec is missing methods: {missing_methods}"