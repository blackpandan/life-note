# for django imports
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

#for rest_framework imprts
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

#module imports
from .serializers import TodoSerializer, ProjectSerializer, UserSerializer
from .models import Todo, Project


# views

#this is for the todo request handling configuration
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
            def get(item):
                return request.data[item]
            update = get("update")
            if update:
                data = Todo.objects.get(pk=pk)
                for i in range(len(update)):
                    if ("title" == update[i]):
                        title = get("title")
                        data.title = title
                    elif ("body" == update[i]):
                        body = get("body")
                        data.body = body
                    elif ("done" == update[i]):
                        done = request.data["done"]
                        data.done = done
                    elif ("pause" == update[i]):
                        pause = request.data["pause"]
                        print(f"pause: {pause}")
                        data.pause = pause
                        
                data.save()
                return Response("todo updated sucessfully", status=status.HTTP_200_OK)
            else:
                return Response("please provide update field", status = status.HTTP_428_PRECONDITION_REQUIRED)
            
        except KeyError as e:
            return Response(f"please provide field: {e}", status=status.HTTP_428_PRECONDITION_REQUIRED)
        except Todo.DoesNotExist as e:
            return Response("todo does not exist, please provide valid id", status=status.HTTP_404_NOT_FOUND)

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
            update = request.data['update']
            if update:
                model = Project.objects.get(pk=id)
                for i in range(len(update)):
                    if("title" == update[i]):
                        name = request.data['title']
                        model.title = name
                    elif("details" == update[i]):
                        details = request.data["details"]
                        model.body = details
                model.save()
                return Response("sucessfully updated", status=status.HTTP_200_OK)
            else:
                return Response(f"please provide update field", status=status.HTTP_428_PRECONDITION_REQUIRED)
            
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


# user authentication and requests handling
@api_view(["POST"])
def get_user_details(request):
    try:
        token = request.data["token"]
        if token:
            user_id = Token.objects.get(key=token).user_id
            details = User.objects.get(id=user_id)
            serial = UserSerializer(details)
            return Response(serial.data, status=status.HTTP_200_OK)
        else:
            return Response("token field is empty", status=status.HTTP_428_PRECONDITION_REQUIRED)
    except KeyError as e:
        return Response("token is missing, please provide required field", status=status.HTTP_428_PRECONDITION_REQUIRED)
    except Token.DoesNotExist as e:
        return Response("token is invalid, it does not exist", status=status.HTTP_404_NOT_FOUND)
    except User.DoesNotExist as e:
        return Response("sorry the user account does not exist or has been deleted", status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
def register_user(request):
    try:
        def get(item):
            return request.data[item]
        email = get("email")
        password = get("password")
        User.objects.create_user(username=email, email=email, password=password)
        return Response("Account was sucessfully created", status=status.HTTP_201_CREATED)
    except KeyError as e:
        return Response(f"please provide valid field: {e}", status=status.HTTP_428_PRECONDITION_REQUIRED)
