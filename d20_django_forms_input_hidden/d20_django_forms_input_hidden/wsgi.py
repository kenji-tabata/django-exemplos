"""
WSGI config for d20_django_forms_input_hidden project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "d20_django_forms_input_hidden.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
