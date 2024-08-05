from django.urls import path
from .views import timer11, timer12, timer13

urlpatterns = [
    path('', timer11, name='user-timer1-1'),
    path('1-1', timer11, name='user-timer1-1'),
    path('1-2', timer12, name='user-timer1-2'),
    path('1-3', timer13, name='user-timer1-3')
]