from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,Http404
from django.core.paginator import Paginator
from django.shortcuts import render
from qa.models import Question,Answer,QuestionManager
def vpage(request):
    request=request
    try:
       limit=int(request.GET.get('limit',10))
#12
    except:
       limit=10
    try:
       page=int(request.GET.get('page',1))
    except:
       page=1
    if page==2:
       vnew(request,page,limit)       
#21
    else:
       return Http404
def vnew(request,page,limit):
    quesn=Question.objects.mnew()
    paginator=Paginator(quesn,limit)
#    paginator.baseurl='/?page=2'
#    page=paginator.page(page)
    return render(request,'list.html', {
#           'title':     'Latest',
#31
           'quesn': page.object_list,
           'paginator': paginator,
           'page':      page,
    })
def vpopular(request):
    quesp=Question.objects.mpopular()
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
    page=paginator.page(page)
    return render(request,'list.html', {
#           'title':   quesp.title,
           'quesp':   page.object_list,
           'paginator': paginator,
           'page':    page,
     })
    
def test(request,*args,**kwargs):
    return HttpResponse('OK')

