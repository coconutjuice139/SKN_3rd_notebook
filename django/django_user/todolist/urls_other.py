from django.urls import path
from .views import selecet_todolist, update_todolist, delete_todolist

# localhost:8000/ -> select or insert
# localhost:8000/update/<str:task> -> update  <str:task> <- 여기에 ID를 받아옴
# localhost:8000/delete/<str:task> -> delete  <str:task> <- 여기에 ID를 받아옴
urlpatterns = [
    path('', selecet_todolist, name="todolist-select"),
    path('update/<str:task>', update_todolist, name="todolist-update"),
    path('delete/<str:task>', delete_todolist, name="todolist-delete")
]
# 위의 /<str:task>는 html에서 task로 넘어오는 ID를 이용해서 어떤 것을 업데이트할지, 삭제할지 표현해줘야 한다.
# 수정 삭제가 끝나면 다시 조회를 해줘야 한다. 이는 redirect를 통해 다시 조회를 실행해야 한다.
# 이는 view에서 redirect로 지정해줘야 한다.