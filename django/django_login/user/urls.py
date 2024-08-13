from django.urls import path, include
from .views import research, modify, delete

urlpatterns = [
    path('', research, name = 'user-research'),
    path('modify/<str:task>', modify, name = 'user-modify'),
    path('delete/<str:task>', delete, name = 'user-delete'),
]
