#coding: utf-8
from django.db import models
from django.conf import settings
from django.utils.encoding import smart_str

from yandex_maps import utils

YANDEX_KEY = getattr(settings, 'YANDEX_MAPS_API_KEY', None)

class MapAndAddress(models.Model):

    address = models.CharField(u'Адрес', max_length=300, blank=True)
    longtitude = models.FloatField(u'Долгота', null=True, blank=True)
    latitude = models.FloatField(u'Широта', null=True, blank=True)

    def get_detail_level(self):
        return 5

    def get_map_url(self, width=None, height=None, detail_level = 5):
        w = int(width) if width else settings.YANDEX_MAPS_W
        h = int(height) if height else settings.YANDEX_MAPS_H
        detail_level = int(detail_level) or self.get_detail_level()
        if YANDEX_KEY is not None:
            return utils.get_map_url(YANDEX_KEY, self.longtitude, self.latitude, detail_level, w, h)
        else:
            return ''

    def fill_geocode_data(self):
        if YANDEX_KEY is not None:
            (self.longtitude, self.latitude) = utils.geocode(settings.YANDEX_MAPS_API_KEY, smart_str(self.address))

    def save(self, *args, **kwargs):
        if self.pk or (self.longtitude is None) or (self.latitude is None): # don't fill geocode data if it is known already
            self.fill_geocode_data()
        super(MapAndAddress, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.address

