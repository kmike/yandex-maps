#!/usr/bin/env python
from distutils.core import setup

# hack for utf8 long_description support
import sys
reload(sys).setdefaultencoding("UTF-8")

setup(
      name='django-yandex-maps',
      version='0.2',
      author='Mikhail Korobov',
      author_email='kmike84@gmail.com',
      url='http://bitbucket.org/kmike/django-yandex-maps/',

      description = 'Django app for Yandex Maps integration.',
      license = 'MIT license',
      packages=['yandex_maps', 'yandex_maps.templatetags'],

      package_data={'yandex_maps': ['templates/yandex_maps/*']},

      requires = ['django (>=1.0)'],
      long_description = open('README.rst').read().decode('utf8'),

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
