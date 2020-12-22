from django.urls import path
from .views import get_all_todos, get_all_projects, delete_todo, modify_projects

urlpatterns = [
    path("", get_all_projects),
    path("projects/modify/<int:id>", modify_projects),
    path("todos-all", get_all_todos),
    path("delete/todo/<int:pk>", delete_todo)
]