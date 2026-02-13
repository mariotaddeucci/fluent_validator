# fluent_validator

Fluent, composable data validation for Python — a simple, expressive API to build readable validation rules.

[![PyPI version](https://badge.fury.io/py/fluent-validator.svg)](https://badge.fury.io/py/fluent-validator)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/fluent-validator.svg)](https://pypi.org/project/fluent-validator/)

## Overview

`fluent_validator` makes it easy to declare validation rules in a fluent, composable way. Build reusable specifications with clear messages and combine them using logical operators.

- [Installation](#installation)
- [Quick start](#quick-start)
- [Combining validators](#combining-validators)
- [describe (document rules)](#describe-document-rules)
- [Available validations](#available-validations)
- [Validation strategies](#validation-strategies)
- [Quick API](#quick-api)

## Installation

Install from PyPI:

```bash
pip install fluent-validator
```

## Quick start

Basic usage examples:

```python
from fluent_validator import Validator, ValidationError

# build a composed specification
spec = (
    Validator.is_number()
    .is_greater_than(5)
    .is_less_than(20)
)

# validate (default: raise_after_first_error)
try:
    spec.validate(7)
    print("Valid")
except ValidationError as e:
    print("Invalid:", e)

# get boolean result without raising
is_valid = spec.validate(7, strategy="return_result")  # True/False

# validate each item of an iterable
list_spec = Validator.is_iterable().contains_at_least(2)
list_spec.validate_each([1, 2, 3], strategy="return_result")  # True
```

## Combining validators

Specifications can be combined with logical operators:

```python
# AND (concatenate validations)
a = Validator.is_number().is_gte(0)
b = Validator.is_number().is_lte(100)
combined = a & b
combined.validate(50)

# OR (at least one group must pass)
num_or_str = Validator.is_number() | Validator.is_string()
num_or_str.validate("abc", strategy="return_result")  # True

# Negation
not_none = ~Validator.is_none()
not_none.validate(None, strategy="return_result")  # False
```

## describe (document rules)


Each `ValidatorSpec` can render a textual description of the specification. Here's a more complex example combining `AND`, `OR` and negation:

```python
spec = (
    (Validator.is_number().is_between(10, 20) | Validator.is_none())
    & ~Validator.is_string()
)
print(spec.describe())
print(spec.describe(pretty=True))
```

Example output for `pretty=True`:

```
(
    (
        'Should be a number (rule: is_number)' AND
        'Should be between 10 and 20 (closed='both') (rule: is_between)'
    )
    OR
    'Should be None (rule: is_none)'
)
AND not 'Should be a string (rule: is_string)'
```

Use `describe()` to generate messages for logs, documentation, or custom error reporting.

## Available validations

Below is a table of validator builder functions and a short description of each.

| Function | Description |
|---|---|
| `is_instance_of(types)`<br>`is_not_instance_of(types)` | Checks the value is an instance of the provided types. |
| `is_callable()`<br>`is_not_callable()` | Checks the value is callable. |
| `is_iterable()`<br>`is_not_iterable()` | Checks the value is iterable. |
| `is_dataclass()`<br>`is_not_dataclass()` | Checks the value is a dataclass. |
| `is_string()`<br>`is_not_string()` | Checks the value is a string. |
| `is_number()`<br>`is_not_number()` | Checks the value is numeric (`int`, `float`, `Decimal`). |
| `is_bool()`<br>`is_not_bool()` | Checks the value is a boolean. |
| `is_none()`<br>`is_not_none()` | Checks the value is `None`. |
| `is_greater_than(value)` (`is_gt`)<br>`is_not_greater_than(value)` | Checks the value is greater than `value`. |
| `is_greater_or_equal(value)` (`is_gte`)<br>`is_not_greater_or_equal(value)` | Checks the value is greater than or equal to `value`. |
| `is_equal(value)` (`is_eq`)<br>`is_not_equal(value)` | Checks the value is equal to `value`. |
| `is_less_than(value)` (`is_lt`)<br>`is_not_less_than(value)` | Checks the value is less than `value`. |
| `is_less_or_equal(value)` (`is_lte`)<br>`is_not_less_or_equal(value)` | Checks the value is less than or equal to `value`. |
| `is_between(lower, upper, closed='both')`<br>`is_not_between(...)` | Checks the value is between `lower` and `upper` (closed/open according to `closed`). |
| `contains_at_least(n)`<br>`contains_at_most(n)`<br>`contains_exactly(n)` | Checks collection size (at least/at most/exactly `n` items). |
| `has_unique_values()` | Checks that values in a collection are unique. |
| `is_empty()`<br>`is_not_empty()` | Checks if the collection/value is empty. |
| `is_true()`<br>`is_not_true()`<br>`is_false()`<br>`is_not_false()` | Checks boolean `True`/`False` values. |
| `is_in(collection)`<br>`is_not_in(collection)` | Checks if the value is in `collection`. |
| `add_validation(fn, msg)`<br>`add_validations(list[(fn, msg)])` | Adds custom validations by providing functions and messages. |

See the function and class docstrings in the source for details and default messages.

## Validation strategies

The `validate` method accepts a `strategy` parameter:

- `raise_after_first_error` (default): raises `ValidationError` on the first failing rule.
- `raise_after_all_errors`: evaluates all rules and raises `ValidationError` with all messages joined.
- `return_result`: does not raise; returns `True` if the value passes all rules or `False` otherwise.

Use `validate_each` to validate every item in an iterable; errors include the failing item index when applicable.

## Quick API

Primary imports:

```python
from fluent_validator import Validator, ValidatorSpec, ValidationError
```

- `Validator` provides factory classmethods (e.g. `is_number()`, `is_string()`) returning configured `ValidatorSpec` instances.
- `ValidatorSpec` is the builder that lets you chain validations, combine specs with `&`, `|`, negate with unary `-`, and call `describe()` / `validate()`.

## License

MIT License — see [LICENSE](LICENSE).

## Support

Open an issue: https://github.com/mariotaddeucci/fluent_validator/issues

Happy validating! 🚀
