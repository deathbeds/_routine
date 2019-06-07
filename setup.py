#!/usr/bin/env python
# coding: utf-8

# Standard Library
from pathlib import Path

import setuptools

package_name = "COROUTINE"
name = "_routine"

__version__ = None


file = Path(globals().get("__file__", "setup.py"))


package_dir = {"": str(file.parent / "src")}

__name__ == "__main__" and setuptools.setup(
    name=package_name,
    version="0.1.0",
    author="deathbeds",
    author_email="tony.fast@gmail.com",
    description="A decentralized approach to blogging, testing, and documentation.",
    url="https://github.com/deathbeds/_routine",
    python_requires=">=3.6",
    license="BSD-3-Clause",
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "hypothesis", "nbval"],
    install_requires=[],
    include_package_data=True,
    packages=list(filter(bool, package_dir)),
    package_dir=package_dir,
    entry_points={"pytest11": []},
    classifiers=(
        "Development Status :: 4 - Beta",
        "Framework :: IPython",
        "Framework :: Jupyter",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
    ),
    zip_safe=False,
)
# !jupyter nbconvert --to python --TemplateExporter.exclude_input_prompt=True setup.ipynb
# !black setup.py
# !isort setup.py
# !source activate p6 && python setup.py develop
#
