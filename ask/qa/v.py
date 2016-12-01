from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render

def vnew(request):
    quesn=Question.objects.new()
    try:
       limit=int(request.GET.get'limit',10))
    except:
       limit=10
    try:
       page=int(request.GET.get('page',1))
    except:
       page=1
    paginator=Paginator(quesn,limit)
#    paginator.baseurl='/?page=2'
    page=Paginator.page(page)
    return render(request,'list.html', {
           'title':     quesn.title,
           'paginator': paginator,
           'ques':      quesn.text,
    })
def vpopular:
    quesp=Question.objects.popular()
    try:
       limit=int(request.GET.get('limit',10))
    except:
       limit=10
    try:
       page=int(request.GET.get('page',1))
    except:
       page=1
    paginator=Paginator(quesp,limit)
#    paginator.baseurl='/popular/?page=3'
    paginator.page=Paginator(page)
    return render(request,'list.html', {
           'title':   quesp.title,
           'paginator': paginator,
           'ques':    quesp.text,
     })
    
def test(request,*args,**kwargs):
    return HttpResponse('OK')

