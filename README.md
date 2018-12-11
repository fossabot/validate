# validate

[![Build Status](https://travis-ci.org/datacamp/validate.svg?branch=master)](https://travis-ci.org/datacamp/validate)
[![codecov](https://codecov.io/gh/datacamp/validate/branch/master/graph/badge.svg)](https://codecov.io/gh/datacamp/validate)
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fdatacamp%2Fvalidate.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fdatacamp%2Fvalidate?ref=badge_shield)
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
$ validate <course_id> <path_to_chapter_file>

$ # test specific exercise of chapter
$ validate <course_id> <path_to_chapter_file> -k <ex_key>
```

## Testing

```
pip install -r requirements.txt
pip install -e .
pytest
```


## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fdatacamp%2Fvalidate.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fdatacamp%2Fvalidate?ref=badge_large)