from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    friends = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.name
