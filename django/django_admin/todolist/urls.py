
from django.urls import path
from .views import getIndex

urlpatterns = [
    path('', getIndex, name = 'todolist-index'),
    path('index/', getIndex, name = 'todolist-index')
]