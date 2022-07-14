from django.urls import path
from .views import (CustomLoginView, RegisterView, Main) 
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register_super/', RegisterView.as_view(), name = 'register_super'),
    path('logout/', LogoutView.as_view(next_page= 'login'), name= 'logout'),
    path('', Main.as_view(), name = 'main'),
]