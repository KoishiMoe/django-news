from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    """
    用户
    :param display_name: 显示名称
    :param username: 用户名
    """
    display_name = models.CharField(max_length=50, blank=True)
    username = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.username

    @property
    def name(self):
        return self.display_name or self.username
