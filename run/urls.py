from django.urls import path
from .views import (CustomLoginView, RegisterSupView, RegisterPerView, Main) 
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register_super/', RegisterSupView.as_view(), name = 'register_super'),
    path('logout/', LogoutView.as_view(next_page= 'login'), name= 'logout'),
    path('register_persons/', RegisterPerView.as_view(), name = 'register_persons'),
    path('', Main.as_view(), name = 'main'),
]