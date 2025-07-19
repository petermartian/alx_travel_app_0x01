import os
from django.core.asgi import get_asgi_application

# Point to your settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alx_travel_app.settings')

application = get_asgi_application()
