from django.shortcuts import render, redirect
from .models import todo
# 장고를 통해 메세지를 보내는 import
from django.contrib import messages
# 로그인 권한 확인
from django.contrib.auth.decorators import login_required
from user.constant import USER_ROLE

# Create your views here.
# 1. 화면에 data 조회가 필요
# 2. 정보 삽입
# 3. 정보 삭제
# 4. 정보 업데이트

# 로그인 권한 확인, 안되어 있으면 user/login으로 보내버림
@ login_required(login_url="./user/login.html")
# 조회 & 생성
def selecet_todolist(request):
    # 생성 post -> html에서 form 태그의 method로 받아온다.
    if request.method == "POST":
        # html에 작성된 input의 데이터를 받아와야 한다.
        # 해당 데이터는 django의 name을 task로 받는다. -> form에서 input안에 name = 'str' 의 str을 받는다
        # 브라우저에 작성한 todo 제목이 있음!!!!
        new_todo = request.POST.get("new_task")
        new_todo = new_todo.strip() # 양쪽 공백을 제거하는 함수
        if not new_todo: #오류 메세지를 올리기 위해 html에 미리 뚫어둠 massage로...
            messages.error(request, "error_massage: 에러가 발생했단다\n빈칸으로 작성한거 같아")
        else:
            # todo클래스의 인스턴스가 생성!!!!
            # todo에 새로 만든 custom을 입력해줘야 한다.
            insert_todo = todo(custom = request.user, todo_name = new_todo)
            insert_todo.save() # 위의 인스턴스 데이터를 DB에 저장/수정을 할 수 있다!!!

    # 생성 프로세스가 끝나면 조회가 되어야 한다.
    # 조회 get
    # 이것도 html에 작성한 name을 확인해야 한다.
    # 관리자 = 전체조회
    # 일반사용자 = 본인것만 조회
    if request.user.role == USER_ROLE.ADMIN.name:
        todolist = todo.objects.all()
    else:
        todolist = todo.objects.filter(custom = request.user)
    context = {
        'todos':todolist
    }
    return render(request, "todolist/index.html", context)


# 로그인 권한 확인, 안되어 있으면 user/login으로 보내버림
@ login_required(login_url="./user/login.html")
# 수정
def update_todolist(request, task):
    # DB에 있는 데이터 조회
    if request.user.role == USER_ROLE.ADMIN.name:
        get_todo = todo.objects.get(todo_name = task)
    else:
        get_todo = todo.objects.get(custom = request.user, todo_name = task)
    # get_todo = todo.objects.get(todo_name = request.user, todo_name = task)
    # 수정할 데이터
    get_todo.status = True
    # 데이터 저장
    get_todo.save()

    return redirect("todolist-select") #이렇게 하면 http 호출기로 todolist-select라는 알리아스를 통해 url을 동작시킬 수 있다.


# 로그인 권한 확인, 안되어 있으면 user/login으로 보내버림
@ login_required(login_url="./user/login.html")
# 삭제
def delete_todolist(request, task):
    # DB에 있는 데이터 조회
    if request.user.role == USER_ROLE.ADMIN.name:
        get_todo = todo.objects.get(todo_name = task)
    else:
        get_todo = todo.objects.get(custom = request.user, todo_name = task)
    # get_todo = todo.objects.get(todo_name = request.user, todo_name = task)
    # DB에 있는 데이터 삭제
    get_todo.delete()

    return redirect("todolist-select") #이렇게 하면 http 호출기로 todolist-select라는 알리아스를 통해 url을 동작시킬 수 있다.