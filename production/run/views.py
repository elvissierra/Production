from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from production.run.models import Area, Function, Material, Quality


class Department(ListView):
    model = Area


class Tools(DetailView):
    model = Material


class ToolList(ListView):
    model = Area


class Tasks(ListView):
    model = Function


class Quality(DetailView):
    model = Quality
