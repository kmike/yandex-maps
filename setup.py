#!/usr/bin/env python
from distutils.core import setup

# hack for utf8 long_description support
import sys
reload(sys).setdefaultencoding("UTF-8")

version='0.6.1'

setup(
    name = 'yandex-maps',
    version = version,
    author = 'Mikhail Korobov',
    author_email = 'kmike84@gmail.com',
    url = 'https://bitbucket.org/kmike/yandex-maps/',

    description = 'Yandex.Maps API python wrapper with optional django integration.',
    long_description = open('README.rst').read().decode('utf8') + open('CHANGES.rst').read().decode('utf8'),
    license = 'MIT license',
    requires = ['django (>=1.2)'],

    packages=['yandex_maps', 'yandex_maps.templatetags', 'yandex_maps.migrations'],
    package_data={'yandex_maps': ['templates/yandex_maps/*']},

    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Natural Language :: Russian',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
