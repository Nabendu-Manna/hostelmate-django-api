from django.contrib import admin
from hostels.models import Room

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'landlord', 'address', 'town', 'district', 'state', 'pin', 'phone']
