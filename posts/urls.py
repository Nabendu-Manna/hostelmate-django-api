from django.urls import path

from hostelmate import settings
from .views import RoomPostView

urlpatterns = [
    path('room/', RoomPostView.as_view()),
]