#coding: utf-8
from django import template
from django.utils.html import conditional_escape
from yandex_maps.models import MapAndAddress
register = template.Library()

def _url_for(address, *args, **kwargs):
    if not isinstance(address, MapAndAddress):
        address, created = MapAndAddress.objects.get_or_create(address=address)
    try:
        return address.get_map_url(*args, **kwargs)
    except:
        return ''

@register.filter
def static_map_url(address, params=None):
    '''Фильтр, который возвращает URL картинки с картой.
    Можно применять к объекту класса MapAndAddress или к строке с адресом.
    Параметры: ширина, высота, уровень детализации - через запятую без пробелов.

    Пример:

        <img src='{{ address|static_map_url:"300,200" }}'>

    '''
    data = [] if params is None else params.split(",")
    return _url_for(address, *data)


@register.simple_tag
def yandex_map(address, width, height, zoom = 14):
    '''Тег, который выводит <img> с картой.

    Параметры:

        1. адрес (строка или объект класса MapAndAddress)
        2. ширина
        3. высота
        4. уровень детализации (по умолчанию = 14)

    Пример:

        {% yandex_map "Санкт-Петербург, ул. Бумажная 4" 300 200 8 %}

    '''
    url = _url_for(address, width, height, zoom)
    return "<img src='%s' width='%s' height='%s' alt='%s' />" % (
             url, width, height, conditional_escape(address))
