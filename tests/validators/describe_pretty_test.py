from fluent_validator.validators import ValidatorBuilder as vb
from fluent_validator.validators import ValidatorSpec


def test_describe_pretty_empty():
    validator = ValidatorSpec()
    assert validator.describe(pretty=True) == "No validations"


def test_describe_pretty_single_validator():
    validator = vb.is_number()
    assert validator.describe(pretty=True) == "'Should be a number (rule: is_number)'"


def test_describe_pretty_and_chain():
    validator = vb.is_number().is_string()

    expected = "'Should be a number (rule: is_number)'\nAND 'Should be a string (rule: is_string)'"
    assert validator.describe(pretty=True) == expected


def test_describe_pretty_or_combination():
    validator = vb.is_number() | vb.is_string()

    expected = (
        "(\n"
        "    'Should be a number (rule: is_number)'\n"
        "    OR\n"
        "    'Should be a string (rule: is_string)'\n"
        ")"
    )
    assert validator.describe(pretty=True) == expected


def test_describe_pretty_not():
    validator = -vb.is_number()
    assert validator.describe(pretty=True) == "not 'Should be a number (rule: is_number)'"


def test_describe_pretty_complex_and_or_not():
    validator = (vb.is_number().is_between(10, 20) | vb.is_none()) & -vb.is_string()

    expected = (
        "(\n"
        "    (\n"
        "        'Should be a number (rule: is_number)' AND\n"
        "        'Should be between 10 and 20 (closed='both') (rule: is_between)'\n"
        "    )\n"
        "    OR\n"
        "    'Should be None (rule: is_none)'\n"
        ")\n"
        "AND not 'Should be a string (rule: is_string)'"
    )
    assert validator.describe(pretty=True) == expected


def test_describe_pretty_not_compound():
    validator = -vb.is_number().is_string()

    expected = (
        "not (\n"
        "    'Should be a number (rule: is_number)' AND\n"
        "    'Should be a string (rule: is_string)'\n"
        ")"
    )
    assert validator.describe(pretty=True) == expected


def test_describe_pretty_nested_or():
    validator = (vb.is_number() | vb.is_string()) | vb.is_none()

    expected = (
        "(\n"
        "    (\n"
        "        'Should be a number (rule: is_number)'\n"
        "        OR\n"
        "        'Should be a string (rule: is_string)'\n"
        "    )\n"
        "    OR\n"
        "    'Should be None (rule: is_none)'\n"
        ")"
    )
    assert validator.describe(pretty=True) == expected


def test_describe_pretty_multiple_and():
    validator = vb.is_number().is_greater_than(0).is_less_than(100)

    expected = (
        "'Should be a number (rule: is_number)'\n"
        "AND 'Should be greater than 0 (rule: is_greater_than)'\n"
        "AND 'Should be less than 100 (rule: is_less_than)'"
    )
    assert validator.describe(pretty=True) == expected


def test_describe_pretty_does_not_affect_non_pretty():
    validator = (vb.is_number() | vb.is_none()) & -vb.is_string()

    non_pretty = validator.describe(pretty=False)
    assert "AND" in non_pretty
    assert "OR" in non_pretty


def test_describe_pretty_and_operator():
    validator = vb.is_number() & vb.is_string()

    expected = "'Should be a number (rule: is_number)'\nAND 'Should be a string (rule: is_string)'"
    assert validator.describe(pretty=True) == expected


def test_describe_pretty_not_inside_or():
    validator = -vb.is_number().is_string() | vb.is_none()

    expected = (
        "(\n"
        "    not (\n"
        "        'Should be a number (rule: is_number)' AND\n"
        "        'Should be a string (rule: is_string)'\n"
        "    )\n"
        "    OR\n"
        "    'Should be None (rule: is_none)'\n"
        ")"
    )
    assert validator.describe(pretty=True) == expected
