from django.db import models

from apps import users


# Create your models here.


class Comment(models.Model):
    """
    新闻评论
    :param user: 评论用户
    :param text: 评论内容
    :param created_time: 评论时间
    :param post: 评论对应的的新闻
    """
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    # post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:20]
