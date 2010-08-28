#coding: utf-8
from django.core.urlresolvers import reverse
from django.test import TestCase

class YandexMapTest(TestCase):
    fixtures=['yandex_maps']

    def _check_url(self, url_name, status=200, **kwargs):
        url = reverse(url_name, kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status)
        return response

    def test_views(self):
        self._check_url('yandex_map', map_id=1)
        self._check_url('yandex_map', 404, map_id=4)
