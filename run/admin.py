from django.contrib import admin
from django.db import models
from .models import Material, Function, Area

models = [Material, Function, Area]

admin.site.register(models)
