"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


env = os.environ.get('DJANGO_ENV')
settings_module = f'src.infrastructure.settigns.{env}'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings_module')

application = get_wsgi_application()
