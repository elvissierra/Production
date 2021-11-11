from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from production.run.models import Area, Function, Material, Quality


class Department(ListView):
    model = Area

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["materials"] = context["materials"].filter(data=self.request.GET)
        context["time"] = context["time"].add()
        context["function"] = context["function"].

        return context


class Tools(DetailView):
    model = Material


class ToolList(ListView):
    model = Area


class Tasks(ListView):
    model = Function


class Quality(DetailView):
    model = Quality
