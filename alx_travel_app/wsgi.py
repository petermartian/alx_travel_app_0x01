import os
from django.core.wsgi import get_wsgi_application

# Point to your settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alx_travel_app.settings')

application = get_wsgi_application()
