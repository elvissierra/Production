from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    first = models.CharField(max_length=20)
    last = models.CharField(max_length=20)


class Technicians(models.Model):
    name = models.CharField(max_length=20)
    id = models.AutoField(user_id=id)
    role = models.CharField(max_length=20)


class Processes(models.Model):
    name = models.TextField(null=True, blank=True)
    time = models.TimeField(auto_now_add=True)
    tool = models.CharField(max_length=20)
    order = models.IntegerField()

    def __str__(self):
        return self().name


class Tools(models.Model):
    name = models.CharField(max_length=20)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


# all classes associate with Department class
class Department(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    area = models.CharField(max_length=50)
    material = models.ForeignKey(on_delete=models.CASCADE)
    quantity = models.IntegerField()


""" working on how to tie in the output
class Quality(models.Model):
    component = models.TextField(blank=True, null=True)
    time = models.TimeField(auto_now_add=True)
"""
