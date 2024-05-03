from django.db import models
from django.contrib.auth.models import User 
# Create your models here.


class comments(models.Model):
    comment = models.TextField(max_length=1000,default="",blank=False)
    user = models.ForeignKey(User , null=True , on_delete=models.SET_NULL)

    def __str__(self):
        return self.comment
    


class suggestions(models.Model):
    suggestion = models.TextField(max_length=1000,default="",blank=False)
    user = models.ForeignKey(User , null=True , on_delete=models.SET_NULL)

    def __str__(self):
        return self.suggestion