import uuid
from django.contrib.postgres.indexes import GinIndex
from django.db import models


class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120, null=False, blank=False, db_index=True)
    email = models.EmailField()
    address = models.CharField(max_length=120)

    def __str__(self):
        return str(self.name)

    # class Meta:
    #     indexes = [models.Index(fields=['email', 'name', 'address'])]

    class Meta:
        indexes = [
            GinIndex(
                name='myginindex',
                fields=['name']
            )
        ]


# for  caching

class Redis(models.Model):
    name = models.CharField(max_length=120)
    desc = models.TextField()

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.CharField(max_length=400)
    ticket_price = models.PositiveIntegerField()

    def __str__(self):
        return self.name
