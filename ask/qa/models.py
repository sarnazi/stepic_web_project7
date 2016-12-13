from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils.timezone import datetime
class QuestionManager(models.Manager):
      def mnew(self):
          return self.order_by('-added_at')
      def mpopular(self):
          return self.order_by('-rating')
#          qss=Question.objects.filter(added_at__gt=(datetime.today()-7))
      def mques(self,dd):
          return self.filter(id=dd)
      def mq(self,dd):
          return self.get(id=dd)
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



      

