from calendar import c
from django.shortcuts import render
from .models import *
from .serializers import *
# Create your views here.
from rest_framework import generics,filters
from django_filters.rest_framework import DjangoFilterBackend

class RoomList(generics.ListAPIView):
    queryset=Room.objects.all()
    serializer_class=RoomSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['Room_num','Room_type','Price','Room_status']
    search_fields=['Room_num','Room_type','Price','Room_status']

class RoomSearch(generics.ListAPIView):
    queryset=Room.objects.all()
    serializer_class=RoomSerializer
    filter_backends=[filters.SearchFilter]
    search_fields=['Room_num','Room_type','Price','Room_status']

class manageRoom(generics.ListAPIView):
    queryset=Room.objects.all()
    serializer_class=RoomSerializer