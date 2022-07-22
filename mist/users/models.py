from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(default="images/profile_photo/default_img.png", upload_to="images/profile_photo")
    bio = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username