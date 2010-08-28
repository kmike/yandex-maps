from django.conf.urls.defaults import *

urlpatterns = patterns('yandex_maps.views',
    url(r'^map/(?P<map_id>\d+)/$', 'yandex_map', name='yandex_map'),
)
