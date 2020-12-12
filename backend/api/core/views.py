# for django imports
from django.shortcuts import render
from django.http import HttpResponse

#for rest_framework imprts
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#module imports
from .serializers import TodoSerializer, ProjectSerializer
from .models import Todo, Project

# views
@api_view(['GET'])
def get_all_todos(request):
    try:
        data = Todo.objects.all()
        serial = TodoSerializer(data, many=True)
        return Response(serial.data)
    except:
        return Response(request, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_projects(request):
    data = Project.objects.all()
    serial = ProjectSerializer(data, many=True)
    return Response(serial.data)

@api_view(['POST','PUT'])
def delete_todo(request, pk):
    try:
        data = Todo.objects.get(pk=pk)
        data.delete()
        return Response("completed")
    except:
        return Response("sorry", status=status.HTTP_400_BAD_REQUEST)