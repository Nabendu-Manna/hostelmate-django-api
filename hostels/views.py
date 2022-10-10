from django.shortcuts import render
from os import path
from sqlite3 import IntegrityError
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework import status
from rest_framework import viewsets
from django.http import HttpResponse
from django.views import View
from rest_framework.views import APIView
from django.http import Http404
from django.db import transaction

from .models import Room, RoomImage
from accounts.models import User, LandlordProfile
from hostels.serializers import RoomSerializer
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsUserLandlord

class RoomView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        try:
            room = Room.objects.all()
        except:
            return Response({}, status = status.HTTP_400_BAD_REQUEST)
        
        serializer = RoomSerializer(room, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

            


