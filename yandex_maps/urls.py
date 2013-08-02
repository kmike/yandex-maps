try:
    from django.conf.urls import patterns, url, handler500
except ImportError:
    from django.conf.urls.defaults import patterns, url, handler500


urlpatterns = patterns('yandex_maps.views',
    url(r'^map/(?P<map_id>\d+)/$', 'yandex_map', name='yandex_map'),
)
