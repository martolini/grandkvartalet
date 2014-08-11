from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'grandkvartalet.core.comingsoon.views.comingsoon', name='comingsoon'),
	url(r'^display_pdf/(?P<filename>)\w+/$', 'grandkvartalet.core.landing.views.display_pdf', name='display_pdf'),
	url(r'^landing/$', 'grandkvartalet.core.landing.views.landing_view', name='landing'),
	url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)