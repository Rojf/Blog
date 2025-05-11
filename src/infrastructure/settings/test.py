import os

from src.infrastructure.settings.base import *


SECRET_KEY = os.getenv('SECRET_KEY', '')

DEBUG = True

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': os.environ.get('POSTGRES_PORT'),
    }
}

# Configuration of the email server.
# https://docs.djangoproject.com/en/5.0/topics/email/

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

