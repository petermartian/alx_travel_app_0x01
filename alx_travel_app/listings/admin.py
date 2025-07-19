from django.contrib import admin
from .models import Listing

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price', 'available', 'created_at')
    list_filter  = ('available', 'location')
    search_fields = ('title', 'description')
