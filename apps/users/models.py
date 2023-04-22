from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    display_name = models.CharField(max_length=50, blank=True)
    username = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.display_name or self.username
