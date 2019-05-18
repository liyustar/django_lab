from django.shortcuts import render

import tushare as ts

# Create your views here.

def my_fun():
    df = ts.get_hist_data('600848') #一次性获取全部日k线数据
    print(df)


def hello_tushare(request):
    my_fun()
    return render(request, 'marketdata/hello_tushare.html')


def get_h_data(request):
    if request.GET.__contains__('symbol'):
        symbol = request.GET['symbol']
        df = ts.get_h_data(symbol, start='2019-01-01', end='2019-03-16') #一次性获取全部日k线数据
        return render(request, 'marketdata/get_h_data.html', {"symbol":symbol, "result":str(df)})
    else:
        return render(request, 'marketdata/get_h_data.html', {"symbol":"None", "result":"None"})


def get_hist_data(request):
    if request.GET.__contains__('symbol'):
        symbol = request.GET['symbol']
        df = ts.get_hist_data(symbol) #一次性获取全部日k线数据
        return render(request, 'marketdata/get_hist_data.html', {"symbol":symbol, "result":str(df)})
    else:
        return render(request, 'marketdata/get_hist_data.html', {"symbol":"None", "result":"None"})

