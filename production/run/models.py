from django.db import models
from django.contrib.auth import User


class A(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    area = models.CharField(max_length=50)
    functions = models.TextField(null=True, blank=True)
    time = models.TimeField(auto_now=True, auto_now_add=True)
