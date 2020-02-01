from django.db import models

# Create your models here.
from django.db import models


class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name


class Publisher(models.Model):
    name = models.TextField(blank=True, null=True)

    def __str__(self):   # Для того чтобы в ./admin отоборажалоось
        return self.name


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    copy_count = models.SmallIntegerField()
    Publisher_id = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    price = models.FloatField()
    #
    # def __str__(self):
    #     return self.title

    # def __str__(self):
    #     return self.author.full_name
