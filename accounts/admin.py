from django.contrib import admin
from accounts.models import CustomerProfile, LandlordProfile, ManagerProfile, User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'email', 'first_name', 'last_name', 'date_of_joining', 'is_active', 'is_deleted', 'created_at', 'modified_at', 'deleted_at', 'created_by', 'modified_by', 'deleted_by',
    ]

@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'user', 'town', 'district', 'state', 'pin', 'phone', 'home_address', 'home_town', 'home_district', 'home_state', 'home_pin',]

@admin.register(LandlordProfile)
class LandlordProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'address', 'town', 'district', 'state', 'pin', 'phone']

@admin.register(ManagerProfile)
class ManagerProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'address', 'town', 'district', 'state', 'pin']

