from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^$', 'perfis.views.index'),
	url(r'^perfis/(?P<perfil_id>\d+)$', 'perfis.views.exibir')
)