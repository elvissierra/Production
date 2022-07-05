from django.db import models

# Create your models here.
#class login():
#class register():
#class logout():
#class map_overview():

class Person(models.Model):
    first = models.CharField(max_length= 20)
    last = models.CharField(max_length= 20)

    def full_name(self):
        return "{} {}" .format(self.first, self.last)


class Technician(models.Model):
    tech = models.ForeignKey(Person, on_delete=models.CASCADE, default = True)
    role = models.CharField(max_length= 20)


class Task(models.Model):
    name = models.CharField(max_length= 20)
    tools = models.CharField(max_length= 20)
    time = models.DateTimeField()
    order = models.IntegerField()


class Tools(models.Model):
    name = models.CharField(max_length= 20)
    description = models.TextField(null= True, blank = True)
    price = models.FloatField()
    quantity = models.IntegerField()


class Area(models.Model):
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE)
    tasks = models.ManyToManyField(Task)
    tools = models.ManyToManyField(Tools)