from django.conf.urls import patterns, include, url
from django.contrib import admin


from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^/?$', include('home.urls', namespace="home")),
    # url('^', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
