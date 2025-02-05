from rest_framework import serializers
from .models import Room,User,Booking,Customer

class RoomSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Room
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):  
    class Meta:
        model = User
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Booking
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Customer
        fields = '__all__'