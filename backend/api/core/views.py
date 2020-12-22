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
@api_view(['GET', 'POST'])
def get_all_todos(request):
    if (request.method == "GET"):
        try:
            data = Todo.objects.all()
            serial = TodoSerializer(data, many=True)
            return Response(serial.data)
        except:
            return Response(request, status=status.HTTP_400_BAD_REQUEST)
    elif (request.method == "POST"):
        try:
            title = request.data["title"]
            body = request.data["body"]
            done = request.data["done"]
            pause = request.data["pause"]
            data = Todo(title=title, body=body, done=done, pause=pause)
            data.save()
            return Response("sucessfully added", status=status.HTTP_201_CREATED)
        except KeyError as e:
            return Response(f"provide valid field: {e}")

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
            return Response(f"required field is missing: {e}", status=status.HTTP_428_PRECONDITION_REQUIRED)


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
            return Response("sucessfully deleted", status=status.HTTP_200_OK)
        except Project.DoesNotExist as e:
            return Response(f"project does not exist, provide valid id", status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT','DELETE'])
def modify_todo(request, pk):
    if (request.method == "DELETE"):
        try:
            data = Todo.objects.get(pk=pk)
            data.delete()
            return Response("Todo sucessfully deleted")
        except Todo.DoesNotExist as e:
            return Response("sorry todo does not exist, provide valid id", status=status.HTTP_400_BAD_REQUEST)
    elif(request.method == "PUT"):
        try:
            data = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist as e:
            return Response("todo does not exist, please provide valid id", status=status.HTTP_404_NOT_FOUND)