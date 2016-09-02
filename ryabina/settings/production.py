# coding=utf-8
from .base import *

DEBUG = TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'ryabina.spb.ru', 'www.ryabina.spb.ru', 'ryabina-stom.ru', 'www.ryabina-stom.ru', 'xn----7sbc2awdjkok0l.xn--p1ai','www.xn----7sbc2awdjkok0l.xn--p1ai', 'ryabinaclinic.ru', 'www.ryabinaclinic.ru']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ryabina',
        'USER': 'django',
        'PASSWORD': 'progress',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

FORCE_SCRIPT_NAME = ''

EMAIL_ADDRESS_FROM = '"Стоматологический центр Рябина" <privet@ryabinaclinic.ru>'
DEFAULT_FROM_EMAIL = EMAIL_ADDRESS_FROM
EMAIL_HOST = '127.0.0.1'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_SSL = False
EMAIL_USE_TLS = False
EMAIL_PORT = 25