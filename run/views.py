from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import DeptView, DetailView, ListView
from .models import Person, Technicians, Processes, Tools, Department


class Department(ListView):
    model = Area

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["cost"] = context["price"].filter()
        context["time"] = context["time"].filter()
        context["members", "function", "material"] = Members
        Function
        Material.objects.all()
        context["count"] = context["members", "function", "material"].count()

        return context


class Tools(DetailView):
    model = Material


class ToolList(ListView):
    model = Area


class Tasks(ListView):
    model = Function


class Quality(DetailView):
    model = Quality
