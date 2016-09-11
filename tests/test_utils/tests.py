from pg_utils import (
    Date, DateTZ, Seconds, DistinctSum,
    NullIf, Float, divide, multiply,
    subtract, add
)

from datetime import timedelta

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
        tomorrow_date = (timezone.now() + timedelta(days=1)).date()
        Author.objects.create(name='test_name', created_at=current_time)

        queryset = Author.objects.annotate(
            created_date=Date('created_at')
        )
        self.assertEqual(queryset[0].created_date, current_date)

        # Cast date to tomorrow using timezone
        queryset = Author.objects.filter(name='test_name').annotate(created_date=DateTZ('created_at', '+24:00'))
        self.assertEqual(queryset[0].created_date, tomorrow_date)

    def test_divide_works_correctly(self):
        Author.objects.create(name='test_name_1', books_started=5, books_completed=8)
        Author.objects.create(name='test_name_2', books_started=0, books_completed=0)

        queryset = Author.objects.order_by('name').annotate(
            completion_rate=divide(F('books_started'), F('books_completed'))
        )
        self.assertEqual(queryset[0].completion_rate, 0.625)
        self.assertEqual(queryset[1].completion_rate, None)

    def test_multiply_works_correctly(self):
        Author.objects.create(name='test_name_1', price=2.5, books_completed=9)

        queryset = Author.objects.annotate(
            revenue=multiply('price', 'books_completed')
        )
        self.assertEqual(queryset[0].revenue, 22.5)

    def test_add_and_subtract_work_correctly(self):
        Author.objects.create(name='test_name_1', price=12.5, cost=9)

        queryset = Author.objects.annotate(
            profit=subtract('price', 'cost'),
            dummy=add('price', 'cost')
        )
        self.assertEqual(queryset[0].profit, 3.5)
        self.assertEqual(queryset[0].dummy, 21.5)

    def test_cast_duration_into_seconds_works_correctly(self):
        current_time = timezone.now()
        offset_time = current_time + timedelta(seconds=5)
        Author.objects.create(name='test_name', modified_at=offset_time, created_at=current_time)

        queryset = Author.objects.annotate(
            duration=Seconds(F('modified_at') - F('created_at'))
        )
        self.assertEqual(queryset[0].duration, 5)
