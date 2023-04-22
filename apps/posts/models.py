from django.db import models
from django.utils import timezone


# Create your models here.


class Post(models.Model):
    """
    新闻
    :param title: 新闻标题
    :param body: 新闻内容
    :param image: 新闻图片（单张，可选）
    :param created_time: 新闻创建时间
    :param modified_time: 新闻修改时间
    :param excerpt: 新闻摘要（可选）
    :param category: 新闻分类
    :param tags: 新闻标签（可选）
    :param author: 新闻作者
    """
    title = models.CharField(max_length=70)
    body = models.TextField()
    image = models.ImageField(upload_to='posts/%Y/%m/%d', blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey('posts.Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField('posts.Tag', blank=True)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        super().save(*args, **kwargs)


class Category(models.Model):
    """
    新闻分类
    """
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    新闻标签
    """
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
