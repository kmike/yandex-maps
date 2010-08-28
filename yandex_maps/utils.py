#coding: utf-8
import xml.dom.minidom
import urllib2
from django.utils.http import urlencode

def get_map_url(API_key, longtitude, latitude, zoom, width, height):
    url = u"http://static-maps.yandex.ru/1.x/?ll=%0.7f,%0.7f&size=%d,%d&z=%d&l=map&pt=%0.7f,%0.7f&key=%s" % \
          (longtitude, latitude, width, height, zoom, longtitude, latitude, API_key)
    return url

def geocode(API_key, address):
    url = u'http://geocode-maps.yandex.ru/1.x/?'
    params = urlencode({'geocode':address,'key':API_key})
    try:
        response = urllib2.urlopen(url+params).read()
    except IOError:
        return (None, None,)
    return _parse_response(response)

def _parse_response(response):
    try:
        dom = xml.dom.minidom.parseString(response)
        pos_elem = dom.getElementsByTagName('pos')[0]
        pos_data = pos_elem.childNodes[0].data
        return pos_data.split()
    except IndexError:
        return None, None
