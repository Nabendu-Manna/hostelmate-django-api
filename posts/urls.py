from django.urls import path

from hostelmate import settings

from .views import RoomPostDetailsView, RoomPostImagesView, RoomPostView

urlpatterns = [
    path('room/', RoomPostView.as_view()),
    path('room/<int:pk>', RoomPostDetailsView.as_view()),
    path('room/<int:pk>/image/', RoomPostImagesView.as_view())
]