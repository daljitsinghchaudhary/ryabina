# coding=utf-8
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SECRET_KEY = '25-*3+#l8btg4y59xyqciu@u*60^$lfe&y3c7*y@cx_!zx*a85'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'tinymce',
    'filebrowser',
    'sorl.thumbnail',
    'treebeard',
    'django_mailer',
    'request_provider',
    'bootstrap3',
    'captcha',
    'django_comments',
    'newsletter',
    'apps.pages',
    'apps.slideshow',
    'apps.services',
    'apps.discounts',
    'apps.newsboard',
    'apps.statictext',
    'apps.questions',
    'apps.custom_comments'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'request_provider.middleware.RequestProvider',
)

ROOT_URLCONF = 'ryabina.urls'

TEMPLATES = [{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.template.context_processors.media',
                'django.contrib.messages.context_processors.messages',
                'annoying.context_processors.site_constants',
                'annoying.context_processors.questions_forms',
            ]
        },
    },
]

WSGI_APPLICATION = 'ryabina.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ryabina',
        'USER': 'root',
        'PASSWORD': 'progress',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

SITE_TITLE = u'Стоматологический центр "Рябина"'

LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'Etc/GMT-3'
USE_I18N = True
USE_L10N = True
USE_TZ = True

SITE_ID=1

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'public')

ADMINS = (
    ('a.sinyavskiy', 'sinyawskiy@gmail.com'),
)

MANAGERS = ADMINS

THUMBNAIL_BASEDIR = '_thumbs'
THUMBNAIL_EXTENSION = 'png'
THUMBNAIL_PROCESSORS = (
    # 'apps.utils.thumb.colorspace',
    'sorl.thumbnail.processors.colorspace',
    'sorl.thumbnail.processors.autocrop',
    'sorl.thumbnail.processors.scale_and_crop',
    'sorl.thumbnail.processors.filters',
)

FILEBROWSER_DIRECTORY = 'filebrowser/'
# FILEBROWSER_URL_FILEBROWSER_MEDIA = os.path.join(STATIC_URL, 'filebrowser/')
# FILEBROWSER_PATH_FILEBROWSER_MEDIA = os.path.join(STATIC_ROOT, 'filebrowser/')

COMMENTS_APP = 'apps.custom_comments'
COMMENTS_PHOTO_DELETE_TIMEOUT = 3600 #seconds
COMMENTS_ALLOW_PROFANITIES = True

CAPTCHA_LENGTH = 3
# CAPTCHA_FONT_PATH = os.path.join(STATIC_ROOT, 'captcha', 'fonts', 'Vera.ttf')
CAPTCHA_FONT_PATH = os.path.join(STATIC_ROOT, 'font', 'bliss', 'BlissPro-Light.ttf')
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'
CAPTCHA_NOISE_FUNCTIONS = ('captcha.helpers.noise_dots',)
CAPTCHA_LETTER_ROTATION = (-10, 10)
CAPTCHA_OUTPUT_FORMAT = u'%(hidden_field)s <div class="input-group"><span class="input-group-addon">%(image)s</span>%(text_field)s</div>'

EMAIL_BACKEND = 'django_mailer.smtp_queue.EmailBackend'
MAILER_EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_ADDRESS_FROM = u'"Стоматологический центр Рябина" <privet@ryabinaclinic.ru>'
DEFAULT_FROM_EMAIL = EMAIL_ADDRESS_FROM

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_HOST_USER = 'stomryabina@yandex.ru'
EMAIL_HOST_PASSWORD = 'QLnFsafIeU'
EMAIL_USE_SSL = True
EMAIL_USE_TLS = False
EMAIL_PORT = 465

DEFAULT_NEWSLETTER_EMAIL = u'info@ryabinaclinic.ru'
DEFAULT_NEWSLETTER_SENDER = u'"Стоматологический центр Рябина"'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
            },
        # 'file': {
        #     'level': 'DEBUG',
        #     'class': 'logging.FileHandler',
        #     'filename': '/path/to/your/file.log',
        #     'formatter': 'simple'
        #     },
    },
    'loggers': {
        'debug': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
            },
        'sql': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
            },
        'signals': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
            },
    }
}

MAX_ATTACH_FEEDBACK_FILE_SIZE = 5*1024*1024

QR_PASS_PHRASE = 'QT8asdSN_TWC4A-QEAEhj4MFY2O=='