from django.conf.urls import patterns, include, url

urlpatterns = [
    url(r'^$', 'simplemooc.core.views.home', name='home'),
    url(r'^contato/$', 'simplemooc.core.views.contact', name='contact'),

]

