from django import forms
from qa.models import Question,Answer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.shortcuts import get_object_or_404
from django.utils.timezone import datetime
from django.db.models import Max
from django.contrib.auth.hashers import make_password,PBKDF2PasswordHasher
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
#19          if not is_ethic(text):
#             raise forms.ValidationError(
#                   'Question error', code=12)
          return text
      def save(self):
          question = Question(**self.cleaned_data)   
#t7          user,_ = User.objects.get_or_create(username='test',password='test')
#t7          question.author=user
          question.author_id=self._user.id
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
#37                   'Answer error', code=12)
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
#t7          user,_ = User.objects.get_or_create(username='test',password='test')
#t7          answer.author=user
          answer.author_id=self._user.id
          answer.save()
          return answer
class SignupForm(forms.Form):
      username=forms.CharField(max_length=100,required=False)
      email=forms.EmailField(required=False)
      password=forms.CharField(widget=forms.PasswordInput,required=False)
      def clean_username(self):
          username=self.cleaned_data.get('username')
          if not username:
             raise forms.ValidationError('No username')
          try:
             User.objects.get(username=username)
             raise forms.ValidationError('Username exist')
          except User.DoesNotExist:
             pass
          return username
      def clean_password(self):
          password=self.cleaned_data.get('password')
          if not password:
             raise forms.ValidationError('No password')
          self.moi_password=password
          salt="salt"
          hasher=PBKDF2PasswordHasher()
          return make_password(password,salt,hasher)
      def save(self):
          user=User(**self.cleaned_data)
          user.save()
          return user
#76
class LoginForm(forms.Form):
      username=forms.CharField(max_length=100,required=False)
      password=forms.CharField(widget=forms.PasswordInput,required=False)
      def clean_username(self):
          username=self.cleaned_data.get('username')
          if not username:
             raise forms.ValidationError('No user')
          return username
      def clean_password(self):
          password=self.cleaned_data.get('password')
          if not password:
             raise forms.ValidationError('No password')
          return password
      def clean(self):
          username=self.cleaned_data.get('username')
          password=self.cleaned_data.get('password')
          try:
             user=User.objects.get(username=username)
          except User.DoesNotExist:
             raise forms.ValidationError('Bad username or pasword')
          if not user.check_password(password):
             raise forms.ValidationError('Bad username or password')
#99

