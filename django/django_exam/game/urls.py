from django.urls import path
from .views import game11, game12

urlpatterns = [
    path('', game11, name='user-game1-1'),
    path('1-1', game11, name='user-game1-1'),
    path('1-2', game12, name='user-game1-2')
]