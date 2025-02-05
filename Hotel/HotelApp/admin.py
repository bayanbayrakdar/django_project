from django.contrib import admin
from .models import *
# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_display=['Room_num','Room_type','Price','Room_status']

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Room,RoomAdmin)
admin.site.register(Booking)

