from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField('email address', blank=False, null=False, unique=True)


class Ava(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_path = models.ImageField(upload_to='src/media_content')