===========
yandex-maps
===========

Библиотека для работы с API Яндекс.Карт. Умеет работать с геокодером и
формировать адреса статичных карт. Опционально - интеграция с Django:
кеширование результатов геокодирования, шаблонный фильтр для вывода карт.
Лицензия MIT.


Установка
=========

::

    pip install yandex-maps

Использование
=============

::

    >>> from yandex_maps import api
    >>> api_key = 'my_api_key'
    >>> pos = api.geocode(api_key, u'Санкт-Петербург, Бумажная 4')
    >>> print pos
    [u'30.271446', u'59.903300']

    >>> api.get_map_url(api_key, float(pos[0]), float(pos[1]), 13, 200, 300)
    http://static-maps.yandex.ru/1.x/?ll=30.2714460,59.9033000&size=200,300&z=12&l=map&pt=30.2714460,59.9033000&key=my_api_key


Интеграция с django
===================

1. В settings.py нужно добавить переменную YANDEX_MAPS_API_KEY со
своим API-ключом от Яндекса. Ключ можно получить тут:
http://api.yandex.ru/maps/form.xml/

2. Добавить 'yandex_maps' в INSTALLED_APPS

TODO: дописать
