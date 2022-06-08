from django.urls import path
from django.urls import include, path
from django.contrib import admin
from .views import ListView


url_patterns = [
    path("admin/", admin.site.urls),
    path("department", ListView.as_view(), name="department"),
]
