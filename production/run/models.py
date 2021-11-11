from django.db import models
from django.contrib.auth.models import User


class Material(models.Model):
    item = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Function(models.Model):
    action = models.TextField(null=True, blank=True)
    time = models.TimeField(auto_now_add=True)
    # materials_used = models.ManyToManyField(
    #    "Area", related_name="area_functions", through="Materials"
    # )

    def __str__(self):
        return self().name


class Area(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    department = models.CharField(max_length=50)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Quality(models.Model):
    component = models.TextField(blank=True, null=True)
    time = models.TimeField(auto_now_add=True)
