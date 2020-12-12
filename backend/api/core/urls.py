from django.urls import path
from .views import get_all_todos, get_all_projects, delete_todo

urlpatterns = [
    path("", get_all_projects),
    path("todos-all", get_all_todos),
    path("delete/todo/<int:pk>", delete_todo)
]