#!/usr/bin/env python
from distutils.core import setup

setup(
      name='django-yandex-maps',
      version='0.2',
      author='Mikhail Korobov',
      author_email='kmike84@gmail.com',
      url='http://bitbucket.org/kmike/django-yandex-maps/',

      description = 'Django app for work with Yandex Maps service.',
      license = 'MIT license',
      packages=['yandex_maps', 'yandex_maps.templatetags'],

      package_data={'yandex_maps': ['templates/yandex_maps/*']},

      requires = ['django (>=1.0)', 'BeautifulSoup'],

      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Plugins',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Natural Language :: Russian',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
)