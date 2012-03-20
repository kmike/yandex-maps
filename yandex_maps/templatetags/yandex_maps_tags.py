#coding: utf-8
from django import template
from django.contrib.gis.geos import Point
from django.utils.html import conditional_escape
from yandex_maps.models import MapAndAddress, get_static_map_url
register = template.Library()

def _url_for(address, *args, **kwargs):
    if isinstance(address, Point):
        return get_static_map_url(address.x, address.y, *args, **kwargs)

    if not isinstance(address, MapAndAddress):
        address, created = MapAndAddress.objects.get_or_create(address=address)
    try:
        return address.get_map_url(*args, **kwargs)
    except:
        return ''

@register.filter
def static_map_url(address, params=None):
    '''Фильтр, который возвращает URL картинки с картой.
    Можно применять к объекту класса MapAndAddress, к строке с адресом
    или к экземпляру Point из GeoDjango (например, PointField с координатами).

    Параметры: ширина, высота, уровень детализации - через запятую без пробелов.

    Пример:

        <img src='{{ address|static_map_url:"300,200" }}'>

    '''
    data = [] if params is None else params.split(",")
    return _url_for(address, *data)


@register.simple_tag
def yandex_map(address, width, height, zoom = 14, attrs=''):
    '''Тег, который выводит <img> с картой.

    Параметры:

        1. адрес (строка с адресом, объект класса MapAndAddress или Point из GeoDjango)
        2. ширина
        3. высота
        4. уровень детализации (по умолчанию = 14)

    Пример:

        {% yandex_map "Санкт-Петербург, ул. Бумажная 4" 300 200 8 %}

    '''
    url = _url_for(address, width, height, zoom)
    return "<img src='%s' width='%s' height='%s' alt='%s' %s />" % (
             url, width, height, conditional_escape(address), attrs)
