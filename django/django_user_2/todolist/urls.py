
from .views import get_todolist, update_todo, delete_todo
from django.urls import path

urlpatterns = [
    path('', get_todolist, name="todolist-index"),
    path('delete-todo/<str:title>', delete_todo, name="delete-todo"),
    path('update-todo/<str:title>', update_todo, name="update-todo"),
]