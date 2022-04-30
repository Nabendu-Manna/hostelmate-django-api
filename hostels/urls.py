from django.urls import path

from hostelmate import settings
from .views import RoomView

urlpatterns = [
    path('room/', RoomView.as_view()),
]

# if settings.DEBUG:
#     from django.conf.urls.static import static
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
