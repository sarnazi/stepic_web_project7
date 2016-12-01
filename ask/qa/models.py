from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils.timezone import datetime
class QuestionManager(models.Manager):
      def mnew(self):
          qbs=Question.objects.filter(added_at__lte=datetime.today())
          qbs=Question.objects.order_by('-added_at')
          qbs=qbs.all()
      def mpopular(self):
          qss=Question.objects.filter(added_at__gt=(datetime.today()-7))
          qss=Question.objects.order_by('-rating')
          qss=qss.all()
class Question(models.Model):
      objects=QuestionManager()
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



      

