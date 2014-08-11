from django.conf.urls import patterns, include, url
from .views import *

ajaxpatterns = patterns('edgebet.app.contact.ajax',
	url(r'^send/$', 'send_ajax', name='send_contact'),
)

viewpatterns = patterns('',
	url(r'^contact/$', contact_view, name='contact'),
)

urlpatterns = ajaxpatterns + viewpatterns