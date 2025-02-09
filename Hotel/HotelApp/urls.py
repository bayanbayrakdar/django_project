from django.urls import path
from . import views
urlpatterns = [
    path('',views.HotelApp),
    path('RoomAll/',views.RoomAll),
    path('RoomUpdate/<int:id>',views.update_room),
    path('RoomDelete/<int:id>',views.delete_room),
    path('RoomAdd/',views.add_room),
    path('RoomFilter/',views.RoomFilter.as_view()),
    path('RoomSearch/',views.RoomSearch.as_view()),
]