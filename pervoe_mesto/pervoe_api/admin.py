from django.contrib import admin
from .models import Apartment

@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('room_type', 'area', 'image')
    list_filter = ('room_type', 'area')
    search_fields = ('room_type', 'area')