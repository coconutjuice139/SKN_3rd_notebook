from django.shortcuts import render, redirect
from django.contrib import messages
from .models import todo

# Create your views here.

# def index(request):
#     return render(request, "./todolist/index.html")

# 조회 & 생성

def search(req):
    # 만약 조회했는데 없으면? 생성
    if req.method == "POST":
        new_todo = req.POST.get("task")
        new_todo = new_todo.strip()
        confirm = todo.objects.filter(todo_name = new_todo)
        if confirm:
            messages.error(req, "이미 있는 todo 입니다.")
        elif not len(new_todo):
            messages.error(req, "잘못된 입력입니다.")
        else:
            insert_todo = todo(todo_name = new_todo)
            insert_todo.save()

    all_todo = todo.objects.all()
    context = {
        "todos": all_todo
    }

    return render(req, "./todolist/index.html", context)


# 수정
def modify(req, task):
    get_todo = todo.objects.get(todo_name = task)
    if get_todo.status == True:
        get_todo.status = False
    else:
        get_todo.status = True
    
    get_todo.save()
    return redirect("todolist-list")


# 삭제
def delete(req, task):
    get_todo = todo.objects.get(todo_name = task)
    get_todo.delete()
    return redirect("todolist-list")