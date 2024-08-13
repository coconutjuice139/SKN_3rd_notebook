from django.db import models

# Create your models here.
class todo(models.Model):
    #todo_name이 식별자임을 확인 -> unique = True
    todo_name = models.CharField(max_length=200, unique= True)
    status = models.BooleanField(default=False)

    def __str__(self)->str:
        return self.todo_name