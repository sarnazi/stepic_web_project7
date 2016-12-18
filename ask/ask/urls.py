from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from qa.views import test,vnew,vpopular,vques,vq,vask,vq123,vnach,vsignup,vlogin,vmain

urlpatterns = patterns('qa.views',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^nach/',vnach),
    url(r'^$',vmain),   
    url(r'^new/.$',vnew),
    url(r'^login/.*$',vlogin),
    url(r'^signup/.*$',vsignup),
#    url(r'^question/<+([0-9])+>/$',vq123),
    url(r'^question/(?P<dd>\d)+/$',vq123),
#    url(r'^question/(?P<dd>\d)+/$',vq),
    url(r'^ask/',vask),
#    url(r'^popular/+(?P<num>)+$',vpopular),
     url(r'^popular/',vpopular),
#    url(r'^new/*$',test,name='index7'),
#    url(r'^\.?+Page=$',test),
#     url(r'^(?P<num>\d+)$',vpage),
)
