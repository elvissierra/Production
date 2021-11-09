from django.db import models
from django.contrib.auth import User
from django.db.models.fields.related import ManyToManyField


class Material(models.Model):
    item = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2)


class Function(models.Model):
    action = models.TextField(null=True, blank=True)
    time = models.TimeField(auto_now=True, auto_now_add=True)
    materials_used = models.ManyToManyField(Material, through="Cost")


class Area(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    department = models.CharField(max_length=50)
    item = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.IntegerField()
