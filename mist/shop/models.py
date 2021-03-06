from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default='')
    url = models.SlugField(max_length=50, unique=True, default='')

    def __str__(self):
        return self.name


class Developer(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default='')
    url = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default='')
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
    developer = models.ManyToManyField(Developer)
    release_date = models.DateField()
    price = models.PositiveIntegerField()
    poster = models.ImageField(default="images/default_photos/poster.png", upload_to="images/posters")
    # screenshots
    # videos

    def get_absolute_url(self):
        return reverse('shop:product_detail', kwargs={"slug": self.url})

    def __str__(self):
        return self.name


class Review(models.Model):

    Rating_CHOICES = (
        (1, 'Poor'),
        (2, 'Average'),
        (3, 'Good'),
        (4, 'Very good'),
        (5, 'Excellent'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField(choices=Rating_CHOICES, default=3)
    recommended = models.BooleanField(default=False)
    body = models.TextField(default="")

    def __str__(self):
        return f'Username: {self.user.username}, product name: {self.product.name}, rate: {self.rate}'
