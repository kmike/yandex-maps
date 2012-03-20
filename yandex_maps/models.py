#coding: utf-8
from django.db import models
from django.conf import settings
from yandex_maps import api

YANDEX_KEY = getattr(settings, 'YANDEX_MAPS_API_KEY', None)

class MapAndAddress(models.Model):
    address = models.CharField(u'Адрес', max_length=255, blank=True, db_index=True)
    longitude = models.FloatField(u'Долгота', null=True, blank=True)
    latitude = models.FloatField(u'Широта', null=True, blank=True)

    def get_detail_level(self):
        return 5

    def get_map_url(self, width=None, height=None, detail_level = 5):
        w = int(width) if width else settings.YANDEX_MAPS_W
        h = int(height) if height else settings.YANDEX_MAPS_H
        detail_level = int(detail_level) or self.get_detail_level()

        if YANDEX_KEY is not None:
            return api.get_map_url(YANDEX_KEY, self.longitude, self.latitude, detail_level, w, h)
        else:
            return ''

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
