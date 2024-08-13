"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# 생성된 app.urls.py 파일로 연동하는 코드만 짜기 -> 그래야 라우팅 기능을 함
# 일일이 모든 view.py에 연동하기엔 너무 복잡함
# 따라서 url.py가 각각 받은 명령을 적절한 view에 분할시키기 -> 이렇게 하면 코드의 복잡성이 낮아짐
# 위의 django.urls의 import에 include를 추가하였음.
urlpatterns = [
    # path('admin/', admin.site.urls),
    # localhost: ??/ ???? -> 모두 todolist.urls로 보내기
    # 아래가 추가됨으로 ??/user/????이외의 모든 호스트는 todolist.urls로 보낸다.
    path('', include("todolist.urls")),
    # localhost: ??/user/??? -> 모두 user.urls로 보내기
    path('user/', include("user.urls")),
    path('list/', include("todolist.urls"))

]
