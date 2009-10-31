#coding: utf-8

from BeautifulSoup import BeautifulSoup
import urllib
from django.utils.http import urlencode

def get_map_url(API_key, longtitude, latitude, zoom, width, height):
    url = u"http://static-maps.yandex.ru/1.x/?ll=%0.7f,%0.7f&size=%d,%d&z=%d&l=map&pt=%0.7f,%0.7f&key=%s" % \
          (longtitude, latitude, width, height, zoom, longtitude, latitude, API_key)
    return url

def geocode(API_key, address):
    url = u'http://geocode-maps.yandex.ru/1.x/?'
    params = urlencode({'geocode':address,'key':API_key})

    try:
        response = urllib.urlopen(url+params).read()
    except IOError:
        return (None, None,)

    try:
        data = BeautifulSoup(response).find('pos').string.split()
    except AttributeError:
        data = (None,None,)
    return data
