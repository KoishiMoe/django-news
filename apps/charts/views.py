from django.shortcuts import render
from .models import StockSimple_sh, StockSimple_sz, StockComplex_sh, StockComplex_sz

# Create your views here.

from django.http import JsonResponse
from .models import StockSimple_sh, StockSimple_sz


def stock_simple(request):
    # 从数据库中查询所有的上证指数和深证指数的数据
    stocks_sh = StockSimple_sh.objects.all()
    stocks_sz = StockSimple_sz.objects.all()
    # 将数据转换为列表格式
    stocks_sh_list = list(stocks_sh.values())
    stocks_sz_list = list(stocks_sz.values())
    # 将数据打包成一个字典
    data = {
        'stocks_sh': stocks_sh_list,
        'stocks_sz': stocks_sz_list
    }
    # 返回一个JsonResponse对象，包含数据和状态码
    return JsonResponse(data, status=200)


def stock_complex(request):
    stockc_sh = StockComplex_sh.objects.all()
    stockc_sz = StockComplex_sz.objects.all()
    return render(request, 'stock_complex.html', {'stockc_sh': stockc_sh, 'stockc_sz': stockc_sz})
