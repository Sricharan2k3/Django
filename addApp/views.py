from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def addNum(request):
    return render(request, 'add.html')


def result(request):
    var1 = int(request.GET["val1"])
    var2 = int(request.GET["val2"])
    res = var1+var2

    return render(request, 'result.html', {'result': res})
