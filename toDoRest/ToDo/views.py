from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ToDoSerializer
from rest_framework import viewsets
from .models import Todo
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


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







#authuntication
from rest_framework.permissions import IsAuthenticated


class Hello(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        content={'message' : 'hello world'}
        return Response(content)

class deletetoken(APIView):
    permission_classes=(IsAuthenticated,)
    def detete(self,request,id):
        item = Todo.objects.get(id=id)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DeleteToken(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, id):
        try:
            item = Todo.objects.get(id=id)
            item.delete()
            return Response({"message": "delete done" }, status=status.HTTP_204_NO_CONTENT)
        except Todo.DoesNotExist:
            return Response({"error": "not found item"}, status=status.HTTP_404_NOT_FOUND)