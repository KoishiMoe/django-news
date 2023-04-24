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
    :param pinned: 新闻是否置顶
    """
    class Meta:
        permissions = (
            ('approve_post', 'Can approve post'),
            ('pin_post', 'Can pin post'),
            ('change_author', 'Can change author'),
        )
        verbose_name = '文章'
        verbose_name_plural = '文章'
    title = models.CharField(max_length=70, verbose_name='标题')
    body = models.TextField(verbose_name='内容')
    image = models.ImageField(upload_to='posts/%Y/%m/%d', blank=True, verbose_name='头图')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modified_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    excerpt = models.CharField(max_length=200, blank=True, verbose_name='摘要')
    category = models.ForeignKey('posts.Category', on_delete=models.PROTECT, verbose_name='分类')
    # tags = models.ManyToManyField('posts.Tag', blank=True, verbose_name='标签')
    author = models.ForeignKey('users.User', on_delete=models.PROTECT, blank=True, verbose_name='作者')
    approved = models.BooleanField(default=False, verbose_name='审核通过')
    pinned = models.BooleanField(default=False, verbose_name='置顶')
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
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'
    name = models.CharField(max_length=20, verbose_name='名称')
    parent = models.ForeignKey('self', related_name='sub_category', on_delete=models.CASCADE, blank=True, null=True,
                               verbose_name='父分类')

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
                raise ValidationError('不能将自己作为父分类.')
            if self.parent.parent:
                raise ValidationError('分类最多只能有两级.')
        except AttributeError:
            pass
        super().clean()

    @property
    def subcategories(self):
        return Category.objects.filter(parent=self)


# class Tag(models.Model):
#     """
#     新闻标签
#     """
#     class Meta:
#         verbose_name = '标签'
#         verbose_name_plural = '标签'
#     name = models.CharField(max_length=20)
#
#     def __str__(self):
#         return self.name
