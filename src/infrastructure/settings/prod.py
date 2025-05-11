import os
from src.infrastructure.settings.base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', '')

INSTALLED_APPS += [
    'rest_framework_simplejwt.token_blacklist',
]

DEBUG = False

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('HOST', 'db'),
        'PORT': os.getenv('POSTGRES_PORT'),
    }
}

# Configuration of the email server.
# https://docs.djangoproject.com/en/5.0/topics/email/

EMAIL_HOST = os.getenv(''),
EMAIL_HOST_USER = os.getenv(''),
EMAIL_HOST_POSSWORD = os.getenv(''),
EMAIL_PORT = os.getenv(''),
EMAIL_USE_TLS = True


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=5),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=2),
    'SLIDING_TOKEN_LIFETIME': timedelta(days=1),
    'SLIDING_TOKEN_REFRESH_LIFETIME_LATE_USER': timedelta(days=1),
    'SLIDING_TOKEN_LIFETIME_LATE_USER': timedelta(days=30),
}
