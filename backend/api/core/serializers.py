from rest_framework.serializers import ModelSerializer
from . import models 

class TodoSerializer(ModelSerializer):
    class Meta:
        model=models.Todo
        fields = "__all__"

class ProjectSerializer(ModelSerializer):
    class Meta:
        model=models.Project
        fields="__all__"