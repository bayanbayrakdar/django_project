from django.urls import path , include 

from rest_framework import serializers
from rest_framework.routers import DefaultRouter
from .views import add_task ,update_task,delete_task,view_task
# router=DefaultRouter()
# router.register('ToDo',getTasks)
from . import views

# urlpatterns = [
#     path('', include(router.urls)), 
# ]
urlpatterns = [
    path('', views.ApiOverview, name='home'),
    # path('', getTasks, name='getTasks'),
    path('create/',add_task, name='add_task'),
    path('all/',view_task, name='view_task'),
    path('update/<int:id>',update_task, name='update_task'),
    path('item/<int:id>/delete/',delete_task, name='delete_task'),

]