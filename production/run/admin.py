from django.contrib import admin
from django.db import models
from .models import Material, Function, Area

models = [
    models.Material,
    models.Function,
    models.Area,
]
admin.site.register(models)
