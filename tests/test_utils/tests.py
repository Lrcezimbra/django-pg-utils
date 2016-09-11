from pg_utils import (
    Date, DateTZ, Seconds, DistinctSum,
    NullIf, Float, divide
)

from django.test import TestCase
from django.utils import timezone
from django.db.models import F

from .models import Author


class AuthorQueryExpressionTests(TestCase):
    def setUp(self):
        pass

    def test_date_cast_works_correctly(self):
        current_time = timezone.now()
        current_date = current_time.date()
        Author.objects.create(name='test_name')

        queryset = Author.objects.filter(name='test_name').annotate(created_date=Date('created_at'))
        self.assertEqual(queryset[0].created_date, current_date)

    def test_divide_works_correctly(self):
        Author.objects.create(name='test_name', books_started=5, books_completed=8)

        queryset = Author.objects.annotate(completion_rate=divide(F('books_started'), F('books_completed')))
        self.assertEqual(queryset[0].completion_rate, 0.625)
