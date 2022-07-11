from django.urls import path
from . views import (BackendArea, CustomLoginView, PersonsPage, RegisterView, TechPage) 
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name = 'register_super'),
    path('logout/', LogoutView.as_view(next_page= 'login'), name= 'logout'),
    path('', TechPage.as_view(), name= 'technicians')
]