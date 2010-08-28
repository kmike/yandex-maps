#coding: utf-8
import os, sys
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(PROJECT_ROOT, '..')))

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = ':memory:'
ROOT_URLCONF = 'urls'
TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, 'templates'),)

YANDEX_MAPS_API_KEY = 'sdfkjhg'
INSTALLED_APPS=('yandex_maps', 'test_app')
