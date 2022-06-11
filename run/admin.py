from django.contrib import admin
from django.db import models
from .models import Person, Technicians, Processes, Tools, Department

models = [Person, Technicians, Processes, Tools, Department]

admin.site.register(models)
