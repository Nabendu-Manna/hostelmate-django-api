from django.shortcuts import get_object_or_404, render
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
from django.template import RequestContext

class RoomView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        try:
            room = Room.objects.all()
        except:
            return Response({}, status = status.HTTP_400_BAD_REQUEST)
        
        serializer = RoomSerializer(room, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        permission_classes = [IsAuthenticated, IsUserLandlord]
        requeste = RequestContext(request, {'landlord': request.user.landlordprofile})
        roomData = request.data 
        roomData["landlord"] = request.user.landlordprofile.id
        serializer = RoomSerializer(data = request.data)
        if serializer.is_valid():
            room = serializer.save()
            return Response({"room_id": room.id, "massage": "Successful"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoomDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, *args, **kwargs):
        try:
            room = Room.objects.objects.get(pk=pk)
        except:
            return Response({}, status = status.HTTP_400_BAD_REQUEST)
        
        serializer = RoomSerializer(room, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def patch(self, request, pk, *args, **kwargs):
        room = Room.objects.get(pk=pk)
        serializer = RoomSerializer(instance=room, data=request.data)
    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, *args, **kwargs):
        room = get_object_or_404(Room, pk=pk)
        room.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
