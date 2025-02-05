from django.urls import path
from . import views
urlpatterns = [
    path('',views.RoomList.as_view()),
    path('manageRoom/',views.manageRoom.as_view()),
    path('RoomSearch/',views.RoomSearch.as_view()),
]