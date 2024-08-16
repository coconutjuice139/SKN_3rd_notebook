from django.db import models

# Create your models here.

class mysql(models.Model):
    user_number = models.IntegerField(unique= True, null= False)
    user = models.CharField(max_length=20)
    address = models.TextField(max_length=100)

    def __str__(self):
        return self.user