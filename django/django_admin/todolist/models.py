from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# 스키마를 정의
# 우리가 작성한 테이블이 ORM을 받으려면
# 상위 모델에서 상속을 받아야 함
# 우리가 생성한 테이블은 자식 클래스
class todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    status = models.BooleanField(default=False)

    # 매직메소드 입력
    def __str__(self) -> str:
        return self.title