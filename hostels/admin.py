from csv import list_dialects
from django.contrib import admin
from hostels.models import Room, RoomImage

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'landlord', 'address', 'town', 'district', 'state', 'pin', 'phone']

@admin.register(RoomImage)
class RoomImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'room', 'room_image']
