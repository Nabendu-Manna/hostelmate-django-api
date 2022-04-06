from django.urls import include, path
from django.contrib import admin
from . import views
from django.conf.urls import url
from rest_framework import routers



urlpatterns = [
    path(r'^admin/', admin.site.urls),
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]