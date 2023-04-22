from django.db import models

# Create your models here.


class Market(models.Model):
    """
    市场，作用是区分各个曲线的所属类型，例如分为A股，美股，港股等
    """
    name = models.CharField(max_length=50)
    description = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
