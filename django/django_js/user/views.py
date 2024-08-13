from django.shortcuts import render

# Create your views here.

def index(request):
    # 일반적으로 dict 타입으로 사용한다.
    # DB접속을 했을 때, data의 형식을 dict 형태로 html에 넘겨줘야 한다.
    context = {
        'massage1':'user 초기화면인가요?',
        'massage2':'django 쵝오!!'
    }
    return render(request, "user/index.html", context)

def getUserInfo(request):

    # dict 내부에서 list형식으로 넘겨줄 수도 있다.
    context = {
        'like_food':'좋아하는 음식',
        'foods': ['쌀','국','수','라','면'],
        'like_country':'좋아하는 나라',
        'countries':[
            {'name':'호주'},
            {'name':'영국'},
            {'name':'스위스'}
        ]
    }

    return render(request, "user/userinfo.html", context)