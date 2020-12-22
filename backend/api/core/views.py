# for django imports
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import ObjectDoesNotExist

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

# this is the configuration for the projects section request handling
@api_view(['GET', 'POST'])
def get_all_projects(request):
    if (request.method == "GET"):
        data = Project.objects.all()
        serial = ProjectSerializer(data, many=True)
        return Response(serial.data)
    elif(request.method == 'POST'):
        try:
            name = request.data['title']
            details = request.data['details']
            new = Project(title=name, body=details)
            # serial = ProjectSerializer(new)
            new.save()
            return Response("sucessfully added", status=status.HTTP_201_CREATED)
        except KeyError as e:
            return Response(f"required fields is missing: {e}", status=status.HTTP_428_PRECONDITION_REQUIRED)


@api_view(["PUT", "DELETE"])
def modify_projects(request, id):
    if (request.method == "PUT"):
        try:
            name = request.data['title']
            details = request.data['details']
            model = Project.objects.get(pk=id)
            model.title=name
            model.details=details
            model.save()
            return Response("tested")
        except KeyError as e:
            return Response(f"please provide {e} field", status=status.HTTP_428_PRECONDITION_REQUIRED)
        except Project.DoesNotExist as e:
            return Response(f"project does not exist, provide valid id", status=status.HTTP_404_NOT_FOUND)
    elif(request.method == "DELETE"):
        try:
            project = Project.objects.get(pk=id)
            project.delete()
        except Project.DoesNotExist as e:
            return Response(f"project does not exist, provide valid id", status=status.HTTP_404_NOT_FOUND)


@api_view(['POST','PUT'])
def delete_todo(request, pk):
    try:
        data = Todo.objects.get(pk=pk)
        data.delete()
        return Response("completed")
    except:
        return Response("sorry", status=status.HTTP_400_BAD_REQUEST)