from django.shortcuts import render
from .serializers import ToDoSerializer
from rest_framework import viewsets
from .models import Todo
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

# class TaskViewSet(viewsets.ModelViewSet):
#     queryset=Todo.objects.all()
#     serializer_class=ToDoSerializer

from rest_framework.decorators import api_view

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Search by Category': '/?category=category_name',
        'Search by Subcategory': '/?subcategory=category_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }
    return Response(api_urls)



@api_view(['GET'])
def view_task(request):
    items = Todo.objects.all()
    
    if items.exists():
        serializer = ToDoSerializer(items, many=True, context={'request': request})  # Fix: Add many=True
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['PATCH'])
def update_task(request,id):
    item=request.get(id=id)
    data=ToDoSerializer(instance=item,data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_task(request):
    item=ToDoSerializer(data=request.data,context={'request': request})
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_task(request, id):
    item = Todo.objects.get(id=id)
    item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


