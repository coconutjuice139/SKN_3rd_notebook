# response(응답) 사용
from django.shortcuts import render, redirect
# models(테이블) User 객체 -> join, login, logout
from django.contrib.auth.models import User
# 오류 메세지 전달
from django.contrib import messages
# 웹 페이지 인증(사용자 인증에 사용되는 함수), 로그인, 로그아웃
from django.contrib.auth import authenticate, login, logout

# Create your views here.

# def index(request):
    # return render(request, "./todolist/index.html")

def __check_pwd(pwd:str) -> bool:
    result = False
    if not pwd or\
        len(pwd) < 3 or\
            False :
        result = True
    return result


# 로그인
# -> 사용자 id, pw 같은 사용자가 db에 있는지 확인
# -> 오류
#    해당 아이디가 없습니다.
#    비번이 다릅니다.
# -> 성공
#    user 화면
def login_user(request):
    if request.user.is_authenticated:
        return render(request, "todolist/login.html")
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
# 사용자 인증
    user = authenticate(username = username, password=password)
    if user:
        login(request, user)
        return redirect("user-research")
    else:
        messages.error(request, "잘못된 입력 혹은 사용자가 아닙니다.")
        #html 조심...
        return render(request, "todolist/login.html")
    


# 회원가입
# -> 입력값 : 사용자 아이디, 비번 등
# -> 오류
#   -> DB에 해당 사용자 아이디 유무 확인
# -> 성공
#    로그인 화면 이동

def join_user(request):
    if request.user.is_authenticated:
        return redirect("user-research")
    elif request.method =="POST":
        username = request.POST.get("username")
        password = request.POST.get('password')
        email = request.POST.get('email')

        mysql_user = User.objects.filter(username = username)
        if mysql_user:
            messages.error(request, "이미 있는 아이디임")
            pass
        elif __check_pwd(password):
            messages.error(request, "비번이 이게 뭐냐")
            pass
        else:
            new_user = User.objects.create_user(username, email, password)
            new_user.save()
            return redirect("user-login")
    return render(request, "todolist/join.html")


# 로그아웃
# -> 로그아웃 성공
#    로그인 화면으로 이동

def logout(request):
    if request.user.is_authenticated:
        return redirect("user-login")