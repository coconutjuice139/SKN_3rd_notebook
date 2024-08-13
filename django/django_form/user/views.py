from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CustomForm, CustomCreationForm

# Create your views here.
def user_login(request): #유저 로그인 응답
    if request.user.is_authenticated: # 요청한 유저가 로그인 되었는가?
        return redirect("task-list")  # Yes! -> tack-list(메인 홈)로 redirect(get) 시킴
    elif request.method == 'POST':    # 요청한 유저가 'POST' 명령을 가지고 있는가?
        name = request.POST.get("name")    # Yes! -> input의 name.value의 키워드인 name의 값을 받자
        pwd = request.POST.get("password") # Yes! -> input의 name.value의 키워드인 password의 값을 받자
        validate_user = authenticate(name=name, password=pwd)  # 입력한 정보가 인가를 받은 유저인지 확인해보자
        if validate_user is not None:      # 인가받은 유저인가?
            login(request, validate_user)  # Yes! -> 로그인 승인
            return redirect('task-list')   # task-list(메인 홈)로 보내자
        else:                                                                           # 인가 받지 않은 유저이다.
            messages.info(request, 'Try again! username or password is incorrect')      # 에러 메세지를 띄우자
            return redirect("login")                                                    # 로그인 페이지로 redirect(get) 시키자

    template_name = 'user/login.html'                   # user/login 페이지를 변수에 저장
    context={'form':CustomForm()}                       # CustomForm 클래스의 형태(form)를 이용해서 데이터 받을 준비
    return render(request, template_name, context)      # 요청을 user/login에 보내고 context와 함께 뿌려진다.

def user_register(request):
    if request.user.is_authenticated:
        return redirect("task-list")
    elif request.method == "POST":
        form = CustomCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
        else:
            # messages.info(request, 'Try again!')
            messages.error(request, form.errors)
            return redirect("register")
    
    template_name = 'user/register.html'
    context={'form':CustomCreationForm()}
    return render(request, template_name, context)  

