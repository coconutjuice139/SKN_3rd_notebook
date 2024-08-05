from django.shortcuts import render

# Create your views here.
# urls.py(controller)를 통해 처리하는 함수
# 데이터/DB(Model)를 -> 화면(Template)에 띄우는 역할
def index(request):
    # 화면 연결하는 역할
    # 받는 변수, 가고싶은 루트
    # setting.py에서 templates의 기본 dir를 templates로 설정하였기 때문에
    # 기본 루트 뒤에 필요한 위치(디렉토리)를 입력함으로써 가고싶은 html로 연결한다.
    return render(request, "user/index.html")