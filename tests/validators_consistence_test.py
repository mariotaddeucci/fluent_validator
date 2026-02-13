from fluent_validator.validators.validator_fns import ValidatorFns
from fluent_validator.validators.validator_spec import ValidatorSpec
from fluent_validator.validators.validator_builder import ValidatorBuilder
import inspect
def test_all_validator_methods_available_in_spec():
    validators = {m_name for m_name in dir(ValidatorFns) if not m_name.startswith("_")}
    missing_methods = validators - set(dir(ValidatorSpec))
    assert not missing_methods, f"ValidatorSpec is missing methods: {missing_methods}"

def test_all_validator_methods_available_in_builder():
    validators = {m_name for m_name in dir(ValidatorFns) if not m_name.startswith("_")}
    missing_methods = validators - set(dir(ValidatorBuilder))
    assert not missing_methods, f"ValidatorBuilder is missing methods: {missing_methods}"

def test_builder_methods_has_same_signature_as_spec():
    spec_methods = {m_name for m_name in dir(ValidatorSpec) if not m_name.startswith("_")}
    common_methods = spec_methods  & set(dir(ValidatorBuilder))
    invalid_methods = []
    for method_name in common_methods:
        spec_method = getattr(ValidatorSpec, method_name)
        builder_method = getattr(ValidatorBuilder, method_name)

        spec_signature = dict(inspect.signature(spec_method).parameters)
        spec_signature.pop("self", None)  # Remove 'self' from spec signature for comparison
        builder_signature = dict(inspect.signature(builder_method).parameters)
        builder_signature.pop("cls", None)  # Remove 'cls' from builder signature for comparison

        if spec_signature != builder_signature:
            print(f"Method {method_name} has different signatures:")
            print(f"  ValidatorSpec: {spec_signature}")
            print(f"  ValidatorBuilder: {builder_signature}")
            invalid_methods.append(method_name)

    assert not invalid_methods, f"Methods with different signatures: {invalid_methods}"
