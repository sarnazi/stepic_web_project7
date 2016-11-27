from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index1(request):
    return HttpResponse("ura1")
def index2(request):
    return HttpResponse("ura2")
def index3(request):
    return HttpResponse("ura3")
def index4(request):
    return HttpResponse("ura4")
def index5(request):
    return HttpResponse("ura5")
def index6(request):
    return HttpResponse("ura6")
def index7(request):
    return HttpResponse("ura7")
def test(request,*args,**kwargs):
    return HttpResponse('OK')

