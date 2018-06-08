# validate

[![Build Status](https://travis-ci.org/datacamp/validate.svg?branch=master)](https://travis-ci.org/datacamp/validate)
[![codecov](https://codecov.io/gh/datacamp/validate/branch/master/graph/badge.svg)](https://codecov.io/gh/datacamp/validate)
<!-- [![PyPI version](https://badge.fury.io/py/validate.svg)](https://badge.fury.io/py/validate) -->

Test DataCamp exercises you have locally against the exercise validator

## Installation

```
pip install git+https://github.com/datacamp/validate.git
```

## Demo

```
testch 
```

## Testing

```
pip install -e .
pytest
```

## LOCAL DEV

```python
from validate.command_line import another_function
another_function(672, 'chapter1.md', None)
```