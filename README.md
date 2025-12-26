
# fluent_validator

**Validate Your Data with Ease!**

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PyPI version](https://badge.fury.io/py/fluent-validator.svg)](https://badge.fury.io/py/fluent-validator)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/fluent-validator)](https://pypi.org/project/fluent-validator/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/fluent-validator.svg)](https://pypi.org/project/fluent-validator/)
[![GitHub stars](https://img.shields.io/github/stars/mariotaddeucci/fluent_validator.svg?style=flat-square)](https://github.com/mariotaddeucci/fluent_validator/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/mariotaddeucci/fluent_validator.svg?style=flat-square)](https://github.com/mariotaddeucci/fluent_validator/network)
[![GitHub license](https://img.shields.io/github/license/mariotaddeucci/fluent_validator.svg?style=flat-square)](https://github.com/mariotaddeucci/fluent_validator/blob/main/LICENSE)

## Overview

`fluent_validator` is a Python package that makes data validation a breeze! Say goodbye to complex, nested if statements and hello to a fluent and expressive way to validate your data. With `fluent_validator`, you can easily define and execute validation rules for your data in a clean and readable manner.

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Available Validations](#available-validations)
- [License](#license)
- [Support](#support)


## Features

- **Fluent Syntax**: Define validation rules in a clean and fluent manner.
- **Custom Error Messages**: Provide custom error messages for any validation method.
- **No Extra Dependencies**: `fluent_validator` is lightweight and doesn't require any additional packages.
- **Python 3.7+ Support**: It works seamlessly with Python versions 3.7, 3.8, 3.9, 3.10, and 3.11.
- **Type Hints**: Full type hint support with Pyrefly type checking.
- **Extensive Validation Library**: Check out our extensive list of available validations to cover all your validation needs.

## Installation

You can install `fluent_validator` using pip:

```bash
pip install fluent-validator
```

### Development Installation

For development with type checking and linting tools:

```bash
pip install -r dev-requirements.txt
```

This includes:
- `pytest` for testing
- `pyrefly` for fast type checking
- `black` for code formatting
- `isort` for import sorting
- `pre-commit` for git hooks

## Usage

Here's a quick example of how to use `fluent_validator`:

```python
from fluent_validator import validate, validate_all

# Validate a single value (old style - still supported for backward compatibility)
validate(10).not_is_none().greater_than(5).not_equal(40)

# New semantic style (more readable)
validate(10).is_not_none().greater_than(5).is_not_equal(40)

# Or validate multiple values
validate_all(10, 100).is_not_none().greater_than(5).is_not_equal(40)

# Check if values are empty or not
validate([]).is_empty()
validate("hello").is_not_empty()
```

### Custom Error Messages

You can provide custom error messages for any validation by using the `message` parameter:

```python
from fluent_validator import validate

# Custom message for a single validation
validate(15).greater_than(18, message="Age must be greater than 18")
# Raises: ValueError: Age must be greater than 18

# Custom messages work with all validation methods
validate(None).is_not_none(message="Value cannot be None")
validate("hello").is_number(message="Expected a number, got a string")

# Custom messages in validation chains
validate(5).is_not_none().is_number().greater_than(10, message="Value must be greater than 10")

# Custom messages with validate_all
validate_all(5, 15, 20).greater_than(10, message="All values must be greater than 10")
```

## Available Validations

`fluent_validator` offers a wide range of validations to suit your needs.

Notably, all validations have a corresponding negative form using **two styles**:

1. **Old style** (for backward compatibility): Prefix with `not_` - e.g., `not_is_none()`, `not_equal()`
2. **New semantic style** (recommended): Use `is_not_*` methods - e.g., `is_not_none()`, `is_not_equal()`

Both styles are fully supported and can be mixed in the same validation chain.

### Check out the full list of available above.

| Validation | Description | Semantic Negative |
| --- | --- | --- |
| `between(min_vl, max_vl)` | Check if the object is within the specified range. | - |
| `contains_at_least(value)` | Check if the object (assumed to be iterable) contains at least the specified number of elements. | - |
| `contains_at_most(value)` | Check if the object (assumed to be iterable) contains at most the specified number of elements. | - |
| `contains_exactly(value)` | Check if the object (assumed to be iterable) contains exactly the specified number of elements. | - |
| `equal(value)` | Check if the object is equal to the specified value. | `is_not_equal(value)` |
| `greater_or_equal_than(value)` | Check if the object is greater than or equal to the specified value. | - |
| `greater_than(value)` | Check if the object is greater than the specified value. | - |
| `has_unique_values()` | Check if the object (assumed to be iterable) contains unique values. Note: This function assumes that the object's elements are hashable. | - |
| `is_bool()` | Check if the object is a boolean. | `is_not_bool()` |
| `is_callable()` | Check if the object is callable (e.g., a function or method). | `is_not_callable()` |
| `is_empty()` | Check if the object is empty (length is 0 or is None). | `is_not_empty()` |
| `is_false()` | Check if the object is a boolean and has a value of False. | `is_not_false()` |
| `is_in()` | Check if the object is in a collection of values. | `is_not_in()` |
| `is_instance()` | Check if the object is an instance of one or more specified types. | `is_not_instance()` |
| `is_iterable()` | Check if the object is iterable. | `is_not_iterable()` |
| `is_none()` | Check if the object is None. | `is_not_none()` |
| `is_number()` | Check if the object is a number (int or float). | `is_not_number()` |
| `is_string()` | Check if the object is a string. | `is_not_string()` |
| `is_true()` | Check if the object is a boolean and has a value of True. | `is_not_true()` |
| `less_or_equal_than(value)` | Check if the object is less than or equal to the specified value. | - |
| `less_than(value)` | Check if the object is less than the specified value. | - |
| `max(value)` | Check if the object is less than or equal to the specified maximum value. | - |
| `min(value)` | Check if the object is greater than or equal to the specified minimum value. | - |

## Development

### Project Structure

The project follows the `src` layout for better organization:

```
fluent_validator/
├── src/
│   └── fluent_validator/      # Main package code
│       ├── __init__.py
│       ├── validator.py
│       └── validators/
│           ├── __init__.py
│           ├── base_validator.py
│           ├── type_validator.py
│           └── value_validator.py
├── tests/                     # Test files
├── dev-requirements.txt       # Development dependencies
├── pyrefly.toml              # Pyrefly type checker configuration
└── .pre-commit-config.yaml   # Pre-commit hooks
```

### Type Checking

This project uses [Pyrefly](https://github.com/facebook/pyrefly), a fast Python type checker, to ensure type safety:

```bash
# Run type checking
pyrefly check src/
```

### Running Tests

```bash
# Install test dependencies
pip install -r requirements.txt

# Run all tests
pytest

# Run tests with coverage
pytest --cov=fluent_validator
```

### Code Quality

We use pre-commit hooks to maintain code quality:

```bash
# Install pre-commit hooks
pre-commit install

# Run pre-commit on all files
pre-commit run --all-files
```

The pre-commit hooks include:
- `black` for code formatting
- `isort` for import sorting
- `pyrefly` for type checking
- Various other checks for code quality

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have questions about `fluent_validator`, please feel free to [open an issue](https://github.com/mariotaddeucci/fluent_validator/issues). We're here to help!

Happy Validating! 🚀
