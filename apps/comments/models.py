from django.db import models

from apps import users


# Create your models here.


class Comment(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:20]
