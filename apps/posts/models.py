from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
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
    :param approved: 新闻是否通过审核

    """
    title = models.CharField(max_length=70)
    body = models.TextField()
    image = models.ImageField(upload_to='posts/%Y/%m/%d', blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey('posts.Category', on_delete=models.PROTECT)
    tags = models.ManyToManyField('posts.Tag', blank=True)
    author = models.ForeignKey('users.User', on_delete=models.PROTECT, blank=True)
    approved = models.BooleanField(default=False)
    pinned = models.BooleanField(default=False)
    # comments = models.ManyToManyField('comments.Comment', blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'id': self.id})

    def get_image_url(self):
        try:
            if self.image:
                return self.image.url
            else:
                return ""
        except ValueError:
            return ""

    def clean(self):
        try:
            if self.pinned and not self.image:
                raise ValidationError('Pinned post must have an image.')
        except AttributeError:
            pass


class Category(models.Model):
    """
    新闻分类
    """
    name = models.CharField(max_length=20)
    parent = models.ForeignKey('self', related_name='sub_category', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_full_name(self):
        if self.parent:
            return self.parent.name + ' - ' + self.name
        else:
            return self.name

    def clean(self):
        try:
            if self.parent == self:
                raise ValidationError('Category parent must be different from category itself.')
            if self.parent.parent:
                raise ValidationError('Category parent must be top category.')
        except AttributeError:
            pass
        super().clean()

    @property
    def subcategories(self):
        return Category.objects.filter(parent=self)


class Tag(models.Model):
    """
    新闻标签
    """
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
