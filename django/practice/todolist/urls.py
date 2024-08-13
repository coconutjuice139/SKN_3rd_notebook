from .views import research, modify, delete
from django.urls import path, include

urlpatterns = [
    path('', research, name="todo-todo"),
    path('modify/<str:task>', modify, name="todo-modify"),
    path('delete/<str:task>', delete, name="todo-delete"),
]