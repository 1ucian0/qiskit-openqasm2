# This code is part of Qiskit.
#
# (C) Copyright IBM 2017.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"The Qiskit OpenQASM2 setup file."

import os
from setuptools import setup, find_packages


REQUIREMENTS = [
    "contextvars>=2.4;python_version<'3.7'",
    "jsonschema>=2.6",
    "networkx>=2.2",
    "retworkx>=0.5.0",
    "numpy>=1.17",
    "ply>=3.10",
    "psutil>=5",
    "scipy>=1.4",
    "sympy>=1.3",
    "dill>=0.3",
    "fastjsonschema>=2.10",
    "python-constraint>=1.4",
    "python-dateutil>=2.8.0",
]

# Read long description from README.
README_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                           'README.md')
with open(README_PATH) as readme_file:
    README = readme_file.read()

setup(
    name="qiskit-openqasm2",
    version="0.16.0",
    description="Software for developing quantum computing programs",
    long_description=README,
    long_description_content_type='text/markdown',
    url="https://github.com/Qiskit/qiskit-terra",
    author="Qiskit Development Team",
    author_email="hello@qiskit.org",
    license="Apache 2.0",
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering",
    ],
    keywords="qiskit sdk quantum",
    packages=find_packages(exclude=['test*']),
    install_requires=REQUIREMENTS,
    include_package_data=True,
    python_requires=">=3.6",
    extras_require={
        'visualization': ['matplotlib>=2.1', 'ipywidgets>=7.3.0',
                          'pydot', "pillow>=4.2.1", "pylatexenc>=1.4",
                          "seaborn>=0.9.0", "pygments>=2.4"],
        'full-featured-simulators': ['qiskit-aer>=0.1'],
        'crosstalk-pass': ['z3-solver>=4.7'],
    },
    project_urls={
        "Bug Tracker": "https://github.com/Qiskit/qiskit-terra/issues",
        "Documentation": "https://qiskit.org/documentation/",
        "Source Code": "https://github.com/Qiskit/qiskit-terra",
    },
    zip_safe=False
)
