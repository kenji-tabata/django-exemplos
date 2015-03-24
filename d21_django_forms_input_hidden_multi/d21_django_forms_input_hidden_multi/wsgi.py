"""
WSGI config for d21_django_forms_input_hidden_multi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "d21_django_forms_input_hidden_multi.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
