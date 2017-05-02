from django.conf.urls import patterns, url
from perfis.views import index

urlpatterns = patterns('',
	url(r'^$', 'perfis.views.index'),
)