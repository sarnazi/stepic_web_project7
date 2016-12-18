from django.db import models

# Create your models here.
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils.timezone import datetime
from datetime import timedelta
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
      rating=models.IntegerField(default=1)
      author=models.ForeignKey(User,default=1)
      likes=models.ManyToManyField(User,related_name='likes_user')
      def __unicode__(self):
          return self.title
      def get_url(self):
          return "/question/{}".format(self.id)
class Answer(models.Model):
      text=models.TextField()
      added_at=models.DateTimeField(auto_now_add=True)
      author=models.ForeignKey(User,default=1)
      question=models.ForeignKey(Question,null=True,
                                 on_delete=models.SET_NULL)
      def __unicode__(self):
         return self.text
      def get_url(self):
          return "/ask/"
#class Session(models.Model):
#      key=models.CharField(unique=True)
#      user=models.ForeignKey(User)
#      expires=models.DateTimeField(null=True,blank=True)
#      expire_date=models.DateTimeField()
#default=datetime.now()+timedelta(days=5))



      

