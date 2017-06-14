from django.conf.urls import patterns, include, url
from .views import AuthorCreate, AuthorUpdate, AuthorDelete


urlpatterns = patterns('pro_final.courses.views',
	url(r'^$', 'index', name='index'),
	# url(r'^(?P<pk>\d+)/$', 'details', name='details'),
	url(r'^(?P<slug>[\w_-]+)/$', 'details', name='details'),
	url(r'^(?P<slug>[\w_-]+)/inscricao/$', 'enrollment', name='enrollment'),
	url(r'^(?P<slug>[\w_-]+)/cancelar-inscricao/$', 'undo_enrollment', name='undo_enrollment'),
	url(r'^(?P<slug>[\w_-]+)/anuncios/$', 'announcements', name='announcements'),
	url(r'^(?P<slug>[\w_-]+)/anuncios/(?P<pk>\d+)/$', 'show_announcement', name='show_announcement'),
	url(r'^(?P<slug>[\w_-]+)/aulas/$', 'lessons', name='lessons'),
    url(r'^(?P<slug>[\w_-]+)/aulas/(?P<pk>\d+)/$', 'lesson', name='lesson'),
    url(r'^(?P<slug>[\w_-]+)/materiais/(?P<pk>\d+)/$', 'material', name='material'),
    url(r'author/add/$', AuthorCreate.as_view(), name='author_add'),
    url(r'author/(?P<pk>[0-9]+)/%', AuthorUpdate.as_view(), name='author_update'),
    url(r'author/(?P<pk>[0-9]+)/delete/%', AuthorDelete.as_view(), name='author_delete')

)