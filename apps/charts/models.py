from django.db import models

from apps import markets, charts


# Create your models here.


class Chart(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    market = models.ForeignKey('markets.Market', on_delete=models.CASCADE)
    data = models.ManyToManyField('charts.DataPoint')

    def __str__(self):
        return self.title


class DataPoint(models.Model):
    chart = models.ForeignKey('charts.Chart', on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    value = models.IntegerField()

    def __str__(self):
        return self.label
