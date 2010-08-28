# coding: utf-8

# Yandex maps API wrapper.

import xml.dom.minidom
import urllib
from yandex_maps import http

STATIC_MAPS_URL = 'http://static-maps.yandex.ru/1.x/?'
GEOCODE_URL = 'http://geocode-maps.yandex.ru/1.x/?'

def get_map_url(api_key, longtitude, latitude, zoom, width, height):
    ''' returns URL of static yandex map '''
    params = [
       'll=%0.7f,%0.7f' % (longtitude, latitude,),
       'size=%d,%d' % (width, height,),
       'z=%d' % zoom,
       'l=map',
       'pt=%0.7f,%0.7f' % (longtitude, latitude,),
       'key=%s' % api_key
    ]
    return STATIC_MAPS_URL + '&'.join(params)

def geocode(api_key, address, timeout=2):
    ''' returns (longtitude, latitude,) tuple for given address '''
    if isinstance(address, unicode):
        address = address.encode('utf8')
    params = urllib.urlencode({'geocode': address, 'key': api_key})
    url = GEOCODE_URL + params
    try:
        status_code, response = http.request('GET', url, timeout=timeout)
    except IOError:
        return None, None
    return _get_coords(response)

def _get_coords(response):
    try:
        dom = xml.dom.minidom.parseString(response)
        pos_elem = dom.getElementsByTagName('pos')[0]
        pos_data = pos_elem.childNodes[0].data
        return pos_data.split()
    except IndexError:
        return None, None
