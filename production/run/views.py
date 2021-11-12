from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from production.run.models import Area, Function, Material, Members, Quality


class Department(ListView):
    model = Area

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["cost"] = context["price"].()
        context["time"] = context["time"].()
        context["members"] = Members.objects.all()
        context["count"] = context["members"].count()
        context["function"] = Function.objects.all()
        context["count"] = context["function"].count()
        context["materials"] = Material.objects.all()
        context["count"] = context["materials"].count()

        return context


class Tools(DetailView):
    model = Material
    


class ToolList(ListView):
    model = Area


class Tasks(ListView):
    model = Function


class Quality(DetailView):
    model = Quality
