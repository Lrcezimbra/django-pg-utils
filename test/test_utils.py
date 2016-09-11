from pg_utils import (
    Date, DateTZ, Seconds, DistinctSum,
    NullIf, Float, divide
)

from .models import Author


def test_date_cast_works_correctly():
    assert 1 == 2
