from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,Http404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render
from qa.models import Question,Answer,QuestionManager
def vnew(request):
    try:
       limit=int(request.GET.get('limit',10))
    except:
       limit=10
    try:
       page=int(request.GET.get("page",1))
    except ValueError:
      page=1
    except TypeError:
      page=1
    questions = Question.objects.mnew()
    paginator = Paginator(questions,10)
    paginator.baseurl='http://127.0.0.1/?page='
    page = paginator.page(page)
    return render(request,'list.html', {
           'title':     'Latest',
           'questions': page.object_list,
           'paginator': paginator,
           'page':      page,
    })
def vpopular(request):
    try:
       limit=int(request.GET.get('limit',10))
    except:
       limit=10
    try:
       page=int(request.GET.get("page",1))
    except ValueError:
       page=1
    except TypeError:
       page=1
    questions=Question.objects.mpopular()
    paginator=Paginator(questions,10)
    paginator.baseurl='http://127.0.0.1/popular/?page='
    try:
       page=paginator.page(page)
    except EmptyPage:
       page=1
    return render(request,'listp.html', {
           'title':   'Popular',
           'questions':   page.object_list,
           'paginator': paginator,
           'page':    page,
     })
#53
def vques(request,dd):
    limit=int(request.GET.get("limit",10))
    page=int(request.GET.get("page",1))
    try:
       questions=Question.objects.mques(dd)
    except Question.DoesNotExist:
       raise Http404
    try:
       answers=Answer.objects.all()
    except Answer.DoesNotExist:
       raise Http404
    paginator=Paginator(questions,10)
    page=paginator.page(page)
    paginator.baseurl='http://127.0.0.1/question/5/'
    return render(request,'listo.html', {
                                            'title': 'One',
                                            'questions': page.object_list,
#                                         'answers':   Answer,
#                                         'paginator':   paginator,
#70                                             'page':        page,
    })

def vq(request,dd):
    try:
       questions=Question.objects.mq(dd)
    except Question.DoesNotExist:
       raise Http404
    try:
       answer=Answer.objects.all()
    except Answer.DoesNotExist:
       raise Http404
    return render(request,'listo2.html', {
                                           'title':     'One',
                                           'questions': questions,
                                           'answer':    answer,
    })
def test(request,*args,**kwargs):
    return HttpResponse('OK')

