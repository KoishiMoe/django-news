from django.db import models

from apps import users, groups


# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    members = models.ManyToManyField('users.User', through='Membership')
    permissions = models.ManyToManyField('groups.Permission')

    def __str__(self):
        return self.name


class Membership(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    group = models.ForeignKey('groups.Group', on_delete=models.CASCADE)


class Permission(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
