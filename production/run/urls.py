from django.urls import path
from django.urls import include, path
from django.contrib import admin


url_patterns = [
    path("admin/", admin.site.urls),
    path("", include("run.urls")),
]
