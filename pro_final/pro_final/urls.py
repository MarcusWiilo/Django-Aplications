from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('pro_final.proedu.urls', namespace='proedu')),
    url(r'^conta/', include('pro_final.accounts.urls', namespace='accounts')),
    url(r'^cursos/', include('pro_final.courses.urls', namespace='courses')),
    url(r'^forum/', include('pro_final.forum.urls', namespace='forum')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)