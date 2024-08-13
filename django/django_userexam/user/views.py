from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# 로그인, 로그아웃, 권한(인가) 있는지 확인
from .constant import USER_ROLE # 권한 enum classs
from .models import Custom # 기존엔 User를 사용했으나, 우리가 제작한 User class로 대체


# Create your views here.

# 로그인
# 들어올 수 있는 변수 : 
# -> 로그인 한 사람 -> todo로
# -> 로그인 요청한 사람 -> 아이디/비번이 맞는지 확인
# -> 로그인 화면 요청하는 사람 -> 로그인 화면으로 안내
def login_user(req): 
    # -> 이미 로그인한 사람 -> todolist 화면 
    if req.user.is_authenticated:
        return redirect("todolist-select")
    # -> 로그인 요청한 사람 -> 아이디/비번 맞는지 확인 하고
    elif req.method == "POST":
        username = req.POST.get("username")
        password = req.POST.get("password") 
        print(f"{username}/ {password}")
        valid_user = authenticate(username=username, password=password)
        print(f"valid_user: {valid_user}")
        if valid_user:
            login(req, valid_user)
            return redirect("todolist-select")
        
        messages.error(req, "아이디 또는 비번이 틀립니다. 다시 입력해주세요.")

    # -> 로그인 화면 접속하는 사람 -> 로그인 화면으로 안내 
    return render(req, "user/login.html")


# # -> 로그인 한 사람 -> todo로
#     if req.user.is_authenticated: # 권한(로그인) 확인
#         return redirect("todolist-select") # todolist 메인 페이지로 보냄
    
# # -> 로그인 요청한 사람 -> 아이디/비번이 맞는지 확인
#     elif req.method == "POST": # 입력한 값 있는지 확인
#         username = req.POST.get("username") # username에 입력한 값 추출
#         password = req.POST.get("password") # password에 입력한 값 추출
#         valid_user = authenticate(username=username, password=password)
#         if valid_user:
#             login(req, valid_user)
#             return redirect("todolist-select")
#         else:
#             # 사용자 이름 또는 비밀번호가 틀린 경우
#             if not Custom.objects.filter(username=username).exists():
#                 messages.error(req, "존재하지 않는 아이디입니다.")
#             elif not Custom.objects.filter(username=username).exists():
#                 messages.error(req, "잘못된 비밀번호입니다.")
#             else:
#                 messages.error(req, "조회 문제")
#         # messages.error(req, "잘못된 아이디 또는 비밀번호 입니다. 헤이 리츄라이 츄라이")        
# # -> 로그인 화면 요청하는 사람 -> 로그인 화면으로 안내
#     return render(req, "./user/login.html")

# join가입
# 로그인한 사람 -> todo로
# 가입을 요청하는 사람 -> 검증
# 가입화면으로 이동하는 사람 -> 보내기
def join_user(req):
# 로그인한 사람 -> todo로
    if req.user.is_authenticated: # 권한(로그인) 확인
        return redirect("todolist-select") # todolist 메인 페이지로 보냄
    
# 가입을 요청하는 사람 -> 검증
    elif req.method == "POST":
        username = req.POST.get("username") # join.html내의 POST에서 username 함수에 담기
        password = req.POST.get("password") # join.html내의 POST에서 password 함수에 담기
        email = req.POST.get("email") # join.html내의 POST에서 email 함수에 담기
        # 요청한 데이터가 정상적인지 검증
        is_vaild = __is_vaild_user_info(req = req, username = username, password=password, email = email)
        # 요청한 데이터가 기존 DB에 있는지 검증
        custom = Custom.objects.filter(username = username)
        # 신규 고객 데이터 기록
        if is_vaild and not custom:
            # 고객인지 admin인지 확인
            role = USER_ROLE.ADMIN.name if "admin" in username.lower() else USER_ROLE.CUST.name
            # 신규 고객 정보 입력
            new_custom = Custom.objects.create_user(
                username = username,
                password = password,
                email = email,
                role = role
            )
            new_custom.save()

            return redirect("user_login")

        elif custom:
            messages.error(req, "이미 등록한 사람이 있습니다.")
    return render(req, "./user/join.html") # userjoin 메인 페이지로 보냄
            

    
# 가입화면으로 이동하는 사람 -> 보내기

# 검증 함수
def __is_vaild_user_info(req, **user_info) -> bool:
    is_vaild = True
    if not user_info['username'].strip():
        is_vaild = False
        messages.error(req, "유저 이름 입력해 주세요")
    elif len(user_info['password'].strip()) < 5:
        is_vaild = False
        messages.error(req, "공백 제외 비번을 5자 이상 입력해주세요")
    elif not user_info['email'].strip():
        is_vaild = False
        messages.error(req, "이메일을 입력하시오")
        
    return is_vaild


# 로그아웃
def logout_user(req):
    if req.user.is_authenticated: # 권한(로그인) 확인
        logout(req)               # 로그아웃
    return redirect("user_login") # 로그인 페이지로 보냄