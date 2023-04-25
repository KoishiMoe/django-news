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
    class Meta:
        verbose_name = '图表'
        verbose_name_plural = verbose_name
    title = models.CharField(max_length=100, verbose_name='标题')
    description = models.TextField(verbose_name='描述')
    market = models.ForeignKey('charts.Market', on_delete=models.CASCADE, verbose_name='市场')
    data = models.ManyToManyField('charts.DataPoint', verbose_name='数据点')

    def __str__(self):
        return self.title


class DataPoint(models.Model):
    """
    图表数据点，包括标签和值
    :param label: 数据点标签，一般是日期
    :param value: 数据点值
    """
    class Meta:
        verbose_name = '数据点'
        verbose_name_plural = verbose_name
    label = models.CharField(max_length=100, verbose_name='标签')
    value = models.FloatField(verbose_name='值')

    def __str__(self):
        return self.label


class Market(models.Model):
    """
    市场，作用是区分各个曲线的所属类型，例如分为A股，美股，港股等
    """
    class Meta:
        verbose_name = '市场'
        verbose_name_plural = verbose_name
    name = models.CharField(max_length=50, unique=True, verbose_name='名称')
    description = models.TextField(verbose_name='描述')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __str__(self):
        return self.name


class StockSimple_sh(models.Model):
    class Meta:
        verbose_name = '上证指数'
        verbose_name_plural = verbose_name
    date_sh = models.CharField(max_length=100, verbose_name='日期')
    open_price_sh = models.FloatField(verbose_name='开盘价')
    close_price_sh = models.FloatField(verbose_name='收盘价')
    highest_price_sh = models.FloatField(verbose_name='最高价')
    lowest_price_sh = models.FloatField(verbose_name='最低价')

    def __str__(self):
        return self.date_sh


class StockSimple_sz(models.Model):
    class Meta:
        verbose_name = '深证指数'
        verbose_name_plural = verbose_name
    date_sz = models.CharField(max_length=100, verbose_name='日期')
    open_price_sz = models.FloatField(verbose_name='开盘价')
    close_price_sz = models.FloatField(verbose_name='收盘价')
    highest_price_sz = models.FloatField(verbose_name='最高价')
    lowest_price_sz = models.FloatField(verbose_name='最低价')

    def __str__(self):
        return self.date_sz


class StockComplex_sh(models.Model):
    class Meta:
        verbose_name = '上证指数'
        verbose_name_plural = verbose_name
    stock_date_sh = models.CharField(max_length=100, verbose_name='日期')
    stock_code_sh = models.CharField(max_length=100, verbose_name='代码')
    stock_name_sh = models.CharField(max_length=100, verbose_name='名称')
    stock_open_sh = models.FloatField(verbose_name='开盘价')
    stock_close_sh = models.FloatField(verbose_name='收盘价')
    stock_highest_sh = models.FloatField(verbose_name='最高价')
    stock_lowest_sh = models.FloatField(verbose_name='最低价')
    stock_main_purchase_sh = models.FloatField(verbose_name='主力净流入')
    stock_increase_sh = models.FloatField(verbose_name='涨跌幅')

    def __str__(self):
        return self.stock_date_sh


class StockComplex_sz(models.Model):
    class Meta:
        verbose_name = '深证指数'
        verbose_name_plural = verbose_name
    stock_date_sz = models.CharField(max_length=100, verbose_name='日期')
    stock_code_sz = models.CharField(max_length=100, verbose_name='代码')
    stock_name_sz = models.CharField(max_length=100, verbose_name='名称')
    stock_open_sz = models.FloatField(verbose_name='开盘价')
    stock_close_sz = models.FloatField(verbose_name='收盘价')
    stock_highest_sz = models.FloatField(verbose_name='最高价')
    stock_lowest_sz = models.FloatField(verbose_name='最低价')
    stock_main_purchase_sz = models.FloatField(verbose_name='主力净流入')
    stock_increase_sz = models.FloatField(verbose_name='涨跌幅')

    def __str__(self):
        return self.stock_date_sz
