from django.conf.urls import patterns, include, url

urlpatterns = [
    url(r'^$', 'simplemooc.core.views.home', name='home'),
    url(r'^cursos/$', 'simplemooc.courses.views.index', name='index'),
    url(r'^(?P<pk>\d+)/$', 'simplemooc.courses.views.details', name='details'),
]