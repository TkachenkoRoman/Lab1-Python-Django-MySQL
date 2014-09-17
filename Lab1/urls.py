from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = patterns("",
    url(r'^', include('GuitarDataBaseApp.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

#urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Lab1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
#)
