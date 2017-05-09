from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('pro_final.proedu.urls', namespace='proedu')),
    url(r'^admin/', include(admin.site.urls)),
)
