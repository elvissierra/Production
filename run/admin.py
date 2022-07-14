from django.contrib import admin
from .models import Technician, Tools, Task, Area, Person

admin.site.register(Technician)
admin.site.register(Tools)
admin.site.register(Task)
admin.site.register(Area)
admin.site.register(Person)