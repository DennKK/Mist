from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(default='')

    def __str__(self):
        return self.name


class Developer(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default='')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField('')
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ManyToManyField(Category)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField()
    genre = models.ManyToManyField(Genre)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    release_date = models.DateField()
    price = models.PositiveIntegerField()
    # poster
    # screenshots
    # videos

    def __str__(self):
        return self.name
