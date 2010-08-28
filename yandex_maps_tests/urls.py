from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    url(r'^yandex/', include('yandex_maps.urls')),
    url(r'^$', direct_to_template, {'template': 'index.html'}, 'index')
)
