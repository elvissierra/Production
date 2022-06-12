from unicodedata import name
from unittest import FunctionTestCase
from django.db import models

# Create your models here.


class Person(models.Model):
    first = models.CharField(max_length= 20)
    last = models.CharField(max_length= 20)


class Technician(models.Model):
    name = 
    role = models.CharField(max_length= 20)


class Task(models.Model):
    name = models.CharField(max_length= 20)
    tools = models.CharField(max_length= 20)
    time = models.DateTimeField()
    order = models.IntegerField()


class Tools(models.Model):
    name = models.CharField(max_length= 20)
    price = models.FloatField()
    quantity = models.IntegerField()


class Area(models.Model):
    technician = 
    tools = 
    functions = 
