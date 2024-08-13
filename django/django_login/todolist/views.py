# response(응답) 사용
from django.shortcuts import render, redirect
# models(테이블) User -> join  
from django.contrib.auth.models import User 
# 오류 메세지 전달할때, 
from django.contrib import messages
# authenticate -> 사용자 인증에 사용되는 함수
from django.contrib.auth import authenticate, login, logout

# Create your views here.
# 로그인 
# -> 사용자 아이디, 비번 같은 사용자가 DB에 있는지 확인  
# -> 오류
#   -> 해당 아이디가 없습니다? 
#   -> 비번이 다릅니다?
# -> 성공 
#   -> todolist 화면!!
def login_user(req):
    if req.user.is_authenticated:
        return redirect("select-todolist")
    elif req.method == "POST":
        username = req.POST.get("username")
        password = req.POST.get("password")

        # 사용자 인증
        user = authenticate(username=username, password=password)
        if user: 
            login(req, user) 
            return redirect("select-todolist")
        
        messages.error(req
            , "Error, wrong user details or user does not exit") 
    
    return render(req, "user/login.html")


# 회원가입 
# -> 입력값: 사용자 아이디, 비번 등...
# -> 오류
#   -> 사용자 아이디, 비번 값 유무 확인 
#   -> DB에 해당 사용자 아이디 유무 확인
# -> 성공
#   -> 로그인 화면!! 

def __check_join_info(**join_user) -> bool:
    is_false = False 

    if not pwd \
        or len(pwd) < 3 \
        or False:
        is_false = True

    return is_false

def join_user(req):
    if req.user.is_authenticated:
        return redirect("select-todolist") 
    elif req.method == "POST":
        username = req.POST.get("username")
        password = req.POST.get("password")
        email = req.POST.get("email")

        mysql_user = User.objects.filter(username=username)
        if mysql_user:
            messages.error(req
            , "Error, username already exists, User another.")
        elif __check_join_info(password):
            messages.error(req
            , "Error, Wrong Password, You have to..")
        else:
            new_user = User.objects.create_user(
                username, email, password)
            new_user.save()
            return redirect("user-login")

    return render(req, "user/join.html")


# 로그아웃 
# -> 로그아웃 진행 
# -> 로그인 화면!! 
def logout_user(req):
    if req.user.is_authenticated:
        logout(req) 
    
    return redirect("user-login")

