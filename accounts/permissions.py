from rest_framework import permissions
from django.utils.translation import gettext_lazy as _

class IsUserLandlord(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated or not hasattr(request.user, "landlordprofile"):
            # raise ValueError(_("You don't have the permission to access this API."))
            return False
        else:
            return True
        

        