import os

from src.infrastructure.settings.base import *


# SECURITY WARNING: keep the secret key used in production secret!

DEBUG = True

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ.get('DEV_POSTGRES_DB'),
#         'USER': os.environ.get('DEV_POSTGRES_USER'),
#         'PASSWORD': os.environ.get('DEV_POSTGRES_PASSWORD'),
#         'HOST': os.environ.get('DEV_POSTGRES_HOST'),
#         'PORT': os.environ.get('DEV_POSTGRES_PORT'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Configuration of the email server.
# https://docs.djangoproject.com/en/5.0/topics/email/

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = os.environ.get(''),
EMAIL_HOST_USER = os.environ.get(''),
EMAIL_HOST_POSSWORD = os.environ.get(''),
EMAIL_PORT = os.environ.get(''),
EMAIL_USE_TLS = True


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
    'SLIDING_TOKEN_LIFETIME': timedelta(days=30),
    'SLIDING_TOKEN_REFRESH_LIFETIME_LATE_USER': timedelta(days=1),
    'SLIDING_TOKEN_LIFETIME_LATE_USER': timedelta(days=30),
}
