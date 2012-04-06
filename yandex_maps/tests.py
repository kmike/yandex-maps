#coding: utf-8
from unittest import TestCase
from yandex_maps.api import _get_coords, get_map_url

RESPONSE = u"""<?xml version="1.0" encoding="utf-8"?>
<ymaps xmlns="http://maps.yandex.ru/ymaps/1.x" xmlns:x="http://www.yandex.ru/xscript">
  <GeoObjectCollection>
    <metaDataProperty xmlns="http://www.opengis.net/gml">
      <GeocoderResponseMetaData xmlns="http://maps.yandex.ru/geocoder/1.x">
        <request>Екатеринбург, Свердлова 27</request>
        <found>1</found>
        <results>10</results>
      </GeocoderResponseMetaData>
    </metaDataProperty>
    <featureMember xmlns="http://www.opengis.net/gml">
      <GeoObject xmlns="http://maps.yandex.ru/ymaps/1.x">
        <metaDataProperty xmlns="http://www.opengis.net/gml">
          <GeocoderMetaData xmlns="http://maps.yandex.ru/geocoder/1.x">
            <kind>house</kind>
            <text>Россия, Свердловская область, Екатеринбург, улица Свердлова, 27</text>
            <precision>number</precision>
            <AddressDetails xmlns="urn:oasis:names:tc:ciq:xsdschema:xAL:2.0">
              <Country>
                <CountryName>Россия</CountryName>
                <AdministrativeArea>
                  <AdministrativeAreaName>Свердловская область</AdministrativeAreaName>
                  <Locality>
                    <LocalityName>Екатеринбург</LocalityName>
                    <Thoroughfare>
                      <ThoroughfareName>улица Свердлова</ThoroughfareName>
                      <Premise>
                        <PremiseNumber>27</PremiseNumber>
                      </Premise>
                    </Thoroughfare>
                  </Locality>
                </AdministrativeArea>
              </Country>
            </AddressDetails>
          </GeocoderMetaData>
        </metaDataProperty>
        <boundedBy xmlns="http://www.opengis.net/gml">
          <Envelope>
            <lowerCorner>60.599720 56.852332</lowerCorner>
            <upperCorner>60.607931 56.856830</upperCorner>
          </Envelope>
        </boundedBy>
        <Point xmlns="http://www.opengis.net/gml">
          <pos>60.603826 56.854581</pos>
        </Point>
      </GeoObject>
    </featureMember>
  </GeoObjectCollection>
</ymaps>
""".encode('utf8')

UNKNOWN_ADDRESS = u'''<?xml version="1.0" encoding="utf-8"?>
<ymaps xmlns="http://maps.yandex.ru/ymaps/1.x" xmlns:x="http://www.yandex.ru/xscript">
  <GeoObjectCollection>
    <metaDataProperty xmlns="http://www.opengis.net/gml">
      <GeocoderResponseMetaData xmlns="http://maps.yandex.ru/geocoder/1.x">
        <request>Екатеринбург, Свердлова 87876</request>
        <found>0</found>
        <results>10</results>
      </GeocoderResponseMetaData>
    </metaDataProperty>
  </GeoObjectCollection>
</ymaps>
'''.encode('utf8')

TEST_API_KEY = 'vasia'
COORDS = (u'60.603826', u'56.854581')
MAP_URL = 'http://static-maps.yandex.ru/1.x/?ll=60.6038260,56.8545810&size=200,300&z=5&l=map&pt=60.6038260,56.8545810&key=vasia'

class GeocodeParsingTest(TestCase):
    def test_parsing(self):
        self.assertEqual(_get_coords(RESPONSE), COORDS)

    def test_unknown(self):
        self.assertEqual(_get_coords(UNKNOWN_ADDRESS), (None, None,))


# FIXME: тест полагается на порядок параметров в url
class MapUrlTest(TestCase):
    def test_map_url(self):
        url = get_map_url(TEST_API_KEY, COORDS[0], COORDS[1], 5, 200, 300)
        self.assertEqual(url, MAP_URL)
