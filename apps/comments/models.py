from django.db import models

# Create your models here.


class Comment(models.Model):
    content = models.TextField(verbose_name='内容')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='作者')
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, verbose_name='文章')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'
