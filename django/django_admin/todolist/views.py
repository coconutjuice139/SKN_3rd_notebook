from django.shortcuts import render

# Create your views here.
def getIndex(request):
    context = {
        'title':'배고파요~~~',
        'foods': ['족발', '자장면', '라맹', '회']
    }
    return render(request, 'todolist/todolist.html', context)