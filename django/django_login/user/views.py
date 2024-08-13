from django.shortcuts import render, redirect
from django.contrib import messages
from .models import user
from .constant import ERROR_MSG

# Create your views here.

# def index(request):
#     return render(request, "./user/index.html")

# repactoring
def __insert_user(request):
    new_user = request.POST.get("task").strip()
    user_obj = user.objects.filter(user_name = new_user)
    if user_obj:
        messages.error(request, ERROR_MSG.EXIST_MSG.value[1])
    elif not len(new_user) :
        messages.error(request, ERROR_MSG.NO_MSG.value[1])
    else:
        insert_user = user(user_name = new_user)
        insert_user.save()


# 생성, 조회
def research(request):
    if request.method == "POST":
        __insert_user(request)
        
    all_user = user.objects.all()
    context = {
        'users': all_user
    }
    return render(request, "./user/index.html", context)


# 수정
def modify(request, task):
    get_user = user.objects.get(user_name = task)
    if get_user.status:
        get_user.status = False
    elif not get_user.status:
        get_user.status = True
    get_user.save()
    return redirect("user-research")

# 삭제
def delete(request, task):
    get_user = user.objects.get(user_name = task)
    get_user.delete()
    return redirect("user-research")
