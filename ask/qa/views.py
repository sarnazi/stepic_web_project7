from django.shortcuts import render
from django.contrib.auth import authenticate,login
# Create your views here.
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render
from qa.models import Question,Answer,QuestionManager
from qa.forms import AskForm,AnswerForm
from django.contrib.auth.models import User
from django.utils.timezone import datetime
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
#56
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
#76                                             'page':        page,
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
def vask(request):
    if request.method=="POST":  
       form=AskForm(request.POST)
       if form.is_valid():
          question=form.save()
          dd=question.id
          question=Question.objects.get(id=dd)
          url=question.get_url()
          return HttpResponseRedirect(url)
#104          form=AnswerForm(initial={'question': question.id})
    else:
       form=AskForm()
    return render(request,'ask.html', {
       'form': form,
#109       'question': question,
#       'dd': dd,
    })
#112
def vq123(request,dd):
    question=Question.objects.get(id=dd)
    if request.method=="POST":
       form=AnswerForm(request.POST)
       if form.is_valid():
          answer=form.save()
          url=answer.get_url()
          return HttpResponseRedirect(url)
    else:
       form=AnswerForm(initial={'question': question.id})
    return render(request,'question.html', {
          'form': form,
    })
def vnach(request):
#    user,_=User.objects.get_or_create(username='test',password='test')
#128
    i=1
    for i in range(40):
        user,_=User.objects.get_or_create(username='user'+str(i),password='t'+str(i))
        question=Question.objects.create(title='titleq'+str(i),text='textq'+str(i),author=user,rating=i)
        answer=Answer.objects.create(text='texta'+str(i),question=question,author=user)
#,added_at=cast(concat('2016-01-',convert(i)) as date)))
    return HttpResponse('Happy end')

