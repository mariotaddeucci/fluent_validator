---
applyTo: "src/fluent_validator/validators/**/*.py,tests/validators/**/*.py"
description: "Rules for implementing validators in Fluent Validator (Python)."
name: "Fluent Validator - Python Validators Rules"
---

Follow these strict rules when creating validators:

1. ValidatorFns
- Implement validation logic only in `ValidatorFns`.
- Implement ONLY positive checks (e.g., `is_none`, NOT `is_not_none`).
- Keep methods static and composable.

2. ValidatorSpec
- Map each function from `ValidatorFns` to a `ValidatorSpec`.
- Error messages MUST use format placeholders for parameters (e.g., "Value must be greater than {threshold}").
- ALWAYS implement the negative version in `ValidatorSpec` (e.g., `is_not_none` for `is_none`).

3. ValidatorBuilder
- Expose validators through `ValidatorBuilder`.
- Provide BOTH positive and negative versions.

4. Tests (MANDATORY)
- Create tests in `tests/validators`.
- File name: `test_<positive_validator>.py`
  - Example: `is_none` → `test_is_none.py`
- Test BOTH positive and negative validators.
- Use `strategy="return_result"` in assertions.
- Cover:
  - Valid cases
  - Invalid cases
  - Edge cases
  - Error message formatting (when applicable)

Example pattern:

from fluent_validator.validators import ValidatorBuilder as vb

def test_is_example():
    value = ...

    validator_positive = vb.is_example(...)
    validator_negative = vb.is_not_example(...)

    assert validator_positive.validate(value, strategy="return_result") is True
    assert validator_negative.validate(value, strategy="return_result") is False

Do not:
- Implement negative logic inside `ValidatorFns`.
- Skip negative specs.
- Skip test coverage.