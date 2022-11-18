import json
from os import path
from sqlite3 import IntegrityError
from webbrowser import get

from django.db import transaction
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext
from django.views import View
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView

from accounts.models import LandlordProfile, User
from accounts.permissions import IsUserLandlord
from hostels.models import Room
from posts.serializers import RoomPostImagesSerializer, RoomPostSerializer

from .models import RoomPost, RoomPostImage


class RoomPostView(APIView):
    permission_classes = [IsAuthenticated, IsUserLandlord]
    def get(self, request, *args, **kwargs):
        try:
            roomPost = RoomPost.objects.all()
        except:
            return Response({}, status = status.HTTP_400_BAD_REQUEST)
        
        serializer = RoomPostSerializer(roomPost, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        room = get_object_or_404(Room, id=request.data["room"])
        result = RequestContext(request, {
            "landlord": request.user.landlordprofile,
            "room": room
        })
        print(request.data)
        serializer = RoomPostSerializer(data = request.data)
        if serializer.is_valid():
            roomPost = serializer.save()
            return Response({"post_id": roomPost.id, "massage": "Successfully Created."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoomPostDetailsView(APIView):
    permission_classes = [IsAuthenticated, IsUserLandlord]
    def get(self, request, pk, *args, **kwargs):
        # try:
        #     roomPost = RoomPost.objects.get(id=pk)
        # except:
        #     return Response({}, status = status.HTTP_400_BAD_REQUEST)
        roomPost = get_object_or_404(RoomPost, id=pk)
        serializer = RoomPostSerializer(roomPost)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def patch(self, request, pk, *args, **kwargs):
        roomPost = get_object_or_404(RoomPost, id=pk)
        serializer = RoomPostSerializer(instance = roomPost, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTT_202_ACCEPTED)
        else: 
            return Response({}, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        roomPost = get_object_or_404(RoomPost, id=pk)
        roomPost.delete()
        return Response({"massage": "Successfully deleted."}, status=status.HTTP_202_ACCEPTED)

class RoomPostImagesView(APIView):
    permission_classes = [IsAuthenticated, IsUserLandlord]
    
    def post(self, request, pk, *args, **kwargs):
        room_post = get_object_or_404(RoomPost, id=pk)
        payload = request.data.copy()
        payload['room_post'] = pk
        serializer = RoomPostImagesSerializer(data = payload)
        if serializer.is_valid():
            roomPostImages = serializer.save()
            return Response({"room_post_images": roomPostImages.id, "massage": "Successfully Created."}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)