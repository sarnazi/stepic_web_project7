from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
#from django.core.paginator import Paginator
#from django.shortcuts import render

   
def test(request,*args,**kwargs):
    return HttpResponse('OK')

