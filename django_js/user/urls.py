from django.urls import path
from .views import index, getUserInfo

urlpatterns = [
    path('', index, name="user-index"),
    path('info', getUserInfo, name="user-info"),
]
