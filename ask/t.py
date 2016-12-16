#from django.shortcuts import render
#from django.contrib.auth import authenticate,login
# Create your views here.
#from django.http import HttpResponse,Http404,HttpResponseRedirect
#from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
#from django.shortcuts import render
#from qa.models import Question,Answer,QuestionManager
#from qa.forms import AskForm,AnswerForm
from django.contrib.auth.models import User
from django.core.management import setup_environ
from django.db import transaction
from django.conf import settings
#from django.utils.timezone import datetime
#from django.test import TestCase
settings.configure()
import os
import sys
import unittest
sys.path.append('/home/box/test6/ask/')
#os.environ.setdefault(['DJANGO_SETTINGS_MODULE']='/home/box/test6/ask/settings'
#os.environ.setdefault("DJANGO_SETTINGS_MODULE","ask.settings")
os.environ['DJANGO_SETINGS_MODULE']='ask.settings' 
from django.core.wsgi import get_wsgi_application
application=get_wsgi_application()
#setup_environ(settings)
#settings.configure()
#os.environ['DEFAULT__INDEX_TABLESPACE']='indexs'
class Test(unittest.TestCase):
 def test_import(self):
    from qa.models import Question,Answer
    i=1
    for i in range(40):
        user,_=User.objects.get_or_create(username='user'+str(i),password='test'+str(i))
        question=Question.objects.create(title='titleq'+str(i),text='textq'+str(i),author=user,rating=i)
        answer=Answer.objects.create(text='texta'+str(i),question=question,author=user)
#added_at=cast(concat('2016-02-',convert(i)) as date)))
#    return HttpResponse('Happy end')

if __name__ == "__main__":
  unittest.main()
#suite=unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
#unittest.TextTestRunner(verbosity=2).run(suite)
