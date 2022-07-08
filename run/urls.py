from django.urls import path
from . views import (CustomLoginView, PersonsPage, RegisterView) 
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name = 'register_super'),
    path('logout/', LogoutView.as_view(next_page= 'login'), name= 'logout'),
    path('',PersonsPage.as_view(), name= 'main')
]