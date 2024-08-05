# urls라는 파일은 path에 따라 view에 연결해줘야 하므로 urls에서 path를 들고 와야 함
from django.urls import path
# 해당 디렉토리에 설정된 views에 있는 목록을 들고 와야 함
from .views import index


# app.urls.py -> request & view를 연결해주는 역할
urlpatterns = [
    # localhost -> user 제외한 모든 호스트
    path('', index, name="todolist-index"),
]