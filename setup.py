from setuptools import setup

long_description = """
# Fluent Validator

Package to validate data in a fluent way
"""

setup(
    name="fluent_validator",
    version="{{VERSION_PLACEHOLDER}}",
    author="Mario Taddeuci",
    author_email="mariotaddeucci@gmx.com",
    description="Package to validate data in a fluent way",
    url="https://github.com/mariotaddeucci/fluent_validator",
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=["fluent_validator"],
    install_requires=[],
    keywords=["validator", "check", "fluent", "assert"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
