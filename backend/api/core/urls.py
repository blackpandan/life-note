from django.urls import path
from .views import get_all_todos, get_all_projects

urlpatterns = [
    path("", get_all_projects),
    path("todos-all", get_all_todos)
]