from django.shortcuts import render, redirect
from django.contrib import messages
from .models import todo

# Create your views here.

# def todo(request):
#     return render(request, "./todolist/index.html")

# 생성 & 조회
def research(request):
    if request.method == 'POST':
        new_todo = request.POST.get('task')
        todo_obj = todo.objects.filter(todo_name = new_todo)
        if todo_obj:
            messages.error(request, "중복이요~")
        elif not len(new_todo):
            messages.error(request, "안적었어?")
        else:
            insert_todo = todo(todo_name = new_todo)
            insert_todo.save()

    all_todos = todo.objects.all()
    context = { "todos" : all_todos }
    return render(request, "./todolist/index.html", context)


# 수정

def modify(request, task):
    get_todo = todo.objects.get(todo_name = task)
    get_todo.status = True
    get_todo.save()

    return redirect("todo-todo")


# 삭제

def delete(request, task):
    get_todo = todo.objects.get(new_todo = task)
    get_todo.delete()

    return redirect("todo-todo")