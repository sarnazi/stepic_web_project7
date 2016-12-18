from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render
from qa.models import Question,Answer,QuestionManager
from qa.forms import AskForm,AnswerForm,LoginForm,SignupForm
from django.contrib.auth.models import User
from django.utils.timezone import datetime
from django.contrib.auth.hashers import make_password,PBKDF2PasswordHasher
from django.contrib.sessions.models import Session
from random import random,randrange,uniform,choice,sample
from datetime import timedelta
def get_secret_key():
    i=1
    prstr=''
    for i in range(50):
        charr='abcdefghijklmnopqrstuvwxyz0123456789#!@#$%^&*-_()=+'
        prstr1=choice(charr)
        prstr=prstr+prstr1
    return prstr
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
#68
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
#88                                             'page':        page,
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
def vmain(request):
    return render(request,'main.html', {'title': 'Main',
    })
def vask(request):
    if request.method=="POST":  
       form=AskForm(request.POST)
       form._user=request.user
       if form.is_valid():
#          form._user=request.user
          question=form.save()
          dd=question.id
          question=Question.objects.get(id=dd)
          url=question.get_url()
          return HttpResponseRedirect(url)
#116          form=AnswerForm(initial={'question': question.id})
    else:
       form=AskForm()
    return render(request,'ask.html', {
       'form': form,
#121       'question': question,
#       'dd': dd,
    })
#124
def vq123(request,dd):
    question=Question.objects.get(id=dd)
    if request.method=="POST":
       form=AnswerForm(request.POST)
       form._user=request.user
       if form.is_valid():
#          form._user=request.user
          answer=form.save()
          url=answer.get_url()
          return HttpResponseRedirect(url)
    else:
       form=AnswerForm(initial={'question': question.id})
    return render(request,'question.html', {
          'form': form,
    })
def vnach(request):
#139    user,_=User.objects.get_or_create(username='test',password='test')
#140
    i=1
    for i in range(40):
        user,_=User.objects.get_or_create(username='user'+str(i),password='t'+str(i))
        question=Question.objects.create(title='titleq'+str(i),text='textq'+str(i),author=user,rating=i)
        answer=Answer.objects.create(text='texta'+str(i),question=question,author=user)
#146,added_at=cast(concat('2016-01-',convert(i)) as date)))
    return HttpResponse('Happy end')
def vsignup(request):
    if request.method=='POST':
       form=SignupForm(request.POST)
       if form.is_valid():
          user=form.save()
          username=form.cleaned_data["username"]
          password=form.moi_password
          user=authenticate(username=username,password=password)
          if user is not None:
             if user.is_active:
                login(request,user)
             else:
                pass
          else:
             pass
       return HttpResponseRedirect('/')
    else:
       form=SignupForm()
    return render(request,'signup.html',{'form': form,
                                         'user': request.user,
    })
#165
def vlogout(request):
    sessid=request.COOKIE.get('sessid')
    if sessid is not None:
       session.objects.delete(key='sessid')
#    url=request.Get.get('/')
    return HttpResponseRedirect('/')
def vlogin(request): 
    if request.method=='POST':
       form=LoginForm(request.POST)
       if form.is_valid():
#176          username=form.cleaned_data["username"]
#          password=form.cleaned_data["password"]
          username=request.POST.get('username')
#          login=request.POST.get('login')
          moi_password=request.POST.get('password')
          url=request.POST.get('/')
#          user=request.user   
#          if user.is_authenticate():
          user=authenticate(username=username,password=moi_password)
#          if user is None:
#186             return HttpResponseRedirect('/')
          if user is not None:
             if user.is_active:
                login(request, user)
             else:
                return HttpResponse('User None')
#195          else:
#            return HttpResponseRedirect('/')
             sessid=do_login(login,moi_password,username)
#          error=''
             if sessid is not None:
#                url=request.POST.get('/')
                response=HttpResponseRedirect('/')
                response.set_cookie('sessionid',sessid,
                httponly=True,expires=datetime.now()+timedelta(days=5)
                )
#                response=HttpResponseRedirect('/')
                return response
             else:
                return HttpResponse('What is it?')
          else:
             return HttpResponseRedirect('/')
    else:
#208       HttpResponse('Bad login or password')
       form=LoginForm()
    return render(request, 'login.html', { 'form': form,
    })
#212
def do_login(login,moi_password,username):
    try:
       user=User.objects.get(username=username)
    except User.DoesNotExist:
       return None
#218    pw=user.password
    salt="salt"
    hasher=PBKDF2PasswordHasher()
    hashed_pass=make_password(moi_password,salt,hasher)
    if user.password==hashed_pass:
       session=Session()
       session.key=get_secret_key()
#225nerate_long_random_key()
       session.user=user
       session.expires=datetime.now()+timedelta(days=5)
       session.expire_date=datetime.now()+timedelta(days=5)
       session.save()
#       sessid=session.key
    else:
       return None
    return session.key

 
   
              

