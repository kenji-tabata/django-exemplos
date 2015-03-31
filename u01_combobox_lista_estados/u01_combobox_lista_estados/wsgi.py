"""
WSGI config for u01_combobox_lista_estados project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "u01_combobox_lista_estados.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
