import ast
import glob
import os

TEMPLATE = """
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
{{ validation_list }}

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have questions about `fluent_validator`, please feel free to [open an issue](https://github.com/mariotaddeucci/fluent_validator/issues). We're here to help!

Happy Validating! 🚀
"""


def extract_validators_docs(filename):
    with open(filename, "r", encoding="utf-8") as file:
        tree = ast.parse(file.read())

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            docstring = ast.get_docstring(node)
            if docstring:
                docstring = [
                    line.strip() for line in docstring.split("\n") if line.strip() != ""
                ]
                docstring = " ".join(docstring)

                method_name = node.name.strip("_")
                args = [arg.arg for arg in node.args.args if arg.arg != "self"]
                yield f"| `{method_name}({', '.join(args)})` | {docstring} |"


def main():
    project_dir = os.path.join(os.path.dirname(__file__), "..")
    validators_dir = os.path.join(project_dir, "fluent_validator", "validators")
    output_file = os.path.join(project_dir, "README.md")

    validations_list = [
        validator_doc.strip()
        for file in glob.glob(os.path.join(validators_dir, "*.py"))
        for validator_doc in extract_validators_docs(file)
    ]

    content = TEMPLATE.replace(
        "{{ validation_list }}", "\n".join(sorted(validations_list))
    )

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(content)


if __name__ == "__main__":
    main()
