from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Question(models.Model):
      title=models.CharField(max_length=255)
      text=models.TextField()
      added_at=models.DateTimeField(auto_now_add=True)
      rating=models.IntegerField(default=0)
      author=models.ManyToManyField(User)
      likes=models.ManyToManyField(User,related_name='likes_user')
class Answer(models.Model):
      text=models.TextField()
      added_at=models.DateTimeField(auto_now_add=True)
      author=models.ManyToManyField(User)
      question=models.ForeignKey(Question,null=True,
                                 on_delete=models.SET_NULL)
class QuestionManager(models.Manager):
      def new(self):
          qbs=Question.objects.filter(added_at=datetime.date.today())
          qbs=qbs.all()
      def popular(self):
          qss=Question.objects.filter(added_at=datetime.date.today())
          qss=qs.order_by('rating')
          qss=qss.all()


      

