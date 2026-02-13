import inspect

from fluent_validator import functions as ValidatorFns
from fluent_validator.validator import Validator
from fluent_validator.validator_spec import ValidatorSpec


def test_all_validator_methods_available_in_spec():
    validators = {m_name for m_name in dir(ValidatorFns) if m_name.startswith(("is_", "has_", "contains_"))}
    missing_methods = validators - set(dir(ValidatorSpec))
    assert not missing_methods, f"ValidatorSpec is missing methods: {missing_methods}"


def test_all_validator_methods_available_in_builder():
    validators = {m_name for m_name in dir(ValidatorFns) if m_name.startswith(("is_", "has_", "contains_"))}
    missing_methods = validators - set(dir(Validator))
    assert not missing_methods, f"Validator is missing methods: {missing_methods}"


def test_builder_methods_has_same_signature_as_spec():
    spec_methods = {m_name for m_name in dir(ValidatorSpec) if not m_name.startswith("_")}
    common_methods = spec_methods & set(dir(Validator))
    invalid_methods = []
    for method_name in common_methods:
        spec_method = getattr(ValidatorSpec, method_name)
        builder_method = getattr(Validator, method_name)

        spec_signature = dict(inspect.signature(spec_method).parameters)
        spec_signature.pop("self", None)
        builder_signature = dict(inspect.signature(builder_method).parameters)
        builder_signature.pop("cls", None)

        if spec_signature != builder_signature:
            invalid_methods.append(method_name)

    assert not invalid_methods, f"Methods with different signatures: {invalid_methods}"


def test_builder_has_all_spec_methods():
    ignore_methods = {
        "from_validations",
        "validate",
        "validate_each",
        "validations",
        "describe",
    }
    spec_methods = {m_name for m_name in dir(ValidatorSpec) if not m_name.startswith("_")}
    missing_methods = spec_methods - set(dir(Validator)) - ignore_methods
    assert not missing_methods, f"Validator is missing methods: {missing_methods}"
