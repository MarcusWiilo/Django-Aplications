from django.conf.urls import patterns, include, url

urlpatterns = patterns('pro_final.courses.views',
    url(r'^$', 'index', name='index'),
    # url(r'^(?P<pk>\d+)/$', 'details', name='details'),
    url(r'^(?P<slug>[\w_-]+)/$', 'details', name='details'),
)