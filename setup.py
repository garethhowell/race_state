#!/usr/bin/env python

"""The setup script."""

import os

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

the_lib_folder = os.path.dirname(os.path.realpath(__file__))
requirement_path = the_lib_folder + 'requirements.txt'
install_requires = []
if os.path.isfile(requirement_path):
    with open(requirement_path) as f:
        install_requires = f.read().splitlines()

test_requirements = ['pytest>=3', ]

setup(
    author="Gareth Howell",
    author_email='gareth.howell@gmail.com',
    python_requires='>=3.9',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.9',
    ],
    description="A python package to get the status of a current motor race and update a status select in Home Assistant.",
    entry_points={
        'console_scripts': [
            'race_state=race_state.cli:main',
        ],
    },
    install_requires=install_requires,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='race_state',
    name='race_state',
    packages=find_packages(include=['race_state', 'race_state.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/garethhowell/race_state',
    version='0.2.0',
    zip_safe=False,
)
