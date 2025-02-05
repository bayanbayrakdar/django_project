from django.core.validators import MinValueValidator
from django.db import models
from django.db.models.fields import validators

# Create your models here.
class User(models.Model):
    user_name=[('admin','admin'),('staff','staff'),('customer','customer')]
    user=models.CharField(max_length=100,choices=user_name)
    password=models.CharField(max_length=100)

# manage room by admin
class Room(models.Model):
    TypeRoom=[('Single','Single'),('Double','Double'),('Suite','Suite')]
    StatusRoom=[('Available','Available'),('Booked','Booked'),('UnderMaintenance','UnderMaintenance')]
    Room_num=models.PositiveIntegerField()
    Room_type=models.CharField(max_length=100,choices=(TypeRoom),default='please selete typr room')
    Price=models.DecimalField(max_digits=10,decimal_places=2,validators=[MinValueValidator(0)])
    Room_status=models.CharField(max_length=100,choices=StatusRoom)

    
    def __str__(self):
        return f"{self.Room_num}/{self.Room_type}"



# manage booking by staff
class Booking(models.Model):
    Room=models.ForeignKey(Room,on_delete=models.CASCADE,limit_choices_to={'Room_status':'Available'})
    check_in=models.DateField()
    check_out=models.DateField()
    avaliable=models.BooleanField(default=False)
    occupied=models.BooleanField(default=False)



class Customer(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)

    
    room=models.ForeignKey(Room,on_delete=models.CASCADE,limit_choices_to={'Room_status':'Available'})

    def __str__(self):
        return self.name


