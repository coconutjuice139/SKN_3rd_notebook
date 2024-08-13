from django.urls import path
from .views import search, modify, delete

urlpatterns = [
    path('', search, name="todolist-list"),
    path('modify/<str:task>', modify, name="todolist-modify"),
    path('delete/<str:task>', delete, name="todolist-delete")
]