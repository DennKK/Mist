from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Genre(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Developer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField()
    genre = models.ManyToManyField(Genre)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    release_date = models.DateField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name
