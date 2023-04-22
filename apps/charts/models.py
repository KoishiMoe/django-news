from django.db import models


# Create your models here.


class Chart(models.Model):
    """
    存储图表需要的数据，包括标题、描述、数据点等。
    :param title: 图表标题
    :param description: 图表描述
    :param market: 图表所属市场
    :param data: 图表数据点
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    market = models.ForeignKey('charts.Market', on_delete=models.CASCADE)
    data = models.ManyToManyField('charts.DataPoint')

    def __str__(self):
        return self.title


class DataPoint(models.Model):
    """
    图表数据点，包括标签和值
    :param label: 数据点标签，一般是日期
    :param value: 数据点值
    """
    label = models.CharField(max_length=100)
    value = models.FloatField()

    def __str__(self):
        return self.label


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
