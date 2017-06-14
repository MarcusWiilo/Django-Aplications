from django.conf.urls import patterns, include, url

urlpatterns = patterns('pro_final.proedu.views',
    url(r'^$', 'home', name='home'),
    url(r'^contato/$', 'contact', name='contact'),
    url(r'^contato2/$', 'contact2', name='contact2'),
    url(r'^contato3/$', 'contact3', name='contact3'),
)