from django.db import models

# Create your models here.

class user(models.Model):
    user_name = models.CharField(max_length=10)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.user_name