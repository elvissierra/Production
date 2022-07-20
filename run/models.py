from django.db import models


class Person(models.Model):
    first = models.CharField(max_length= 20)
    last = models.CharField(max_length= 20)
    id = models.BigAutoField(primary_key= True)

    def full_name(self):
        return "{}{}".format(self.first, self.last)
    
    class Meta:
        db_table = "person"

class Technician(models.Model):
    tech = models.ForeignKey(Person, on_delete=models.CASCADE)
    role = models.CharField(max_length= 20)
    
    class Meta:
        db_table = "technician"


class Tools(models.Model):
    name = models.CharField(max_length= 20)
    description = models.TextField(null= True, blank = True)
    price = models.FloatField()
    quantity = models.IntegerField()
    
    class Meta:
        db_table = "tools"


class Task(models.Model):
    name = models.CharField(max_length= 20)
    tools = models.CharField(Tools)
    time = models.DateTimeField()
    order = models.IntegerField()
    
    class Meta:
        db_table = "task"


class Area(models.Model):
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE)
    tasks = models.ManyToManyField(Task)
    tools = models.ManyToManyField(Tools)
    
    class Meta:
        db_table = "production"