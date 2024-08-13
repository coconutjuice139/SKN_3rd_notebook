from django.db import models
# 다른 app에서 들고올 때, app 이름.file(folder) 이름 으로 입력
from user.models import Custom

# Create your models here.
class todo(models.Model):
    custom = models.ForeignKey(Custom, on_delete=models.CASCADE)
    #todo_name이 식별자임을 확인 -> unique = True
    todo_name = models.CharField(max_length=200)
    status = models.BooleanField(default=False)

    def __str__(self)->str:
        return self.todo_name