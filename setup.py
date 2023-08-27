import codecs
import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name="fluent_validator",
    version="{{VERSION_PLACEHOLDER}}",
    author="Mario Taddeuci",
    author_email="mariotaddeucci@gmx.com",
    description="Package to validate data in a fluent way",
    url="https://github.com/mariotaddeucci/fluent_validator",
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=["fluent_validator", "fluent_validator.validators"],
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
