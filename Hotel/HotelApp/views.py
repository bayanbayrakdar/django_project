from calendar import c
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.
from rest_framework import generics,filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view


@api_view(['GET'])
def HotelApp(request):
    api_urls = {
        'welcome message':'/hotelapp',
        'all_Room': '/RoomAll',
        'Add': '/RoomAdd',
        'Update': '/RoomUpdate/pk',
        'Delete': '/RoomDelete/pk',
        'Filter': '/RoomFilter',
        'Search': '/RoomSearch',
    }
    return Response(api_urls)
####### Room Management   ##########


# get all rooms
@api_view(['GET'])
def RoomAll(request):
    room=Room.objects.all()
    if room.exists():

        serializer=RoomSerializer(room,many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


# update room
@api_view(['PATCH'])
def update_room(request,id):
    room=request.get(id=id)
    data=RoomSerializer(instance=room,data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# add room
@api_view(['POST'])
def add_room(request):
    item=RoomSerializer(data=request.data,context={'request': request})
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

# delete room
@api_view(['DELETE'])
def delete_room(request, id):
    item = Room.objects.get(id=id)
    item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# filter room
class RoomFilter(generics.ListAPIView):
    queryset=Room.objects.all()
    serializer_class=RoomSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['Room_num','Room_type','Price','Room_status']
    
# search room
class RoomSearch(generics.ListAPIView):
    queryset=Room.objects.all()
    serializer_class=RoomSerializer
    filter_backends=[filters.SearchFilter]
    search_fields=['Room_num','Room_type','Price','Room_status']



###### Booking Management #########