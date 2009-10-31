#coding: utf-8
from generic_utils.test_helpers import ViewTest

class YandexMapTest(ViewTest):
    
    fixtures=['yandex_maps']

    def test_views(self):
        self.check_url('yandex_map', kwargs={'map_id': 1})
        self.check_url('yandex_map', 404, kwargs={'map_id': 4})
        