#coding: utf-8
from django.db import models
from django.conf import settings
from yandex_maps import api

YANDEX_KEY = getattr(settings, 'YANDEX_MAPS_API_KEY', None)

def get_static_map_url(longitude, latitude, width=None, height=None, detail_level=14):
    """
    Возвращает адрес статичной карты с учетом настроек в settings.py
    """
    w = int(width) if width else settings.YANDEX_MAPS_W
    h = int(height) if height else settings.YANDEX_MAPS_H
    detail_level = int(detail_level)
    return api.get_map_url(YANDEX_KEY, longitude, latitude, detail_level, w, h)


class MapAndAddress(models.Model):
    address = models.CharField(u'Адрес', max_length=255, blank=True, db_index=True)
    longitude = models.FloatField(u'Долгота', null=True, blank=True)
    latitude = models.FloatField(u'Широта', null=True, blank=True)

    def get_detail_level(self):
        return 5

    def get_map_url(self, width=None, height=None, detail_level = 5):
        if YANDEX_KEY is None:
            return ""
        return get_static_map_url(self.longitude, self.latitude, width, height, detail_level)

    def get_external_map_url(self, detail_level=14):
        return api.get_external_map_url(self.longitude, self.latitude, detail_level)

    def fill_geocode_data(self):
        if YANDEX_KEY is not None:
            self.longitude, self.latitude = api.geocode(settings.YANDEX_MAPS_API_KEY, self.address)

    def save(self, *args, **kwargs):
        # fill geocode data if it is unknown
        if self.pk or (self.longitude is None) or (self.latitude is None):
            self.fill_geocode_data()
        super(MapAndAddress, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.address
