from django.contrib import admin
from .models import Material, Function, Area

admin.site.register(Material, Function, Area)
