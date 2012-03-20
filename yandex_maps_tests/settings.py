#coding: utf-8
import os, sys
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(PROJECT_ROOT, '..')))

DEBUG = True
DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = 'db.sqlite'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite'
    }
}
ROOT_URLCONF = 'urls'
TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, 'templates'),)

SECRET_KEY = '123'

# мой ключ для домена example.com
YANDEX_MAPS_API_KEY = "AOmQeUwBAAAAxp1AOQIAlTD0uSCCp1ukf-GmyqC5tbvCGAgAAAAAAAAAAAAeazHdQX6EPpcOJnuUPR-QlXyJPQ=="

INSTALLED_APPS=(
    'yandex_maps',
    'test_app',
#    'devserver',
    'south',
)
