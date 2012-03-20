from django.shortcuts import get_object_or_404
from django.views.generic.simple import direct_to_template
from django.conf import settings
from yandex_maps.models import MapAndAddress

def yandex_map(request, map_id):
    map = get_object_or_404(MapAndAddress, id=map_id)
    api_key = settings.YANDEX_MAPS_API_KEY
    return direct_to_template(request, 'yandex_maps/map.html', {
                                 'longitude': map.longitude,
                                 'latitude': map.latitude,
                                 'api_key': api_key,
                                 'detail': 15,
                                 'address' : map.address,
                             })
