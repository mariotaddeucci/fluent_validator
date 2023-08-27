
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
- **No Extra Dependencies**: `fluent_validator` is lightweight and doesn't require any additional packages.
- **Python 3.7+ Support**: It works seamlessly with Python versions 3.7, 3.8, 3.9, 3.10, and 3.11.
- **Extensive Validation Library**: Check out our extensive list of available validations to cover all your validation needs.

## Installation

You can install `fluent_validator` using pip:

```bash
pip install fluent-validator
````

## Usage

Here's a quick example of how to use `fluent_validator`:

```python
from fluent_validator import validate, validate_all

# Validate a single value
validate(10).not_is_none().greater_than(5).not_equal(40)

# Or validate multiple values
validate_all(10, 100).not_is_none().greater_than(5).not_equal(40)
```

## Available Validations

`fluent_validator` offers a wide range of validations to suit your needs.

Notably, all validations have a corresponding negative form. Simply prefix the method with `not_`.

For example, the negative of `is_none()` is `not_is_none()`.

### Check out the full list of available above.

| Validation | Description |
| --- | --- |
| `between(min_vl, max_vl)` | Check if the object is within the specified range. |
| `contains_at_least(value)` | Check if the object (assumed to be iterable) contains at least the specified number of elements. |
| `contains_at_most(value)` | Check if the object (assumed to be iterable) contains at most the specified number of elements. |
| `contains_exactly(value)` | Check if the object (assumed to be iterable) contains exactly the specified number of elements. |
| `equal(value)` | Check if the object is equal to the specified value. |
| `greater_or_equal_than(value)` | Check if the object is greater than or equal to the specified value. |
| `greater_than(value)` | Check if the object is greater than the specified value. |
| `has_unique_values()` | Check if the object (assumed to be iterable) contains unique values. Note: This function assumes that the object's elements are hashable. |
| `is_bool()` | Check if the object is a boolean. |
| `is_callable()` | Check if the object is callable (e.g., a function or method). |
| `is_false()` | Check if the object is a boolean and has a value of False. |
| `is_in()` | Check if the object is in a collection of values. |
| `is_instance()` | Check if the object is an instance of one or more specified types. |
| `is_iterable()` | Check if the object is iterable. |
| `is_none()` | Check if the object is None. |
| `is_number()` | Check if the object is a number (int or float). |
| `is_string()` | Check if the object is a string. |
| `is_true()` | Check if the object is a boolean and has a value of True. |
| `less_or_equal_than(value)` | Check if the object is less than or equal to the specified value. |
| `less_than(value)` | Check if the object is less than the specified value. |
| `max(value)` | Check if the object is less than or equal to the specified maximum value. |
| `min(value)` | Check if the object is greater than or equal to the specified minimum value. |

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have questions about `fluent_validator`, please feel free to [open an issue](https://github.com/mariotaddeucci/fluent_validator/issues). We're here to help!

Happy Validating! 🚀
