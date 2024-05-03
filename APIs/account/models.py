from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class refreshtoken(models.Model):
    refresh = models.TextField(max_length=1000)
    user = models.ForeignKey(User , null=True , on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username