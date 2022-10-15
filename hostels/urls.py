from django.urls import path
from hostelmate import settings
from .views import RoomDetailsView, RoomView

urlpatterns = [
    path('room/', RoomView.as_view(), name="room-list"),
    path('room/<int:pk>/', RoomDetailsView.as_view(), name="room-details"),
]

# if settings.DEBUG:
#     from django.conf.urls.static import static
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
