from django.contrib import admin
from django.shortcuts import redirect        # ← add this
from django.urls import path, include

# if you factored swagger out to swagger.py
from .swagger import schema_view      

urlpatterns = [
    # redirect root “/” to swagger UI
    path('', lambda req: redirect('schema-swagger-ui', permanent=False)),

    path('admin/', admin.site.urls),
    path('api/listings/', include('listings.urls')),

    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/',    schema_view.with_ui('swagger', cache_timeout=0),  name='schema-swagger-ui'),
    path('redoc/',      schema_view.with_ui('redoc',   cache_timeout=0),  name='schema-redoc'),
]
