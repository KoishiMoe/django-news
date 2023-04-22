from django.db import models
from django.utils import timezone

from apps import users


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    image = models.ImageField(upload_to='posts/%Y/%m/%d', blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey('news.Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField('news.Tag', blank=True)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        super().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
