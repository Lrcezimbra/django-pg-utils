from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)

    created_at = models.DateTimeField(null=True)
    modified_at = models.DateTimeField(null=True)

    friends = models.ManyToManyField('self', blank=True)

    books_started = models.IntegerField(null=True)
    books_completed = models.IntegerField(null=True)

    price = models.FloatField(null=True)
    cost = models.IntegerField(null=True)

    def __str__(self):
        return self.name
