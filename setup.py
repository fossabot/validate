#!/usr/bin/env python

import re
import ast
from os import path
from setuptools import setup

_version_re = re.compile(r'__version__\s+=\s+(.*)')

PACKAGE_NAME = 'validate'
HERE = path.abspath(path.dirname(__file__))
with open(path.join(HERE, 'README.md'), encoding='utf-8') as fp:
    README = fp.read()
with open(path.join(HERE, PACKAGE_NAME, '__init__.py'), 'rb') as fp:
    VERSION = str(ast.literal_eval(_version_re.search(
        fp.read().decode('utf-8')).group(1)))

setup(
	name=PACKAGE_NAME,
	version=VERSION,
	packages=['validate'],
	install_requires=['requests'],
    entry_points = {
        'console_scripts': ['testch=validate.command_line:main'],
    },
    description = 'Test DataCamp exercises you have locally against the exercise validator',
    long_description=README,
    long_description_content_type='text/markdown',
    license='GNU version 3',
    author='Filip Schouwenaars',
    author_email='filip@datacamp.com',
    url = 'https://github.com/datacamp/validate')
