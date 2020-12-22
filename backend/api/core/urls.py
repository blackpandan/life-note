from django.urls import path
from .views import get_all_todos, get_all_projects, modify_todo, modify_projects

urlpatterns = [
    path("projects/all", get_all_projects),
    path("projects/modify/<int:id>", modify_projects),
    path("todos/all", get_all_todos),
    path("todos/modify/<int:pk>", modify_todo)
]