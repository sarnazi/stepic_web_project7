from django import forms
from qa.models import Question,Answer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.shortcuts import get_object_or_404
from django.utils.timezone import datetime
from django.db.models import Max
class AskForm(forms.Form):
      title=forms.CharField(max_length=225)
      text=forms.CharField(widget=forms.Textarea)
      def clean_title(self):
          title=self.cleaned_data['title']
#          if not is_ethic(title):
#             raise forms.ValidationError('Title error',code=12)
#u''
          return title
      def clean_text(self):
          text=self.cleaned_data['text']
#          if not is_ethic(text):
#             raise forms.ValidationError(
#                   'Question error', code=12)
          return text
      def save(self):
          question = Question(**self.cleaned_data)   
          user,_ = User.objects.get_or_create(username='test',password='test')
          question.author=user
          question.added_at=datetime.today()
          question.save()
          return question
class AnswerForm(forms.Form):
      text=forms.CharField(widget=forms.Textarea)
      question=forms.IntegerField(widget=forms.HiddenInput)
      def clean_text(self):
          text=self.cleaned_data['text']
#          if not is_ethic(text):
#             raise forms.ValidationError(
#                   'Answer error', code=12)
          return text
      def clean_question(self):
          question_id=self.cleaned_data['question']
          try:
             question=Question.objects.get(id=question_id)
          except Question.DoesNotExist:
             question = None
          return question
      def save(self):
          answer=Answer(**self.cleaned_data)
          user,_ = User.objects.get_or_create(username='test',password='test')
          answer.author=user
          answer.save()
          return answer
