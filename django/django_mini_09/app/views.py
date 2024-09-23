from django.shortcuts import render

# Create your views here.

def go_homepage(request):

    return render(request, "app/index.html")