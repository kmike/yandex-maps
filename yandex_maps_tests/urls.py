from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^yandex/', include('yandex_maps.urls')),
)
