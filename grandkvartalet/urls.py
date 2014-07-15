from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'grandkvartalet.core.comingsoon.views.comingsoon', name='comingsoon'),
    url(r'^admin/', include(admin.site.urls)),
)
