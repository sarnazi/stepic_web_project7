from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from qa.views import test
urlpatterns = patterns('qa.views',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',test,name='index1'),
    url(r'^login/.*$',test,name='index2'),
    url(r'^signup/.*$',test,name='index3'),
    url(r'^question/<+([0-9])+>/$',test,name='index4'),
    url(r'^ask/.*$',test,name='index5'),
    url(r'^popular/.*$',test,name='index6'),
    url(r'^new/*$',test,name='index7'),
)
