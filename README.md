## django-pg-utils
Utility methods for Django + PostgreSQL applications

[![PyPI version](https://badge.fury.io/py/django-pg-utils.svg)](https://badge.fury.io/py/django-pg-utils)
[![Build Status](https://travis-ci.org/hypertrack/django-pg-utils.svg?branch=master)](https://travis-ci.org/hypertrack/django-pg-utils)

### What is this?
The utils module provides custom query expressions for Django, built on top of PostgreSQL functions. These can be used as a part of update, create, filter, order by, annotation, or aggregate. As with all query expressions, the computations leverage capabilities of the database, instead of loading data in the Django application.

### Usage
```
pip install django-pg-utils
```

```
from pg_utils import DateTZ, divide

queryset.annotate(created_date=DateTZ(F('created_at'), 'Asia/Kolkata')
queryset.annotate(speed=divide(F('distance'), F('time')))
```

| Query expression | Use case                                                      |
|------------------|---------------------------------------------------------------|
| Date             | Cast datetime field into date                                 |
| DateTZ           | Cast datetime field into date and change timezone if required |
| Seconds          | Cast difference of datetime fields (durations) into seconds   |
| DistinctSum      | Compute SUM of values with the DISTINCT flag                  |
| Float            | Cast integer field to float                                   |
| NullIf           | Return NULL if value is 0                                     |
| divide           | Divide two integer or float columns and return a float        |
| multiply         | Multiply two integer or float columns and return a float      |
| add              | Add two integer or float columns and return a float           |
| subtract         | Subtract two integer or float columns and return a float      |
| LeftPad          | Because no package should ever be uploaded without left pad   |

### Tests
To run tests with coverage, you will need the coverage package.

```
pip install coverage
coverage run --source=./pg_utils tests/runtests.py
coverage report
```

### Contribute
We would love to have your contributions! To contribute to the repo, please open an issue or create a pull request.
