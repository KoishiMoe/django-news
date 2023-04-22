from django.db import models

# Create your models here.


class Market(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
