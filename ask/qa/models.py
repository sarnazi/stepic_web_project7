from django.db import models

# Create your models here.
from django.contrib.auth.models import User
#from django.core.management import setup_environ
#from project import settings
#setup_environ(settings)
##from django.db import connection
#cursor=connection.cursor()
class QuetionManager(models.Manager):
      def new():
          qbs=Question.objects.filter(added_at=datetime.date.today())
          qbs=qbs.all()
      def popular():
          qss=Question.objects.filter(added_at=datetime.date.today())
          qss=Question.order_by('rating')
          qss=qss.all()
class Question(models.Model):
      title=models.CharField(max_length=255)
      text=models.TextField()
      added_at=models.DateTimeField(auto_now_add=True)
      rating=models.IntegerField(default=0)
      author=models.ForeignKey(User)
      likes=models.ManyToManyField(User,related_name='likes_user')
class Answer(models.Model):
      text=models.TextField()
      added_at=models.DateTimeField(auto_now_add=True)
      author=models.ForeignKey(User)
      question=models.ForeignKey(Question,null=True,
                                 on_delete=models.SET_NULL)



      

