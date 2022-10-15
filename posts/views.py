from django.shortcuts import render
from os import path
from sqlite3 import IntegrityError
from django.http import JsonResponse

from django.http import HttpResponse
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from django.views import View
from django.db import transaction
from django.template import RequestContext

from accounts.permissions import IsUserLandlord
from rest_framework.permissions import IsAuthenticated

from .models import RoomPostImage, RoomPost
from accounts.models import User, LandlordProfile

from posts.serializers import RoomPostSerializer

class RoomPostView(APIView):
    permission_classes = [IsAuthenticated, IsUserLandlord]
    def get(self, request, *args, **kwargs):
        try:
            room = RoomPost.objects.all()
        except:
            return Response({}, status = status.HTTP_400_BAD_REQUEST)
        
        serializer = RoomPostSerializer(room, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        result = RequestContext(request, {"landlord": request.user.landlordprofile})
        serializer = RoomPostSerializer(data = request.data)
        if serializer.is_valid():
            roomPost = serializer.save()
            return Response({"post_id": roomPost.id, "massage": "Successfully Created."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

