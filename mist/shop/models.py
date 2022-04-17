from django.db import models
from django.urls import reverse

class Genre(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default='')
    url = models.SlugField(max_length=50, unique=True, default='')

    def __str__(self):
        return self.name


class Developer(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default='')
    url = models.SlugField(max_length=50, unique=True, default='')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField('')
    url = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ManyToManyField(Category)
    name = models.CharField(max_length=50)
    url = models.SlugField(max_length=50, unique=True)
    description = models.TextField()
    genre = models.ManyToManyField(Genre)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    release_date = models.DateField()
    price = models.PositiveIntegerField()
    # poster
    # screenshots
    # videos

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={"slug": self.url})

    def __str__(self):
        return self.name
