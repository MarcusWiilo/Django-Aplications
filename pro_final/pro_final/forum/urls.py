from django.conf.urls import patterns, include, url

urlpatterns = patterns('pro_final.forum.views',
    url(r'^$', 'index', name='index'),
    url(r'^tag/(?P<tag>[\w_-]+)/$', 'index', name='index_tagged'),
    url(r'^respostas/(?P<pk>\d+)/correta/$', 'reply_correct', 
        name='reply_correct'),
    url(r'^respostas/(?P<pk>\d+)/incorreta/$', 'reply_incorrect', 
        name='reply_incorrect'),
    url(r'^slug/(?P<slug>[\w_-]+)/$', 'thread', name='thread'),
)