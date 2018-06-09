#!/usr/bin/env python

import re
import ast
from os import path
from setuptools import setup

_version_re = re.compile(r'__version__\s+=\s+(.*)')

HERE = path.abspath(path.dirname(__file__))
with open(path.join(HERE, 'README.md'), encoding='utf-8') as fp:
    README = fp.read()
with open(path.join(HERE, 'validate.py'), 'rb') as fp:
    VERSION = str(ast.literal_eval(_version_re.search(
        fp.read().decode('utf-8')).group(1)))

setup(
	name='validate',
	version=VERSION,
	py_modules= ['validate'],
	install_requires=['requests'],
    entry_points = {
        'console_scripts': ['validate=validate:main'],
    },
    description = 'Test DataCamp exercises you have locally against the exercise validator',
    long_description=README,
    long_description_content_type='text/markdown',
    license='GNU version 3',
    author='Filip Schouwenaars',
    author_email='filip@datacamp.com',
    url = 'https://github.com/datacamp/validate')
