from django.db import models
from django.shortcuts import render
from django.views.generic import ListView

from production.run.models import Area


class Department(ListView):
    model = Area
