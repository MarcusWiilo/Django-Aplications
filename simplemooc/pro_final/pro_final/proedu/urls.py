from django.conf.urls import patterns, include, url

urlpatterns = patterns('pro_final.proedu.views',
    url(r'^$', 'home', name='home'),
    url(r'^contato/$', 'contact', name='contact'),
)