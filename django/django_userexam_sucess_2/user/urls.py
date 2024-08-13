from django.urls import path
from .views import login_user, join_user, logout_user

urlpatterns = [
    path('', login_user, name="user_login"),
    path('login/', login_user, name="user_login"),
    path('join/', join_user, name="user_join"),
    path('logout/', logout_user, name="logout_user"),
]