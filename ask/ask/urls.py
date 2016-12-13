from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from qa.views import test,vnew,vpopular,vques,vq
urlpatterns = patterns('qa.views',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',vnew),
#    url(r'^login/.*$',test,name='index2'),
#    url(r'^signup/.*$',test,name='index3'),
#    url(r'^question/<+([0-9])+>/$',vques),
    url(r'^question/(?P<dd>\d)+/$',vq),
#    url(r'^ask/.*$',test,name='index5'),
#    url(r'^popular/+(?P<num>)+$',vpopular),
     url(r'^popular/',vpopular),
#    url(r'^new/*$',test,name='index7'),
#    url(r'^\.?+Page=$',test),
#     url(r'^(?P<num>\d+)$',vpage),
)
