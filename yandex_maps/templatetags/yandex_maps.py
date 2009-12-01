#coding: utf-8
from django import template

register = template.Library()

@register.filter
def static_map_url(address, params=None):
    ''' Фильтр, который возвращает URL картинки с картой.
        Применять на объект класса MapAndAddress.
        Параметры: ширина, высота, уровень детализации - через запятую
        без пробелов.
    '''
    data = [] if params is None else params.split(",")
    try:
        return address.get_map_url(*data)
    except:
        return ''