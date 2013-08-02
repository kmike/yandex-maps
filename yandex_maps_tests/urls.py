try:
    from django.conf.urls import url, patterns, include
except ImportError:
    from django.conf.urls.defaults import *

try:
    from django.shortcuts import render
except ImportError:
    from django.views.generic.simple import direct_to_template as render

urlpatterns = patterns('',
    url(r'^yandex/', include('yandex_maps.urls')),
    url(r'^$', lambda request: render(request, 'index.html'), name='index')
)
