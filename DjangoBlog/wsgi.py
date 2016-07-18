"""
WSGI config for DjangoBlog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
from django.conf import settings

sys.path.append(settings.BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoBlog.settings")

application = get_wsgi_application()
