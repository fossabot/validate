# validate

[![Build Status](https://travis-ci.org/datacamp/validate.svg?branch=master)](https://travis-ci.org/datacamp/validate)
[![codecov](https://codecov.io/gh/datacamp/validate/branch/master/graph/badge.svg)](https://codecov.io/gh/datacamp/validate)
<!-- [![PyPI version](https://badge.fury.io/py/validate.svg)](https://badge.fury.io/py/validate) -->

Test DataCamp exercises you have locally against the exercise validator.

## Installation

You need Python 3 to use this package.

```
pip install git+https://github.com/datacamp/validate.git
```

## Demo

You can use the validate package from the command line:

```
$ cd <root_of_course_repo>

$ # test entire chapter1.md
$ testch <course_id> <path_to_chapter_file>

$ # test specific exercise of chapter
$ testch <course_id> <path_to_chapter_file> -k <ex_key>
```

## Testing

```
pip install -r requirements.txt
pip install -e .
pytest
```
